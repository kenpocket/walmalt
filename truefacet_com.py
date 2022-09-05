import scrapy
from scrapy import Request
from scrapy.http.response.text import TextResponse
import execjs
from scrapy.cmdline import execute
from parsel import Selector
from html import unescape


class TruefacetCom(scrapy.Spider):
    name = 'truefacet_com'
    allowed_domains = ['truefacet.com']
    start_urls = ['https://www.truefacet.com/']

    def start_requests(self):
        """
        通过start_url获取各个category的url
        :return:
        """
        yield Request(url=self.start_urls[0], dont_filter=True, callback=self.parse_categories)
        pass

    def parse_categories(self, response: TextResponse):
        pass

    def parse(self, response: TextResponse):
        """
        承接parse_categories，
        此function处理列表页，获得页数并返回将详情页封装好的Request
        :param response:
        :return:
        """
        pass

    def parse_details(self, response: TextResponse):
        """
        承接parse方法，处理详情页数据，并返回获取到的数据
        :param response:
        :return:
        """
        meta = response.meta
        descriptions = response.xpath('''//div[@id="details"]''')
        description = ''
        for desc in descriptions.xpath('''.//ul/li'''):
            description =description+ desc.label('''./label/text()''').get()+":"+desc.xpath('''./span/text()''').get()+'\n'
        description = description+response.xpath('''.//div[@class="text-content"]/text()''').get().strip()
        thumb_images = response.xpath('''//div[@id="ProImageThumb"]/div/a/img/@src''').extract()
        big_image = [i.replace("/80x/","/800x600/") for i in thumb_images]


