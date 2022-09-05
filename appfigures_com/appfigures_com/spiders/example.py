import scrapy
from scrapy import Request
from scrapy.http.response.text import TextResponse
import execjs
from scrapy.cmdline import execute
from parsel import Selector
from html import unescape


class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['appfigures.com']
    start_urls = ['https://appfigures.com/top-apps/google-play/united-states/top-overall']

    def start_requests(self):
        yield Request(url=self.start_urls[0], callback=self.parse, dont_filter=True)
        for i in range(50, 700, 50):
            url = 'https://appfigures.com/_u/api/ranks/snapshots?category=100&country=US&count=50&start={}&fields=results,id,entries,name,developer,developer_id,price,currency,storefront,vendor_identifier,category,subtype,timestamp,total_count'
            request_url = url.format(i)
            yield Request(url=request_url, callback=self.parse, dont_filter=True)

    def parse(self, response: TextResponse):
        meta = {}
        is_json = True
        try:
            response.json()
        except:
            is_json = False
        if is_json:
            data = response.json()
        else:
            for data in response.xpath('''//script[@type="text/javascript"]/text()''').extract():
                if '__appData' in data:
                    s = execjs.compile(data)
                    data = s.eval('__appData')[6]['-1503775441']
        for d in data['results']:
            for j in d['entries']:
                product_id = j['id']
                name = j['name']
                developer = j['developer']
                # print(name, developer)
                meta['name'] = name
                meta['developer'] = developer
                yield Request(url='https://appfigures.com/_u/data/profiles/product/{}'.format(product_id),
                              callback=self.parse_next, dont_filter=True, meta=meta)
                yield Request(url='https://appfigures.com/_u/data/profiles/product/{}/details'.format(j['id']),
                              callback=self.parse_google, dont_filter=True, meta=meta)
                yield Request(url='https://appfigures.com/_u/api/products?ids=' + str(j['id']), callback=self.get_icon,
                              dont_filter=True, meta=meta)

    def get_icon(self, response):
        meta = response.meta
        product_id = response.url.split('=')[-1]
        data = response.json()
        logo = data[product_id]['icon']
        # print("logo:", logo)
        yield {
            'name': meta['name'],
            'developer': meta['developer'],
            'logo': logo
        }

    def parse_next(self, response: TextResponse):
        meta = response.meta
        data = response.json()  # type: dict

        if 'exact_products' in data.keys():
            app_id = ''
            for app in data['exact_products']:
                if 'apple:ios' in app['storefronts'] or app['storefront'] == 'apple:ios':
                    app_id = app['id']
                else:
                    app_id = ''
        else:
            app_id = ''
        if app_id:
            yield Request(url='https://appfigures.com/_u/data/profiles/product/{}/details'.format(app_id),
                          callback=self.parse_app, dont_filter=True, meta=meta)

    def parse_app(self, response):
        meta = response.meta
        data = response.json()
        stores_id = data['stores_id']
        categories = []
        for category in data['categories']:
            category = category['name']
            categories.append(category)
        try:
            price = data['monetization']['price']
            print(price)
            if price > 0:
                price /= 100
        except:
            price = ''
            print(response.meta)
        # print(categories, price)
        yield {
            'name': meta['name'],
            'developer': meta['developer'],
            "price": price,
            "category": categories,
            "appstore_url": "https://apps.apple.com/app/id"+str(stores_id)
        }

    def parse_google(self, response):
        meta = response.meta
        data = response.json()
        stores_id = data['stores_id']
        # print(data)
        try:
            star = data['rating']['stars']
        except:
            star = ''
        try:
            google_description = data['description']
            s = Selector(google_description)
            google_description = '\n'.join(s.xpath('''//text()''').extract())
            google_description = unescape(google_description)
        except:
            google_description = ''
            print(response.meta)
        yield {
            'name': meta['name'],
            'developer': meta['developer'],
            "star": star,
            "google_description": google_description,
            "GooglePlay_url": "https://play.google.com/store/apps/details?id="+stores_id

        }


if __name__ == '__main__':
    execute('scrapy crawl example'.split())
