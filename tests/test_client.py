import logging

import llm_mastodon_agent as llmma


class TestClient:
    def test__get_timline(self, client: llmma.mastodon.Client):
        timeline = client.get_timeline()
        assert isinstance(timeline, llmma.mastodon.Timeline)
        logging.debug(timeline)
        logging.debug(timeline.to_prompt_segment(n=2))

        post = timeline.select_random()
        assert isinstance(post, llmma.mastodon.Post)
        logging.debug(post)
        logging.debug(post.to_prompt_segment())

    def test__get_history(self, client: llmma.mastodon.Client):
        history = client.get_history()
        logging.debug(history)

    def test__get_post_w_replies(self, client: llmma.mastodon.Client):
        thread = client.get_post_w_replies("112734105231328503")
        logging.debug(thread)
        logging.debug(thread.to_prompt_segment())
