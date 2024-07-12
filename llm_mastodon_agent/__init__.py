import pydantic

from . import schemas
from . import integrations

from .client import Client
from .scheduler import Scheduler

__all__ = ["schemas", "Client"]


class Agent(pydantic.BaseModel):
    persona: str
    
    client: Client
    integration: integrations.Interface

    scheduler: Scheduler = Scheduler()

    def __call__(self):
        pass

    def post(self, topic: str):
        response = self.integration.inference(
            system=f"Your are politicially {self.persona}",
            prompt=f"Generate a social media post about {topic}",
        )
        self.client.post(response)
