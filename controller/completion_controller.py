from fastapi import APIRouter

from dto.completion_request import CompletionRequest
from service.completion_service import CompletionService


router = APIRouter(
    prefix="/api/v1/completions",
    tags=["completion"]
)

__completion_service = CompletionService()


@router.post("")
async def completions(request: CompletionRequest):
    generated_text = __completion_service.generate_by_prompt(request.prompt)
    return {"generated_text": generated_text}