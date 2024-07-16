import logging

import pytest


import llm_mastodon_agent as src


class TestAgent():
     
    @pytest.fixture
    def agent(self, client, integration):
        return src.Agent(client=client, integration=integration)

    @pytest.mark.skip(reason="FIXME")
    def test__agent(self, agent):
        logging.debug(agent)
    
    @pytest.mark.skip(reason="FIXME")
    def test__post_across_idelogies(agent):
        for ideology in agent.prompts.ideologies.keys():
            agent.post(ideology=ideology, topic="Voting Age", retrieve_news=True)

