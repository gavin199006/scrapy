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
import pymysql


class TutorialPipeline(object):
    def __init__(self):
        self.file=open('item','w',encoding='utf-8')

    def process_item(self,item,spider):
        line=json.dumps(dict(item), ensure_ascii=False)
        # print(line)
        # self.file.write(line.decode("unicode_escape")+"\r\n")
        self.file.write(line +"\r\n" )
        return item

    def close_spider(self, spider):
        self.file.close()



class MysqlPipeline(object):
    def __init__(self):
        config = {
            'host': '192.168.1.200',
            'port': 3308,
            'user': 'root',
            'password': '1qaz@WSX',
            'db': 'data_department',
            'charset':'utf8',

        }
        self.connect = pymysql.connect(**config)
        self.cursor = self.connect.cursor()

    def process_item(self,item,spider):

        title = item['title']

        link = item['link']

        des = item['desc']

        price = item['price']

        insert_sql = """
            insert into zk_cylw(title,link,des,price)values(%s,%s,%s,%s);
        """
        para = (title,link,des,price)

        self.cursor.execute(insert_sql,para)
        self.connect.commit()
        return item

    def close_spider(self,spider):
        self.cursor.close()
        self.connect.close()
