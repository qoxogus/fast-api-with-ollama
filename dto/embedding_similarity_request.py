from pydantic import BaseModel


class EmbeddingSimilarityRequest(BaseModel):
    first: str
    second: str