import os
import tomllib


import llm_mastodon_agent

CONF = tomllib.load(open(f"{os.path.dirname(os.path.realpath(__file__))}/_conf.toml", "rb"))
USER = CONF["users"][0]

agent = llm_mastodon_agent.Agent(
    client=llm_mastodon_agent.Client(name=USER["name"], bearer=USER["bearer"]),
    integration=llm_mastodon_agent.integrations.WebAPI(
        llm_slug="mixtral:8x7b-instruct-v0.1-q6_K", api="https://inf.cl.uni-trier.de/"
    ),
    # integration=llm_mastodon_agent.integrations.Ollama(llm_slug="phi3:instruct"),
)


def test_post_across_idelogies(topic="Voting Age"):
    for ideology in agent.prompts.ideologies.keys():
        agent.post(ideology=ideology, topic=topic, retrieve_news=True)


print(agent.get_persona("liberal"))
test_post_across_idelogies()
