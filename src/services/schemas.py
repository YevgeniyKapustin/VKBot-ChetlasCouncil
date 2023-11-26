from pydantic import BaseModel


class Message(BaseModel):
    """Объект для сообщений."""
    peer_id: int
    from_id: int
    chat_id: int = None
    text: str
