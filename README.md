# LLM Mastodon Agent

## Usage

### Integrations
```python
import llm_mastodon_agent

# functional, requires endpoint structure defined in https://inf.cl.uni-trier.de/docs
web_api = llm_mastodon_agent.integrations.WebAPI(
    llm_slug="mixtral:8x7b-instruct-v0.1-q6_K", api="https://inf.cl.uni-trier.de/"
)

# functional, with local ollama installation: https://ollama.com/download
ollama = llm_mastodon_agent.integrations.Ollama(llm_slug="phi3:instruct")

# currently in development
huggingface = llm_mastodon_agent.integrations.Ollama(llm_slug="$slug$")
```

### Client
```python
client = llm_mastodon_agent.Client(name="$mastodon_username$", bearer="$mastodon_bearer_token$")
```

### Agent

```python
import llm_mastodon_agent

# creates the agent
agent = llm_mastodon_agent.Agent(
    persona="far-right",
    client=client,
    integration=web_api | ollama
)

# generates a post using the defined integration and posts it through mastodon client
agent.post(topic="Baseball")
```

### Scheduler

todo, for now a proposal