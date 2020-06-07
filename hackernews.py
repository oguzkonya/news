from newssource import NewsSource

class HackerNews(NewsSource):

    URL = "https://news.ycombinator.com/rss"
    title = "Hacker News"
    spanclass = "hacker-news"