import feedparser
from newssource import NewsSource
from newspiece import NewsPiece

class Slashdot(NewsSource):

    URL = "http://rss.slashdot.org/Slashdot/slashdotMain"
    title = "Slashdot"
    spanclass = "slashdot"


    def frontpage(self):
        rss = feedparser.parse(self.URL)
        news = []

        for story in rss.entries:

            date = story.updated
            link = story.link
            title = story.title
            comments = story.link

            newsPiece = NewsPiece(title, date, link, comments)
            news.append(newsPiece)

        return news