export interface Segment {
  type: "text" | "strong" | "code";
  value: string;
}

const PATTERN = /(\*\*[^*]+\*\*|`[^`]+`)/g;

/** I modelli locali usano spesso "* voce" o "- voce": li rendiamo come elenco leggibile. */
export function normalizeListMarkers(text: string): string {
  return text.replace(/^[ \t]*[*-][ \t]+/gm, "• ");
}

/** Grassetto e codice inline: quanto basta per le risposte del tutor, senza dipendenze. */
export function formatInline(text: string): Segment[] {
  return normalizeListMarkers(text)
    .split(PATTERN)
    .filter((part) => part !== "")
    .map((part) => {
      if (part.startsWith("**") && part.endsWith("**") && part.length > 4) {
        return { type: "strong", value: part.slice(2, -2) };
      }
      if (part.startsWith("`") && part.endsWith("`") && part.length > 2) {
        return { type: "code", value: part.slice(1, -1) };
      }
      return { type: "text", value: part };
    });
}
