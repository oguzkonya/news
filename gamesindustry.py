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
                try:
                    date = headline.find("span", {"class": "timestamp"}).contents[-1].strip()
                    t = headline.find("h2", {"class": "title"}).a
                    link = "https://www.gamesindustry.biz" + t['href']
                    title = t.getText()
                    comments = link

                    newsPiece = NewsPiece(title, date, link, comments)
                    news.append(newsPiece)
                except Exception as e:
                    print(e)

            entries = bs.find_all("div", {"class": "entry"})

            for entry in entries:
                try:
                    date = entry.find("a", {"class": "timestamp"}).contents[-1].strip()
                    t = entry.find("h2", {"class": "title"}).a
                    link = "https://www.gamesindustry.biz" + t['href']
                    title = t.getText()
                    comments = link

                    newsPiece = NewsPiece(title, date, link, comments)
                    news.append(newsPiece)
                except Exception as e:
                    print(e)

            features = bs.find_all("div", {"class": "feature"})

            for feature in features:
                try:
                    date = feature.find("a", {"class": "timestamp"}).contents[-1].strip()
                    t = feature.find("h2", {"class": "title"}).a
                    link = "https://www.gamesindustry.biz" + t['href']
                    title = t.getText()
                    comments = link

                    newsPiece = NewsPiece(title, date, link, comments)
                    news.append(newsPiece)
                except Exception as e:
                    print(e)

        return news