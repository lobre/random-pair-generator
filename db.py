from pymongo import MongoClient
from bson.objectid import ObjectId
import config

def get_db():
    client = MongoClient('{}:{}'.format(config.DB_HOST, config.DB_PORT))
    db = client[config.DB_NAME]
    return db

def add_item(name, photo):
    get_db().items.insert({
        "name": name,
        "photo": photo
    })
    
def get_items():
    return get_db().items.find()

def get_item(id):
    return get_db().items.find_one({"_id": ObjectId(id)})

def remove_item(id):
    get_db().items.delete_one({"_id": ObjectId(id)})

def init_config():
    if get_db().config.count() == 0:
        get_db().config.insert({
            "message-before": "",
            "message-after": ""
        })

def get_config():
    init_config()
    return get_db().config.find_one()
    
def set_message_before(message):
    init_config()
    get_db().config.update({}, {"$set": {"message-before": message}})

def set_message_after(message):
    init_config()
    get_db().config.update({}, {"$set": {"message-after": message}})

def get_pairs():
    return get_db().pairs.find()

def add_pair(pair):
    get_db().pairs.insert(pair)

def reset_pairs():
    get_db().pairs.drop()

def has_pairs():
    return get_db().pairs.count() != 0
