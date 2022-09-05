import pymongo
from copy import deepcopy
import logging
class AppfiguresComPipeline:
    def __init__(self, settings):
        self.count = 0
        self.mongo_cli = pymongo.MongoClient(host='127.0.0.1', port=27017)
        # self.mongo_cli = pymongo.MongoClient(host='192.168.131.163', port=27017, username='mongouser', password='JHFjsh980$#@.')
        self.mongo_db = self.mongo_cli['crawlab_test']
        self.collection = self.mongo_db['Store_Rewiews']

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings)

    def close_spider(self, spider):
        self.mongo_cli.close()

    def process_item(self, item, spider):
        itemd = dict(item)
        cond1 = {'name': itemd['name']}

        c1 = self.collection.find_one(filter=cond1)
        if c1:
            # 已存在的产品更新价格
            data = deepcopy(itemd)
            try:
                del data['_id']
            except KeyError:
                pass
            try:
                ret = self.collection.update_one(filter=cond1, update={'$set': data}, upsert=True)
            except Exception as e:
                logging.log(msg="fAILED UPDATE MONGO %s" % e, level=logging.INFO)
            else:
                logging.log(msg="UPDATE MONGO %s" % itemd['name'], level=logging.INFO)

        else:
            try:
                self.collection.insert_one(dict(item))
                self.count += 1
            except Exception as e:
                logging.log(msg="FAILED TO INSERT INTO MONGO %s" % e, level=logging.INFO)

            else:
                logging.log(msg="INSERT INTO MONGO %d" % self.count, level=logging.INFO)

        return item
