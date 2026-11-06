import { useState } from "react";

import { DocumentPanel } from "./components/DocumentPanel";
import { DocumentReader } from "./components/DocumentReader";
import { TutorChat } from "./components/TutorChat";
import { client, gatewayLabel } from "./config";
import type { ReaderTarget } from "./reader";

export function App() {
  const [selectedId, setSelectedId] = useState<string | null>(null);
  const [reader, setReader] = useState<ReaderTarget | null>(null);

  return (
    <div className="app">
      <header className="topbar">
        <div className="brand">
          <span className="brand-mark">N</span>
          <div>
            <strong>Noesis Studio</strong>
            <span className="muted">Studia con fonti verificabili</span>
          </div>
        </div>
        <span className="status" title={gatewayLabel}>
          <span className="dot" /> locale
        </span>
      </header>

      <main className="layout">
        <DocumentPanel client={client} selectedId={selectedId} onSelect={setSelectedId} />
        <TutorChat
          client={client}
          documentId={selectedId}
          onCitationClick={(citation) =>
            setReader({
              documentId: citation.document_id,
              page: citation.page,
              section: citation.section,
            })
          }
        />
        {reader && (
          <DocumentReader
            client={client}
            target={reader}
            onClose={() => setReader(null)}
          />
        )}
      </main>
    </div>
  );
}
