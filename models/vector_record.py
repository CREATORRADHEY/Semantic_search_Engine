from pydantic import BaseModel

from models.chunk import Chunk


class VectorRecord(BaseModel):

    chunk: Chunk

    embedding: list[float]