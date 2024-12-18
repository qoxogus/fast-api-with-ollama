from langchain_community.embeddings import OllamaEmbeddings


class EmbeddingUtil:
    __ollama_embeddings = OllamaEmbeddings(base_url="http://localhost:11434", model="nomic-embed-text")

    def embed(self, text: str):
        return self.__ollama_embeddings.embed_query(text)