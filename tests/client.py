import os
import tomllib


import llm_mastodon_agent

CONF = tomllib.load(open(f"{os.path.dirname(os.path.realpath(__file__))}/_conf.toml", "rb"))
USER = CONF["users"][0]

client = llm_mastodon_agent.Client(name=USER["name"], bearer=USER["bearer"])

timeline = llm_mastodon_agent.schemas.Timeline.from_request(client.get_timeline())
history = llm_mastodon_agent.schemas.Timeline.from_request(client.get_history())

print(timeline.remove_replies().to_prompt_segment(n=3))

print(timeline.remove_replies().select_random())

thread = llm_mastodon_agent.schemas.Timeline.from_request(
    client.get_post_w_replies("112734105231328503")
)

print(thread[0].to_prompt_segment() + thread.to_prompt_segment(n=3))
