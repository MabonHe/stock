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

stock.createmaintable(cursor)
