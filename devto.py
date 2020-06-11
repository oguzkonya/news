from bs4 import BeautifulSoup as bs
from newspiece import NewsPiece
from newssource import NewsSource
import time

class DevTo(NewsSource):

    URL = "https://dev.to/"
    title = "Dev.to"
    spanclass = "devto"


    def frontpage(self):
        bs = self.fetch(self.URL)
        news = []

        if bs is not None:
            stories = bs.find_all("div", {"class": "crayons-story"})

            for story in stories:
                date = self.parseDate(time.strptime(story.find("time")["datetime"], "%Y-%m-%dT%H:%M:%SZ"))
                t = story.find("h2", {"class": "crayons-story__title"}).a
                link = "https://dev.to" + t['href']
                title = t.contents[-1].strip()
                comments = link + "#comments"

                newsPiece = NewsPiece(title, date, link, comments)
                news.append(newsPiece)

        return news