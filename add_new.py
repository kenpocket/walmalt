import json
import pymongo
mongo = pymongo.MongoClient(host='192.168.131.163', port=27017, username='mongouser', password='JHFjsh980$#@.')
db = mongo['crawlab_test']
col = db['AFC_appurse']

brands = [i.get('brand', '') for i in col.find({},{"brand":1,"_id":0})]
data = json.load(open('add_new.json', encoding='utf-8'))
data = data['RECORDS']
for i in data:
    brand = i['brand']
    if brand in brands:
        col.update_many({"brand": brand}, {"$set": i})
    else:
        col.insert_one(i)
