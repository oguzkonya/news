class Printer():

    def __init__(self):
        self.storyTemplate = self.readContents("includes/story.html")
        self.sourceTemplate = self.readContents("includes/source.html")
        self.commentsTemplate = self.readContents("includes/comments.html")
        self.homeTemplate = self.readContents("layouts/home.html")


    def readContents(self, filename):
        f = open(filename, "r")
        contents = f.read()
        f.close()
        return contents


    def printStory(self, story):
        if story.comments != "#":
            c = self.commentsTemplate.replace("{comments}", story.comments)
        else:
            c = ""

        return self.storyTemplate.replace("{link}", story.link).replace("{title}", story.title).replace("{domain}", story.domain).replace("{date}", story.date).replace("{comments}", c)


    def printSource(self, source, stories):
        return self.sourceTemplate.replace("{spanclass}", source.spanclass).replace("{title}", source.title).replace("{stories}", stories)


    def printIndex(self, news, date):
        return self.homeTemplate.replace("{news}", news).replace("{date}", date)