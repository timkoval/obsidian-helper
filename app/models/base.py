from pydantic import BaseModel
from typing import Optional

class BaseNote(BaseModel):
    title: str
    text: str
    moc: Optional[str] = None

class ReadNote(BaseModel):
    title: str