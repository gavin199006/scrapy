#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-3-7 下午6:10
# @Author  : Gavin
# @Site    : 
# @File    : test.py
# @Software: PyCharm


import requests

def get_proxy():
    return requests.get("http://127.0.0.1:5555/random").content


if __name__ == '__main__':
    ip=get_proxy().decode()
    print(ip)


