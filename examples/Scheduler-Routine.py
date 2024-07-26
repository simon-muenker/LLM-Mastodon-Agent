import dotenv

import llm_mastodon_agent as llmma

ENV = dotenv.dotenv_values(".env")

agent = llmma.Agent(
    client=llmma.mastodon.Client(
        name=ENV["MASTODON_USERNAME"],
        bearer=ENV["MASTODON_BEARER"],
        api=ENV["MASTODON_API"],
    ),
    integration=llmma.integrations.WebAPI(
        llm_slug=ENV["WEBAPI_MODEL"], api=ENV["WEBAPI_ENDPOINT"]
    ),
)

llmma.Scheduler()()
