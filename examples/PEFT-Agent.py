import time

import dotenv

import llm_mastodon_agent as src

ENV = dotenv.dotenv_values(".env")

agent = src.Agent(
    client=src.mastodon.Client(
        name=ENV["MASTODON_USERNAME"], bearer=ENV["MASTODON_BEARER"]
    ),
    integration = src.integrations.Huggingface(
        llm_slug=ENV["HUGGINGFACE_PEFT_PATH"],
        auth_token=ENV["HUGGINGFACE_AUTH"],
    )
)

topics = ["Trump", "Biden", "healthcare", "rifles", "voting age"]

for topic in topics:
    agent.post(topic=topics, ideology="alt-right", retrieve_news=False)

    time.sleep(10)
