import { useState } from "react";

import { DocumentPanel } from "./components/DocumentPanel";
import { TutorChat } from "./components/TutorChat";
import { client, gatewayLabel } from "./config";

export function App() {
  const [selectedId, setSelectedId] = useState<string | null>(null);

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
          onCitationClick={setSelectedId}
        />
      </main>
    </div>
  );
}
