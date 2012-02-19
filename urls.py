# inspired by http://bitworking.org/news/Why_so_many_Python_web_frameworks

import selector
from json import dumps
import db
import os

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
    return render(start_response, dumps({"books": "/books", "peers": "/list"}))

def books(environ, start_response):
    return render(start_response, dumps(db.get_books()))

def info_on_a_book(environ, start_response):
    id = environ['selector.vars']['id']
    return render(start_response, dumps(db.get_a_book(id)))

def about(environ, start_response):
    print start_response
    return render(start_response, dumps({"owner": os.environ["USER"]}))

urls = selector.Selector()
urls.add('/', GET=home)
urls.add('/books', GET=books)
urls.add('/info/{id}', GET=info_on_a_book)
urls.add('/about', GET=about)
