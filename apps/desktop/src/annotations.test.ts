import { describe, expect, it } from "vitest";

import { rangeOffsets, segmentsFor } from "./annotations";
import type { Annotation } from "./types";

const annotation = (overrides: Partial<Annotation>): Annotation => ({
  id: "a",
  document_id: "d1",
  chunk_id: "d1:0",
  kind: "highlight",
  start: 0,
  end: 0,
  note: "",
  created_at: "2026-01-01T00:00:00Z",
  ...overrides,
});

describe("segmentsFor", () => {
  it("marca solo l'intervallo selezionato", () => {
    const segments = segmentsFor("La varianza misura", [annotation({ start: 3, end: 11 })]);
    expect(segments.map((segment) => segment.text)).toEqual(["La ", "varianza", " misura"]);
    expect(segments.map((segment) => segment.annotations.length)).toEqual([0, 1, 0]);
  });

  it("ignora i segnalibri e ritaglia gli intervalli oltre il testo", () => {
    const segments = segmentsFor("testo", [
      annotation({ kind: "bookmark" }),
      annotation({ start: 2, end: 99 }),
    ]);
    expect(segments.map((segment) => segment.text)).toEqual(["te", "sto"]);
    expect(segments[1]?.annotations).toHaveLength(1);
  });

  it("unisce annotazioni sovrapposte nello stesso segmento", () => {
    const segments = segmentsFor("abcdef", [
      annotation({ id: "uno", start: 1, end: 4 }),
      annotation({ id: "due", start: 3, end: 5 }),
    ]);
    expect(
      segments.map((segment) => ({
        text: segment.text,
        ids: segment.annotations.map((item) => item.id),
      })),
    ).toEqual([
      { text: "a", ids: [] },
      { text: "bc", ids: ["uno"] },
      { text: "d", ids: ["uno", "due"] },
      { text: "e", ids: ["due"] },
      { text: "f", ids: [] },
    ]);
  });

  it("restituisce un solo segmento quando non ci sono annotazioni", () => {
    expect(segmentsFor("testo", [])).toEqual([{ text: "testo", annotations: [] }]);
    expect(segmentsFor("", [])).toEqual([]);
  });
});

describe("rangeOffsets", () => {
  it("misura la selezione anche tra elementi figli", () => {
    const paragraph = document.createElement("p");
    paragraph.innerHTML = "abc<mark>de</mark>f";
    const range = document.createRange();
    range.setStart(paragraph.firstChild as Text, 1);
    range.setEnd(paragraph.lastChild as Text, 1);

    expect(rangeOffsets(paragraph, range)).toEqual({ start: 1, end: 6 });
  });

  it("rifiuta una selezione fuori dal passaggio", () => {
    const paragraph = document.createElement("p");
    paragraph.textContent = "testo";
    const other = document.createElement("p");
    other.textContent = "altro";
    const range = document.createRange();
    range.selectNodeContents(other);

    expect(rangeOffsets(paragraph, range)).toBeNull();
  });

  it("rifiuta una selezione vuota", () => {
    const paragraph = document.createElement("p");
    paragraph.textContent = "testo";
    const range = document.createRange();
    range.setStart(paragraph.firstChild as Text, 2);
    range.setEnd(paragraph.firstChild as Text, 2);

    expect(rangeOffsets(paragraph, range)).toBeNull();
  });
});
