import logging

import pytest

import llm_mastodon_agent as llmma


class TestAgent:
    @pytest.fixture
    def scheduler(self) -> llmma.Scheduler:
        return llmma.Scheduler(planck_time=1, cycle_duration=36)

    def test__scheduler(self, scheduler: llmma.Scheduler):
        logging.debug(scheduler)
        scheduler()
