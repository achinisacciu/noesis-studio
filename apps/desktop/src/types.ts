export interface DocumentSummary {
  id: string;
  title: string;
  filename: string;
  created_at: string;
  chunk_count: number;
}

export interface Chunk {
  id: string;
  document_id: string;
  position: number;
  text: string;
  page: number | null;
  section: string | null;
}

export interface Citation {
  document_id: string;
  page: number | null;
  section: string | null;
  snippet: string;
}

export interface ReadingPosition {
  document_id: string;
  chunk_id: string;
  position: number;
  updated_at: string;
}

export interface Flashcard {
  id: string;
  document_id: string;
  front: string;
  back: string;
  page: number | null;
  section: string | null;
  created_at: string;
}

export interface FlashcardInput {
  document_id: string;
  front: string;
  back: string;
  page?: number | null;
  section?: string | null;
}

export type TutorEvent =
  | { type: "token"; delta: string }
  | { type: "citation"; citation: Citation }
  | { type: "done"; citations: number }
  | { type: "error"; code: string; message: string };
