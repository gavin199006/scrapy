#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-11-30 下午4:52
# @Author  : Gavin
# @Site    : 
# @File    : groupSpider.py
# @Software: PyCharm

# coding=utf-8
__author__ = 'Kun zhang'
import re
import sys
sys.path.append('/home/gavin/PycharmProjects/scrapy/douban')
from scrapy.spiders import CrawlSpider
from douban.items import DoubanItem

from scrapy import Selector

class GroupSpider(CrawlSpider):
    name = "Douban"
    # allowed_domains = ["douban.com"]
    # start_urls = ["https://www.douban.com/group/explore?start=0"]

    # start_urls = ["https://www.douban.com/doulist/1264675/?start=",]
    start_urls = []
    for i in range(20):
        start_urls.append("https://www.douban.com/doulist/1264675/?start=" + str(i*25))


    def parse(self, response):
        # print(response.body)
        item = DoubanItem()
        selector=Selector(response)
        sel = selector.xpath('//div[@class="bd doulist-subject"]')
        for each in sel:
            title = each.xpath('div[@class="title"]/a/text()').extract()[0].replace(' ','').replace('\n','')
            url = each.xpath('div[@class="title"]/a/@href').extract()[0].replace(' ','').replace('\n','')
            rate = each.xpath('div[@class="rating"]/span[@class="rating_nums"]/text()').extract()[0].replace(' ','').replace('\n','')
            autor = re.search('<div class="abstract">(.*?)<br',each.extract(),re.S).group(1).replace(' ','').replace('\n','')
            # publishingHouse = re.search('<div class="abstract">(.*?)<br',each.extract(),re.S).group(1).replace(' ','').replace('\n','')
            # publishingTime = re.search('<div class="abstract">.*?<br />(.*?)<br',each.extract(),re.S).group(1).replace(' ','').replace('\n','')

            item["title"] = title
            item["rate"] = rate
            item["autor"] = autor
            item["url"] = url
            print(title + '\n' + rate + '\n' + autor + '\n'  )
            # print(each.xpath('div[@class="title"]/a/text()]').extract())
            # print( re.search('<divclass="abstract">(.*?)<br/>',each.extract().replace(' ',''),re.S))
            yield item
        return item