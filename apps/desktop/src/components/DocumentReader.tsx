import { useQuery } from "@tanstack/react-query";
import { useEffect, useMemo, useRef } from "react";

import type { ApiClient } from "../api";
import { chunkLabel, selectChunkIndex, type ReaderTarget } from "../reader";

interface Props {
  client: ApiClient;
  target: ReaderTarget;
  onClose: () => void;
}

export function DocumentReader({ client, target, onClose }: Props) {
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
          </article>
        ))}
      </div>
    </aside>
  );
}
