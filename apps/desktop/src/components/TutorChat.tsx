import { useEffect, useRef, useState } from "react";

import { ApiClient, ApiRequestError } from "../api";
import type { Citation } from "../types";

interface Props {
  client: ApiClient;
  documentId: string | null;
  onCitationClick: (documentId: string) => void;
}

interface Message {
  role: "user" | "assistant";
  text: string;
  citations: Citation[];
  error?: string;
}

function citationLabel(citation: Citation): string {
  if (citation.section) return citation.section;
  if (citation.page !== null) return `pagina ${citation.page}`;
  return citation.document_id.slice(0, 8);
}

export function TutorChat({ client, documentId, onCitationClick }: Props) {
  const [messages, setMessages] = useState<Message[]>([]);
  const [question, setQuestion] = useState("");
  const [streaming, setStreaming] = useState(false);
  const abortRef = useRef<AbortController | null>(null);
  const endRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    endRef.current?.scrollIntoView({ behavior: "smooth", block: "end" });
  }, [messages]);

  const updateLast = (updater: (message: Message) => Message) => {
    setMessages((previous) => {
      const next = [...previous];
      const last = next.at(-1);
      if (last) next[next.length - 1] = updater(last);
      return next;
    });
  };

  const send = async () => {
    const trimmed = question.trim();
    if (!trimmed || streaming) return;

    setQuestion("");
    setStreaming(true);
    setMessages((previous) => [
      ...previous,
      { role: "user", text: trimmed, citations: [] },
      { role: "assistant", text: "", citations: [] },
    ]);

    const controller = new AbortController();
    abortRef.current = controller;

    try {
      for await (const event of client.chat(trimmed, documentId, controller.signal)) {
        if (event.type === "token") {
          updateLast((message) => ({ ...message, text: message.text + event.delta }));
        } else if (event.type === "citation") {
          updateLast((message) => ({
            ...message,
            citations: [...message.citations, event.citation],
          }));
        } else if (event.type === "error") {
          throw new ApiRequestError(event.code, event.message);
        }
      }
    } catch (error) {
      if (error instanceof DOMException && error.name === "AbortError") return;
      updateLast((message) => ({
        ...message,
        error: error instanceof Error ? error.message : "risposta non riuscita",
      }));
    } finally {
      setStreaming(false);
      abortRef.current = null;
    }
  };

  return (
    <section className="chat">
      <div className="chat-scroll">
        {messages.length === 0 && (
          <div className="empty-chat">
            <h1>Studia con le tue fonti</h1>
            <p>
              Importa un documento, selezionalo e chiedi una spiegazione. Ogni
              risposta cita pagina e sezione del materiale originale.
            </p>
            <ul>
              <li>Carica un PDF, DOCX o Markdown dalla colonna a sinistra.</li>
              <li>Lascia selezionata la libreria per cercare in tutti i documenti.</li>
              <li>Ferma la risposta con il pulsante durante la generazione.</li>
            </ul>
          </div>
        )}

        {messages.map((message, index) => (
          <article key={index} className={`message ${message.role}`}>
            <div className="message-role">
              {message.role === "user" ? "Tu" : "Noesis"}
            </div>
            {message.text && <p className="message-text">{message.text}</p>}
            {streaming && index === messages.length - 1 && !message.text && (
              <p className="muted">Sto cercando nelle fonti…</p>
            )}
            {message.error && <p className="notice error">{message.error}</p>}
            {message.citations.length > 0 && (
              <div className="citations">
                {message.citations.map((citation, position) => (
                  <button
                    key={`${citation.document_id}-${position}`}
                    className="citation"
                    title={citation.snippet}
                    onClick={() => onCitationClick(citation.document_id)}
                  >
                    [{position + 1}] {citationLabel(citation)}
                    {citation.page !== null && citation.section
                      ? ` · p. ${citation.page}`
                      : ""}
                  </button>
                ))}
              </div>
            )}
          </article>
        ))}
        <div ref={endRef} />
      </div>

      <form
        className="composer"
        onSubmit={(event) => {
          event.preventDefault();
          void send();
        }}
      >
        <textarea
          value={question}
          onChange={(event) => setQuestion(event.target.value)}
          onKeyDown={(event) => {
            if (event.key === "Enter" && !event.shiftKey) {
              event.preventDefault();
              void send();
            }
          }}
          placeholder={
            documentId
              ? "Chiedi qualcosa sul documento selezionato…"
              : "Chiedi qualcosa su tutta la libreria…"
          }
          rows={2}
        />
        {streaming ? (
          <button
            type="button"
            className="button stop"
            onClick={() => abortRef.current?.abort()}
          >
            Ferma
          </button>
        ) : (
          <button type="submit" className="button primary" disabled={!question.trim()}>
            Invia
          </button>
        )}
      </form>
    </section>
  );
}
