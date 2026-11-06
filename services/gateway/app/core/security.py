import os

from fastapi import Header, HTTPException


def require_token(authorization: str | None = Header(default=None)) -> None:
    # shortcut: senza NOESIS_TOKEN il gateway resta aperto per lo sviluppo locale; il supervisore lo imposta sempre
    token = os.getenv("NOESIS_TOKEN")
    if token and authorization != f"Bearer {token}":
        raise HTTPException(status_code=401, detail="token assente o non valido")
