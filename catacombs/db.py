import pymongo
from pymongo.objectid import ObjectId
from utils import md5Checksum

def _format_peer(peer):
    peer["_id"] = str(peer["_id"])
    return peer

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

def get_peers():
    return map(_format_peer, list(connect()['peers'].find()))

def get_a_book(id, remove_path=True):
    if remove_path:
        return _format_book(connect()['books'].find_one({"_id": ObjectId(id)}))
    else:
        return connect()['books'].find_one({"_id": ObjectId(id)})

def add_a_book(book_path, file_name):
    file_hash = md5Checksum(book_path)
    in_db_book = connect()["books"].find_one({"hash": file_hash})
    if in_db_book is not None:
        print "Error: file '%s' is already in the db with path '%s'" % (book_path, in_db_book["path"])
        if book_path != in_db_book["path"]:
            print "Updating file path with new path"
            in_db_book["path"] = book_path
            connect()["books"].save(in_db_book)
        return None
    return connect()["books"].insert(
        {
         "path": book_path,
         "name": file_name,
         "hash": file_hash,
        }
    )

def add_a_peer(peer_url, name):
    if connect()["peers"].find_one({"url": peer_url}) is not None:
        print "error: peer with url '%s' already exists" % peer_url
        return None
    return connect()["peers"].insert(
        {
         "url": peer_url,
         "name": name,
        }
    )
