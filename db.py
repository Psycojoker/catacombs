import pymongo

def connect():
    return pymongo.Connection()["catacombs"]

def get_books():
    a = list(connect()['books'].find())
    for i in a:
        i["_id"] = str(i["_id"])
        i["info_url"] = "/info/%s" % i["_id"]
        i["get_url"] = "/get/%s" % i["_id"]
    return a
