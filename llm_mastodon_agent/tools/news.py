import random
import functools
import re
import base64

import pydantic

import gnews
import newspaper
import requests


# source: https://stackoverflow.com/a/59023463/
_ENCODED_URL_PREFIX = "https://news.google.com/rss/articles/"
_ENCODED_URL_PREFIX_WITH_CONSENT = "https://consent.google.com/m?continue=https://news.google.com/rss/articles/"
_ENCODED_URL_RE = re.compile(fr"^{re.escape(_ENCODED_URL_PREFIX_WITH_CONSENT)}(?P<encoded_url>[^?]+)")
_ENCODED_URL_RE = re.compile(fr"^{re.escape(_ENCODED_URL_PREFIX)}(?P<encoded_url>[^?]+)")
_DECODED_URL_RE = re.compile(rb'^\x08\x13".+?(?P<primary_url>http[^\xd2]+)\xd2\x01')


@functools.lru_cache(2048)
def _decode_google_news_url(url: str) -> str:
    match = _ENCODED_URL_RE.match(url)
    encoded_text = match.groupdict()["encoded_url"]  # type: ignore
    encoded_text += "==="  # Fix incorrect padding. Ref: https://stackoverflow.com/a/49459036/
    decoded_text = base64.urlsafe_b64decode(encoded_text)

    match = _DECODED_URL_RE.match(decoded_text)

    primary_url = match.groupdict()["primary_url"]  # type: ignore
    primary_url = primary_url.decode()
    return primary_url.strip()


def decode_google_news_url(url: str) -> str:
    return _decode_google_news_url(url) if url.startswith(_ENCODED_URL_PREFIX) else url


class NewsArticle(pydantic.BaseModel):
    topic: str

    n: int = 10

    url: str = ""
    title: str = ""
    summary: str = ""

    def model_post_init(self, _):
        news_page = self.retrieve_news_page()
        news = random.choice(news_page)

        self.url = decode_google_news_url(requests.get(news["url"]).url)

        article = self.retrieve_article()

        self.title = article.title
        self.summary = article.summary.replace("\n", " ")

    def __call__(self) -> dict:
        return {
            "url": self.url,
            "title": self.title,
            "summary": self.summary.replace("\n", " "),
        }

    def __str__(self) -> str:
        return f"Title:{self.title}\nSummary:{self.summary}"

    def retrieve_news_page(self):
        return gnews.GNews(max_results=self.n).get_news(self.topic)

    def retrieve_article(self):
        article = newspaper.Article(self.url)
        article.download()
        article.parse()
        article.nlp()

        return article



