import re
import string
import pymysql
import sys

sql = """CREATE TABLE  updatestatus
			(
				symbol        char(30),
				code          char(20) ,
				year          char(50) ,
			);"""

class StockDatabase():
	version='1.0'
	m_symbol        =''
	m_code          =''
	m_name          =''
	m_trade         =''
	m_pricechange   =''
	m_changepercent =''
	m_buy           =''
	m_sell          =''
	m_settlement    =''
	m_open          =''
	m_high          =''
	m_low           =''
	m_volume        =''
	m_amount        =''
	m_tickitime     =''
	m_per           =''
	m_per_d         =''
	m_nta           =''
	m_pb            =''
	m_mktcap        =''
	m_nmc           =''
	m_turnoverratio =''
	m_update_status =''

	m_db = ''
	def connectdatabase(self):
		try:
			self.m_db = pymysql.connect('localhost','root','123','STOCKDATA')
		except:
			print('connect error!')
	def closedb(self):
		self.m_db.close()
	def getcursor(self):
		try:
			cursor = self.m_db.cursor()
		except:
			print('get cursor error')
		return cursor
	def update_status(self,cursor,code,year,symbol,status,num):
		sql = "UPDATE updatestatus SET symbol = '%s',code = '%s',year = '%s',status = %s,updatetime = Now() WHERE num = %s" % (symbol,code,year,status,num)
		try:
			cursor.execute(sql)
			self.m_db.commit()
		except:
			self.m_db.rollback()
	def update_status_status(self,cursor,status,num):
		sql = "UPDATE updatestatus SET status = %s WHERE num = %s" % (status,num)
		try:
			cursor.execute(sql)
			self.m_db.commit()
		except:
			self.m_db.rollback()
	def select_status(self,cursor,num = 1):
		sql = "SELECT * FROM updatestatus where num = %s" % num
		try:
			cursor.execute(sql)
			data = cursor.fetchone()
		except:
			print('select error')
		return data
	def delete_status(self,cursor,year,symbol):
		startyear=year + "-01-02"
		year = int(year) +1
		endyear = "%s" % year+"-01-02"
		sql = "DELETE FROM main%s WHERE tickitime >= '%s'  and tickitime <= '%s' " % (symbol,startyear,endyear)
		try:
			cursor.execute(sql)
			self.m_db.commit()
		except:
			self.m_db.rollback()
	def createtable(self,cursor,symbol):
		sql = """CREATE TABLE IF NOT EXISTS main%s
			(
				symbol        char(20) NOT NULL,
				code          char(20) NOT NULL,
				trade         float     ,
				pricechange   float     ,
				changepercent float     ,
				buy           float     ,
				sell          float     ,
				settlement    float     ,
				open          float     ,
				high          float     ,
				low           float     ,
				volume        float     ,
				amount        float     ,
				tickitime     char(50)  NOT NULL,
				per           float     ,
				per_d         float     ,
				nta           float     ,
				pb            float     ,
				mktcap        float     ,
				nmc           float     ,
				turnoverratio float     ,
				PRIMARY KEY(tickitime)

			);""" % symbol

		try:
			cursor.execute(sql)
		except:
			print('create table error')
		print(sql)
	def testselect(self,cursor):
		sql = 'SELECT * from maininfo WHERE update_status != 0 LIMIT 1'
		try:
			cursor.execute(sql)
			data = cursor.fetchone()
		except:
			print('get data error')
		return data
	def selectdata(self,cursor,status = 1):
		#if status == 0 return code
		#if status == 1 return all
		if status == 0:
			sql = "SELECT code from maininfo WHERE update_status != 1 LIMIT 1"
		elif status == 1:
			sql = "SELECT * from maininfo WHERE update_status != 1 LIMIT 1"
		elif status == 2:
			sql = "SELECT * from maininfo WHERE status != 1 LIMIT 1"
		elif status == 3:
			sql = "SELECT * from maininfo WHERE update_status != 1 ORDER BY tickitime DESC LIMIT 1"
		try:
			cursor.execute(sql)
			data = cursor.fetchone()
		except:
			print('get data error')
		return data
	def updatestockdata(self,cursor):
		sql = "UPDATE maininfo SET trade = %s,pricechange = %s,changepercent = %s,buy = %s,sell = %s,settlement = %s,open = %s,high = %s,low = %s,volume = %s,amount = %s,tickitime = %s,per = %s,per_d = %s,nta = %s,pb = %s,mktcap = %s,nmc = %s,turnoverratio = %s  WHERE code = %s " % \
			(self.m_trade,self.m_pricechange,self.m_changepercent,self.m_buy,self.m_sell,self.m_settlement,self.m_open,self.m_high,self.m_low,self.m_volume,self.m_amount,self.m_tickitime,self.m_per,self.m_per_d,self.m_nta,self.m_pb,self.m_mktcap,self.m_nmc,self.m_turnoverratio,self.m_code)
		print(sql)
		try:
			cursor.execute(sql)
			self.m_db.commit()
		except:
			self.m_db.rollback()
	def insertdata(self,cursor, status = 0):
		if status == 0:
			sql = """INSERT main%s(symbol,code,trade,pricechange,changepercent,open,high,low,volume,amount,tickitime,turnoverratio) \
					VALUES ('%s','%s',%s,%s,%s,%s,%s,%s,%s,%s,'%s',%s)""" % \
					(self.m_symbol,self.m_symbol,self.m_code,self.m_trade,self.m_pricechange,self.m_changepercent,self.m_open,self.m_high,self.m_low,self.m_volume,self.m_amount,self.m_tickitime,self.m_turnoverratio)
		elif status == 1:
			sql = """INSERT maininfo(symbol,code,name,trade,pricechange,changepercent,buy,sell,settlement,open,high,low,volume,amount,tickitime,per,per_d,nta,pb,mktcap,nmc,turnoverratio) \
					VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""" % \
					(self.m_symbol,self.m_code,self.m_name,self.m_trade,self.m_pricechange,self.m_changepercent,self.m_buy,self.m_sell,self.m_settlement,self.m_open,self.m_high,self.m_low,self.m_volume,self.m_amount,self.m_tickitime,self.m_per,self.m_per_d,self.m_nta,self.m_pb,self.m_mktcap,self.m_nmc,self.m_turnoverratio)
		elif status == 2:
			sql = """INSERT main%s(symbol,code,trade,pricechange,changepercent,buy,sell,settlement,open,high,low,volume,amount,tickitime,per,per_d,nta,pb,mktcap,nmc,turnoverratio) \
					VALUES ('%s','%s',%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,'%s',%s,%s,%s,%s,%s,%s,%s)""" % \
					(self.m_symbol,self.m_symbol,self.m_code,self.m_trade,self.m_pricechange,self.m_changepercent,self.m_buy,self.m_sell,self.m_settlement,self.m_open,self.m_high,self.m_low,self.m_volume,self.m_amount,self.m_tickitime,self.m_per,self.m_per_d,self.m_nta,self.m_pb,self.m_mktcap,self.m_nmc,self.m_turnoverratio)
		try:
			cursor.execute(sql)
			self.m_db.commit()
		except:
			self.m_db.rollback()
		#print(sql)
	def updatestatus(self,cursor,code,status = 0):
		if status == 0:
			sql = "UPDATE maininfo SET update_status = 1 WHERE code = '%s'" % code
		elif status == 1:
			sql = "UPDATE maininfo SET status = 1 WHERE code = '%s'" % code
		elif status == 2:
			sql = "UPDATE maininfo SET status = 0 WHERE code = '%s'" % code
		try:
			cursor.execute(sql)
			self.m_db.commit()
		except:
			self.m_db.rollback()
	def getdatafromdatabase(self,data):
		m_symbol         = data[0]
		m_code           = data[1]
		m_name           = data[2]
		m_trade          = data[3]
		m_pricechange    = data[4]
		m_changepercent  = data[5]
		m_buy            = data[6]
		m_sell           = data[7]
		m_settlement     = data[8]
		m_open           = data[9]
		m_high           = data[10]
		m_low            = data[11]
		m_volume         = data[12]
		m_amount         = data[13]
		m_tickitime      = data[14]
		m_per            = data[15]
		m_per_d          = data[16]
		m_nta            = data[17]
		m_pb             = data[18]
		m_mktcap         = data[19]
		m_nmc            = data[20]
		m_turnoverratio  = data[21]
	def printall(self):
		print(self.m_symbol        )
		print(self.m_code          )
		print(self.m_name          )
		print(self.m_trade         )
		print(self.m_pricechange   )
		print(self.m_changepercent )
		print(self.m_buy           )
		print(self.m_sell          )
		print(self.m_settlement    )
		print(self.m_open          )
		print(self.m_high          )
		print(self.m_low           )
		print(self.m_volume        )
		print(self.m_amount        )
		print(self.m_tickitime     )
		print(self.m_per           )
		print(self.m_per_d         )
		print(self.m_nta           )
		print(self.m_pb            )
		print(self.m_mktcap        )
		print(self.m_nmc           )
		print(self.m_turnoverratio )
	def getdata(self,data):
		k =0
		j =1
		m = data[k:j]
		self.m_symbol        =''.join(m)
		k +=1
		j +=1
		m = data[k:j]
		self.m_code          =''.join(m)
		k +=1
		j +=1
		m = data[k:j]
		self.m_name          =''.join(m)
		k +=1
		j +=1
		m = data[k:j]
		self.m_trade         =''.join(m)
		k +=1
		j +=1
		m = data[k:j]
		self.m_pricechange   =''.join(m)
		k +=1
		j +=1
		m = data[k:j]
		self.m_changepercent =''.join(m)
		k +=1
		j +=1
		m = data[k:j]
		self.m_buy           =''.join(m)
		k +=1
		j +=1
		m = data[k:j]
		self.m_sell          =''.join(m)
		k +=1
		j +=1
		m = data[k:j]
		self.m_settlement    =''.join(m)
		k +=1
		j +=1
		m = data[k:j]
		self.m_open          =''.join(m)
		k +=1
		j +=1
		m = data[k:j]
		self.m_high          =''.join(m)
		k +=1
		j +=1
		m = data[k:j]
		self.m_low           =''.join(m)
		k +=1
		j +=1
		m = data[k:j]
		self.m_volume        =''.join(m)
		k +=1
		j +=1
		m = data[k:j]
		self.m_amount        =''.join(m)
		k +=1
		j +=1
		m = data[k:j]
		self.m_tickitime     =''.join(m)
		k +=1
		j +=1
		m = data[k:j]
		self.m_per           =''.join(m)
		k +=1
		j +=1
		m = data[k:j]
		self.m_per_d         =''.join(m)
		k +=1
		j +=1
		m = data[k:j]
		self.m_nta           =''.join(m)
		k +=1
		j +=1
		m = data[k:j]
		self.m_pb            =''.join(m)
		k +=1
		j +=1
		m = data[k:j]
		self.m_mktcap        =''.join(m)
		k +=1
		j +=1
		m = data[k:j]
		self.m_nmc           =''.join(m)
		k +=1
		j +=1
		m = data[k:j]
		self.m_turnoverratio =''.join(m)
		k +=1
		j +=1
		m = data[k:j]
		self.m_update_status =''.join(m)

	def gethistorydata(self,data,symbol,code):
		self.m_symbol        =symbol
		self.m_code          =code
		k =0
		j =1
		m =data[k:j]
		self.m_tickitime     =''.join(m)
		k +=1
		j +=1
		m =data[k:j]
		self.m_open          =''.join(m)
		k +=1
		j +=1
		m =data[k:j]
		self.m_trade         =''.join(m)
		k +=1
		j +=1
		m =data[k:j]
		self.m_pricechange   =''.join(m)
		k +=1
		j +=1
		m =data[k:j]
		m = ''.join(m)
		m = re.match(r'(.*)%',m)
		if m == None:
			print("null")
			m = 0
		else:
			m = m.group(1)
		self.m_changepercent =m
		k +=1
		j +=1
		m =data[k:j]
		self.m_low           =''.join(m)
		k +=1
		j +=1
		m =data[k:j]
		self.m_high          =''.join(m)
		k +=1
		j +=1
		m =data[k:j]
		m = ''.join(m)
		if m == '':
			print(m)
		else:
			m = float(m) *100
		self.m_volume        =m
		k +=1
		j +=1
		m =data[k:j]
		m = ''.join(m)
		if m == '':
			print(m)
		else:
			m = float(m)*10000
		print(m)
		self.m_amount        =m
		k +=1
		j +=1
		m =data[k:j]
		m = ''.join(m)
		m = re.match(r'(.*)%',m)
		if m == None:
			print("null")
			m = 0
		else:
			m = m.group(1)
		self.m_turnoverratio = m











