import abc

import pydantic


class Prompt(pydantic.BaseModel):
    system: str
    user: str


class Interface(abc.ABC, pydantic.BaseModel):
    llm_slug: str

    @abc.abstractmethod
    def inference(self, prompt: Prompt, **kwargs) -> str:
        raise NotImplementedError
