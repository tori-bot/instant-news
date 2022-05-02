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