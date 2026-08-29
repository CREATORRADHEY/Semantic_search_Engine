from pydantic import BaseModel

from models.citation import Citation


class AnswerResponse(BaseModel):
    answer: str
    citations: list[Citation]