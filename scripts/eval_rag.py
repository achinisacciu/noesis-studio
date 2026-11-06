#!/usr/bin/env python
"""Valuta la qualità delle citazioni RAG sul corpus in evaluation/.

Flusso: importa i file del corpus nel gateway, indicizza, interroga ogni domanda
di `evaluation/questions.jsonl` filtrando per documento, controlla che la sezione
attesa compaia tra i primi hit, stampa l'accuratezza e ripulisce la libreria.

Serve uno stack attivo (`python scripts/stack.py --dev`).
"""
import argparse
import json
from pathlib import Path

from stack import request, upload

ROOT = Path(__file__).resolve().parents[1]
CORPUS = ROOT / "evaluation" / "corpus"
QUESTIONS = ROOT / "evaluation" / "questions.jsonl"


def load_cases(path: Path) -> list[dict[str, str]]:
    cases = []
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip():
            continue
        case = json.loads(line)
        missing = {"document", "section", "question"} - case.keys()
        if missing:
            raise SystemExit(f"{path}:{number}: campi mancanti {sorted(missing)}")
        cases.append(case)
    return cases


def import_corpus(gateway: str, token: str) -> dict[str, str]:
    ids: dict[str, str] = {}
    for path in sorted(CORPUS.glob("*.md")):
        status, body = upload(
            f"{gateway}/api/documents", token, path.name, path.read_bytes()
        )
        if status != 200:
            raise SystemExit(f"import fallito per {path.name}: {status} {body}")
        document_id = str(body["data"]["id"])
        status, body = request("POST", f"{gateway}/api/index/{document_id}", token)
        if status != 200:
            raise SystemExit(f"indice fallito per {path.name}: {status} {body}")
        ids[path.name] = document_id
        print(f"import   ok     {path.name:32} {body['data']['chunks']} chunk")
    return ids


def sections_of(gateway: str, token: str, document_id: str) -> set[str]:
    status, body = request("GET", f"{gateway}/api/documents/{document_id}/chunks", token)
    if status != 200:
        raise SystemExit(f"chunk non leggibili: {status} {body}")
    return {chunk["section"] for chunk in body["data"]["chunks"] if chunk["section"]}


def evaluate(
    gateway: str, token: str, cases: list[dict[str, str]], ids: dict[str, str]
) -> tuple[int, int, float]:
    failures: list[str] = []
    for case in cases:
        document_id = ids[case["document"]]
        status, body = request(
            "POST",
            f"{gateway}/api/rag/search",
            token,
            {"query": case["question"], "document_id": document_id, "limit": 3},
        )
        if status != 200:
            raise SystemExit(f"ricerca fallita: {status} {body}")
        hits = body["data"]["hits"]
        found = [hit["section"] for hit in hits]
        if case["section"] not in found:
            failures.append(
                f"  KO  {case['question']}\n"
                f"      attesa: {case['section']} | trovate: {found}"
            )

    total = len(cases)
    correct = total - len(failures)
    accuracy = correct / total if total else 0.0
    print()
    if failures:
        print("citazioni non corrette:")
        print("\n".join(failures))
        print()
    print(f"accuratezza citazioni: {correct}/{total} = {accuracy:.1%}")
    return total, correct, accuracy


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--gateway", default="http://127.0.0.1:8010")
    parser.add_argument("--token", default="dev-token")
    parser.add_argument("--min-accuracy", type=float, default=0.9)
    parser.add_argument("--keep", action="store_true", help="non eliminare i documenti importati")
    args = parser.parse_args()

    cases = load_cases(QUESTIONS)
    ids = import_corpus(args.gateway, args.token)
    try:
        for name, document_id in ids.items():
            expected = {case["section"] for case in cases if case["document"] == name}
            available = sections_of(args.gateway, args.token, document_id)
            unknown = expected - available
            if unknown:
                raise SystemExit(f"{name}: sezioni attese assenti dal documento: {sorted(unknown)}")
        _, correct, accuracy = evaluate(args.gateway, args.token, cases, ids)
    finally:
        if not args.keep:
            for document_id in ids.values():
                request("DELETE", f"{args.gateway}/api/documents/{document_id}", args.token)
            print("corpus rimosso dalla libreria")

    if accuracy < args.min_accuracy:
        print(f"gate non superato: serve almeno {args.min_accuracy:.0%}")
        return 1
    print(f"gate superato: {accuracy:.1%} >= {args.min_accuracy:.0%}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
