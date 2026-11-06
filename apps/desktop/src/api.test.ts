import { afterEach, describe, expect, it, vi } from "vitest";

import { ApiClient, ApiRequestError } from "./api";

const client = new ApiClient("http://gateway.test/", "secret");

afterEach(() => vi.unstubAllGlobals());

describe("ApiClient", () => {
  it("legge la lista documenti e invia il token", async () => {
    const fetchMock = vi.fn().mockResolvedValue(
      new Response(
        JSON.stringify({
          status: "success",
          data: [
            {
              id: "d1",
              title: "Statistica",
              filename: "statistica.md",
              created_at: "2026-01-01T00:00:00Z",
              chunk_count: 2,
            },
          ],
          error: null,
        }),
        { status: 200 },
      ),
    );
    vi.stubGlobal("fetch", fetchMock);

    const documents = await client.listDocuments();

    expect(documents.map((document) => document.id)).toEqual(["d1"]);
    expect(fetchMock).toHaveBeenCalledWith("http://gateway.test/api/documents", {
      headers: { Authorization: "Bearer secret" },
    });
  });

  it("traduce l'envelope di errore in ApiRequestError", async () => {
    vi.stubGlobal(
      "fetch",
      vi.fn().mockResolvedValue(
        new Response(
          JSON.stringify({
            status: "error",
            data: null,
            error: { code: "SERVICE_UNAVAILABLE", message: "rag non pronto" },
          }),
          { status: 503 },
        ),
      ),
    );

    await expect(client.listDocuments()).rejects.toEqual(
      new ApiRequestError("SERVICE_UNAVAILABLE", "rag non pronto"),
    );
  });

  it("crea e legge le flashcard dal gateway", async () => {
    const card = {
      id: "c1",
      document_id: "d1",
      front: "Che cosa misura la varianza?",
      back: "La dispersione.",
      page: null,
      section: "Varianza",
      created_at: "2026-01-01T00:00:00Z",
    };
    const fetchMock = vi
      .fn()
      .mockResolvedValueOnce(
        new Response(JSON.stringify({ status: "success", data: { cards: [card] } }), {
          status: 200,
        }),
      )
      .mockResolvedValueOnce(
        new Response(JSON.stringify({ status: "success", data: card }), { status: 200 }),
      );
    vi.stubGlobal("fetch", fetchMock);

    const cards = await client.listFlashcards("d1");
    const created = await client.createFlashcard({
      document_id: "d1",
      front: "Che cosa misura la varianza?",
      back: "La dispersione.",
    });

    expect(cards.map((item) => item.id)).toEqual(["c1"]);
    expect(created.id).toBe("c1");
    expect(fetchMock).toHaveBeenNthCalledWith(1, "http://gateway.test/api/flashcards?document_id=d1", {
      headers: { Authorization: "Bearer secret" },
    });
    expect(fetchMock.mock.calls[1]?.[1]).toMatchObject({
      method: "POST",
      body: JSON.stringify({
        document_id: "d1",
        front: "Che cosa misura la varianza?",
        back: "La dispersione.",
      }),
    });
  });

  it("trasforma lo stream SSE negli eventi del tutor", async () => {
    const body = [
      'event: citation\ndata: {"citation":{"document_id":"d1","page":2,"section":"Varianza","snippet":"..."}}\n\n',
      'event: token\ndata: {"delta":"La varianza"}\n\n',
      'event: token\ndata: {"delta":" misura la dispersione."}\n\n',
      'event: done\ndata: {"model":"fake","citations":1}\n\n',
    ].join("");
    vi.stubGlobal(
      "fetch",
      vi.fn().mockResolvedValue(new Response(body, { status: 200 })),
    );

    const events = [];
    for await (const event of client.chat(
      "cos'è la varianza?",
      "d1",
      new AbortController().signal,
    )) {
      events.push(event);
    }

    expect(events).toEqual([
      {
        type: "citation",
        citation: { document_id: "d1", page: 2, section: "Varianza", snippet: "..." },
      },
      { type: "token", delta: "La varianza" },
      { type: "token", delta: " misura la dispersione." },
      { type: "done", citations: 1 },
    ]);
  });
});
