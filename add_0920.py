import gc
import re
from copy import deepcopy
import json
import requests
from pandas import read_csv
from playwright.sync_api import Playwright, sync_playwright, expect
from parsel import Selector, selector
import pymongo
from pymongo.collection import Collection

mongo = pymongo.MongoClient(host='127.0.0.1')
db = mongo['test']
col = db['add_new']  # type: Collection
df = read_csv('add_0921_finished.csv').fillna('')
T_df = df.T
headers = {'Host': 'en.softonic.com',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
           'Accept-Language': 'zh-CN,zh;q=0.9'}


def get_demo(keyword: str = None):
    url = 'https://en.softonic.com/s/{}:android'
    name = keyword
    request_url = url.format(name)
    response = requests.get(url=request_url, headers=headers)
    x = Selector(response.text)
    search_title = x.xpath('''//li[@class="search-results-list__item"][1]//h2/text()''').get().strip()
    n = re.findall(r'[a-zA-Z0-9]+', name.lower())
    t = re.findall(r'[a-zA-Z0-9]+', search_title.lower())
    if len(n) == 0 or len(t) == 0:
        return {}
    count = 0
    for k in t:
        k = k.lower()
        if k in n:
            count += 1
    rate = count / len(n)
    if rate <= 0.4:
        return {}
    s = x.xpath('''//li[@class="search-results-list__item"]''')[0]
    next_url = s.xpath('''.//a[@class="app-item-info__title"]/@href''').get()
    h = deepcopy(headers)
    h['Host'] = next_url.split('/')[2]
    response = requests.get(url=next_url, headers=h)
    x = Selector(response.text)
    articles = x.xpath('//article[@class="editor-review"]').get()
    try:
        articles = re.sub('<article(.*?)>', '', articles, count=0, flags=0)
    except:
        return
    articles = articles.replace("</article>", "")
    length = len(articles.split('<h3>'))
    detail = []
    big_art = ""
    for i in range(length):
        if i < 2:
            if i == 0:
                string = f'<div class="detailinfo">{articles.split("<h3>")[i]}</div>'
            else:
                string = f'<div class="detailinfo"><h3>{articles.split("<h3>")[i]}</div>'
            detail.append(string)
        else:
            string = f'<div class="detailinfo"><h3>{articles.split("<h3>")[i]}</div>'
            big_art += string
    detail.append(big_art)
    dt = {}
    for j in range(len(detail)):
        if j == 0:
            k = 1
        else:
            k = j + 1
        dt[f"detailinfo_{k}"] = detail[j]
    dt['brand'] = keyword
    dt['rate'] = rate
    return dt


def get_sth(keyword: str = None):
    url = 'https://en.softonic.com/s/{}:android'

    # threading.Thread(target=demo, args=(df, )).start()
    name = keyword
    request_url = url.format(name)
    response = requests.get(url=request_url, headers=headers)
    x = Selector(response.text)
    search_title = x.xpath('''//li[@class="search-results-list__item"][1]//h2/text()''').get().strip()
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
        return {}
    result = ''.join(s.xpath('''.//text()''').extract())
    ins = {
        "softonic_desc": result.replace('\xa0', ''),
        "search_title": search_title
    }
    # print(ins)
    return ins


def get_apps(app_name, content):
    """
    开发者，price， 标签
    :param app_name:
    :param link:
    :return: developer， price， category
    """
    response = Selector(content)
    appstore_developer = response.xpath('''//h2/a/text()''').get().strip()
    if response.xpath(
            '''//li[@class="inline-list__item inline-list__item--bulleted app-header__list__item--price"]/text()'''):
        appstore_price = response.xpath(
            '''//li[@class="inline-list__item inline-list__item--bulleted app-header__list__item--price"]/text()''').get().strip()
    else:
        appstore_price = ''
    try:
        category = re.findall(r'#\d+ in (\w+)',
                              response.xpath(
                                  '''//ul[@class="inline-list inline-list--mobile-compact"]/a/text()''').get())
    except:
        category = ''
    if category:
        category = category[0]
    else:
        category = ''
    rating_raw = response.xpath('''//figcaption/text()''').get()
    return {
        "developer": appstore_developer,
        "price": appstore_price,
        "category": category,
        "brand": app_name,
        "rating_raw": rating_raw
    }


def get_google(app_name, content):
    """
    app介绍，评分，logo，app名字
    :param app_name:
    :param link:
    :return: app_name, link, description, rating, logo
    """
    response = Selector(content)
    google_desc = response.xpath('''//div[@data-g-id="description"]''').get()
    google_logo = response.xpath('''//div[@class="l8YSdd"]/img[@alt="Icon image"]/@src''').get()
    if response.xpath('''//div[@itemprop="starRating"]/div/text()'''):
        rating = response.xpath('''//div[@itemprop="starRating"]/div/text()''').get()
    else:
        rating = ''
    return {
        "brand": app_name,
        "rating": rating,
        "google_description": google_desc.replace('<div class="bARER" data-g-id="description">', '').strip('</div>'),
        "logo": google_logo
    }


def run(playwright, brand, google_link, appstore_link):
    results = {}
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    if google_link:
        page.goto(google_link)
        page.wait_for_url(google_link)
        google_content = page.content()
        google_data = get_google(brand, google_content)
        # print(google_data)
    else:
        google_data = {}
        # print(google_data)
    if appstore_link:
        page.goto(appstore_link)
        page.wait_for_url(appstore_link)
        appstore_content = page.content()
        apple_data = get_apps(brand, appstore_content)
        # print(apple_data)
    else:
        apple_data = {}
        # print(apple_data)
    softonic = get_sth(brand)
    s = get_demo(brand)
    # print(softonic)
    page.close()
    context.close()
    browser.close()
    gc.collect()
    results.update(google_data)
    results.update(apple_data)
    results.update(s)
    results.update(softonic)
    results['app_store_link'] = appstore_link
    results['google_play_link'] = google_link
    results['brand'] = brand
    if 'brans' in results.keys():
        del results['brans']
    print(json.dumps(results))
    col.insert_one(results)
    print(1)


def get_pr(keyword):
    url = 'https://en.softonic.com/s/{}:android'

    # threading.Thread(target=demo, args=(df, )).start()
    name = keyword
    request_url = url.format(name)
    response = requests.get(url=request_url, headers=headers)
    x = Selector(response.text)
    search_title = x.xpath('''//li[@class="search-results-list__item"][1]//h2/text()''').get().strip()
    s = x.xpath('''//li[@class="search-results-list__item"]''')[0]
    next_url = s.xpath('''.//a[@class="app-item-info__title"]/@href''').get()
    h = deepcopy(headers)
    h['Host'] = next_url.split('/')[2]
    response = requests.get(url=next_url, headers=h)
    response = Selector(response.text)
    if response.xpath('''//section[@class="pros-and-cons"]'''):
        CP = response.xpath('''//section[@class="pros-and-cons"]''')
        Pros = CP.xpath('''./div[@data-meta="app-pros"]/ul/li/text()''').extract()
        Cons = CP.xpath('''./div[@data-meta="app-cons"]/ul/li/text()''').extract()
    else:
        return {}
    return {
        "brand": keyword,
        "Prons": Pros,
        "Crons": Cons
    }


# for i in T_df:
#     i = T_df[i]
#     brand = i['app name']
#     google_link = i['andriod']
#     appstore_link = i['apple']
#     # print(brand, google_link, appstore_link)
#     with sync_playwright() as playwright:
#         run(playwright, brand, google_link, appstore_link)

if __name__ == '__main__':
    for i in T_df:
        i = T_df[i]
        brand = i['app name']
        # print(brand, google_link, appstore_link)
        value = get_pr(brand)
        if value:
            print(value)
            v = col.update_one({"brand": brand}, {"$set": value})
            print(v.raw_result)
