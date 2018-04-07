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
n = 0
symbol = ''
code = ''
url = 'http://q.stock.sohu.com/hisHq?code=cn_600004&start=20180318&end=20180319'
year = 1996
mon = '01'
startday = '02'
endday = '01'

stock = mysqldb.StockDatabase()
stock.connectdatabase()
cursor = stock.getcursor()
status = stock.select_status(cursor,1)
year = status[2]
code = status[1]
symbol = status[0]
rets = status[3]
stock.delete_status(cursor,year,symbol)

while n < 1:
	status = stock.select_status(cursor,1)
	rets = status[3]
	if rets == 1:
		data = stock.selectdata(cursor)
		if data == None:
			break;
		code = data[1]
		symbol = data[0]
		stock.createtable(cursor,symbol)
		print('start work')
	while int(year) < 2019:
		stock.update_status(cursor,code,year,symbol,0,1)
		if int(year) % 2 != 0:
			headers = {'User-Agent':'what_the_fuck'}
		else:
			headers = {'User-Agent':'gsi'}

		url = 'http://q.stock.sohu.com/hisHq?code=cn_%s' % code + '&start=%s%s%s' %(year,mon,startday) + '&end=%s%s%s' %(int(year)+1,mon,endday)
		print(url)
		request=urllib.request.Request(url, headers = headers)
		try:
			response=urllib.request.urlopen(request)
			html = response.read()
		except urllib.error.URLError as e:
			print('urlerror!!')
			time.sleep(12)
			continue
		htmlstr = html.decode()
		search=re.search(r'\[\[(.*)',htmlstr)
		if search == None:
			print('search none')
			year = int(year) + 1
			time.sleep(3)
			continue
		else:
			search = search.group()
		#print(search)
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
			stock.gethistorydata(stocklist,symbol,code)
			stock.insertdata(cursor)
		year = int(year) + 1
		rdom = random.randint(20,60)
		print(rdom)
		time.sleep(rdom)
	stock.updatestatus(cursor,code)
	stock.update_status_status(cursor,1,1)
	year = 1995


stock.closedb()

