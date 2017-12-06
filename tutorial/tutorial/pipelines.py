# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


# class TutorialPipeline(object):
#     def process_item(self, item, spider):
#         return item
import codecs
import json

class TutorialPipline(object):
    def __init__(self):
        self.file=codecs.open('items','wb',encoding='utf-8')

    def process_item(self,item,spider):
        line=json.dumps(dict(item))
        self.file.write(line.decode("unicode_escape")+"\r\n")
        return item


