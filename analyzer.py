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

class Analyzer():
    def compare_price(self,symbol,price):
        stock = mysqldb.StockDatabase()
        stock.connectdatabase()
        cursor = stock.getcursor()
        sell_volume = 0
        buy_volume=0
        diff_valume=0
        i=0
        try:
            os.remove('mail.txt')
        except:
            print('no file')
        f = open('mail.txt','w')
        sql = 'SELECT SUM(volume) AS volume FROM trade%s WHERE volume < 1' % symbol
        volume = stock.select(cursor,sql)
        print('volume:',volume)
        if volume != None:
            sell_volume = volume[0][0]
            print("sell:",sell_volume)
        else:
            sell_volume = 0
        sql = 'SELECT @r:=@r+1 as rownum,a.* FROM trade%s a,(select @r:=0) b WHERE volume > 1 limit 100' % symbol
        data = stock.select(cursor,sql)
        if data != None:
            for item in data:
                buy_volume = buy_volume + item[2]
                i = i+1
                if buy_volume >= abs(sell_volume):
                    print('buyvolume:',buy_volume,'num:',i)
                    break
        else:
            return 0
        diff_valume = buy_volume - abs(sell_volume)
        sql = 'SELECT * FROM trade%s WHERE volume > 1  limit %i,100' % (symbol,i-1)
        data = stock.select(cursor,sql)
        if data == None:
            print('none')
            return 0
        for item in data:
            f.write(str(item))
            f.write('\n')

        os.system('./sendmail.sh')
        f.close()
        stock.closedb()
