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
symbollist = ['sz000651','sz000333','sz300104','sz300415','sh601777','sz300051']
code_list = ['000651','000333','300104','300415','601777','300051']
basic_url='http://hq.sinajs.cn/list='
stock = mysqldb.StockDatabase()
stock.connectdatabase()
cursor = stock.getcursor()

f = open('/home/hemaobin/workspace/stock/benefit.txt','w')
benefit = 0
for code in code_list:
    sql = "SELECT code,volume,(market_value - yestoday_close) * volume AS benefit from maintrade where code='%s'" %code
    data = stock.select(cursor,sql)
    benefit = benefit + data[0][2]
    f.write(str(data))
    f.write('\n')

f.write("totle:   ")
f.write(str(benefit))
f.close()
stock.closedb()
print(benefit)

os.system('/home/hemaobin/workspace/stock/sendmail_.sh')
 
  
