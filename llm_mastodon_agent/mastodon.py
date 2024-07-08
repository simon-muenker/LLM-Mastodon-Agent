import pydantic

import requests

class MastodonUser(pydantic.BaseModel):
    bearer: str

    ENDPOINT: str = "https://twon.uni-trier.de/api/v1"


    @pydantic.computed_field
    @property
    def request_header(self) -> str:
        return {
            "Authorization": f"Bearer {self.bearer}"
        }
    
    def post(self, status: str) -> None:
        requests.post(
            f"{self.ENDPOINT}/statuses",
            headers=self.request_header,
            data={
                "status": status
            }
        )

    def read(self):
        return requests.get(f"{self.ENDPOINT}/timelines/public").json()
    

    def reply(self, idx: str, comment: str):
        requests.post(
            f"{self.ENDPOINT}/statuses",
            headers=self.request_header,
            data={
                "status": comment,
                "in_reply_to_id": idx
            }
        )
