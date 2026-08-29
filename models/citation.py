from pydantic import BaseModel


class Citation(BaseModel):
    index: int
    source: str
    document_id: str
    chunk_id: str