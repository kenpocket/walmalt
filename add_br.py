import json
import httpx
from parsel import Selector

with open('brand_links.json', 'r', encoding='utf-8') as fp:
    data = json.load(fp)['RECORDS']
headers = {
    "Host": "play.google.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "zh-cn;q=0.8,en-US;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
}
values = {}
for d in data:  # type: dict
    brand = d['brand']
    file = open('finished_brand.txt', 'r', encoding='utf-8')
    data2 = file.read()
    file.close()
    data = data2.split('\n')
    if brand in values.keys() or not d['google_play_link'] or brand in data2:
        print(brand)
        continue
    print(d['google_play_link'])
    response = httpx.get(url=d['google_play_link'], headers=headers)
    if response.status_code == 200:
        pass
    else:
        print(response.status_code)
        continue
    x = Selector(response.text)
    value = x.xpath('''//div[@data-g-id="description"]''').get().rstrip('</div>').lstrip(
        '<div class="bARER" data-g-id="description">')
    print(value)
    values[d['brand']] = {"google_description": value, "brand": d['brand'], "google_play_link": d['google_play_link']}
    with open('change_desc.json', 'a', encoding='utf-8') as fp:
        fp.write(json.dumps(values[brand]) + '\n')
    with open('finished_brand.txt', 'a', encoding='utf-8') as fp:
        fp.write(brand + '\n')
