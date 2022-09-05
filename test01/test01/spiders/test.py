import re

import scrapy
from scrapy import Request
from scrapy.http.response.text import TextResponse
from scrapy.cmdline import execute

class TestSpider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['truefacet.com']
    start_urls = [
        'https://www.truefacet.com/watches/men.html?manufacturer%5B0%5D=Rolex&order=newarrival&p=1&categoryId%5B0%5D=8&section=marketplace']

    def start_requests(self):
        yield Request(url=self.start_urls[0], callback=self.parse, dont_filter=True)

    def parse(self, response: TextResponse):
        length = len(response.xpath('''//div[@class="product-wrapper"]/div'''))
        if length:
            last_url = response.url
            page = re.findall(r'&p=(\d+)&', last_url)[0]
            this_url = last_url.replace(f'&p={page}&', f'&p={int(page)+1}&')
            print(page)
            yield Request(url=this_url, callback=self.parse, dont_filter=True)
        for div in response.xpath('''//div[@class="product-wrapper"]/div'''):
            detail_url = div.xpath('''./a/@href''').get()
            title = div.xpath('''.//div[@class="listProTxt"]/div[@class="productTitle"]/text()''').get()
            brand_name = div.xpath('''.//div[@class="brand-name"]/text()''').get()
            price_now = div.xpath('''.//div[@class="listProTxt"]//span[@class="price"]/text()''').get().strip()
            meta = {
                "url": detail_url,
                "title": title,
                "brand": brand_name,
                "price_now": price_now,

            }
            # yield Request(url=detail_url, dont_filter=True, callback=self.parse_details, meta=meta)

    def parse_details(self, response: TextResponse):
        meta = response.meta
        descriptions = response.xpath('''//div[@id="details"]''')
        description = ''
        for desc in descriptions.xpath('''.//ul/li'''):
            description = description + desc.xpath('''./label/text()''').get() + ":" + desc.xpath(
                '''./span/text()''').get() + '\n'
        description = description + ''.join(response.xpath('''.//div[@class="text-content"]//text()''').extract())
        description = description.strip()
        thumb_images = response.xpath('''//div[@id="ProImageThumb"]/div/a/img/@src''').extract()
        big_image = [i.replace("/80x/", "/800x600/") for i in thumb_images]
        url = response.url
        title = meta['title']
        brand_name = meta['brand']
        price_now = meta['price_now']


if __name__ == '__main__':
    execute('scrapy crawl test'.split())
from h2 import exceptions
exceptions.ProtocolError