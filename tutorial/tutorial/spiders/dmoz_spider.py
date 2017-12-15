#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-11-27 下午3:13
# @Author  : Gavin
# @Site    : 
# @File    : dmoz_spider.py
# @Software: PyCharm
import sys
sys.path.append('/home/gavin/PycharmProjects/scrapy/tutorial')
from scrapy.spiders import Spider
from scrapy.selector import Selector
from tutorial.items import DmozItem
from scrapy import http

class DmozSpider(Spider):
    name = "dmoz"
    # allowed_domains = ["dmoz.org"]
    start_urls=[]
    # for i in range(10):
    #     start_urls.append("http://www.ushsh.com/index.php?route=product/productall&page=" + str(i))
    start_urls = [
        "http://www.ushsh.com/index.php?route=product/productall&page=1",

    ]

    def parse(self, response):
        sel = Selector(response)
        # sites = sel.xpath('//div[@class="name"]/a')
        sites = sel.css('div.product-grid > div')
        items = []
        for site in sites:
            item = DmozItem()
            title = site.css('div.name > a::text').extract()[0]
            link = site.css('div.name > a::attr("href")').extract()[0]
            des = site.css('div.description::text').extract()[0]
            price = site.css('div.price::text').extract()[0].replace(' ','').replace('\n','').replace('\r','')

            item['title'] = title

            item['link'] = link
            # item['desc'] = des
            item['price'] = price
            items.append(item)
            yield http.Request(url=item["link"], meta={'item': item}, callback=self.parseDetail, dont_filter=True)
            # yield item

        nextPage = sel.xpath('//div[@class="links"]/a/@href').extract()[-2]
        if nextPage:
            next = nextPage
            yield http.Request(next, callback=self.parse)


    def  parseDetail(self,response):
        item = response.meta['item']


        selector = Selector(response)
        des = selector.xpath('//meta[@name="description"]/@content').extract()[-1]
        item['desc'] = des
        yield item



