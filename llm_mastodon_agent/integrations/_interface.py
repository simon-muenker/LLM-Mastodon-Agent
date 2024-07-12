import abc

import pydantic


class Interface(abc.ABC, pydantic.BaseModel):
    llm_slug: str

    @abc.abstractmethod
    def inference(self, system: str, prompt: str, **kwargs) -> str:
        raise NotImplementedError
