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