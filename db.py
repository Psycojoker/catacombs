import pymongo

def connect():
    return pymongo.Connection()["catacombs"]

def get_books():
    a = list(connect()['books'].find())
    for i in a:
        i["_id"] = str(i["_id"])
    return a
