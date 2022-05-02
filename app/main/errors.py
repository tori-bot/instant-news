from flask import render_template
from . import main

@main.app_errorhandler(404)
def fourOfour(error):
    #function to render 404 error page
    return render_template('fourOfour.html'),404