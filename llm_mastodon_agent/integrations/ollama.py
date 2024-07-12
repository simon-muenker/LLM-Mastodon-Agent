import ollama

from ._interface import Interface


class Ollama(Interface):
    def inference(self, system: str, prompt: str, **_) -> str:
        return ollama.generate(model=self.llm_slug, system=system, prompt=prompt)["response"]
