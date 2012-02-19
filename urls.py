# inspired by http://bitworking.org/news/Why_so_many_Python_web_frameworks

import selector
from json import dumps
import db

extensions = {
    'html': 'text/html',
    'atom': 'application/atom+xml'
}

def render(start_response, text):
    # I think that the next 2 lines does nothing, was coming from the example, strange
    contenttype = "text/html"
    start_response("200 OK", [('Content-Type', contenttype)])
    return text

def home(environ, start_response):
    return render(start_response, "hello world")

def books(environ, start_response):
    return render(start_response, dumps(db.get_books()))

urls = selector.Selector()
urls.add('/', GET=home)
urls.add('/books', GET=books)
