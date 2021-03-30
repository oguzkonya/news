class NewsPiece():
    
    def __init__(self, title, date, link, comments):
        self.title = self.clearTitle(title)
        self.date = date
        self.link = link
        self.comments = comments
        self.domain = self.convertLinkToDomain(link)


    def convertLinkToDomain(self, url):
        if url.startswith("https://"):
            url = url.replace("https://", "")
        
        if url.startswith("http://"):
            url = url.replace("http://", "")

        if url.startswith("www."):
            url = url.replace("www.", "")

        return url.split('/')[0]


    def clearTitle(self, title):
        mapping = [ ("&amp;", "&"), ("&#039;", "'") ]
        for k, v in mapping:
            title = title.replace(k, v)

        return title


    def __str__(self):
        return f'{self.title} ({self.link}) [{self.date}]'