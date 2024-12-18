from util.embedding_similarity_calculator import EmbeddingSimilarityCalculator
from util.embedding_util import EmbeddingUtil


class EmbeddingService:
    __embedding_util = EmbeddingUtil()
    __embedding_similarity_calculator = EmbeddingSimilarityCalculator()

    def get_embedding(self, text: str):
        return self.__embedding_util.embed(text)

    def get_similarity(self, first: str, second: str):
        return self.__embedding_similarity_calculator.calculate_similarity(x=first, y=second)