import os
import tomllib


import llm_mastodon_agent as src

CONF = tomllib.load(open(f"{os.path.dirname(os.path.realpath(__file__))}/_conf.toml", "rb"))
USER = CONF["users"][0]

client = src.mastodon.Client(name=USER["name"], bearer=USER["bearer"])

timeline = client.get_timeline()
history = client.get_history()

print(timeline.remove_replies().to_prompt_segment(n=3))

print(timeline.remove_replies().select_random())

thread = client.get_post_w_replies("112734105231328503")

print(thread[0].to_prompt_segment() + thread.to_prompt_segment(n=3))
