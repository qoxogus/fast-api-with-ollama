from langchain_community.utils.math import cosine_similarity


class EmbeddingSimilarityCalculator:

    @staticmethod
    def calculate_similarity(x: list[float], y: list[float]):
        return cosine_similarity([x], [y])[0][0]