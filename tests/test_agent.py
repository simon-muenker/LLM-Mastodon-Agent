import logging

import pytest


import llm_mastodon_agent as src


class TestAgent:
    @pytest.fixture
    def agent(
        self, client: src.mastodon.Client, integration: src.integrations.Interface
    ) -> src.Agent:
        return src.Agent(client=client, integration=integration)

    @pytest.mark.skip(reason="FIXME")
    def test__agent(self, agent: src.Agent):
        logging.debug(agent)

    @pytest.mark.skip(reason="Disable posting")
    def test__post_across_idelogies(self, agent: src.Agent):
        for ideology in agent.prompts.ideologies.keys():
            agent.post(ideology=ideology, topic="Politics", retrieve_news=True)
