export interface DocumentSummary {
  id: string;
  title: string;
  filename: string;
  created_at: string;
  chunk_count: number;
}

export interface Citation {
  document_id: string;
  page: number | null;
  section: string | null;
  snippet: string;
}

export type TutorEvent =
  | { type: "token"; delta: string }
  | { type: "citation"; citation: Citation }
  | { type: "done"; citations: number }
  | { type: "error"; code: string; message: string };
