class Page:
    pageNumber = -1
    text = ""
    shortImageDescriptions = []
    longImageDescriptions = []
    discussionQuestions = []
    def __init__(self, pageNumber, text, shortImageDescriptions, longImageDescriptions, discussionQuestions):
        self.text = text
        self.pageNumber = pageNumber
        self.shortImageDescriptions = shortImageDescriptions
        self.longImageDescriptions = longImageDescriptions
        self.discussionQuestions = discussionQuestions
    def returnShortDescriptions(self):
        return self.shortImageDescriptions
    def returnText(self):
        return self.text
    def returnDiscussionQuestions(self):
        return self.discussionQuestions