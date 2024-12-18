from util.completion_util import CompletionUtil


class CompletionService:
    __completion_util = CompletionUtil()

    def generate_by_prompt(self, prompt: str):
        return self.__completion_util.generate_by_prompt(prompt)