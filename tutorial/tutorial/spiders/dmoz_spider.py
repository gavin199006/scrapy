#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-11-27 下午3:13
# @Author  : Gavin
# @Site    : 
# @File    : dmoz_spider.py
# @Software: PyCharm

from scrapy.spider import Spider
from scrapy.selector import Selector
from tutorial.items import DmozItem


class DmozSpider(Spider):
    name = "dmoz"
    # allowed_domains = ["dmoz.org"]
    start_urls=[]
    for i in range(10):
        start_urls.append("http://www.ushsh.com/index.php?route=product/productall&page=" + str(i))
    # start_urls = [
    #     "http://www.ushsh.com/index.php?route=product/productall&page=1",
    #     "http://www.ushsh.com/index.php?route=product/productall&page=2"
    #
    # ]

    def parse(self, response):
        sel = Selector(response)
        print(sel)
        sites = sel.xpath('//div[@class="name"]/a')
        page=sel.xpath('//div[@class="results"]')
        items = []
        for site in sites:
            item = DmozItem()
            item['title'] = site.xpath('text()').extract()
            item['link'] = site.xpath('@href').extract()
            # item['desc'] = site.xpath('text()').extract()
            items.append(item)
        return items