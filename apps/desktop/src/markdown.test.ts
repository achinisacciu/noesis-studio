import { describe, expect, it } from "vitest";

import { formatInline, normalizeListMarkers } from "./markdown";
describe("formatInline", () => {
  it("separa grassetto e codice dal testo normale", () => {
    expect(formatInline("La **varianza** misura `x` e altro")).toEqual([
      { type: "text", value: "La " },
      { type: "strong", value: "varianza" },
      { type: "text", value: " misura " },
      { type: "code", value: "x" },
      { type: "text", value: " e altro" },
    ]);
  });

  it("lascia intatto il testo senza marcatori", () => {
    expect(formatInline("Nessuna fonte nei documenti.")).toEqual([
      { type: "text", value: "Nessuna fonte nei documenti." },
    ]);
  });

  it("non interpreta asterischi spaiati o marcatori vuoti", () => {
    expect(formatInline("5 * 3 = 15 e ****")).toEqual([
      { type: "text", value: "5 * 3 = 15 e ****" },
    ]);
  });

  it("trasforma i marcatori di elenco in punti", () => {
    expect(normalizeListMarkers("Testo:\n* uno\n  - due")).toBe("Testo:\n• uno\n• due");
  });
});
