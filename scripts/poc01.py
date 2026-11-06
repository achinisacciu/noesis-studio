#!/usr/bin/env python
"""POC-01: avvia Document, RAG e Gateway come processi locali indipendenti."""
import argparse
import json
import os
import secrets
import socket
import subprocess
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LOGS = ROOT / "data" / "logs" / "poc01"
SERVICES = ("document", "rag", "gateway")


def free_port() -> int:
    # shortcut: porta scelta e subito rilasciata, race minima in locale; passare a socket ereditato se serve
    with socket.socket() as sock:
        sock.bind(("127.0.0.1", 0))
        return int(sock.getsockname()[1])


def python_for(service: str) -> Path:
    venv = ROOT / "services" / service / ".venv"
    return venv / ("Scripts/python.exe" if os.name == "nt" else "bin/python")


def request(
    method: str, url: str, token: str, payload: dict[str, object] | None = None
) -> tuple[int, dict[str, object]]:
    data = json.dumps(payload).encode() if payload is not None else None
    req = urllib.request.Request(url, data=data, method=method)
    req.add_header("Authorization", f"Bearer {token}")
    if data is not None:
        req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req, timeout=10) as response:
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


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="esegue il flusso completo ed esce")
    parser.add_argument("--no-sync", action="store_true", help="salta uv sync")
    args = parser.parse_args()

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
    LOGS.mkdir(parents=True, exist_ok=True)

    env = {
        **os.environ,
        "NOESIS_TOKEN": token,
        "DOCUMENT_URL": urls["document"],
        "RAG_URL": urls["rag"],
        "PYTHONUNBUFFERED": "1",
    }
    processes: dict[str, subprocess.Popen[bytes]] = {}
    try:
        for service in SERVICES:
            log = (LOGS / f"{service}.log").open("wb")
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
            status, body = request(
                "POST",
                f"{urls['gateway']}/api/documents",
                token,
                {"title": "Statistica", "text": "La media è 3. La varianza misura la dispersione."},
            )
            assert status == 200, body
            document = body["data"]
            assert isinstance(document, dict)
            document_id = document["id"]
            assert isinstance(document_id, str)

            status, body = request(
                "POST",
                f"{urls['gateway']}/api/rag/search",
                token,
                {"query": "varianza", "document_id": document_id},
            )
            assert status == 200, body
            hits = body["data"]["hits"]
            assert hits and "varianza" in hits[0]["text"].lower(), body
            print(f"gateway   ok     documento {document_id} -> {len(hits)} citazione/i")
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

