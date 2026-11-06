import { describe, expect, it } from "vitest";

import { parseSse } from "./sse";

function streamOf(...chunks: string[]): ReadableStream<Uint8Array> {
  const encoder = new TextEncoder();
  return new ReadableStream({
    start(controller) {
      for (const chunk of chunks) controller.enqueue(encoder.encode(chunk));
      controller.close();
    },
  });
}

describe("parseSse", () => {
  it("unisce eventi spezzati tra chunk e normalizza CRLF", async () => {
    const events = [];
    for await (const event of parseSse(
      streamOf(
        'event: token\r\ndata: {"delta":"La "}\r\n\r\n',
        'event: citation\r\ndata: {"citation":{"document_id":"d1"}}\r\n\r\nevent: done\ndata: {"citations":1}\n\n',
      ),
    )) {
      events.push(event);
    }

    expect(events).toEqual([
      { event: "token", data: '{"delta":"La "}' },
      { event: "citation", data: '{"citation":{"document_id":"d1"}}' },
      { event: "done", data: '{"citations":1}' },
    ]);
  });

  it("ignora righe di commento e unisce data multilinea", async () => {
    const events = [];
    for await (const event of parseSse(
      streamOf(": ping\nevent: token\ndata: riga 1\ndata: riga 2\n\n"),
    )) {
      events.push(event);
    }

    expect(events).toEqual([{ event: "token", data: "riga 1\nriga 2" }]);
  });
});
