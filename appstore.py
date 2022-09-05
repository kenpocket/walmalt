from infer import fingVerifChrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import json
import time

import pymongo

client = pymongo.MongoClient('mongodb://127.0.0.1:27017')
db = client.crawlab_test
collection = db.Store_Rewiews  # type:pymongo.collection.Collection


def get_from_Appstore(keywords):
    start_url = 'https://www.apple.com/app-store/'
    chrome = fingVerifChrome().modifyEnviroment()
    chrome.get(start_url)
    chrome.implicitly_wait(30)
    chrome.find_element(By.XPATH, '''//li/a[@href="/us/search"]''').click()
    search = chrome.find_element(By.XPATH, '//input[@id="ac-gn-searchform-input"]')
    search.send_keys(keywords)
    search.send_keys(Keys.ENTER)
    details = chrome.find_element(By.XPATH, '//div[1]/div/ul/li/a')
    try:
        details.click()
    except:
        chrome.close()
        return
    time.sleep(2)
    Price = chrome.find_element(By.XPATH,
                                '''//li[@class="inline-list__item inline-list__item--bulleted app-header__list__item--price"]''').text
    Category = chrome.find_elements(By.XPATH, '''//ul/li/ul/a''')[0].text.split(' in ')[-1].strip()
    url = chrome.current_url
    chrome.close()
    if Price == 'Free':
        price = 0.0
    else:
        price = float(Price.replace('$', '').strip())
    categories = [Category]
    collection.update_one({"name": keywords}, {"$set": {"appstore_url": url, "price": price, "category": categories}})
    print(price, categories, url)


if __name__ == '__main__':
    file = open('names.txt', 'r', encoding='utf-8')
    data = file.readlines()
    for d in data:
        d = d.strip()
        get_from_Appstore(d)
