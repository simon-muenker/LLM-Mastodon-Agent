import typing

import pydantic

import requests


class TWON(pydantic.BaseModel):
    ENDPOINT: str = "https://agents.twon.uni-trier.de"

    HEADER: typing.Dict = {
        "integration": {"model": "mixtral:8x7b-instruct-v0.1-q6_K", "provider": "local"},
        "language": "English",
        "length": "few-word",
        "platform": "Twitter",
    }

    def generate(
        self,
        topic: str,
        persona: typing.Literal["neutral", "liberal", "conservative"] = "neutral",
    ):
        return requests.post(
            f"{self.ENDPOINT}/generate/",
            json={
                "history": {"interactions": []},
                "persona": [persona],
                "topic": topic,
                "meta": {"retrieved_source": True},
            }
            | self.HEADER,
        ).json()

    def reply(
        self, post, persona: typing.Literal["neutral", "liberal", "conservative"] = "neutral"
    ):
        return requests.post(
            f"{self.ENDPOINT}/reply/",
            json={
                "history": {"interactions": []},
                "persona": [persona],
                "thread": {"posts": [post]},
            }
            | self.HEADER,
        ).json()
