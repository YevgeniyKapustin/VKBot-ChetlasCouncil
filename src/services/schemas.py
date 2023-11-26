from pydantic import BaseModel


class Message(BaseModel):
    """Объект для сообщений."""
    peer_id: int
    from_id: int
    text: str
