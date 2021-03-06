from bs4 import BeautifulSoup as bs
from newspiece import NewsPiece
from newssource import NewsSource

class Oyungezer(NewsSource):

    URL = "https://oyungezer.com.tr/etiket/haber"
    title = "Oyungezer"
    spanclass = "oyungezer"


    def frontpage(self):
        bs = self.fetch(self.URL)
        news = []

        if bs is not None:
            try:
                stories = bs.find_all("div", {"class": "card-body"})

                for story in stories:
                    date = story.find("h6", {"class": "card-date"}).a.string
                    t = story.find("h5", {"class": "card-title"}).a
                    link = "https:" + t['href']
                    title = t.string
                    comments = link + "#comment"

                    newsPiece = NewsPiece(title, date, link, comments)
                    news.append(newsPiece)
            except Exception as e:
                print(e)    

        return news