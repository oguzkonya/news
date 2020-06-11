from newssource import NewsSource

class GamasutraNews(NewsSource):

    URL = "http://feeds.feedburner.com/GamasutraNews"
    title = "Gamasutra News"
    spanclass = "gamasutra-news"


class GamasutraBlogs(NewsSource):

    URL = "http://www.gamasutra.com/blogs/rss/"
    title = "Gamasutra Blogs"
    spanclass = "gamasutra-blogs"