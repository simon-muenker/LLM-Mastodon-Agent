import typing
import time
import random
import os
import tomllib

import requests

import agent_controller

CONF = tomllib.load(open(f"{os.path.dirname(os.path.realpath(__file__))}/conf.toml", "rb"))


while True:
    try:
        user = agent_controller.MastodonUser(bearer=random.choice(CONF["USER"]))
        agent = agent_controller.AgentInterface()

        response = agent.generate(
            topic=random.choice(CONF["TOPICS"]), persona=random.choice(CONF["PERSONAS"])
        )
        user.post(response["response"] + "\n" + response["meta"]["retrieved_source"])

        time.sleep(CONF["TIMEOUT"])

    except TypeError:
        continue

    except requests.exceptions.JSONDecodeError:
        continue
