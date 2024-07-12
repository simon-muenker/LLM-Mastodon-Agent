import pydantic

from . import integrations
from . import tools

from .client import Client


class Agent(pydantic.BaseModel):
    persona: str

    client: Client
    integration: integrations.Interface

    def __call__(self):
        pass

    def post(self, topic: str, retrieve_news: bool = True) -> None:
        if retrieve_news:
            article = tools.NewsArticle(topic=topic)
            topic = article.summary

        response: str = self.integration.inference(
            system=f"Your social media user and you are politicially {self.persona}",
            prompt=f"Generate a Tweet about {topic}",
        )

        self.client.post(f"{response}{" " + article.url if retrieve_news else ""}")

    def reply(self):
        raise NotImplementedError

    def like(self):
        raise NotImplementedError
