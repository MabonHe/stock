#!/usr/bin/env python3
# coding=utf-8

import urllib.request
import urllib.parse
import lxml.html
import json
import string
import sys
import time
import random
import re
import io
import http.cookiejar
import http.client

headers = {
'Accept': 'application/json, text/javascript, */*; q=0.01',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'en-US,en;q=0.9,zh;q=0.8',
'Connection': 'keep-alive',
'Content-Length': '204',
'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
'Cookie': 'has_user_token_cookie=0; _hid=26EUCiV9U1oOy_0-R1VbiwA; Hm_lvt_0bc010044cc74756d78a78cf95cf7f16=1520522765; t1=E292D867B03D69E41885A911FE838530CA2E4E274B5DC4BACF; _pk_ref.5.0b86=%5B%22%22%2C%22%22%2C1522550375%2C%22http%3A%2F%2Fetrade.cs.ecitic.com%2Fwebtrade%2Findex.html%22%5D; _pk_id.5.0b86=d74062dda16595c7.1504243195.12.1522550395.1522550375.',
'Host': 'weixin.citicsinfo.com',
'Origin': 'https://weixin.citicsinfo.com',
'Referer': 'https://weixin.citicsinfo.com/tztweb/deal/index.html',
'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linu…) Gecko/20100101 Firefox/59.0',
'X-Requested-With': 'XMLHttpRequest'
}
value = {
'ccount ': '9904036869',
'accounttype': 'ZJACCOUNT',
'action ': '100',
'cfrom  ': 'H5',
'CHANNEL ':'',
'CheckCode ': ' 5513',
'CheckToken ': 'TxCvPvW1JeGsFO6kE/SP9kzq3wsuMpNCn9wD',
'code   ': '',
'maxcount ': '  100',
'MobileCode ': '18512120765',
'MobileType ': '3',
'modulus_id ': '2',
'newindex   ': '1',
'password   ': '3ec526323b9449460e4776b5014f9c0cfc4a89d3cf853623529a2d66cd986ae5a587a8b97e62fcbe3be988aaf1be48a2d5f7c2d885f3ee1d13c1343feec684fbafa6d74c19171e08260360b42f2e0fcc61e5009a3f88575fd9ad15441398b5486af5842499e3e74c125baddb6122b8fc8cf934b0cf0805700f6917431dab8204',
'reqno  ': '1522894571640',
'tfrom  ': 'PC'
}
cj = http.cookiejar.CookieJar()
cookie_support = urllib.request.HTTPCookieProcessor(cj)
LOGIN_EMAIL = 'example@webscraping.com'
LOGIN_PASSWORD = 'example'
url = "https://weixin.citicsinfo.com/tztweb/deal/index.html#!/account/login.html"
host = 'https://weixin.citicsinfo.com/tztweb/deal/index.html'
#url = "/account/login.html"

values = urllib.parse.urlencode(value)
#values = values.encode('ascii')
#url = 'http://example.webscraping.com/places/default/user/login?_next=/places/default/index'
#headers = {'User-Agent':'gsi'}
opener = urllib.request.build_opener(cookie_support,urllib.request.HTTPHandler)
urllib.request.install_opener(opener)
h = urllib.request.urlopen(host)

request = urllib.request.urlopen(url,values,headers)
print(request)


