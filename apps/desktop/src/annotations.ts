import type { Annotation } from "./types";

export interface AnnotatedSegment {
  text: string;
  /** Evidenziazioni e note che coprono il segmento; i segnalibri restano fuori dal testo. */
  annotations: Annotation[];
}

export interface TextOffsets {
  start: number;
  end: number;
}

function marked(annotation: Annotation): boolean {
  return annotation.kind !== "bookmark" && annotation.end > annotation.start;
}

/** Divide il testo nei tratti coperti da almeno un'annotazione, senza perdere nulla. */
export function segmentsFor(text: string, annotations: Annotation[]): AnnotatedSegment[] {
  if (!text) return [];

  const ranges = annotations
    .filter(marked)
    .map((annotation) => ({
      ...annotation,
      start: Math.max(0, annotation.start),
      end: Math.min(text.length, annotation.end),
    }))
    .filter((annotation) => annotation.end > annotation.start);

  if (ranges.length === 0) return [{ text, annotations: [] }];

  const points = new Set<number>([0, text.length]);
  for (const range of ranges) {
    points.add(range.start);
    points.add(range.end);
  }

  const sorted = [...points].sort((left, right) => left - right);
  const segments: AnnotatedSegment[] = [];
  for (let index = 0; index < sorted.length - 1; index += 1) {
    const start = sorted[index] ?? 0;
    const end = sorted[index + 1] ?? text.length;
    if (end <= start) continue;
    segments.push({
      text: text.slice(start, end),
      annotations: ranges.filter((range) => range.start < end && range.end > start),
    });
  }
  return segments;
}

function offsetOf(root: Node, node: Node, offset: number): number {
  const probe = document.createRange();
  probe.setStart(root, 0);
  probe.setEnd(node, offset);
  return probe.toString().length;
}

/** Offset della selezione rispetto al testo contenuto in `root`, in unità UTF-16. */
export function rangeOffsets(root: Node, range: Range): TextOffsets | null {
  if (range.collapsed) return null;
  if (!root.contains(range.startContainer) || !root.contains(range.endContainer)) {
    return null;
  }
  const start = offsetOf(root, range.startContainer, range.startOffset);
  const end = offsetOf(root, range.endContainer, range.endOffset);
  return end > start ? { start, end } : null;
}
