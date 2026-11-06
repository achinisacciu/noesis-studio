from pydantic import BaseModel


def format_event(event: str, payload: BaseModel) -> str:
    return f"event: {event}\ndata: {payload.model_dump_json()}\n\n"
