import logging

import pytest

import llm_mastodon_agent as llmma


class TestAgent:
    @pytest.fixture
    def agent(
        self, client: llmma.mastodon.Client, integration: llmma.integrations.Interface
    ) -> llmma.Agent:
        return llmma.Agent(client=client, integration=integration)

    @pytest.mark.skip(reason="FIXME")
    def test__agent(self, agent: llmma.Agent):
        logging.debug(agent)

    @pytest.mark.skip(reason="Disable posting")
    def test__post_across_idelogies(self, agent: llmma.Agent):
        for ideology in agent.prompts.ideologies.keys():
            agent.post(ideology=ideology, topic="Politics", retrieve_news=True)
