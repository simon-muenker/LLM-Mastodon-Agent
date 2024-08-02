import pydantic

from . import integrations, mastodon, tools
from .prompting import Prompting


class Agent(pydantic.BaseModel):
    prompting: Prompting = Prompting()

    client: mastodon.Client
    integration: integrations.Interface

    @pydantic.computed_field  # type: ignore
    @property
    def history(self) -> mastodon.Timeline:
        return self.client.get_history()

    def get_persona(self, ideology: str, with_history: bool = True) -> str:
        return self.prompting.get_persona_description(self.client.name, ideology) + (
            "\n" + self.prompting.get_persona_history(self.history.to_prompt_segment())
            if with_history
            else ""
        )

    def do_inference(self, ideology: str, prompt: str) -> str:
        return self.integration.inference(
            integrations.Prompt(system=self.get_persona(ideology), user=prompt)
        )

    def post(self, ideology: str, topic: str, retrieve_news: bool = True) -> None:
        if retrieve_news:
            article = tools.NewsArticle(topic=topic)
            topic = article.summary

        response: str = self.do_inference(ideology, self.prompting.get_post_task(topic))

        self.client.post(f"{response}{" " + article.url if retrieve_news else ""}")

    def reply(self, ideology: str, thread: mastodon.Thread, context_length: int = 2) -> None:
        response: str = self.do_inference(
            ideology, self.prompting.get_reply_task(thread.to_prompt_segment(n=context_length))
        )

        self.client.reply(thread[-1].idx, response)
