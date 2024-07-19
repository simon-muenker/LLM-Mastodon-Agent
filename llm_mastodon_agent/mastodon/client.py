import typing

import pydantic

import requests

from .timeline import Timeline
from .thread import Thread


class Client(pydantic.BaseModel):
    name: str
    bearer: str
    api: str

    @pydantic.computed_field  # type: ignore
    @property
    def request_header(self) -> typing.Dict:
        return {"Authorization": f"Bearer {self.bearer}"}

    def __post(self, endpoint: str, data: typing.Dict = {}) -> typing.Dict:
        return requests.post(
            f"{self.api}/{endpoint}", headers=self.request_header, data=data
        ).json()

    def __get(self, endpoint) -> typing.List[typing.Dict]:
        response: typing.List | typing.Dict = requests.get(
            f"{self.api}/{endpoint}", headers=self.request_header
        ).json()

        if isinstance(response, typing.Dict):
            return [response]

        return response

    def like(self, idx: str) -> typing.Dict:
        return self.__post(endpoint=f"statuses/{idx}/favourite")

    def post(self, status: str) -> typing.Dict:
        return self.__post(endpoint="statuses", data={"status": status})

    def reply(self, idx: str, comment: str) -> typing.Dict:
        return self.__post(endpoint="statuses", data={"status": comment, "in_reply_to_id": idx})

    def get_user_meta(self) -> typing.Dict:
        return self.__get(f"accounts/lookup?acct={self.name}")[0]

    def get_post_w_replies(self, idx: str) -> Thread:
        return Thread.from_request(
            [
                self.__get(f"statuses/{idx}")[0],
                *self.__get(f"statuses/{idx}/context")[0]["descendants"],
            ]
        )

    def get_history(self) -> Timeline:
        return Timeline.from_request(
            self.__get(f"accounts/{self.get_user_meta()["id"]}/statuses")
        )

    def get_timeline(self, kind: typing.Literal["public", "home"] = "public") -> Timeline:
        return Timeline.from_request(self.__get(f"timelines/{kind}?local=true&limit=40"))
