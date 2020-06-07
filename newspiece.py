class NewsPiece():
    
    def __init__(self, title, date, link):
        self.title = title
        self.date = date
        self.link = link

    def __str__(self):
        return f'{self.title} ({self.link}) [{self.date}]'