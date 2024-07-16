import logging

import pytest

import llm_mastodon_agent as src


class TestAgent:
    @pytest.fixture
    def scheduler(self) -> src.Scheduler:
        return src.Scheduler(planck_time=1, cycle_duration=36)

    def test__scheduler(self, scheduler: src.Scheduler):
        logging.debug(scheduler)
        scheduler()
