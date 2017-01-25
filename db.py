from pymongo import MongoClient
from bson.objectid import ObjectId
import config

def get_db():
    client = MongoClient('{}:{}'.format(config.DB_HOST, config.DB_PORT))
    db = client[config.DB_NAME]
    return db

def add_item(name):
    get_db().items.insert({"name" : name})
    
def get_items():
    return get_db().items.find()

def remove_item(id):
    get_db().items.delete_one({"_id": ObjectId(id)})

