import { useMutation, useQuery, useQueryClient } from "@tanstack/react-query";
import { useRef, useState } from "react";

import { ApiClient } from "../api";
import type { DocumentSummary } from "../types";

interface Props {
  client: ApiClient;
  selectedId: string | null;
  onSelect: (documentId: string | null) => void;
}

function errorMessage(error: unknown): string {
  return error instanceof Error ? error.message : "operazione non riuscita";
}

export function DocumentPanel({ client, selectedId, onSelect }: Props) {
  const queryClient = useQueryClient();
  const inputRef = useRef<HTMLInputElement>(null);
  const [error, setError] = useState<string | null>(null);

  const documents = useQuery({
    queryKey: ["documents"],
    queryFn: () => client.listDocuments(),
    // all'avvio desktop i servizi possono impiegare qualche secondo
    retry: 5,
    retryDelay: (attempt) => Math.min(2000, 400 * attempt),
  });

  const refresh = () => queryClient.invalidateQueries({ queryKey: ["documents"] });

  const importMutation = useMutation({
    mutationFn: async (file: File) => {
      const document = await client.importDocument(file);
      await client.indexDocument(document.id);
      return document;
    },
    onMutate: () => setError(null),
    onSuccess: (document) => onSelect(document.id),
    onError: (mutationError) => setError(errorMessage(mutationError)),
    onSettled: refresh,
  });

  const deleteMutation = useMutation({
    mutationFn: (document: DocumentSummary) => client.deleteDocument(document.id),
    onMutate: () => setError(null),
    onSuccess: (_data, document) => {
      if (document.id === selectedId) onSelect(null);
    },
    onError: (mutationError) => setError(errorMessage(mutationError)),
    onSettled: refresh,
  });

  const rebuildMutation = useMutation({
    mutationFn: () => client.rebuildIndex(),
    onMutate: () => setError(null),
    onError: (mutationError) => setError(errorMessage(mutationError)),
  });

  const busy = importMutation.isPending || deleteMutation.isPending;

  return (
    <aside className="panel">
      <div className="panel-head">
        <h2>Documenti</h2>
        <button
          className="button primary"
          disabled={busy}
          onClick={() => inputRef.current?.click()}
          title="Importa PDF, DOCX, Markdown o TXT"
        >
          {importMutation.isPending ? "Importo…" : "Importa"}
        </button>
        <input
          ref={inputRef}
          className="visually-hidden"
          type="file"
          accept=".pdf,.docx,.md,.markdown,.txt"
          onChange={(event) => {
            const file = event.target.files?.[0];
            event.target.value = "";
            if (file) importMutation.mutate(file);
          }}
        />
      </div>

      {error && <p className="notice error">{error}</p>}

      <div className="document-list">
        {documents.isLoading && <p className="muted">Carico i documenti…</p>}
        {documents.isError && (
          <div className="notice error">
            <p>Gateway non raggiungibile. Avvia lo stack con `python scripts/stack.py --dev`.</p>
            <button className="button ghost" onClick={() => void documents.refetch()}>
              Riprova
            </button>
          </div>
        )}
        {documents.data?.length === 0 && (
          <p className="muted">
            Nessun documento. Importa un PDF o un file Markdown per iniziare.
          </p>
        )}
        {documents.data?.map((document) => (
          <div
            key={document.id}
            className={`document ${document.id === selectedId ? "selected" : ""}`}
          >
            <button
              className="document-open"
              onClick={() => onSelect(document.id)}
              title={document.filename}
            >
              <span className="document-title">{document.title}</span>
              <span className="document-meta">
                {document.chunk_count} chunk · {document.filename}
              </span>
            </button>
            <button
              className="icon-button"
              disabled={busy}
              onClick={() => deleteMutation.mutate(document)}
              title="Elimina documento e indice"
            >
              ✕
            </button>
          </div>
        ))}
      </div>

      <div className="panel-foot">
        <button
          className="button"
          disabled={rebuildMutation.isPending}
          onClick={() => rebuildMutation.mutate()}
          title="Ricostruisce l'indice vettoriale da SQLite"
        >
          {rebuildMutation.isPending ? "Ricostruisco…" : "Ricostruisci indice"}
        </button>
        {selectedId && (
          <button className="button ghost" onClick={() => onSelect(null)}>
            Tutta la libreria
          </button>
        )}
      </div>
    </aside>
  );
}
