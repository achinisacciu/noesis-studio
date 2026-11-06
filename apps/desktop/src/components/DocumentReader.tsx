import { useMutation, useQuery, useQueryClient } from "@tanstack/react-query";
import { useEffect, useMemo, useRef, useState } from "react";

import type { ApiClient } from "../api";
import { chunkLabel, selectChunkIndex, type ReaderTarget } from "../reader";
import type { Chunk } from "../types";

interface Props {
  client: ApiClient;
  target: ReaderTarget;
  onClose: () => void;
}

export function DocumentReader({ client, target, onClose }: Props) {
  const queryClient = useQueryClient();
  const [draft, setDraft] = useState<{ chunk: Chunk; front: string; back: string } | null>(null);
  const [notice, setNotice] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);

  const chunks = useQuery({
    queryKey: ["chunks", target.documentId],
    queryFn: () => client.getChunks(target.documentId),
  });
  const documents = useQuery({
    queryKey: ["documents"],
    queryFn: () => client.listDocuments(),
  });

  const activeIndex = useMemo(
    () => (chunks.data ? selectChunkIndex(chunks.data, target) : -1),
    [chunks.data, target],
  );

  const activeRef = useRef<HTMLElement>(null);
  useEffect(() => {
    activeRef.current?.scrollIntoView({ block: "start", behavior: "smooth" });
  }, [activeIndex, chunks.data]);

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
        <button className="icon-button" onClick={onClose} title="Chiudi documento">
          ✕
        </button>
      </header>

      <div className="reader-body">
        {notice && <p className="notice">{notice}</p>}
        {chunks.isLoading && <p className="muted">Apro il documento…</p>}
        {chunks.isError && <p className="notice error">Testo non disponibile.</p>}
        {chunks.data?.map((chunk, index) => (
          <article
            key={chunk.id}
            ref={index === activeIndex ? activeRef : undefined}
            className={`reader-chunk ${index === activeIndex ? "active" : ""}`}
          >
            {chunkLabel(chunk) && (
              <span className="reader-label">{chunkLabel(chunk)}</span>
            )}
            <p>{chunk.text}</p>
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
        ))}
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
    </aside>
  );
}
