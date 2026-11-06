import { useMutation, useQuery, useQueryClient } from "@tanstack/react-query";
import { useState } from "react";

import type { ApiClient } from "../api";
import type { Flashcard } from "../types";

interface Props {
  client: ApiClient;
  documentId: string | null;
  onClose: () => void;
}

function errorMessage(error: unknown): string {
  return error instanceof Error ? error.message : "operazione non riuscita";
}

export function FlashcardsPanel({ client, documentId, onClose }: Props) {
  const queryClient = useQueryClient();
  const [onlySelected, setOnlySelected] = useState(false);
  const [revealed, setRevealed] = useState<string | null>(null);
  const [editing, setEditing] = useState<string | null>(null);
  const [draft, setDraft] = useState({ front: "", back: "" });
  const [error, setError] = useState<string | null>(null);

  const filterId = onlySelected ? documentId : null;
  const cards = useQuery({
    queryKey: ["flashcards", filterId],
    queryFn: () => client.listFlashcards(filterId),
  });
  const documents = useQuery({
    queryKey: ["documents"],
    queryFn: () => client.listDocuments(),
  });

  const refresh = () => queryClient.invalidateQueries({ queryKey: ["flashcards"] });

  const saveMutation = useMutation({
    mutationFn: (card: Flashcard) =>
      client.updateFlashcard(card.id, { front: draft.front.trim(), back: draft.back.trim() }),
    onMutate: () => setError(null),
    onSuccess: () => setEditing(null),
    onError: (mutationError) => setError(errorMessage(mutationError)),
    onSettled: refresh,
  });

  const deleteMutation = useMutation({
    mutationFn: (card: Flashcard) => client.deleteFlashcard(card.id),
    onMutate: () => setError(null),
    onError: (mutationError) => setError(errorMessage(mutationError)),
    onSettled: refresh,
  });

  const titleOf = (documentId: string) =>
    documents.data?.find((document) => document.id === documentId)?.title ?? "Documento";

  const startEditing = (card: Flashcard) => {
    setEditing(card.id);
    setDraft({ front: card.front, back: card.back });
  };

  return (
    <aside className="reader" aria-label="Flashcard">
      <header className="reader-head">
        <div>
          <strong>Schede</strong>
          <span className="muted"> · {cards.data?.length ?? 0}</span>
        </div>
        <button className="icon-button" onClick={onClose} title="Chiudi schede">
          ✕
        </button>
      </header>

      <div className="cards-toolbar">
        <label className="checkbox">
          <input
            type="checkbox"
            checked={onlySelected}
            disabled={!documentId}
            onChange={(event) => setOnlySelected(event.target.checked)}
          />
          Solo il documento selezionato
        </label>
      </div>

      {error && <p className="notice error">{error}</p>}

      <div className="reader-body">
        {cards.isLoading && <p className="muted">Carico le schede…</p>}
        {cards.isError && <p className="notice error">Schede non disponibili.</p>}
        {cards.data?.length === 0 && (
          <p className="muted">
            Nessuna scheda. Apri un documento e usa “Crea scheda” su un passaggio.
          </p>
        )}
        {cards.data?.map((card) => (
          <article key={card.id} className="flashcard">
            <span className="reader-label">
              {titleOf(card.document_id)}
              {card.section ? ` · ${card.section}` : ""}
              {card.page !== null ? ` · p. ${card.page}` : ""}
            </span>

            {editing === card.id ? (
              <div className="flashcard-edit">
                <textarea
                  aria-label="Fronte della scheda"
                  value={draft.front}
                  onChange={(event) => setDraft({ ...draft, front: event.target.value })}
                  rows={2}
                />
                <textarea
                  aria-label="Retro della scheda"
                  value={draft.back}
                  onChange={(event) => setDraft({ ...draft, back: event.target.value })}
                  rows={4}
                />
                <div className="flashcard-actions">
                  <button
                    className="button primary"
                    disabled={!draft.front.trim() || !draft.back.trim() || saveMutation.isPending}
                    onClick={() => saveMutation.mutate(card)}
                  >
                    {saveMutation.isPending ? "Salvo…" : "Salva"}
                  </button>
                  <button className="button ghost" onClick={() => setEditing(null)}>
                    Annulla
                  </button>
                </div>
              </div>
            ) : (
              <>
                <p className="flashcard-front">{card.front}</p>
                {revealed === card.id && <p className="flashcard-back">{card.back}</p>}
                <div className="flashcard-actions">
                  <button
                    className="button ghost"
                    onClick={() => setRevealed(revealed === card.id ? null : card.id)}
                  >
                    {revealed === card.id ? "Nascondi" : "Mostra risposta"}
                  </button>
                  <button className="button ghost" onClick={() => startEditing(card)}>
                    Modifica
                  </button>
                  <button
                    className="icon-button"
                    disabled={deleteMutation.isPending}
                    onClick={() => deleteMutation.mutate(card)}
                    title="Elimina scheda"
                  >
                    ✕
                  </button>
                </div>
              </>
            )}
          </article>
        ))}
      </div>
    </aside>
  );
}
