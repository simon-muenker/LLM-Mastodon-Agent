import typing
import logging
import time
import random

import pydantic

from .agent import Agent


class Action(pydantic.BaseModel):
    name: str
    frequency: int
    probability: float
    callback: typing.Callable


class Scheduler(pydantic.BaseModel):
    agent: Agent | None = None

    planck_time: int = 60  # smallest time step (60 seconds)
    cycle_duration: int = 60 * 60  # 1 hour

    actions: typing.List[Action] = [
        Action(name="like", frequency=16, probability=0.4, callback=lambda: logging.debug("liked")),
        Action(name="post", frequency=2, probability=0.8, callback=lambda: logging.debug("posted")),
        Action(name="reply", frequency=4, probability=0.4, callback=lambda: logging.debug("replied")),
    ]

    _current_time: int = 0

    def __call__(self) -> None:
        while True:
            for action in self.actions:
                if self._current_time % (self.cycle_duration / action.frequency) < 0.1:
                    if random.uniform(0.0, 1.0) < action.probability:
                        action.callback()


            self._current_time += self.planck_time
            self._current_time %= self.cycle_duration
            time.sleep(self.planck_time)

