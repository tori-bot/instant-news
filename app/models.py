from unicodedata import name


class NewsSource:
    #clas that defines news source objects
    def __init__(self,org_name,description,url,language,country):
        self.org_name=org_name
        self.description=description
        self.url=url
        self.language=language
        self.country=country


class NewsArticle:
    #class that defines news article objects
    def __init__(self,title,url,image,description,created_time):
        self.title=title
        self.url=url
        self.image=image
        self.description=description
        self.created_time=created_time
