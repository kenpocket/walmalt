import threading

import requests
import json
from parsel import Selector
from copy import deepcopy
import pymongo
myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
mydb = myclient["crawlab_test"]
mycol = mydb["Store_Rewiews"]
proxies = {"https": "http://127.0.0.1:7890"}
headers = {'Host': 'en.softonic.com',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
           'Accept-Language': 'zh-CN,zh;q=0.9'}
def demo(df):
    url = 'https://en.softonic.com/s/{}:android'
    for d in df:
        if 'search_title' not in d.keys():
            continue
        name = d['name'].split(':')[0]
        request_url = url.format(name)
        response = requests.get(url=request_url, headers=headers)
        x = Selector(response.text)
        s = x.xpath('''//li[@class="search-results-list__item"]''')[0]
        next_url = s.xpath('''.//a[@class="app-item-info__title"]/@href''').get()
        h = deepcopy(headers)
        h['Host'] = next_url.split('/')[2]
        response = requests.get(url=next_url, headers=h)
        x = Selector(response.text)
        try:
            s = x.xpath('''//article[@class="editor-review"]''')[0]
        except Exception as e:
            print(e)
        s = s.xpath('''.//p''')[0]
        print(s)
        # ins = {
        #     "softonic_desc": '',
        # }
        # mycol.update_one(filter={"name": d['name']}, update={'$set': ins}, upsert=True)

def get_sth(keywords: str = None):
    url = 'https://en.softonic.com/s/{}:android'
    data = mycol.find()
    data = [i for i in data]
    df = data[::-1]
    # threading.Thread(target=demo, args=(df, )).start()
    for d in data:
        if 'search_title' not in d.keys():
            continue
        name = d['name'].split(':')[0]
        request_url = url.format(name)
        response = requests.get(url=request_url, headers=headers)
        x = Selector(response.text)
        s = x.xpath('''//li[@class="search-results-list__item"]''')[0]
        next_url = s.xpath('''.//a[@class="app-item-info__title"]/@href''').get()
        h = deepcopy(headers)
        h['Host'] = next_url.split('/')[2]
        response = requests.get(url=next_url, headers=h)
        x = Selector(response.text)
        try:
            s = x.xpath('''//article[@class="editor-review"]''')[0]
        except Exception as e:
            print(e)
        try:
            s = s.xpath('''.//p''')[0]
        except:
            continue
        result = ''.join(s.xpath('''.//text()''').extract())
        ins = {
            "softonic_desc": result.replace('\xa0', '')
        }
        print(ins)
        mycol.update_one(filter={"name": d['name']}, update={'$set': ins}, upsert=True)


if __name__ == '__main__':
    get_sth()
