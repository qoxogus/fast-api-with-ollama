from fastapi import APIRouter

from dto.embedding_request import EmbeddingRequest
from dto.embedding_similarity_request import EmbeddingSimilarityRequest
from service.embedding_service import EmbeddingService

router = APIRouter(
    prefix="/api/v1/embeddings",
    tags=["embedding"]
)

__embedding_service = EmbeddingService()


@router.post("")
async def embed(request: EmbeddingRequest):
    embedding = __embedding_service.get_embedding(request.text)
    return {"embedding": embedding}


@router.post("/similarities")
async def get_embedding_similarity(request: EmbeddingSimilarityRequest):
    first_embedding = __embedding_service.get_embedding(request.first)
    second_embedding = __embedding_service.get_embedding(request.second)
    similarity = __embedding_service.get_similarity(first_embedding, second_embedding)
    return {"similarity": similarity}
