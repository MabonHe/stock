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
sys.path.append('/home/hemaobin/workspace/web')
import mysqldb
print('start get stock history data!')
headUrl = 'http://money.finance.sina.com.cn/d/api/openapi_proxy.php/?__s=[[%22hq%22,%22hs_a%22,%22%22,0,'
endUrl = ',40]]&amp;callback=FDC_DC.theTableData'
n = 1
headers = {'User-Agent':'gsi'}
stock = mysqldb.StockDatabase()
stock.connectdatabase()
cursor = stock.getcursor()
stocklist = []
while n < 87:
        if n % 2 != 0:
            headers = {'User-Agent':'what_the_fuck'}
        else:
            headers = {'User-Agent':'gsi'}
        print(headers)
        url = headUrl + "%d" % n + endUrl
        print(url)
        request=urllib.request.Request(url, headers = headers)
        try:
            response=urllib.request.urlopen(request)
            html = response.read()
        except urllib.error.URLError as e:
            print('urlerror!!')

        #print(html)
        #html_page=lxml.html.fromstring(html)
        #html_str = lxml.html.tostring(html_page)
        #print(html_str)
        #file = open('data.txt','w').write(html_str)
        #file.close()
        #file = open('data.txt','r').read()
        htmlstr = html.decode()
        search=re.search(r'\[\[(.*)',htmlstr)
        search = search.group()
        split = re.split(r'\[',search)
        for line in split:
        #print(line)
            split_m = re.split(r'\,',line)
            stocklist = []
            for dataline in split_m:
                match = re.match(r'"(.*)"',dataline)
                if match == None:
                    what=dataline
                else:
                    what = match.group(1)
                #print(what)
                stocklist.append(what)
            stock.getdata(stocklist)

            stock.updatestockdata(cursor)
        rdom = random.randint(6,15)
        print(rdom)

        time.sleep(rdom)
        n += 1
stock.closedb()

