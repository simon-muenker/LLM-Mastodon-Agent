import datetime
import typing

import bs4
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

    @classmethod
    def from_request(cls, post: typing.Dict) -> "Post":
        print(post)
        return cls(
            idx=post["id"],
            author=post["account"]["username"],
            message=bs4.BeautifulSoup(post["content"], "lxml").text,
            timestamp=datetime.datetime.fromisoformat(post["created_at"]),
            reply_idx=post["in_reply_to_id"],
        )

    def to_prompt_segment(self) -> str:
        return f"{"Post" if not self.is_reply else "Reply"} by @{self.author}: {self.message}".strip()
