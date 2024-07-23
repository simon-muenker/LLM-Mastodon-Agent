import pytest

import dotenv

import llm_mastodon_agent as llmma

ENV = dotenv.dotenv_values(".env")


@pytest.fixture(scope="session", autouse=True)
def client() -> llmma.mastodon.Client:
    return llmma.mastodon.Client(
        name=ENV["MASTODON_USERNAME"], bearer=ENV["MASTODON_BEARER"], api=ENV["MASTODON_API"]
    )


@pytest.fixture(scope="session", autouse=True)
def integration() -> llmma.integrations.WebAPI:
    return llmma.integrations.WebAPI(llm_slug=ENV["WEBAPI_MODEL"], api=ENV["WEBAPI_ENDPOINT"])
