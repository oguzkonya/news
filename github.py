from bs4 import BeautifulSoup as bs
from newspiece import NewsPiece
from newssource import NewsSource

class GithubTrending(NewsSource):

    URL = "https://github.com/trending"
    title = "GitHub Trending"
    spanclass = "github-trending"

    def frontpage(self):
        bs = self.fetch(self.URL)
        news = []

        if bs is not None:
            stories = bs.find_all("article", {"class": "Box-row"})

            for story in stories:
                date = "today"
                link = story.find("h1").a['href']
                titleP = story.find("p")

                if titleP is not None:
                    title = titleP.encode_contents().decode('UTF-8').strip()
                else:
                    title = link

                link = "https://github.com" + link
                newsPiece = NewsPiece(title, date, link)
                news.append(newsPiece)

        return news