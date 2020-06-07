from bs4 import BeautifulSoup as bs
from newspiece import NewsPiece
import feedparser
import requests

TIMEOUT = 5

class NewsSource():

    URL = ""

    def fetch(self, url):
        result = None

        try:
            response = requests.get(url, timeout=TIMEOUT)
            response.raise_for_status()
            result = bs(response.content, from_encoding=response.encoding, features="html.parser")
        except requests.exceptions.HTTPError as errh:
            print ("Http Error:", errh)
        except requests.exceptions.ConnectionError as errc:
            print ("Connection Error:", errc)
        except requests.exceptions.Timeout as errt:
            print ("Timeout Error:", errt)
        except requests.exceptions.RequestException as err:
            print ("Error: ", err)

        return result

    def frontpage(self):
        rss = feedparser.parse(self.URL)
        news = []

        for story in rss.entries:
            date = story.updated
            link = story.link
            title = story.title

            newsPiece = NewsPiece(title, date, link)
            news.append(newsPiece)

        return news