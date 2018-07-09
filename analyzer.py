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
stock = mysqldb.StockDatabase()
stock.connectdatabase()
cursor = stock.getcursor()

class Analyzer():
    def compare_price(self,symbol,price):
        sql='select * from trade%s where volume > 1'%symbol
        data = stock.select(cursor,sql)
        if data != None:
            print('write data to file')

