import pymongo
# 连接数据库
import re

client = pymongo.MongoClient('mongodb://127.0.0.1:27017')
db = client.crawlab_test
collection = db.Store_Rewiews  # type: pymongo.collection.Collection
s = [i for i in collection.find({}, {"name": 1})]

# 选中所有不重复的id
for item in collection.distinct('name'):
    # 复制第一条id相同的数据
    repeating = collection.find_one({'name': item})
    # 删除所有id相同的数据
    result = collection.delete_many({'name': item})
    # 把刚刚复制的数据加入一条到数据库
    collection.insert_one(repeating)
