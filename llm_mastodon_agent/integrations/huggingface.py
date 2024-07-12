from ._interface import Interface


class Huggingface(Interface):
    def inference(self, system: str, prompt: str, **_) -> str:
        raise NotImplementedError
