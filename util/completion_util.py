from langchain_community.llms.ollama import Ollama


class CompletionUtil:
    __ollama = Ollama(base_url="http://localhost:11434", model="llama3.2")

    def generate_by_prompt(self, prompt: str):
        return self.__ollama.invoke(prompt)