# app/models.py
from pydantic import BaseModel
import uuid

class Document(BaseModel):
    id: uuid.UUID
    text: str
