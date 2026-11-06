import re

from noesis_contracts import SearchHit

TOKEN = re.compile(r"[a-z0-9]+")


def extract_hits(query: str, text: str) -> list[SearchHit]:
    terms = {term for term in TOKEN.findall(query.lower()) if len(term) > 2}
    if not terms:
        return []
    sentences = re.split(r"(?<=[.!?])\s+", text.strip())
    return [
        SearchHit(text=sentence, position=position)
        for position, sentence in enumerate(sentences)
        if any(term in sentence.lower() for term in terms)
    ]
