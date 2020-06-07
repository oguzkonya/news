from bs4 import BeautifulSoup as bs
from newspiece import NewsPiece
from newssource import NewsSource

class GamesIndustry(NewsSource):

    URL = "https://www.gamesindustry.biz/"
    title = "GamesIndustry.biz"
    spanclass = "games-industry"

    def frontpage(self):
        bs = self.fetch(self.URL)
        news = []

        if bs is not None:
            headlines = bs.find_all("div", {"class": "headline"})

            for headline in headlines:
                date = headline.find("span", {"class": "timestamp"}).contents[-1].strip()
                t = headline.find("a", {"class": "link-overlay"})
                link = "https://www.gamesindustry.biz" + t['href']
                title = t['title']

                newsPiece = NewsPiece(title, date, link)
                news.append(newsPiece)

            entries = bs.find_all("div", {"class": "entry"})

            for entry in entries:
                date = entry.find("a", {"class": "timestamp"}).contents[-1].strip()
                t = entry.find("h2", {"class": "title"}).a
                link = "https://www.gamesindustry.biz" + t['href']
                title = t.string

                newsPiece = NewsPiece(title, date, link)
                news.append(newsPiece)

            features = bs.find_all("div", {"class": "feature"})

            for feature in features:
                date = feature.find("a", {"class": "timestamp"}).contents[-1].strip()
                t = feature.find("a", {"class": "link-overlay"})
                link = "https://www.gamesindustry.biz" + t['href']
                title = t['title']

                newsPiece = NewsPiece(title, date, link)
                news.append(newsPiece)

        return news