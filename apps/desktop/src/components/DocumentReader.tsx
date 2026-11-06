import { useMutation, useQuery, useQueryClient } from "@tanstack/react-query";
import { useEffect, useMemo, useRef, useState } from "react";

import type { ApiClient } from "../api";
import { rangeOffsets, segmentsFor } from "../annotations";
import { chunkLabel, selectStartIndex, type ReaderTarget } from "../reader";
import type { AnnotationKind, Chunk } from "../types";

interface Props {
  client: ApiClient;
  target: ReaderTarget;
  onClose: () => void;
}

interface SelectionState {
  chunk: Chunk;
  start: number;
  end: number;
  text: string;
}

interface NoteDraft extends SelectionState {
  note: string;
}

const KIND_LABEL: Record<AnnotationKind, string> = {
  highlight: "Evidenziazione",
  note: "Nota",
  bookmark: "Segnalibro",
};

function excerpt(text: string, length = 110): string {
  const compact = text.replace(/\s+/g, " ").trim();
  return compact.length > length ? `${compact.slice(0, length)}…` : compact;
}

export function DocumentReader({ client, target, onClose }: Props) {
  const queryClient = useQueryClient();
  const [draft, setDraft] = useState<{ chunk: Chunk; front: string; back: string } | null>(null);
  const [selection, setSelection] = useState<SelectionState | null>(null);
  const [noteDraft, setNoteDraft] = useState<NoteDraft | null>(null);
  const [search, setSearch] = useState("");
  const [showAnnotations, setShowAnnotations] = useState(false);
  const [notice, setNotice] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);
  const bodyRef = useRef<HTMLDivElement>(null);

  const chunks = useQuery({
    queryKey: ["chunks", target.documentId],
    queryFn: () => client.getChunks(target.documentId),
  });
  const documents = useQuery({
    queryKey: ["documents"],
    queryFn: () => client.listDocuments(),
  });
  const resume = useQuery({
    queryKey: ["reading-position", target.documentId],
    queryFn: () => client.getReadingPosition(target.documentId),
    // la citazione indica già il punto: la posizione salvata serve solo all'apertura libera
    enabled: target.section === null && target.page === null,
  });
  const annotations = useQuery({
    queryKey: ["annotations", target.documentId],
    queryFn: () => client.listAnnotations(target.documentId),
  });

  const annotationList = useMemo(() => annotations.data ?? [], [annotations.data]);
  const chunksById = useMemo(
    () => new Map((chunks.data ?? []).map((chunk) => [chunk.id, chunk] as const)),
    [chunks.data],
  );
  const visibleAnnotations = useMemo(() => {
    const term = search.trim().toLocaleLowerCase("it");
    if (!term) return annotationList;
    return annotationList.filter((annotation) =>
      `${annotation.note} ${chunksById.get(annotation.chunk_id)?.text ?? ""}`
        .toLocaleLowerCase("it")
        .includes(term),
    );
  }, [annotationList, chunksById, search]);

  const activeIndex = useMemo(
    () =>
      chunks.data
        ? selectStartIndex(chunks.data, target, resume.data?.chunk_id ?? null)
        : -1,
    [chunks.data, target, resume.data],
  );

  const activeRef = useRef<HTMLElement>(null);
  useEffect(() => {
    activeRef.current?.scrollIntoView({ block: "start", behavior: "smooth" });
  }, [activeIndex, chunks.data]);

  // la posizione è "l'ultimo chunk che ha superato il bordo superiore del lettore"
  useEffect(() => {
    const root = bodyRef.current;
    if (!root || !chunks.data?.length) return;
    let frame = 0;
    let lastSaved = "";
    const track = () => {
      frame = 0;
      const rootTop = root.getBoundingClientRect().top;
      let current: HTMLElement | null = null;
      for (const item of root.querySelectorAll<HTMLElement>("[data-chunk-id]")) {
        if (item.getBoundingClientRect().top - rootTop <= 12) current = item;
      }
      const chunk = chunks.data?.find((item) => item.id === current?.dataset.chunkId);
      if (!chunk || chunk.id === lastSaved) return;
      lastSaved = chunk.id;
      void client
        .saveReadingPosition(target.documentId, chunk.id, chunk.position)
        .catch(() => undefined);
    };
    const onScroll = () => {
      if (!frame) frame = requestAnimationFrame(track);
    };
    root.addEventListener("scroll", onScroll, { passive: true });
    return () => {
      root.removeEventListener("scroll", onScroll);
      if (frame) cancelAnimationFrame(frame);
    };
  }, [chunks.data, client, target.documentId]);

  const createCard = useMutation({
    mutationFn: () =>
      client.createFlashcard({
        document_id: target.documentId,
        front: draft?.front.trim() ?? "",
        back: draft?.back.trim() ?? "",
        page: draft?.chunk.page ?? null,
        section: draft?.chunk.section ?? null,
      }),
    onMutate: () => {
      setError(null);
      setNotice(null);
    },
    onSuccess: () => {
      setDraft(null);
      setNotice("Scheda salvata. La trovi in “Schede”.");
    },
    onError: (mutationError) =>
      setError(mutationError instanceof Error ? mutationError.message : "scheda non salvata"),
    onSettled: () => queryClient.invalidateQueries({ queryKey: ["flashcards"] }),
  });

  const invalidateAnnotations = () =>
    queryClient.invalidateQueries({ queryKey: ["annotations", target.documentId] });

  const createAnnotation = useMutation({
    mutationFn: (input: Parameters<ApiClient["createAnnotation"]>[1]) =>
      client.createAnnotation(target.documentId, input),
    onMutate: () => {
      setError(null);
      setNotice(null);
    },
    onError: (mutationError) =>
      setError(mutationError instanceof Error ? mutationError.message : "annotazione non salvata"),
    onSettled: invalidateAnnotations,
  });

  const removeAnnotation = useMutation({
    mutationFn: (annotationId: string) => client.deleteAnnotation(annotationId),
    onMutate: () => {
      setError(null);
      setNotice(null);
    },
    onError: (mutationError) =>
      setError(mutationError instanceof Error ? mutationError.message : "annotazione non eliminata"),
    onSettled: invalidateAnnotations,
  });

  const annotationsFor = (chunkId: string) =>
    annotationList.filter((annotation) => annotation.chunk_id === chunkId);

  const readSelection = (chunk: Chunk, element: HTMLParagraphElement) => {
    const current = window.getSelection();
    if (!current || current.rangeCount === 0) return;
    const offsets = rangeOffsets(element, current.getRangeAt(0));
    setSelection(
      offsets
        ? { chunk, start: offsets.start, end: offsets.end, text: chunk.text.slice(offsets.start, offsets.end) }
        : null,
    );
  };

  const saveHighlight = () => {
    if (!selection) return;
    createAnnotation.mutate(
      {
        chunk_id: selection.chunk.id,
        kind: "highlight",
        start: selection.start,
        end: selection.end,
      },
      {
        onSuccess: () => {
          setSelection(null);
          setNotice("Evidenziazione salvata.");
        },
      },
    );
  };

  const saveNote = () => {
    if (!noteDraft || !noteDraft.note.trim()) return;
    createAnnotation.mutate(
      {
        chunk_id: noteDraft.chunk.id,
        kind: "note",
        start: noteDraft.start,
        end: noteDraft.end,
        note: noteDraft.note.trim(),
      },
      {
        onSuccess: () => {
          setNoteDraft(null);
          setSelection(null);
          setNotice("Nota salvata.");
        },
      },
    );
  };

  const toggleBookmark = (chunk: Chunk) => {
    const existing = annotationList.find(
      (annotation) => annotation.chunk_id === chunk.id && annotation.kind === "bookmark",
    );
    if (existing) {
      removeAnnotation.mutate(existing.id, {
        onSuccess: () => setNotice("Segnalibro rimosso."),
      });
      return;
    }
    createAnnotation.mutate(
      { chunk_id: chunk.id, kind: "bookmark" },
      { onSuccess: () => setNotice("Segnalibro aggiunto.") },
    );
  };

  const jumpToChunk = (chunkId: string) => {
    bodyRef.current
      ?.querySelector<HTMLElement>(`[data-chunk-id="${chunkId}"]`)
      ?.scrollIntoView({ block: "start", behavior: "smooth" });
  };

  const title =
    documents.data?.find((document) => document.id === target.documentId)?.title ??
    "Documento";

  return (
    <aside className="reader" aria-label="Documento">
      <header className="reader-head">
        <div>
          <strong>{title}</strong>
          {target.section && <span className="muted"> · {target.section}</span>}
        </div>
        <div className="reader-head-actions">
          <button
            className="button ghost reader-toggle"
            aria-pressed={showAnnotations}
            onClick={() => setShowAnnotations((current) => !current)}
          >
            Annotazioni {annotationList.length > 0 ? annotationList.length : ""}
          </button>
          <button className="icon-button" onClick={onClose} title="Chiudi documento">
            ✕
          </button>
        </div>
      </header>

      {selection && (
        <div className="annotation-bar">
          <span className="annotation-quote">“{excerpt(selection.text)}”</span>
          <div className="annotation-actions">
            <button
              className="button primary"
              disabled={createAnnotation.isPending}
              onClick={saveHighlight}
            >
              Evidenzia
            </button>
            <button
              className="button ghost"
              onClick={() => setNoteDraft({ ...selection, note: "" })}
            >
              Nota
            </button>
            <button className="button ghost" onClick={() => setSelection(null)}>
              Annulla
            </button>
          </div>
        </div>
      )}

      {showAnnotations && (
        <div className="annotation-panel">
          <input
            type="search"
            value={search}
            onChange={(event) => setSearch(event.target.value)}
            placeholder="Cerca nelle annotazioni…"
            aria-label="Cerca nelle annotazioni"
          />
          {annotations.isLoading && <p className="muted">Carico le annotazioni…</p>}
          {annotations.isError && <p className="notice error">Annotazioni non disponibili.</p>}
          {!annotations.isLoading && visibleAnnotations.length === 0 && (
            <p className="muted">Nessuna annotazione.</p>
          )}
          <ul className="annotation-items">
            {visibleAnnotations.map((annotation) => (
              <li key={annotation.id} className="annotation-item">
                <button
                  className="annotation-jump"
                  onClick={() => jumpToChunk(annotation.chunk_id)}
                >
                  <span className="annotation-kind">{KIND_LABEL[annotation.kind]}</span>
                  <span className="annotation-excerpt">
                    {excerpt(chunksById.get(annotation.chunk_id)?.text ?? "")}
                  </span>
                  {annotation.note && (
                    <span className="annotation-note">{annotation.note}</span>
                  )}
                </button>
                <button
                  className="icon-button"
                  title="Elimina annotazione"
                  onClick={() => removeAnnotation.mutate(annotation.id)}
                >
                  ✕
                </button>
              </li>
            ))}
          </ul>
        </div>
      )}

      <div className="reader-body" ref={bodyRef}>
        {notice && <p className="notice">{notice}</p>}
        {error && !draft && !noteDraft && <p className="notice error">{error}</p>}
        {chunks.isLoading && <p className="muted">Apro il documento…</p>}
        {chunks.isError && <p className="notice error">Testo non disponibile.</p>}
        {chunks.data?.map((chunk, index) => {
          const items = annotationsFor(chunk.id);
          const bookmarked = items.some((annotation) => annotation.kind === "bookmark");
          return (
            <article
              key={chunk.id}
              data-chunk-id={chunk.id}
              ref={index === activeIndex ? activeRef : undefined}
              className={`reader-chunk ${index === activeIndex ? "active" : ""}`}
            >
              <div className="reader-chunk-head">
                {chunkLabel(chunk) ? (
                  <span className="reader-label">{chunkLabel(chunk)}</span>
                ) : (
                  <span />
                )}
                <button
                  className={`icon-button bookmark ${bookmarked ? "on" : ""}`}
                  title={bookmarked ? "Rimuovi segnalibro" : "Aggiungi segnalibro"}
                  aria-pressed={bookmarked}
                  onClick={() => toggleBookmark(chunk)}
                >
                  {bookmarked ? "★" : "☆"}
                </button>
              </div>
              <p onMouseUp={(event) => readSelection(chunk, event.currentTarget)}>
                {segmentsFor(chunk.text, items).map((segment, position) => {
                  const notes = segment.annotations
                    .map((annotation) => annotation.note)
                    .filter(Boolean);
                  return segment.annotations.length > 0 ? (
                    <mark
                      key={position}
                      className="reader-mark"
                      title={notes.length > 0 ? notes.join("\n") : undefined}
                    >
                      {segment.text}
                    </mark>
                  ) : (
                    <span key={position}>{segment.text}</span>
                  );
                })}
              </p>
              <button
                className="button ghost reader-action"
                onClick={() =>
                  setDraft({
                    chunk,
                    front: chunk.section ? `Spiega: ${chunk.section}` : "Spiega questo passaggio",
                    back: chunk.text,
                  })
                }
              >
                Crea scheda
              </button>
            </article>
          );
        })}
      </div>

      {draft && (
        <div className="modal-backdrop" role="presentation">
          <form
            className="modal"
            aria-label="Nuova flashcard"
            onSubmit={(event) => {
              event.preventDefault();
              createCard.mutate();
            }}
          >
            <h2>Nuova scheda</h2>
            <label>
              Fronte
              <textarea
                value={draft.front}
                onChange={(event) => setDraft({ ...draft, front: event.target.value })}
                rows={2}
              />
            </label>
            <label>
              Retro
              <textarea
                value={draft.back}
                onChange={(event) => setDraft({ ...draft, back: event.target.value })}
                rows={6}
              />
            </label>
            {error && <p className="notice error">{error}</p>}
            <div className="flashcard-actions">
              <button
                type="submit"
                className="button primary"
                disabled={!draft.front.trim() || !draft.back.trim() || createCard.isPending}
              >
                {createCard.isPending ? "Salvo…" : "Salva scheda"}
              </button>
              <button type="button" className="button ghost" onClick={() => setDraft(null)}>
                Annulla
              </button>
            </div>
          </form>
        </div>
      )}

      {noteDraft && (
        <div className="modal-backdrop" role="presentation">
          <form
            className="modal"
            aria-label="Nuova annotazione"
            onSubmit={(event) => {
              event.preventDefault();
              saveNote();
            }}
          >
            <h2>Nuova nota</h2>
            <p className="annotation-quote">“{excerpt(noteDraft.text, 160)}”</p>
            <label>
              Nota
              <textarea
                value={noteDraft.note}
                onChange={(event) => setNoteDraft({ ...noteDraft, note: event.target.value })}
                rows={4}
                autoFocus
              />
            </label>
            {error && <p className="notice error">{error}</p>}
            <div className="flashcard-actions">
              <button
                type="submit"
                className="button primary"
                disabled={!noteDraft.note.trim() || createAnnotation.isPending}
              >
                {createAnnotation.isPending ? "Salvo…" : "Salva nota"}
              </button>
              <button type="button" className="button ghost" onClick={() => setNoteDraft(null)}>
                Annulla
              </button>
            </div>
          </form>
        </div>
      )}
    </aside>
  );
}
