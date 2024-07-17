# LLMs as Mastodon User: A scalable Implementation for Autonomous Social Media Agents

This repository presents a novel framework for deploying Large Language Models (LLMs) as autonomous agents on the Mastodon social media platform. Our implementation leverages state-of-the-art LLM integrations (Huggingface, Ollama, generic WebAPIs) to create AI-driven Mastodon accounts capable of generating posts, engaging in conversations, and interacting with other users naturally and contextually appropriate. The system is designed with scalability, allowing deploying and managing multiple AI agents across different Mastodon instances. This project explores the potential and limitations of AI in social media environments and provides a foundation for further research into autonomous online agents.

## Installation

This package uses Poetry for dependency management and packaging. Ensure you have Poetry installed on your system. If not, you can install it by following the [official Poetry installation guide](https://python-poetry.org/docs/#installing-with-the-official-installer). To install the package, follow these steps:

```bash
# clone the repository
git clone https://github.com/XXXX-XXXXX/LLM-Mastodon-Agent.git

# install the package and its dependencies using Poetry
poetry install 

# (optional) to activate the virtual environment created by Poetry
poetry shell
```

## Usage

### Integrations
```python
import llm_mastodon_agent as llmma

# functional, requires post endpoint expecting data in the format:
# {"model": "MODEL_SLUG", "system": "SYSTEM_PROMPT", "prompt": "PROMPT"}
web_api = llmma.integrations.WebAPI(
    llm_slug="MODEL_SLUG", api="API_ENDPOINT"
)

# functional, with local ollama installation: https://ollama.com/download
ollama = llmma.integrations.Ollama(llm_slug="MODEL_SLUG")

# not implemented, currently in development
huggingface = llmma.integrations.Huggingface(llm_slug="MODEL_SLUG")

# inferencing
web_api|ollama|huggingface.inference(system="SYSTEM_PROMPT", prompt="PROMPT")
```

### Client
```python
import llm_mastodon_agent as llmma

# contains methods for recieving (timeline, threads) and posting (liking, posting, replying) content
client = llmma.mastodon.Client(name="USERNAME", bearer="BEARER_TOKEN")
```

### Agent

```python
import llm_mastodon_agent as llmma

# creates the agent
agent = llmma.Agent(
    client=client,
    integration=web_api|ollama
)

# generates a post using the defined integration and posts it through the mastodon client
agent.post(topic="Baseball")
```

### Scheduler

```python
import llm_mastodon_agent as llmma

# currently in development
# creates a scheduler
# initiates the agent lifecycle (reading, posting, liking, replying)
scheduler = llmma.scheduler(agent=agent)
scheduler()
```

## Roadmap

- [ ] Add agent history feature
- [ ] Integrate Hugging Face with PEFT
- [ ] Restructure unit testing
- [ ] Propose Agent Scheduler
- [ ] Add Twitter Tweet collect tool

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.

## Disclaimer

This project is for research purposes only. Users are responsible for complying with Mastodon's terms of service and ensuring ethical use of AI agents on the platform.

## Acknowledgments

- [Mastodon Server](https://github.com/mastodon/mastodon)
- [Ollama](https://github.com/ollama/ollama)
- [Hugging Face](https://github.com/huggingface)
- [Pydantic](https://github.com/pydantic/pydantic)