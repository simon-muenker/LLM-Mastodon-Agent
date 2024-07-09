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

        selected_post = random.choice(user.read())

        reply = agent.reply(
            {
                "author": selected_post["account"]["username"],
                "message": selected_post["content"],
            },
            persona=random.choice(CONF["PERSONAS"]),
        )

        user.reply(comment=reply["response"], idx=selected_post["id"])

        time.sleep(CONF["TIMEOUT"])

    except TypeError:
        continue

    except requests.exceptions.JSONDecodeError:
        continue
