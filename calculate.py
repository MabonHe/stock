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
symbollist = ['sz000651','sz000333','sz300104','sz300415','sh601777','sz300051']
code_list = ['000651','000333','300104','300415','601777','300051']
basic_url='http://hq.sinajs.cn/list='
stock = mysqldb.StockDatabase()
stock.connectdatabase()
cursor = stock.getcursor()

for code in code_list:
    sql = "SELECT code,volume,(market_value - yestoday_close) * volume AS benefit from maintrade where code='%s'" %code
    print(sql) 

 
  
