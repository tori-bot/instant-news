from unicodedata import category
import urllib.request,json
from .models import NewsArticle, NewsSource

api_key=None
base_url=None

def configure_request(app):
    #function to configure the  apirequests for the application
    global api_key,base_url
    api_key=app.config['API_KEY']
    base_url=app.config['BASE_URL']

def get_sources():
    #this function with arg:sources gets json response to our url request
    get_sources_url='https://newsapi.org/v2/top-headlines/sources?apiKey={}'.format(api_key)

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

def get_trending(source):
    #function to get trending news in specific country
    get_trending_url='https://newsapi.org/v2/top-headlines?q={}&apiKey={}'.format(source,api_key)

    with urllib.request.urlopen(get_trending_url) as url:
        get_trending_data=url.read()
        get_trending_response=json.loads(get_trending_data)

        trending_results=None

        if get_trending_response['articles']:
            trending_list=get_trending_response['articles']
            trending_results=process_results(trending_list)

    return trending_results


def get_article(source):
    #function to get a specific article
    get_article_url=base_url.format(source,api_key)

    with urllib.request.urlopen(get_article_url) as url:
        article_data=url.read()
        article_response=json.loads(article_data)

        article=None

        if article_response:
            source=article_response.get('source')
            author=article_response.get('author')
            title=article_response.get('title')
            description=article_response.get('description')
            url=article_response.get('url')
            image=article_response.get('urlToImage')
            content=article_response.get('content')
            created_at =article_response.get('publishedAt')

            article=NewsArticle(source,author,title,url,image,description,created_at,content)

        return article

def search_article(source):
    #function that returns search results from all news in api request
    search_url='https://newsapi.org/v2/top-headlines?q={}&apiKey={}'.format(source,api_key)

    with urllib.request.urlopen(search_url) as url:
        search_data=url.read()
        search_response=json.loads(search_data)

        search_results=None

        if search_response['articles']:
            search_list=search_response['articles']
            search_results=process_results(search_list)

    return search_results

