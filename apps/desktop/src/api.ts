import { parseSse } from "./sse";
import type { Citation, DocumentSummary, TutorEvent } from "./types";

interface Envelope<T> {
  status: "success" | "error";
  data: T | null;
  error: { code: string; message: string } | null;
}

export class ApiRequestError extends Error {
  constructor(
    readonly code: string,
    message: string,
  ) {
    super(message);
    this.name = "ApiRequestError";
  }
}

export class ApiClient {
  private readonly baseUrl: string;
  private readonly token: string;

  constructor(baseUrl: string, token = "") {
    this.baseUrl = baseUrl.replace(/\/+$/, "");
    this.token = token;
  }

  private headers(extra: Record<string, string> = {}): Record<string, string> {
    return {
      ...extra,
      ...(this.token ? { Authorization: `Bearer ${this.token}` } : {}),
    };
  }

  private async envelope<T>(response: Response): Promise<T> {
    let body: Envelope<T> | null = null;
    try {
      body = (await response.json()) as Envelope<T>;
    } catch {
      throw new ApiRequestError("INTERNAL_ERROR", "risposta non valida dal gateway");
    }
    if (!response.ok || body.status === "error" || body.data === null) {
      throw new ApiRequestError(
        body.error?.code ?? "INTERNAL_ERROR",
        body.error?.message ?? "richiesta non riuscita",
      );
    }
    return body.data;
  }

  async listDocuments(): Promise<DocumentSummary[]> {
    const response = await fetch(`${this.baseUrl}/api/documents`, {
      headers: this.headers(),
    });
    return this.envelope<DocumentSummary[]>(response);
  }

  async importDocument(file: File): Promise<DocumentSummary> {
    const form = new FormData();
    form.append("file", file);
    const response = await fetch(`${this.baseUrl}/api/documents`, {
      method: "POST",
      body: form,
      headers: this.headers(),
    });
    return this.envelope<DocumentSummary>(response);
  }

  async deleteDocument(documentId: string): Promise<void> {
    const response = await fetch(`${this.baseUrl}/api/documents/${documentId}`, {
      method: "DELETE",
      headers: this.headers(),
    });
    await this.envelope<{ id: string }>(response);
  }

  async indexDocument(documentId: string): Promise<number> {
    const response = await fetch(`${this.baseUrl}/api/index/${documentId}`, {
      method: "POST",
      headers: this.headers(),
    });
    const data = await this.envelope<{ document_id: string; chunks: number }>(
      response,
    );
    return data.chunks;
  }

  async rebuildIndex(): Promise<void> {
    const response = await fetch(`${this.baseUrl}/api/index/rebuild`, {
      method: "POST",
      headers: this.headers(),
    });
    await this.envelope<{ documents: number; chunks: number }>(response);
  }

  async *chat(
    question: string,
    documentId: string | null,
    signal: AbortSignal,
  ): AsyncGenerator<TutorEvent> {
    const response = await fetch(`${this.baseUrl}/api/ai/chat`, {
      method: "POST",
      headers: this.headers({
        "Content-Type": "application/json",
        Accept: "text/event-stream",
      }),
      body: JSON.stringify({
        question,
        document_id: documentId,
        limit: 5,
      }),
      signal,
    });

    if (!response.ok) {
      await this.envelope<never>(response);
      throw new ApiRequestError("INTERNAL_ERROR", "stream non disponibile");
    }
    if (!response.body) {
      throw new ApiRequestError("INTERNAL_ERROR", "stream non disponibile");
    }

    for await (const event of parseSse(response.body)) {
      const payload = JSON.parse(event.data) as Record<string, unknown>;
      if (event.event === "token") {
        yield { type: "token", delta: String(payload.delta ?? "") };
      } else if (event.event === "citation") {
        yield { type: "citation", citation: payload.citation as Citation };
      } else if (event.event === "done") {
        yield { type: "done", citations: Number(payload.citations ?? 0) };
      } else if (event.event === "error") {
        yield {
          type: "error",
          code: String(payload.code ?? "INTERNAL_ERROR"),
          message: String(payload.message ?? "errore del tutor"),
        };
      }
    }
  }
}
