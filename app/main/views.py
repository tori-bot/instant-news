from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_articles,get_sources, get_trending,search_article
from ..models import NewsArticle, NewsSource

#views
@main.route('/')
def index():
    # function to view root page
    trending_news=get_trending()
    popular_sources=get_sources()

    title='Home of Instant News'

    search_article=request.args.get('news_query')

    if search_article:
        return redirect(url_for('.search',source=search_article))
    else:
        return render_template('index.html',title=title,trending_news=trending_news,popular_sources=popular_sources)

@main.route('/source/<source>')
def article(source):
    #function to view article page 
    articles=get_articles(source)
    
   
    return render_template('source.html',articles=articles)

@main.route('/search/<source>')
def search(source):
    #function to view search results
    news_list=source.split(' ')
    source_format='+'.join(news_list)
    searched_news=search_article(source_format)

    title=f' {source} '

    return render_template('search.html',articles=searched_news,title=title)