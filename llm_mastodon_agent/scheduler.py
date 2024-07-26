import logging
import random
import time
import typing

import numpy as np
import pydantic

from .agent import Agent


class Action(pydantic.BaseModel):
    probability: float

    label: str | None = None
    callback: typing.Callable | None = None


class Scheduler(pydantic.BaseModel):
    agent: Agent | None = None

    sleep_time: int = 1  # smallest time step (60 seconds)

    act: Action = Action(probability=0.2)
    chicken: Action = Action(probability=0.4)

    retrievals: typing.List[Action] = [
        Action(probability=0.4, label="read_home", callback=lambda: logging.debug("read home")),
        Action(
            probability=0.4,
            label="read_notifications",
            callback=lambda: logging.debug("read notifications"),
        ),
        Action(
            probability=0.2,
            label="read_news",
            callback=lambda: logging.debug("read external news"),
        ),
    ]

    actions: typing.List[Action] = [
        Action(
            probability=0.2,
            label="posted",
            callback=lambda x: logging.debug(f"post to context {x}"),
        ),
        Action(
            probability=0.8,
            label="replied",
            callback=lambda x: logging.debug(f"reply to context {x}"),
        ),
    ]

    def __call__(self) -> None:
        while True:
            if random.uniform(0.0, 1.0) > self.act.probability:
                continue

            retrieval: Action = np.random.default_rng().choice(
                self.retrievals, p=[action.probability for action in self.retrievals]
            )
            retrieval.callback()

            if random.uniform(0.0, 1.0) > self.chicken.probability:
                continue

            action: Action = np.random.default_rng().choice(
                self.actions, p=[action.probability for action in self.actions]
            )
            action.callback(retrieval.label)

            time.sleep(self.sleep_time)
