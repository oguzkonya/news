import re
from bs4 import BeautifulSoup as bs
from newspiece import NewsPiece
from newssource import NewsSource

class GithubTrending(NewsSource):

    URL = "https://github.com/trending?spoken_language_code=en"
    title = "GitHub Trending"
    spanclass = "github-trending"
    

    def frontpage(self):
        bs = self.fetch(self.URL)
        news = []

        if bs is not None:
            try:
                stories = bs.find_all("article", {"class": "Box-row"})

                for story in stories:
                    date = "today"
                    link = story.find("h1").a['href']
                    titleP = story.find("p")

                    if titleP is not None:
                        titleP = titleP.getText()
                        title = link + ": " + titleP
                    else:
                        title = link

                    link = "https://github.com" + link
                    comments = "#"
                    newsPiece = NewsPiece(title, date, link, comments)
                    news.append(newsPiece)
            except Exception as e:
                print(e)

        return news