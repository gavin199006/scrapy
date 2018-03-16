#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-3-16 上午8:36
# @Author  : Gavin
# @Site    : 
# @File    : CookieTransform.py
# @Software: PyCharm

# -*- coding: utf-8 -*-

class transCookie:
    def __init__(self, cookie):
        self.cookie = cookie

    def stringToDict(self):
        '''
        将从浏览器上Copy来的cookie字符串转化为Scrapy能使用的Dict
        :return:
        '''
        itemDict = {}
        items = self.cookie.split(';')
        for item in items:
            key = item.split('=')[0].replace(' ', '')
            value = item.split('=')[1]
            itemDict[key] = value
        return itemDict

if __name__ == "__main__":
    cookie = "aliyungf_tc=AQAAAEKlG0ncuwAAjhpad9oIkXOC4Yni; csrfToken=fYO1wr1SmbYKFvdvyL3DFNzC; TYCID=6eaa7e70281d11e886c4e3e6089348bd; undefined=6eaa7e70281d11e886c4e3e6089348bd; ssuid=9535358242; bannerFlag=true; RTYCID=d48646a5875a4b8b91322cb6e517d839; token=89b489114c1e4593879d7f011271da12; _utm=3e26c18f674c495dbef43e41f0855a0d; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1521096752; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1521109134; tyc-user-info=%257B%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxMzY5MzM5MTcyMiIsImlhdCI6MTUyMTEwOTE0NSwiZXhwIjoxNTM2NjYxMTQ1fQ.2uLi9wpZqSXI1_s3P-i03kmnkUpcFBZaZIC8-QW-2nrMu-jvyTE784dtex_sNl7KLyETzKx9ZrTsU_lJXJ0HjQ%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522state%2522%253A%25220%2522%252C%2522vipManager%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522onum%2522%253A%25220%2522%252C%2522mobile%2522%253A%252213693391722%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxMzY5MzM5MTcyMiIsImlhdCI6MTUyMTEwOTE0NSwiZXhwIjoxNTM2NjYxMTQ1fQ.2uLi9wpZqSXI1_s3P-i03kmnkUpcFBZaZIC8-QW-2nrMu-jvyTE784dtex_sNl7KLyETzKx9ZrTsU_lJXJ0HjQ"
    trans = transCookie(cookie)
    print(trans.stringToDict())