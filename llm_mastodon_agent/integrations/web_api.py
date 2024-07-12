import requests

from ._interface import Interface


class WebAPI(Interface):
    api: str

    def inference(self, system: str, prompt: str) -> str:
        return requests.post(
            self.api,
            json={
                "model": self.llm_slug,
                "system": system,
                "prompt": prompt,
            },
        ).json()["response"]
