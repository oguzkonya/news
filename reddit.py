import feedparser
from newspiece import NewsPiece
from newssource import NewsSource

class RedditProgramming(NewsSource):

    URL = "https://www.reddit.com/r/programming/.rss"
    title = "r/programming"
    spanclass = "r-programming"