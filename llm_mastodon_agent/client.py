import typing

import pydantic

import requests


class Client(pydantic.BaseModel):
    name: str
    bearer: str

    API: str = "https://twon.uni-trier.de/api/v1"

    @pydantic.computed_field
    @property
    def request_header(self) -> typing.Dict:
        return {"Authorization": f"Bearer {self.bearer}"}

    def __post(self, endpoint: str, data: typing.Dict = {}) -> typing.Dict:
        return requests.post(
            f"{self.API}/{endpoint}", headers=self.request_header, data=data
        ).json()

    def __get(self, endpoint) -> typing.Dict:
        return requests.get(f"{self.API}/{endpoint}", headers=self.request_header).json()

    def like(self, idx: str) -> typing.Dict:
        return self.__post(endpoint=f"statuses/{idx}/favourite")

    def post(self, status: str) -> typing.Dict:
        return self.__post(endpoint="statuses", data={"status": status})

    def reply(self, idx: str, comment: str) -> typing.Dict:
        return self.__post(endpoint="statuses", data={"status": comment, "in_reply_to_id": idx})

    def get_user_meta(self):
        return self.__get(f"accounts/lookup?acct={self.name}")

    def get_history(self):
        return self.__get(f"accounts/{self.get_user_meta()["id"]}/statuses")

    def get_timeline(self, kind: typing.Literal["public", "home"] = "public") -> typing.Dict:
        return self.__get(f"timelines/{kind}")
