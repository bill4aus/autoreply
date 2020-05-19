#!/usr/bin/env python
#coding:utf-8
# -*- coding: utf-8 -*-

# 导入工具
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.proxy import Proxy,ProxyType

from selenium.common.exceptions import NoSuchElementException 
import time
from bs4 import BeautifulSoup
import sys
import io
import logging
from apscheduler.schedulers.background import BackgroundScheduler
import urllib
import urllib2
import threading
import json
import random
import math
import urlparse


import MySQLdb

reload(sys)
sys.setdefaultencoding('utf-8')

import requests

import hashlib   
from selenium.webdriver.common.keys import Keys  

# from PIL import Image
from PIL import Image

# import pytesseract
# from kmeans import invokefunc

import threading
from selenium.webdriver.support.wait import WebDriverWait

# import damatu

m2 = hashlib.md5()   

# #1.实例化类型 参数是打码兔用户账号和密码	
# dmt=DamatuApi("cdsbtest","cdsb123456")
# print 'damatu:'
# print(dmt.getBalance()) #查询余额 

conn={}
conn= MySQLdb.connect(
        host='localhost',
        port = 3306,
        user='root',
        passwd='',
        db ='adver',
        charset="utf8"
        )
print(conn)


isfinished=0
keywords=[]
url_id=0


# 是否是测试 状态
istest=False
# istest=True



#先重置为0
cur = conn.cursor()
countt=cur.execute('update ad set redundant =0 where id>0')
print(conn.commit())
cur.close()



cur = conn.cursor()
#1
# http://p.qiao.baidu.com/im/index?siteid=10597431
#2
sqli="select * from ad where  chaturl like '%qiao.baidu.com%' or  chaturl like '%53kf.%' or   chaturl like '%kuaishang%' or  chaturl like '%chat%' "
count=cur.execute(sqli)
# print(conn.commit())
results = cur.fetchall()   
for r in results:
    keywords.append({'chaturl':r[6],'id':r[0]})
cur.close()

# keywords_bak=[]
count=0

ip_proxy_list=[

]

ip_proxy=''
ip_count=0

urlkeyvaluedict={}


keywordlist=keywords

# 基本配置
# logging.basicConfig(level=logging.INFO)
openurlstring=''
# openurlstring='http://www.ipip.net/'

def loop():
	global browser
	global keywords
	global count
	global ip_count
	global time
	global result
	global YDMApi
	global isfinished
	global openurlstring

	global keywordlist
	global keywordcolum
	global istest
	global url_id
	global urlkeyvaluedict



	saylist=[
	'您好，解决跳出率高，综合提升对话量30%~50%的"云劫持"来了!劫持对手商务通,电话,全网展示10多种广告样式，安全稳定,防检查!免费3天试用!看效果合作!详询QQ:1011560072',
	'您好，全新"云劫持"，可免费试用3天!劫持对手商务通，电话，全网展现10多种广告样式，安全稳定防检查。有效提升对话30%~50%,后台数据真实可查!详询QQ:1011560072。',
	'您好，手机"云劫持"类百度"，医院营销利器!转化手机端无效访客，劫持对手商通，电话，全网展示10多种广告样式!提升对话量30%~50%。安全无死角，为竞价省钱!免费测试3天，看效果合作!详询QQ:1011560072',
	'您好，"云劫持",  支持所有搜索引擎，可劫持对手商务通，电话,全网展示10多种广告样式，安全稳定，防检查!目前稳定合作机构已达上百家，均提升对话量30%~50%,清晰查看劫持数据!免费试用3 天!详询QQ:1011560072',
	'你好，全新云"劫持"，支持所有搜索引擎【百度 神马 搜狗】安全、高效、无死角，全网展示广告!可劫持对手商务通，电话，全网展示10多种广告样式!提升对话量30%~50%,医院营销利器!免费测试3天，效果满意再使用!详询:QQ:1011560072',
	'您好，最新"云劫持"，每天对话量可增长30%-50%，医院营销之必备利器!10多种广告样式，安全稳定防百度检查，可劫持竞争对手的商务通和电话，全网展现广告，提供3天免费试用，效果满意再付款，详询QQ：1011560072',
	]

	random.shuffle(saylist)


	if istest:
		syastring='你好'
	else:
		syastring=saylist[0]
	# syastring='hello~'

	# 关键词列表是否循环完毕
	if len(keywordlist)<=count:
		# time.sleep(30)
		# ip_count+=1
		cur = conn.cursor()

		recount=0
		# print(urlkeyvaluedict)
		for x in urlkeyvaluedict:
			pass

			print(x)
			print(urlkeyvaluedict[x])
			samehospitallist=urlkeyvaluedict[x]
			remainhospital=samehospitallist[-1]
			print('remainhospital')
			print(remainhospital)
			reduntanthospital=samehospitallist[0:-1]
			print('reduntanthospital')
			print(reduntanthospital)
			recount=recount+len(reduntanthospital)

			if len(reduntanthospital)>0:
				#更新 redundant
				sqlstr2='update ad set redundant =1 where  id in('+','.join(str(i) for i in reduntanthospital)+')'
				print(sqlstr2)
				countt=cur.execute(sqlstr2)
				print(conn.commit())


		print('all url numbers')
		print(len(keywordlist))
		print('recount')
		print(recount)
		time.sleep(5)
		cur.close()

		exit()

	else:
		# 获取下一个关键词
		msgstring=keywordlist[count]['chaturl']
		url_id=keywordlist[count]['id']
		print(url_id)

	
	# 打开浏览器
	# a=urllib.quote(urllib.quote(msgstring))
	
	rr = urlparse.urlparse(msgstring)
	# print (rr) 
	# print (rr.port)
	# print (rr.hostname)  
	# print (rr.query)
	new_url_list=[]
	new_query=[]
	key_list=[]

	for x in rr:
		new_url_list.append(x)
	# print(new_url_list)

	# urlparse.parse_qs(query).
	url_query_list=new_url_list[4].split('&')
	for param in url_query_list:
		paramlist=param.split('=')

		if len(paramlist)==2:
			param_key=paramlist[0]
			param_value=paramlist[1]

			#kuaishang
			if 'kuaishang' in msgstring:
				print('kuaishang')
				if not('did' in param_key) and not('sid' in param_key) and not('cas' in param_key) and not('fi' in param_key):
					param_value=''
				else:
					new_query.append(param_key+'='+param_value)
			# chatpre.aspx 网 zoo
			if 'hatpre' in msgstring:
				if not('id' == param_key):
					param_value=''
				else:
					new_query.append(param_key+'='+param_value)

			# 53kf.com
			if '53kf.' in msgstring:
				if not('arg' == param_key):
					param_value=''
				else:
					new_query.append(param_key+'='+param_value)
			#qiao.baidu.com
			if 'qiao.baidu.com' in msgstring:
				if not('siteid' == param_key):
					param_value=''
				else:
					new_query.append(param_key+'='+param_value)

	# print(''.join(new_query))
	if urlkeyvaluedict.has_key(''.join(new_query)):
		# print(url_id)
		urlkeyvaluedict[''.join(new_query)].append(int(url_id))
	else:
		urlkeyvaluedict[''.join(new_query)]=[]
		# print(url_id)
		urlkeyvaluedict[''.join(new_query)].append(int(url_id))


	new_url_list[4]='&'.join(new_query)
	msgstring = urlparse.urlunparse(new_url_list)
	print(msgstring)
	count+=1

while 1:
	try:
		# print('loop start')
		loop()
		# print('loop over')
	except Exception, e:
		raise e
		# print(str(e))
		# loop()
		pass
