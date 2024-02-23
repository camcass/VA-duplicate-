from Page import Page
class Book:
    bookName = ""
    numPages = -1
    bookStartPage = -1
    pageObjs = []
    def __init__(self, bookName, numPages, bookStartPage):
        self.bookName = bookName
        self.numPages = numPages
        self.bookStartPage = bookStartPage
    def addPage (self, pageToAdd):
        self.pageObjs.append(pageToAdd)