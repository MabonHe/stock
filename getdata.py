#!/usr/bin/env python3
# coding=utf-8
import pymysql
import urllib.request
import lxml.html
import json
import string
import sys
import time
import random
import re
import io
import os
sys.path.append('/home/hemaobin/workspace/stock')
import mysqldb
import analyzer
analyzer = analyzer.Analyzer()
basic_url='http://hq.sinajs.cn/list='
symbollist = ['sz000651','sz000333','sz300104','sz300415','sh601777','sz300051']
code_list = ['000651','000333','300104','300415','601777','300051']
headers = {'User-Agent':'gsi'}
stock = mysqldb.StockDatabase()
stock.connectdatabase()
cursor = stock.getcursor()
while True:
    i = 0
    for symbol in symbollist:
        url = basic_url + symbol
        print(url)
        time.sleep(1)
        request=urllib.request.Request(url, headers = headers)
        try:
            response=urllib.request.urlopen(request)
            html = response.read()
        except urllib.error.URLError as e:
            print('urlerror!!')
            html = ""
            time.sleep(12)
        #print(html)
        htmlstr = html.decode('GBK')
        search=re.search(r'=(.*)',htmlstr)
        #print(search.group(1))
        search = search.group(1)
        split = re.split(r',',search)
        stockdatalist = []
        for line in split:
            # print(line)
            stockdatalist.append(line)
        print(stockdatalist)
        stock.getdatafromsina(stockdatalist,code_list[i],symbol)
        print("stockdata:",stockdatalist[3])
        sql = "UPDATE maintrade SET market_value = %s,yestoday_close=%s,update_time='%s' WHERE code = '%s'" % (stock.m_trade,stock.m_yestoday_close,stock.m_tickitime,code_list[i])
        print(sql)
        stock.update_insert(cursor,sql)
        analyzer.compare_price(symbol,stockdatalist[3])
       # stock.insertdata(cursor,3)
        print(code_list[i])
        i = i + 1
