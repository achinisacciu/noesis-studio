#!/usr/bin/env python
"""Avvia Document, RAG e Gateway come processi locali e verifica il flusso completo.

Flusso `--check`: import file -> indice -> ricerca con citazione -> rebuild -> delete.
"""
import argparse
import json
import os
import secrets
import shutil
import socket
import subprocess
import sys
import time
import urllib.error
import urllib.request
import uuid
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SERVICES = ("document", "rag", "ai", "gateway")


def free_port() -> int:
    # shortcut: porta scelta e subito rilasciata, race minima in locale; passare a socket ereditato se serve
    with socket.socket() as sock:
        sock.bind(("127.0.0.1", 0))
        return int(sock.getsockname()[1])


def python_for(service: str) -> Path:
    venv = ROOT / "services" / service / ".venv"
    return venv / ("Scripts/python.exe" if os.name == "nt" else "bin/python")


def request(
    method: str,
    url: str,
    token: str,
    payload: dict[str, object] | None = None,
    timeout: float = 10,
) -> tuple[int, dict[str, object]]:
    data = json.dumps(payload).encode() if payload is not None else None
    req = urllib.request.Request(url, data=data, method=method)
    req.add_header("Authorization", f"Bearer {token}")
    if data is not None:
        req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req, timeout=timeout) as response:
            return response.status, json.load(response)
    except urllib.error.HTTPError as error:
        return error.code, json.load(error)


def upload(url: str, token: str, filename: str, content: bytes) -> tuple[int, dict[str, object]]:
    boundary = uuid.uuid4().hex
    body = (
        f"--{boundary}\r\n"
        f'Content-Disposition: form-data; name="file"; filename="{filename}"\r\n'
        "Content-Type: text/markdown\r\n\r\n"
    ).encode() + content + f"\r\n--{boundary}--\r\n".encode()
    req = urllib.request.Request(url, data=body, method="POST")
    req.add_header("Authorization", f"Bearer {token}")
    req.add_header("Content-Type", f"multipart/form-data; boundary={boundary}")
    try:
        with urllib.request.urlopen(req, timeout=60) as response:
            return response.status, json.load(response)
    except urllib.error.HTTPError as error:
        return error.code, json.load(error)


def wait_ready(url: str, timeout: float = 60) -> None:
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        try:
            with urllib.request.urlopen(f"{url}/ready", timeout=2) as response:
                if response.status == 200:
                    return
        except OSError:
            pass
        time.sleep(0.3)
    raise SystemExit(f"servizio non pronto: {url}")


def chat(
    gateway: str, token: str, question: str, document_id: str
) -> list[tuple[str, dict[str, object]]]:
    payload = {"question": question, "document_id": document_id, "limit": 3}
    req = urllib.request.Request(
        f"{gateway}/api/ai/chat",
        data=json.dumps(payload).encode(),
        method="POST",
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "Accept": "text/event-stream",
        },
    )
    events: list[tuple[str, dict[str, object]]] = []
    event = ""
    try:
        with urllib.request.urlopen(req, timeout=180) as response:
            for raw in response:
                line = raw.decode().rstrip("\r\n")
                if line.startswith("event: "):
                    event = line[7:]
                elif line.startswith("data: ") and event:
                    events.append((event, json.loads(line[6:])))
    except urllib.error.HTTPError as error:
        raise SystemExit(f"chat fallita: {error.code} {error.read().decode(errors='replace')}")
    return events


def check_flow(gateway: str, token: str) -> None:
    markdown = "# Varianza\n\nLa varianza misura la dispersione dei dati.\n"

    status, body = upload(
        f"{gateway}/api/documents", token, "statistica.md", markdown.encode()
    )
    assert status == 200, body
    document = body["data"]
    assert isinstance(document, dict)
    document_id = document["id"]
    assert isinstance(document_id, str)
    assert document["chunk_count"] == 1, document

    status, body = request("GET", f"{gateway}/api/documents", token)
    assert status == 200, body
    assert [item["id"] for item in body["data"]] == [document_id], body

    status, body = request("POST", f"{gateway}/api/index/{document_id}", token)
    assert status == 200 and body["data"]["chunks"] == 1, body

    status, body = request(
        "POST",
        f"{gateway}/api/rag/search",
        token,
        {"query": "dispersione", "document_id": document_id},
    )
    assert status == 200, body
    hits = body["data"]["hits"]
    assert hits, body
    citation = hits[0]
    assert citation["document_id"] == document_id, citation
    assert citation["section"] == "Varianza", citation
    assert 0 < citation["score"] <= 1, citation

    status, body = request("POST", f"{gateway}/api/index/rebuild", token)
    assert status == 200 and body["data"] == {"documents": 1, "chunks": 1}, body

    events = chat(gateway, token, "Che cosa misura la varianza?", document_id)
    names = [name for name, _ in events]
    assert "citation" in names and "done" in names, events
    assert "error" not in names, events
    answer = "".join(str(data["delta"]) for name, data in events if name == "token")
    assert answer.strip(), events
    print(f"gateway   ok     tutor SSE ({len(answer)} caratteri, {names.count('citation')} citazioni)")

    status, body = request("DELETE", f"{gateway}/api/documents/{document_id}", token)
    assert status == 200, body

    status, body = request("GET", f"{gateway}/api/documents/{document_id}", token)
    assert status == 404, body
    status, body = request("POST", f"{gateway}/api/rag/search", token, {"query": "dispersione"})
    assert status == 200 and body["data"]["hits"] == [], body

    print(
        f"gateway   ok     import + indice + ricerca + rebuild + delete "
        f"(citazione: {citation['section']}, score {citation['score']})"
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="esegue il flusso completo ed esce")
    parser.add_argument("--no-sync", action="store_true", help="salta uv sync")
    parser.add_argument(
        "--data",
        type=Path,
        help="cartella dati condivisa (default: data/; con --check viene isolata e pulita)",
    )
    args = parser.parse_args()

    data_dir = (args.data or ROOT / "data").resolve()
    if args.check:
        data_dir = data_dir / "check"
        shutil.rmtree(data_dir, ignore_errors=True)
    data_dir.mkdir(parents=True, exist_ok=True)
    logs = data_dir / "logs"

    if not args.no_sync:
        for service in SERVICES:
            subprocess.run(
                [
                    sys.executable,
                    "-m",
                    "uv",
                    "sync",
                    "--quiet",
                    "--project",
                    str(ROOT / "services" / service),
                ],
                check=True,
            )

    token = secrets.token_urlsafe(24)
    ports = {service: free_port() for service in SERVICES}
    urls = {service: f"http://127.0.0.1:{ports[service]}" for service in SERVICES}
    logs.mkdir(parents=True, exist_ok=True)

    env = {
        **os.environ,
        "NOESIS_TOKEN": token,
        "NOESIS_DATA": str(data_dir),
        "NOESIS_MODEL": os.getenv("NOESIS_MODEL", "qwen3.5:0.8b"),
        "DOCUMENT_URL": urls["document"],
        "RAG_URL": urls["rag"],
        "AI_URL": urls["ai"],
        "PYTHONUNBUFFERED": "1",
    }
    processes: dict[str, subprocess.Popen[bytes]] = {}
    try:
        for service in SERVICES:
            log = (logs / f"{service}.log").open("wb")
            processes[service] = subprocess.Popen(
                [
                    str(python_for(service)),
                    "-m",
                    "uvicorn",
                    "app.main:app",
                    "--host",
                    "127.0.0.1",
                    "--port",
                    str(ports[service]),
                    "--no-access-log",
                ],
                cwd=ROOT / "services" / service,
                env=env,
                stdout=log,
                stderr=subprocess.STDOUT,
            )

        for service in SERVICES:
            wait_ready(urls[service])
            print(f"{service:9} ready  {urls[service]}")

        if args.check:
            check_flow(urls["gateway"], token)
            return 0

        print("Ctrl+C per arrestare i servizi.")
        while True:
            time.sleep(1)
    finally:
        for process in processes.values():
            process.terminate()
        for process in processes.values():
            try:
                process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                process.kill()
        print("servizi arrestati")


if __name__ == "__main__":
    raise SystemExit(main())
