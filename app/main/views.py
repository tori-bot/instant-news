from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_article,get_sources,search_article
from ..models import NewsArticle, NewsSource

#views
@main.route('/')
def index():
    # view root page function
    trending_news=get_article('source')
