import llm_mastodon_agent as llmma

# TODO
article = llmma.tools.NewsArticle(topic="Baseball")

print(article.url)
print(article)
