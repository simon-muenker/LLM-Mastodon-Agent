import pytest

import dotenv

import llm_mastodon_agent as src

ENV = dotenv.dotenv_values(".env")


@pytest.fixture(scope="session", autouse=True)
def client() -> src.mastodon.Client:
    return src.mastodon.Client(
        name=ENV["MASTODON_USERNAME"], bearer=ENV["MASTODON_BEARER"]
    )


@pytest.fixture(scope="session", autouse=True)
def integration() -> src.integrations.WebAPI:
    return src.integrations.WebAPI(
        llm_slug=ENV["WEBAPI_MODEL"], api=ENV["WEBAPI_ENDPOINT"]
    )
