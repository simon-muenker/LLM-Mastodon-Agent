import time
import random

import pydantic

from .agent import Agent


class Scheduler(pydantic.BaseModel):
    agent: Agent | None = None

    planck_time: int = 60  # smallest time step (60 seconds)
    cycle_duration: int = 60 * 60  # 1 hour

    like_frequency: int = 12
    like_probability: float = 0.8

    post_frequency: int = 2
    post_probability: float = 0.4

    def __call__(self):
        current_time: int = 0

        while True:
            if current_time % (self.cycle_duration / self.like_frequency) < 0.1:
                if random.uniform(0.0, 1.0) < self.like_probability:
                    print(f"{current_time}: Like")

            if current_time % (self.cycle_duration / self.post_frequency) < 0.1:
                if random.uniform(0.0, 1.0) < self.post_probability:
                    print(f"{current_time}: Post")

            current_time += self.planck_time
            current_time %= self.cycle_duration
            time.sleep(self.planck_time)
