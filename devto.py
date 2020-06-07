from bs4 import BeautifulSoup as bs
from newspiece import NewsPiece
from newssource import NewsSource

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
                date = story.find("time")["datetime"]
                t = story.find("h2", {"class": "crayons-story__title"}).a
                link = "https://dev.to" + t['href']
                title = t.contents[-1].strip()

                newsPiece = NewsPiece(title, date, link)
                news.append(newsPiece)

        return news