from pydantic import BaseModel


class CompletionRequest(BaseModel):
    prompt: str