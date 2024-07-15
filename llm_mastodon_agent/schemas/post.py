import datetime

import pydantic


class Post(pydantic.BaseModel):
    idx: str
    author: str
    message: str
    timestamp: datetime.datetime

    reply_idx: str | None = None

    @pydantic.computed_field  # type: ignore
    @property
    def is_reply(self) -> bool:
        return bool(self.reply_idx)

    def to_prompt_segment(self) -> str:
        return f"Post by @{self.author}: {self.message}".strip()
