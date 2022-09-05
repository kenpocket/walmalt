import pymongo

mongoclient = pymongo.MongoClient(host='192.168.131.163', port=27017, username='mongouser', password='JHFjsh980$#@.')
mongo_db = mongoclient['crawlab_test']
mongo_col = mongo_db['AFC_appurse_copy1']  # type: pymongo.collection.Collection
with open('values.json', 'r', encoding='utf-8') as fp:
    data = fp.read()
import json

data = json.loads(data)['RECORDS']
for d in data:
    brand = d['brand']
    d.pop('brand')
    print(d)
    mongo_col.update_many({"name": brand}, {"$set":d})