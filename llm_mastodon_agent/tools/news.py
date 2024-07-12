import random

import pydantic

import gnews
import newspaper
import requests


class NewsArticle(pydantic.BaseModel):
    topic: str

    n: int = 10

    url: str = None
    title: str = None
    summary: str = None

    def model_post_init(self, _):
        news_page = self.retrieve_news_page()
        news = random.choice(news_page)

        self.url = requests.get(news["url"]).url

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
