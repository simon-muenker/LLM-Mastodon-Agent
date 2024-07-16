import pytest

import llm_mastodon_agent as src

@pytest.fixture(scope="session", autouse=True)
def client():
    return src.mastodon.Client(name="octo_pink", bearer="2U8HTyO0pHTflpC-QC7NTiczShp944_KraQZACaHELU")

@pytest.fixture(scope="session", autouse=True)
def integration():
    return src.integrations.WebAPI(llm_slug="mixtral:8x7b-instruct-v0.1-q6_K", api="https://inf.cl.uni-trier.de/")