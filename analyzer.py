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
        sql = 'SELECT SUM(volume) AS volume FROM trade%s WHERE volume < 1' % symbol
        sell_volume = stock.select(cursor,sql)
        if sell_volume != None:
            print(sell_volume)

        sql = 'SELECT @r:=@r+1 as rownum,a.* FROM trade%s a,(select @r:=0) b WHERE volume > 1 limit 10' % symbol
        data = stock.select(cursor,sql)
        if data != None:
            data_dic = {}
            for item in data:
                print(item)
