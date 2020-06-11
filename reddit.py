from bs4 import BeautifulSoup as bs
from newspiece import NewsPiece
from newssource import NewsSource
import feedparser

class RedditProgramming(NewsSource):

    URL = "https://www.reddit.com/r/programming/.rss"
    title = "r/programming"
    spanclass = "r-programming"


    def frontpage(self):
        rss = feedparser.parse(self.URL)
        news = []

        for story in rss.entries:
            b = bs(story.content[0].value, features="html.parser")

            date = self.parseDate(story.updated_parsed)
            link = b.find_all("a")[1]["href"]
            title = story.title
            comments = story.link

            newsPiece = NewsPiece(title, date, link, comments)
            news.append(newsPiece)

        return news