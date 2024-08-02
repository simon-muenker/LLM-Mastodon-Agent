import ollama

from ._interface import Interface, Prompt


class Ollama(Interface):
    def inference(self, prompt: Prompt, **_) -> str:
        return ollama.generate(model=self.llm_slug, system=prompt.system, prompt=prompt.user)[
            "response"
        ]  # type: ignore
