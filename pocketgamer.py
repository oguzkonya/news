from bs4 import BeautifulSoup as bs
from newspiece import NewsPiece
from newssource import NewsSource
import requests

class PocketGamer(NewsSource):

    URL = "https://www.pocketgamer.biz/news/"
    title = "PocketGamer"
    spanclass = "pocket-gamer"

    def frontpage(self):
        bs = self.fetch(self.URL)
        news = []

        if bs is not None:
            stories = bs.find("div", {"class": "listing news"}).find_all("div", {"class": "item"})

            for story in stories:
                date = story.find("span", {"class": "date"}).string
                t = story.find("h2").a
                link = "https://www.pocketgamer.biz" + t['href']
                title = t.string

                newsPiece = NewsPiece(title, date, link)
                news.append(newsPiece)

        return news