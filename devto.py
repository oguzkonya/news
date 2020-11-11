from bs4 import BeautifulSoup as bs
from newspiece import NewsPiece
from newssource import NewsSource
import time

class DevToGamedev(NewsSource):

    URL = "https://dev.to/feed/tag/gamedev"
    title = "Dev.to #gamedev"
    spanclass = "devto-gamedev"

class DevToCsharp(NewsSource):

    URL = "https://dev.to/feed/tag/csharp"
    title = "Dev.to #csharp"
    spanclass = "devto-csharp"