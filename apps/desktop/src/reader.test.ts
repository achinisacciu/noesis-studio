import { describe, expect, it } from "vitest";

import { chunkLabel, selectChunkIndex } from "./reader";
import type { Chunk } from "./types";

const chunk = (overrides: Partial<Chunk>): Chunk => ({
  id: "c",
  document_id: "d1",
  position: 0,
  text: "testo",
  page: null,
  section: null,
  ...overrides,
});

const CHUNKS = [
  chunk({ id: "c0", position: 0, section: "Varianza", page: 1 }),
  chunk({ id: "c1", position: 1, section: "Deviazione standard", page: 2 }),
  chunk({ id: "c2", position: 2, section: "Mediana", page: 2 }),
];

describe("selectChunkIndex", () => {
  it("preferisce la sezione citata, ignorando maiuscole e spazi", () => {
    expect(selectChunkIndex(CHUNKS, { section: "  deviazione STANDARD ", page: 1 })).toBe(1);
  });

  it("usa la pagina quando la sezione non esiste nel documento", () => {
    expect(selectChunkIndex(CHUNKS, { section: "Sezione rimossa", page: 2 })).toBe(1);
  });

  it("restituisce -1 quando la citazione non ha riferimenti", () => {
    expect(selectChunkIndex(CHUNKS, { section: null, page: null })).toBe(-1);
  });
});

describe("chunkLabel", () => {
  it("unisce sezione e pagina e tollera i valori mancanti", () => {
    expect(chunkLabel(CHUNKS[0] as Chunk)).toBe("Varianza · p. 1");
    expect(chunkLabel(chunk({ section: "Solo sezione" }))).toBe("Solo sezione");
    expect(chunkLabel(chunk({ page: 7 }))).toBe("pagina 7");
    expect(chunkLabel(chunk({}))).toBeNull();
  });
});
