import logging

import pytest

import llm_mastodon_agent as src


class TestAgent():
     
    @pytest.fixture
    def scheduler(self):
        return src.Scheduler()
    
    def test__scheduler(self, scheduler):
        logging.debug(scheduler)
