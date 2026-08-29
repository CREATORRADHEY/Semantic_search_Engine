from pydantic import BaseModel


class Collection(BaseModel):

    namespace: str

    description: str | None = None

    