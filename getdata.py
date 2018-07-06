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
sys.path.append('/home/hemaobin/workspace/stock')
import mysqldb
basic_url='http://hq.sinajs.cn/list='
symbollist = ['sz000651','sz000333','sz300104','sz300415','sh601777','sz300051']
code_list = ['000651','000333','300104','300415','601777','300051']
print(len(code_list))
print(code_list[0])
headers = {'User-Agent':'gsi'}
stock = mysqldb.StockDatabase()
stock.connectdatabase()
cursor = stock.getcursor()
while True:
    i = 0
    for symbol in symbollist:
        url = basic_url + symbol
        print(url)
        time.sleep(2)
        request=urllib.request.Request(url, headers = headers)
        try:
            response=urllib.request.urlopen(request)
            html = response.read()
        except urllib.error.URLError as e:
            print('urlerror!!')
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
        stock.getdatafromsina(stockdatalist,code[i],symbol)
        print(code_list[i])
        i = i + 1
