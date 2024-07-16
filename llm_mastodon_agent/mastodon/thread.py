import typing

from .post import Post
from .timeline import Timeline


class Thread(Timeline):
    @classmethod
    def from_request(cls, posts: typing.List[typing.Dict]) -> "Thread":
        return cls(posts=[Post.from_request(post) for post in posts])

    def to_prompt_segment(self, n: int = 4) -> str:
        return "\n".join(
            [post.to_prompt_segment() for post in [self.posts[0], *self.posts[-n:]]]
        )
