import pymongo
from pymongo.objectid import ObjectId

def _format_book(book):
    book["_id"] = str(book["_id"])
    book["info_url"] = "/info/%s" % book["_id"]
    book["get_url"] = "/get/%s" % book["_id"]
    del book["path"]
    return book

def connect():
    return pymongo.Connection()["catacombs"]

def get_books():
    return map(_format_book, list(connect()['books'].find()))

def get_a_book(id):
    return _format_book(connect()['books'].find_one({"_id": ObjectId(id)}))

def add_a_book(book_path, file_name):
    return connect()["books"].insert(
        {
         "path": book_path,
         "name": file_name,
        }
    )
