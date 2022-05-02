from unicodedata import name


class NewsSource:
    #clas that defines news source objects
    def __init__(self,index,org_name,description,category,url,language,country):
        self.index=index
        self.org_name=org_name
        self.description=description
        self.category=category
        self.url=url
        self.language=language
        self.country=country


class NewsArticle:
    #class that defines news article objects
    def __init__(self,author,title,url,image,description,created_time,content):
        self.author=author
        self.title=title
        self.url=url
        self.image=image
        self.description=description
        self.created_time=created_time
        self.content=content

