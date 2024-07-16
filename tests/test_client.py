import logging

import llm_mastodon_agent as src

class TestClient:

    def test__get_timline(self, client):
        timeline = client.get_timeline()
        logging.debug(timeline)

# history = client.get_history()

# print(timeline.remove_replies().to_prompt_segment(n=3))

# print(timeline.remove_replies().select_random())

#thread = client.get_post_w_replies("112734105231328503")

# print(thread[0].to_prompt_segment() + thread.to_prompt_segment(n=3))
