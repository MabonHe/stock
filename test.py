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
import analyzer
analyzer = analyzer.Analyzer()
basic_url='http://hq.sinajs.cn/list='
symbollist = ['sz000651','sz000333','sz300104','sz300415','sh601777','sz300051']
code_list = ['000651','000333','300104','300415','601777','300051']
headers = {'User-Agent':'gsi'}
stock = mysqldb.StockDatabase()
stock.connectdatabase()
cursor = stock.getcursor()
analyzer.compare_price('sz000651',45)
