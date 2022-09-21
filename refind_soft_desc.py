import pymongo
import json
mongo = pymongo.MongoClient(host='192.168.131.163', port=27017, username='mongouser', password='JHFjsh980$#@.')
data = json.load(open('add_soft_desc.json','r', encoding='utf-8'))
crawlab_test = mongo['crawlab_test']
AFC_appurse = crawlab_test['AFC_appurse']

for i in data:
    brand=(i['brand'])
    softonic_desc = (i['softonic_desc'])
    AFC_appurse.update_many({"brand":brand}, {"$set":{"brand": brand, "softonic_desc": softonic_desc}})