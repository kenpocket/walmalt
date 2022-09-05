import pymongo
import re

# 连接数据库
client = pymongo.MongoClient('mongodb://127.0.0.1:27017')
db = client.crawlab_test
collection = db.Store_Rewiews  # type: pymongo.collection.Collection
a = collection.find({}, {"_id": 0, "name": 1, "search_title": 1})
a = [i for i in a]
for i in a:
    name = i['name']
    search_title = i['search_title']
    n = re.findall(r'[a-zA-Z0-9]+', name)
    t = re.findall(r'[a-zA-Z0-9]+', search_title)
    if len(n) == 0 or len(t) == 0:
        continue
    count = 0
    for k in t:
        if k in n:
            count += 1
    rate = count / len(n)
    if rate <= 0.2:
        collection.update_one({"name": name}, {'$set': {"search_title": "", "Prons": "", "Crons": "", "softonic_desc": ""}})
    print(rate)
