import urllib.request,json
from .models import NewsSource

api_key=None
base_url=None

def configure_request(app):
    global api_key,base_url
    api_key=app.config['API_KEY']
    base_url=app.config['BASE_URL']

def get_sources(sources):
    #this function with arg:sources gets json response to our url request
    get_sources_url=base_url.format(sources,api_key)