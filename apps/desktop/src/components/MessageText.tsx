import { formatInline } from "../markdown";

export function MessageText({ text }: { text: string }) {
  return (
    <p className="message-text">
      {formatInline(text).map((segment, index) => {
        if (segment.type === "strong") return <strong key={index}>{segment.value}</strong>;
        if (segment.type === "code") return <code key={index}>{segment.value}</code>;
        return <span key={index}>{segment.value}</span>;
      })}
    </p>
  );
}
