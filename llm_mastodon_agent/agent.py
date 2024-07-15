import pydantic

from . import integrations
from . import tools

from .client import Client
from .prompting import Prompting


class Agent(pydantic.BaseModel):
    prompts: Prompting = Prompting()

    client: Client
    integration: integrations.Interface

    def post(self, persona: str, topic: str, retrieve_news: bool = True) -> None:
        if retrieve_news:
            article = tools.NewsArticle(topic=topic)
            topic = article.summary

        response: str = self.integration.inference(
            system=self.prompts.get_persona_description(persona),
            prompt=self.prompts.get_post_task(topic),
        )

        self.client.post(f"{response}{" " + article.url if retrieve_news else ""}")

    def reply(self):
        raise NotImplementedError

    def like(self):
        raise NotImplementedError
