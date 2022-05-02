from unicodedata import category
import urllib.request,json
from .models import NewsSource

api_key=None
base_url=None

def configure_request(app):
    #function to configure the  apirequests for the application
    global api_key,base_url
    api_key=app.config['API_KEY']
    base_url=app.config['BASE_URL']

def get_sources(sources):
    #this function with arg:sources gets json response to our url request
    get_sources_url=base_url.format(sources,api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data=url.read()
        get_sources_response=json.loads(get_sources_data)

        sources_results=None

        if get_sources_response['sources']:
            news_sources_list=get_sources_response['sources']
            sources_results=process_results(news_sources_list)
        return sources_results

def process_results(sources_list):
    #function processes seources results and transforns them to a list of objects
    sources_results=[]

    for source in sources_list:
        index=source.get('id')
        org_name=source.get('name')
        description=source.get('description')
        url=source.get('url')
        category=source.get('category')
        language=source.get('language')
        country=source.get('country')

        if url:
            source=NewsSource(index,org_name,description,url,category,language,country)

            sources_results.append(source)

        return sources_results

def get_article(index):
    #function to get a specific article
    get_article_url=base_url.format(index,api_key)

    with urllib.request.urlopen(get_article_url) as url:
        article_data=url.read()
        article_response=json.loads(article_data)

        article=None

        if article_response:
            index=article_response.get('id')
            
