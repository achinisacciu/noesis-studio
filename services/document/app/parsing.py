import re
from dataclasses import dataclass
from pathlib import Path

import docx
import pymupdf
from noesis_contracts import Chunk

HEADING = re.compile(r"^(#{1,6})\s+(.*)$")


@dataclass
class Block:
    text: str
    page: int | None = None
    section: str | None = None


def parse_markdown(path: Path) -> list[Block]:
    blocks: list[Block] = []
    section: str | None = None
    buffer: list[str] = []

    def flush() -> None:
        if buffer:
            blocks.append(Block("\n".join(buffer), None, section))
            buffer.clear()

    for line in path.read_text(encoding="utf-8").splitlines():
        heading = HEADING.match(line)
        if heading:
            flush()
            section = heading.group(2).strip() or None
        elif line.strip():
            buffer.append(line.strip())
        else:
            flush()
    flush()
    return blocks


def parse_docx(path: Path) -> list[Block]:
    blocks: list[Block] = []
    section: str | None = None
    buffer: list[str] = []

    def flush() -> None:
        if buffer:
            blocks.append(Block("\n".join(buffer), None, section))
            buffer.clear()

    for paragraph in docx.Document(str(path)).paragraphs:
        text = paragraph.text.strip()
        if not text:
            continue
        style = paragraph.style.name if paragraph.style is not None else ""
        if style.startswith("Heading"):
            flush()
            section = text
        else:
            buffer.append(text)
    flush()
    return blocks


def parse_pdf(path: Path) -> list[Block]:
    blocks: list[Block] = []
    with pymupdf.open(path) as pdf:  # type: ignore[no-untyped-call]
        for page_number, page in enumerate(pdf, start=1):
            for block in page.get_text("blocks"):
                text = " ".join(str(block[4]).split())
                if text:
                    blocks.append(Block(text, page_number))
    return blocks


PARSERS = {
    ".md": parse_markdown,
    ".markdown": parse_markdown,
    ".txt": parse_markdown,
    ".docx": parse_docx,
    ".pdf": parse_pdf,
}


def chunk_blocks(document_id: str, blocks: list[Block], max_chars: int = 800) -> list[Chunk]:
    chunks: list[Chunk] = []
    buffer: list[str] = []
    size = 0
    page: int | None = None
    section: str | None = None

    def flush() -> None:
        nonlocal buffer, size
        if not buffer:
            return
        position = len(chunks)
        chunks.append(
            Chunk(
                id=f"{document_id}:{position}",
                document_id=document_id,
                position=position,
                text="\n".join(buffer),
                page=page,
                section=section,
            )
        )
        buffer = []
        size = 0

    for block in blocks:
        if block.page != page or block.section != section:
            flush()
            page, section = block.page, block.section
        if size + len(block.text) > max_chars:
            flush()
        buffer.append(block.text)
        size += len(block.text)
    flush()
    return chunks
