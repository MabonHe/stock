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
stock = mysqldb.StockDatabase()
stock.connectdatabase()
cursor = stock.getcursor()

stock.createtradetable(cursor)
for symbol in symbollist:
    stock.createtradeRecordtable(cursor,symbol)

stock.closedb()
