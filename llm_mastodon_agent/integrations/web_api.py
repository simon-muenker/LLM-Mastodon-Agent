import requests

from ._interface import Interface, Prompt


class WebAPI(Interface):
    api: str

    def inference(self, prompt: Prompt, **_) -> str:
        return requests.post(
            self.api,
            json={
                "model": self.llm_slug,
                "system": prompt.user,
                "prompt": prompt.system,
            },
        ).json()["response"]
