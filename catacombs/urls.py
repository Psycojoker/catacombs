# inspired by http://bitworking.org/news/Why_so_many_Python_web_frameworks

import selector
from json import dumps
import db
import os
import socket

extensions = {
    'html': 'text/html',
    'atom': 'application/atom+xml'
}

def request(func):
    def decorate(environ, start_response):
        print start_response, func(environ)
        return render(start_response, func(environ))
    return decorate

def render(start_response, text, headers=[('Content-Type', "text/html")]):
    # I think that the next 2 lines does nothing, was coming from the example, strange
    start_response("200 OK", headers)
    return text

@request
def home(environ):
    return dumps({"books": "/books", "peers": "/list", "about": "/about"})

@request
def books(environ):
    return dumps(db.get_books())

@request
def info_on_a_book(environ):
    id = environ['selector.vars']['id']
    return dumps(db.get_a_book(id))

@request
def about(environ):
    return dumps({"owner": "%s@%s" % (os.environ["USER"], socket.gethostname())})

@request
def list_peers(environ):
    return dumps(db.get_peers())

def get_on_a_book(environ, start_response):
    id = environ['selector.vars']['id']
    return render(start_response, open(db.get_a_book(id, remove_path=False)["path"], "r").read(), contenttype="application/pdf")

urls = selector.Selector()
urls.add('/', GET=home)
urls.add('/books', GET=books)
urls.add('/list', GET=list_peers)
urls.add('/info/{id}', GET=info_on_a_book)
urls.add('/get/{id}', GET=get_on_a_book)
urls.add('/about', GET=about)
