#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-3-16 上午8:31
# @Author  : Gavin
# @Site    : 
# @File    : conn_mysql.py
# @Software: PyCharm

import pymysql


def staff(table):
    # 名称 职位 公司名称  entuid
    conn = pymysql.connect(host='10.2.1.190', user='root', passwd='123', db='tianyan', port=3306, charset='utf8')
    cur = conn.cursor()  # 获取一个游标
    sql = "INSERT INTO person (ent_uid, name, role,entName,entUid) VALUES ( '%s', '%s')"
    cur.execute(sql % table)
    conn.commit()
    cur.close()  # 关闭游标
    conn.close()  # 释放数据库资源


def holder(table):
    # 并没有插入股东总量，出资从总额，认缴出资币种，直接从表格上爬取内容入库而已
    #  id ent_uid 股东名称 出资比例 认缴出资额
    conn = pymysql.connect(host='10.2.1.190', user='root', passwd='123', db='tianyan', port=3306, charset='utf8')
    cur = conn.cursor()  # 获取一个游标
    sql = "INSERT INTO share_holder (id, ent_uid, shaName, fundeRatio, subConam)" \
          " VALUES ( '%s', '%s', '%s','%s','%s')"
    cur.execute(sql % table)
    conn.commit()
    cur.close()  # 关闭游标
    conn.close()  # 释放数据库资源


def invest(table):
    #  id ，ent_uid, 投资设立企业名称，法人，建立日期（姑且当做注册日期），出资金额，企业状态
    conn = pymysql.connect(host='10.2.1.190', user='root', passwd='123', db='tianyan', port=3306, charset='utf8')
    cur = conn.cursor()  # 获取一个游标
    sql = "INSERT INTO outinvest (id, ent_uid, name, legalPerson, buildDate, regMoney,entStatus)" \
          " VALUES ( '%s', '%s', '%s','%s','%s','%s','%s' )"
    cur.execute(sql % table)
    conn.commit()
    cur.close()  # 关闭游标
    conn.close()


def base(table):

    conn = pymysql.connect(host='10.2.1.190', user='root', passwd='123', db='tianyan', port=3306, charset='utf8')
    cur = conn.cursor()  # 获取一个游标
    sql = "INSERT INTO ent_basic (ent_uid, ent_name, entPhone, entEmail, ent_url, ent_address, ent_desc," \
          " ent_reg_no,ent_reg_address, ent_english_name, ent_range, credit_code, tax_person_code, entDeadline, " \
          "ent_type) VALUES ( '%s', '%s', '%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s' )"
    cur.execute(sql % table)
    conn.commit()
    cur.close()  # 关闭游标
    conn.close()  # 释放数据库资源


def jingpin(table):
    # 注意数据表设计的时候id是整数还是字符串，其他字段的字符串类型需要选择utf8
    conn = pymysql.connect(host='10.2.1.190', user='root', passwd='123', db='tianyan', port=3306, charset='utf8')
    cur = conn.cursor()  # 获取一个游标
    sql = "INSERT INTO ent_competor ( idd,product, region, turn, industry, service, creat_time," \
          " estimate_value) VALUES ( '%s', '%s', '%s','%s','%s','%s','%s','%s' )"

    cur.executemany(sql, table)
    conn.commit()
    cur.close()  # 关闭游标
    conn.close()  # 释放数据库资源