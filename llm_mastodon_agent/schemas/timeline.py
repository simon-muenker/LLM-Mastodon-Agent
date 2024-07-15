import typing
import random
import datetime

import pydantic
import bs4

from .post import Post


class Timeline(pydantic.BaseModel):
    posts: typing.List[Post]

    def __getitem__(self, key: int) -> Post:
        return self.posts[key]

    def __iter__(self):
        return iter(self.posts)

    @classmethod
    def from_request(cls, posts: typing.List[typing.Dict]) -> "Timeline":
        return cls(
            posts=[
                Post(
                    idx=post["id"],
                    author=post["account"]["username"],
                    message=bs4.BeautifulSoup(post["content"], "lxml").text,
                    timestamp=datetime.datetime.fromisoformat(post["created_at"]),
                    reply_idx=post["in_reply_to_id"],
                )
                for post in posts
            ]
        )

    def select_random(self) -> Post:
        return random.choice(self.posts)

    def remove_replies(self) -> "Timeline":
        return Timeline(posts=[post for post in self.posts if not post.is_reply])

    def sort_by_timestamp(self) -> "Timeline":
        return Timeline(posts=sorted(self.posts, key=lambda x: x.timestamp))

    def to_prompt_segment(self, n: int = 2) -> str:
        return "\n".join([post.to_prompt_segment() for post in self.posts[-n:]])

    def __len__(self) -> int:
        return len(self.posts)
