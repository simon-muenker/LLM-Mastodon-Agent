import dotenv

import llm_mastodon_agent as llmma


ENV = dotenv.dotenv_values(".env")
TOPICS = [
    "Trump",
    "Biden",
    "healthcare",
    "rifles",
    "voting age",
]


prompting = llmma.Prompting(
    persona_description="You are a social media user.",
    ideologies={
        "left-leaning": "You have politically left-leaning views. Reflect progressive values and opinions in your responses.",
        "right-leaning": "Your have politically right-leaning views. Reflect conservative values and opinions in your responses.",
    },
    post_task="Write a tweet on the following topic: {topic}",
)

agents = {
    "left-leaning": llmma.Agent(
        client=llmma.mastodon.Client(
            name=ENV["MASTODON_LEFT_USERNAME"],
            bearer=ENV["MASTODON_LEFT_BEARER"],
            api=ENV["MASTODON_API"],
        ),
        integration=llmma.integrations.Huggingface(
            llm_slug=ENV["HUGGINGFACE_AGENT_LEFT_PATH"],
            auth_token=ENV["HUGGINGFACE_AUTH"],
        ),
        prompting=prompting,
    ),
    "right-leaning": llmma.Agent(
        client=llmma.mastodon.Client(
            name=ENV["MASTODON_RIGHT_USERNAME"],
            bearer=ENV["MASTODON_RIGHT_BEARER"],
            api=ENV["MASTODON_API"],
        ),
        integration=llmma.integrations.Huggingface(
            llm_slug=ENV["HUGGINGFACE_AGENT_RIGHT_PATH"],
            auth_token=ENV["HUGGINGFACE_AUTH"],
        ),
        prompting=prompting,
    ),
}

for topic in TOPICS:
    for ideology, agent in agents.items():
        agent.post(topic=topic, ideology=ideology, retrieve_news=True)
