from noesis_ai_adapters import ChatMessage
from noesis_contracts import Citation, SearchHit

SYSTEM_PROMPT = """Sei Noesis, un tutor di statistica, matematica e machine learning.
Rispondi in italiano, in modo chiaro e concreto.
Usa esclusivamente le fonti fornite nel messaggio dell'utente.
Ogni affermazione tratta dalle fonti deve avere una citazione numerica, per esempio [1] o [2].
Se le fonti non contengono la risposta, dichiara: "Nessuna fonte nei documenti".
Non inventare dati, pagine o sezioni."""


def citations_from_hits(hits: list[SearchHit]) -> list[Citation]:
    return [
        Citation(
            document_id=hit.document_id,
            page=hit.page,
            section=hit.section,
            snippet=hit.text,
        )
        for hit in hits
    ]


def build_messages(question: str, hits: list[SearchHit]) -> list[ChatMessage]:
    sources = []
    for position, hit in enumerate(hits, start=1):
        where = [f"documento {hit.document_id}"]
        if hit.page is not None:
            where.append(f"pagina {hit.page}")
        if hit.section:
            where.append(f"sezione {hit.section}")
        sources.append(f"[{position}] {' | '.join(where)}\n{hit.text}")

    user = (
        "FONTI:\n" + "\n\n".join(sources) + f"\n\nDOMANDA:\n{question}\n\n"
        "Rispondi citando le fonti con [n]. Se non bastano, dillo esplicitamente."
    )
    return [
        ChatMessage(role="system", content=SYSTEM_PROMPT),
        ChatMessage(role="user", content=user),
    ]
