from unicodedata import name


class NewsSource:
    #clas that defines news source objecta
    def __init__(self,org_name,description,url,language,country):
        self.org_name=org_name
        self.description=description
        self.url=url
        self.language=language
        self.country=country