from pydantic import BaseModel


class ChatRequest(BaseModel):
    question: str


class SearchRequest(BaseModel):
    query: str
    top_k: int = 5


class IndexRequest(BaseModel):
    file_path: str
    category: str = "general"


class HealthResponse(BaseModel):
    status: str
    version: str


class SearchResponse(BaseModel):
    score: float
    text: str
    source: str