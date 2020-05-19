#!/opt/anaconda/bin/python
#coding:utf-8
# -*- coding: utf-8 -*-

# 导入工具
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException 
import time
from bs4 import BeautifulSoup
import sys
import io
import logging
# from apscheduler.schedulers.background import BackgroundScheduler
import urllib
import urllib2
import threading
import json
import random
import math
import codecs
import os
# import hashlib


reload(sys)
sys.setdefaultencoding('utf-8')

import requests
import json,urllib2


import codecs
import shelve
import logging

import smtplib    
from email.mime.text import MIMEText  

import ConfigParser, os

def md5(str):
    import hashlib
    m = hashlib.md5()   
    m.update(str)
    return m.hexdigest()
def sendmessage(text):
	phone='13880740996'
	message=text+'【成都商报】'
	# sendurl='http://wxactivity2.cdsb.mobi/index.php/Enroll/IEnroll/sendSmsForQy.html?phone='++'&msg='+
	tt=requests.get('http://wxactivity2.cdsb.mobi/index.php/Enroll/IEnroll/sendSmsForQy.html', params={'phone':phone,'msg':message}) #GET请求
	return tt

def send_email(text):
	usay=text

	sender = 'data@cdsb.com'
	# receiver = 'jishuzu@cdsb.com'
	receiver = 'qianyuan@cdsb.com'
	subject = '四川地震报警-一想监控中心<data@cdsb.com>'
	smtpserver = 'smtp.qq.com'
	username = 'data@cdsb.com'
	# password = 'Qy1120'
	password = 'Cy123456'


	htmlstr='<html><head></head><body>'+usay+'</body></html>'
	msg = MIMEText(htmlstr,'html','utf-8')  
	msg['Subject'] = subject
	# 设置根容器属性  
	msg['From'] = subject
	msg["Accept-Language"]="zh-CN"
	msg["Accept-Charset"]="ISO-8859-1,utf-8"
	# msg['Cc']='qianyuan@cdsb.com'
	smtp =smtplib.SMTP_SSL("smtp.qq.com", 465)
	# smtp.connect('smtp.qq.com')
	smtp.login(username, password)
	smtp.sendmail(sender, receiver, msg.as_string())
	smtp.quit()
	sys.exit(0)



config = ConfigParser.ConfigParser()
config.read('/usr/application/autoreplay/chrome/conf.txt')



def quake(sendstr,timestr):
	pass
	######### 如果是地震信息更新怎么办？？？？会再次发送一次！############
	nowtime=int(float(time.time()))
	# 检查timestr对应的记录，是否有发送记录，没有就新创建一个变量
	# lasttime = config.get("section1", "lasttime")
	try:
		lasttime = config.get("section1",str(timestr))
		#有记录
	except Exception, e:
		# raise e
		try:
			config.add_section("section1")
			config.set("section1", timestr,nowtime)
		except Exception, e:
			config.set("section1", timestr,nowtime)
		config.write((open('/usr/application/autoreplay/chrome/conf.txt','w')))
		#无记录
		# send
		send_email(sendstr)
		sendmessage(sendstr)

# http://tongji.cdsb.mobi/micropub/weibolist/
# 成都高新减灾研究所
# os.path.exists('d:/assist/getTeacherList.py')

url = "http://tongji.cdsb.mobi/micropub/gettwitter/"

req = urllib2.Request(url)
res_data = urllib2.urlopen(req)
res = res_data.read()
dataraw=json.loads(res)
datadict={}

sendstr=''

for x in dataraw['news']:
    # datadict[x['name']]=x
    if x['name']=='地震':
    # if x['name']=='成都突发':
    	pass
    	wlist=x['list']
    	is_authorized=0
    	if len(wlist)>0:
	    	for wb in wlist:
	    		if '减灾研究所-专用' in wb['author']:
	    		# if '四川' in wb['author']:
	    			is_authorized=1
	    			sendstr=wb['twitter']
	    			# timestr=wb['timestr']
	    			md5str=md5(sendstr)
	    			print(' send email')
	    			#send 
	    			#redundent 
	    			quake(sendstr,md5str)

# is_authorized=1
# print('is_authorized')
# print(is_authorized)

# if not is_authorized:
# 	print('no earthquake')
# 	exit()

# try:
# 	lasttime = config.get("section1", "lasttime")
# except Exception, e:
# 	# raise e
# 	config.add_section("section1")
# 	config.set("section1", "lasttime", 0)
# 	config.write((open('/usr/application/autoreplay/chrome/conf.txt','w')))
# 	lasttime=0



# if lasttime=='':lasttime=0

# lasttime=int(float(lasttime))
# print(lasttime)

# # second
# nowtime=int(float(time.time()))
# oneday=24*60*60
# tenminite=2*60
# print(nowtime-lasttime)
# if nowtime-lasttime > oneday:
# 	print('send_email')
# 	config.set("section1", "lasttime", nowtime)
# 	config.write((open('/usr/application/autoreplay/chrome/conf.txt','w')))
# 	send_email(sendstr)
# 	# sendmessage(sendstr)
	
# else:
# 	# print('already send')
# 	pass

