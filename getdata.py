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
url='http://hq.sinajs.cn/list=sz000651'

headers = {'User-Agent':'gsi'}
while True:
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
