from pydantic import BaseModel


class IndexedDocumentState(BaseModel):

    document_id: str
    filename: str
    namespace: str
    sha256: str
    chunks: int