import { useState } from "react";

import { DocumentPanel } from "./components/DocumentPanel";
import { DocumentReader } from "./components/DocumentReader";
import { FlashcardsPanel } from "./components/FlashcardsPanel";
import { TutorChat } from "./components/TutorChat";
import { client, gatewayLabel } from "./config";
import type { ReaderTarget } from "./reader";

type Drawer = { kind: "reader"; target: ReaderTarget } | { kind: "cards" } | null;

export function App() {
  const [selectedId, setSelectedId] = useState<string | null>(null);
  const [drawer, setDrawer] = useState<Drawer>(null);

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
        <div className="topbar-actions">
          <button
            className="button ghost"
            onClick={() =>
              setDrawer((previous) => (previous?.kind === "cards" ? null : { kind: "cards" }))
            }
          >
            Schede
          </button>
          <span className="status" title={gatewayLabel}>
            <span className="dot" /> locale
          </span>
        </div>
      </header>

      <main className="layout">
        <DocumentPanel client={client} selectedId={selectedId} onSelect={setSelectedId} />
        <TutorChat
          client={client}
          documentId={selectedId}
          onCitationClick={(citation) =>
            setDrawer({
              kind: "reader",
              target: {
                documentId: citation.document_id,
                page: citation.page,
                section: citation.section,
              },
            })
          }
        />
        {drawer?.kind === "reader" && (
          <DocumentReader
            client={client}
            target={drawer.target}
            onClose={() => setDrawer(null)}
          />
        )}
        {drawer?.kind === "cards" && (
          <FlashcardsPanel
            client={client}
            documentId={selectedId}
            onClose={() => setDrawer(null)}
          />
        )}
      </main>
    </div>
  );
}
