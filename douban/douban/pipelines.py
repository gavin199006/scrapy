# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import json

class DoubanPipeline(object):
    def __init__(self):
        self.file = codecs.open('data.json', 'wb', encoding="utf-8")
    def process_item(self, item, spider):
        line = json.dumps(dict(item))
        self.file.write(line.decode("unicode_escape") + "\r\n")
        return item
