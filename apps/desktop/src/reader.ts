import type { Chunk } from "./types";

export interface ReaderTarget {
  documentId: string;
  page: number | null;
  section: string | null;
}

function normalize(value: string): string {
  return value.trim().toLocaleLowerCase("it");
}

/**
 * Posizione del chunk da evidenziare: prima la sezione citata, poi la pagina.
 * `-1` quando la citazione non individua un punto preciso.
 */
export function selectChunkIndex(
  chunks: Chunk[],
  target: Pick<ReaderTarget, "page" | "section">,
): number {
  if (target.section) {
    const section = normalize(target.section);
    const index = chunks.findIndex(
      (chunk) => chunk.section !== null && normalize(chunk.section) === section,
    );
    if (index !== -1) return index;
  }
  if (target.page !== null) {
    return chunks.findIndex((chunk) => chunk.page === target.page);
  }
  return -1;
}

export function chunkLabel(chunk: Chunk): string | null {
  if (chunk.section && chunk.page !== null) return `${chunk.section} · p. ${chunk.page}`;
  if (chunk.section) return chunk.section;
  if (chunk.page !== null) return `pagina ${chunk.page}`;
  return null;
}
