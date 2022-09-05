import pymongo
import re

# 连接数据库
client = pymongo.MongoClient('mongodb://127.0.0.1:27017')
db = client.crawlab_test
collection = db.Store_Rewiews  # type: pymongo.collection.Collection
a = collection.find()
for i in a:
    if i.get('price', ''):
        collection.update_one({"name": i['name']}, {"$set": {"price": i['price'] / 10}})