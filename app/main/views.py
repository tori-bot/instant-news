from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_article,get_sources, get_trending,search_article
from ..models import NewsArticle, NewsSource

#views
@main.route('/')
def index():
    # view root page function
    trending_news=get_trending('source')
    popular_sources=get_sources('source')

    title='Home of Instant News'

    search_article=request.args.get('news_query')

    if search_article:
        return redirect(url_for('.search',source=search_article))
    else:
        return render_template('index.html',title=title,trending_news=trending_news,popular_sources=popular_sources)
