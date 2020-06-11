from datetime import datetime
from newsprinter import Printer
from hackernews import HackerNews           # rss
from lobsters import Lobsters               # rss
from pocketgamer import PocketGamer         # rss
from gamesindustry import GamesIndustry     # rss
from gamasutra import GamasutraNews         # rss
from gamasutra import GamasutraBlogs        # rss
from reddit import RedditProgramming        # rss
from slashdot import Slashdot               # rss
from oyungezer import Oyungezer             # bs
from devto import DevTo                     # bs
from github import GithubTrending           # bs

class NewsAggregator():

    sources = []
    printer = Printer()


    def __init__(self):
        self.sources = [
            HackerNews(),
            Lobsters(),
            PocketGamer(),
            GamesIndustry(),
            GamasutraNews(),
            GamasutraBlogs(),
            RedditProgramming(),
            Slashdot(),
            Oyungezer(),
            DevTo(),
            GithubTrending(),
        ]


    def frontpage(self):
        newshtml = ""

        for source in self.sources:
            stories = source.frontpage()
            news = ""

            for story in stories:
                news = news + self.printer.printStory(story)

            newshtml = newshtml + self.printer.printSource(source, news)

        self.write(newshtml)
        

    def write(self, html):
        contents = self.printer.printIndex(html, datetime.now().strftime("%d/%m/%Y %H:%M:%S"))

        g = open("index.html", "w")
        g.write(contents)
        g.close()


if __name__ == "__main__":
    aggregator = NewsAggregator()
    aggregator.frontpage()