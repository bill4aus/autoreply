#!/usr/bin/env python
#coding:utf-8
# -*- coding: utf-8 -*-

# 导入工具
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException 
import time
import datetime
from bs4 import BeautifulSoup
import sys
import io
import logging
#from apscheduler.schedulers.background import BackgroundScheduler
import urllib
# import urllib2
import threading
import json
import random
import math
import codecs
import os
from selenium.webdriver.common.keys import Keys	
# from PIL import Image	
from user_agent import generate_user_agent, generate_navigator

# reload(sys)
# sys.setdefaultencoding('utf-8')

import requests


class robot(object):
	"""docstring for robot"""
	def __init__(self,keshi,userid):
		super(robot, self).__init__()
		# self.arg = arg

		# 构建url
		# 科室
		# %E4%BD%A0%E5%A5%BD&keshi=xinggongnengzhangai
		self.keshi=keshi
		self.userid=userid

	def get_respone(self,messagegot):

		# # #中文机器人	自有  基于  意图分析  tensorflow

		# 新 机器人  基于 关键词 匹配
		urll ='http://127.0.0.1:9003/'
		ress = requests.get(url=urll,params={'role':'patient','word':messagegot,'keshi':self.keshi}).text
		

		# iamtosaystring,doctor_intent,my_intent
		# 需要考虑  多个回复 的情况

		# responsetext = json.loads(ress)
		# retext=responsetext["list"][0]


		usayinfo=ress.split('||')
		goingto_say=usayinfo[0]
		other_intent=usayinfo[1]
		my_intent=usayinfo[2]

		# return retext["word"]+"||"+ "test"+"||"+ "test"+"||"
		return goingto_say+"||"+ other_intent+"||"+ my_intent
		





class msgextractor_for_zoosoft(object):
	"""docstring for msgextractor_for_zoosoft"""
	def __init__(self, botchrome):
		super(msgextractor_for_zoosoft, self).__init__()
		self.botchrome = botchrome


		self.new=False
		self.newmsg=""

		# #此消息的发出人标识
		self.name='0'
		self.if_newmessage={}
		self.if_newmessage[self.name]=0
		self.sayarray=[]
		self.sysinfoarray=[]
		# # 保存此用户上一次说了什么
		self.lastsay={}
		self.isayto={}

		self.is_img=0

		if self.name not in self.lastsay:
			self.lastsay[self.name]=u'测试'

		if self.name not in self.isayto:
			self.isayto[self.name]=u'测试'

		self.fname=random.uniform(1, 10000000000)

	def get(self):
		# 测试
		# inputhtml=self.browser.getelementbycss("#kw")
		# if inputhtml:
		# 	self.new=True
		# 	self.newmsg="new message"
		# return self

		# 重置  重新判断
		# self.new=False
		# self.newmsg=""
		# self.if_newmessage[self.name]=False

		# # 首先确认下是不是有需要的元素
		# # try:
		# # 	listele=self.browser.find_elements_by_css_selector('.msg-box')
		# # 	# print(len(listele))
		# # except Exception, e:
		# # 	# raise e
		# # 	print(str(e))

		# 开始提取
		print("start extract...")
		# nickname=self.name
		#msgArea .msg-box .msg-agent
		# .msg-box .msg-agent
		listele=self.botchrome.getelementsbycss('#msgArea .msg-box .msg-agent')
		msglist_length=len(listele)
		for ele in listele:
			try:
				# ele不是自定义browser 只有原生方法
				usersay= ele.find_element_by_css_selector('.arrow_box_left .text').text
			except Exception as e:
				# raise e
				# usersay= ele.find_element_by_css_selector('.text').text
				usersay=''
			self.sayarray.append({'nickname':self.name,'usersay':usersay})
		
		# 判断聊天长度
		print("len(self.sayarray)")
		print(len(self.sayarray))
		if len(self.sayarray)<=0:
			pass
		else:
			pass
			usersayobj=self.sayarray[-1]
			nname=usersayobj['nickname']
			ssay=usersayobj['usersay'].replace(' ','')

			if self.lastsay[self.name]==ssay:
				pass
				self.new=False
				self.newmsg=""
				self.if_newmessage[self.name]=False
			else:
				if ssay=='' and self.is_img==1:
					# 如果是发图片
					self.if_newmessage[self.name]=True
					self.lastsay[self.name]=ssay
				elif ssay!='':
					# 如果内容不是为空
					self.if_newmessage[self.name]=True
					self.lastsay[self.name]=ssay


			self.new=self.if_newmessage[self.name]

			usersayobj=self.sayarray[-1]
			self.ssay=usersayobj['usersay']
			self.newmsg=self.ssay


		# 	# 保存文本数据
		# 	# f.write('医生||'+ssay+'\n')

		# 	#保存文本到数据库
		# 	# urlprefix='http://liliniao.com.cn/hospital/index.php?m=Api&c=user&a=talklog'
		# 	# urll =urlprefix+'&urole='+urllib.quote('医生'.encode('utf8'))+'&usay='+urllib.quote(ssay.encode('utf8'))+'&chatid='+str(userid)+'-'+str(fname)+'&userid='+str(userid)
		# 	# reqq = urllib2.Request(urll)
		# 	# res_dataa = urllib2.urlopen(reqq)
		# 	# ress = res_dataa.read()



		# 截图 保留
		msglist_length=len(self.sayarray)
		fname=self.fname
		# C:/zip/12/
		if msglist_length<3:
			self.botchrome.screen("D:/zip/"+str(fname)+'s'+"screen.png")
		elif msglist_length<6:
			self.botchrome.screen("D:/zip/"+str(fname)+'m'+"screen.png")
		else:
			self.botchrome.screen("D:/zip/"+str(fname)+"screen.png")


		# 没起作用
		# 没起作用
		# 是否被对方手动结束对话
		# kschat_enddialog
		inputhtml=self.botchrome.getelementsbycss('.other_msg')
		# inputhtml=browser.find_element_by_xpath("//div[contains(text(), '次对话已经结束! 如果您还')]")
		# inputhtml=browser.find_element_by_xpath("//div[@class='other_msg']")

		print('isover')
		for x in inputhtml:
			print(x.text)
			if '次对话已经结束! 如果您还' in x.text:
				self.botchrome.quit()
			if '请您耐心等待' in x.text:
				self.botchrome.quit()


		return self

		# # 是否有新消息
		# if if_newmessage[name]:
		# 	if_newmessage[name]=0

		# 	usersayobj=sayarray[-1]
		# 	nname=usersayobj['nickname']
		# 	ssay=usersayobj['usersay']

		# 	# 保存文本数据
		# 	# f.write('医生||'+ssay+'\n')

		# 	#保存文本到数据库
		# 	# urlprefix='http://liliniao.com.cn/hospital/index.php?m=Api&c=user&a=talklog'
		# 	# urll =urlprefix+'&urole='+urllib.quote('医生'.encode('utf8'))+'&usay='+urllib.quote(ssay.encode('utf8'))+'&chatid='+str(userid)+'-'+str(fname)+'&userid='+str(userid)
		# 	# reqq = urllib2.Request(urll)
		# 	# res_dataa = urllib2.urlopen(reqq)
		# 	# ress = res_dataa.read()

		# 	# 自动回复


		# 	# 保存文本数据
		# 	# f.write('病人||'+uwords+'\n')

		# ress=''#清空上次回答内容






		

# class msgextractor_for_kuaishangtong(object):
# 	"""docstring for msgextractor_for_kuaishangtong"""
# 	def __init__(self, browser):
# 		super(msgextractor_for_kuaishangtong, self).__init__()
# 		self.browser = browser


		

# 		self.new=False
# 		self.newmsg=""

# 		# #此消息的发出人标识
# 		self.name='0'
# 		self.if_newmessage={}
# 		self.if_newmessage[self.name]=0
# 		self.sayarray=[]
# 		self.sysinfoarray=[]
# 		# # 保存此用户上一次说了什么
# 		self.lastsay={}
# 		self.isayto={}

# 		self.is_img=0

# 		if not self.lastsay.has_key(self.name):
# 			self.lastsay[self.name]=u'测试'

# 		if not self.isayto.has_key(self.name):
# 			self.isayto[self.name]=u'测试'

# 		self.fname=random.uniform(1, 10000000000)

# 	def get(self):
# 		# 测试
# 		# inputhtml=self.browser.getelementbycss("#kw")
# 		# if inputhtml:
# 		# 	self.new=True
# 		# 	self.newmsg="new message"
# 		# return self


# 		# 开始提取

# 		# 判断 是  PC  还是  移动端

# 		# .msg_cs .msg  PC
# 		# .msg_left mobile


# 		# #wrapper .content .msg_left
# 		# #msgArea .msg-box .msg-agent
# 		# msg_left
# 		#msgArea .msg-box .msg-agent
# 		listele=self.browser.getelementsbycss('.msg_cs .msg')
# 		msglist_length=len(listele)
# 		for ele in listele:
# 			try:
# 				# ele不是自定义browser 只有原生方法
# 				usersay= ele.text
# 			except Exception, e:
# 				# raise e
# 				# usersay= ele.find_element_by_css_selector('.arrow_box_left .text').text
# 				usersay=""
# 			# try:
# 			# 	# ele不是自定义browser 只有原生方法
# 			# 	usersay= ele.find_element_by_css_selector('.msg').text
# 			# except Exception, e:
# 			# 	# raise e
# 			# 	# usersay= ele.find_element_by_css_selector('.arrow_box_left .text').text
# 			# 	usersay=""
				
# 			self.sayarray.append({'nickname':self.name,'usersay':usersay})
		
# 		# 判断聊天长度
# 		print(len(self.sayarray))
# 		if len(self.sayarray)<=0:
# 			pass
# 		else:
# 			pass
# 			usersayobj=self.sayarray[-1]
# 			nname=usersayobj['nickname']
# 			ssay=usersayobj['usersay'].replace(' ','')

# 			if self.lastsay[self.name]==ssay:
# 				pass
# 				self.new=False
# 				self.newmsg=""
# 				self.if_newmessage[self.name]=False
# 			else:
# 				if ssay=='' and self.is_img==1:
# 					# 如果是发图片
# 					self.if_newmessage[self.name]=True
# 					self.lastsay[self.name]=ssay
# 				elif ssay!='':
# 					# 如果内容不是为空
# 					self.if_newmessage[self.name]=True
# 					self.lastsay[self.name]=ssay


# 			self.new=self.if_newmessage[self.name]

# 			usersayobj=self.sayarray[-1]
# 			self.ssay=usersayobj['usersay']
# 			self.newmsg=self.ssay

# 			# 过滤
# 			if self.newmsg=="正在输入":
# 				self.new=False


# 		# 	# 保存文本数据
# 		# 	# f.write('医生||'+ssay+'\n')

# 		# 	#保存文本到数据库
# 		# 	# urlprefix='http://liliniao.com.cn/hospital/index.php?m=Api&c=user&a=talklog'
# 		# 	# urll =urlprefix+'&urole='+urllib.quote('医生'.encode('utf8'))+'&usay='+urllib.quote(ssay.encode('utf8'))+'&chatid='+str(userid)+'-'+str(fname)+'&userid='+str(userid)
# 		# 	# reqq = urllib2.Request(urll)
# 		# 	# res_dataa = urllib2.urlopen(reqq)
# 		# 	# ress = res_dataa.read()




# 		# 截图 保留
# 		msglist_length=len(self.sayarray)
# 		fname=self.fname
# 		# C:/zip/12/
# 		if msglist_length<3:
# 			self.browser.screen("C:/zip/"+str(fname)+'s'+"screen.png")
# 		elif msglist_length<6:
# 			self.browser.screen("C:/zip/"+str(fname)+'m'+"screen.png")
# 		else:
# 			self.browser.screen("C:/zip/"+str(fname)+"screen.png")


# 		# 没起作用
# 		# 没起作用
# 		# 是否被对方手动结束对话
# 		# kschat_enddialog
# 		# inputhtml=self.browser.getelementsbycss('.other_msg')
# 		inputhtml=self.browser.getelementsbycss('.msg')
# 		# inputhtml=browser.find_element_by_xpath("//div[contains(text(), '次对话已经结束! 如果您还')]")
# 		# inputhtml=browser.find_element_by_xpath("//div[@class='other_msg']")

# 		# print('isover')
# 		if inputhtml!=None:
# 			for x in inputhtml:
# 				print(x.text)
# 				if '次对话已经结束! 如果您还' in x.text:
# 					self.browser.quit()
# 				if '请您耐心等待' in x.text:
# 					self.browser.quit()
# 				if '在线咨询患者较多，回复较慢，请不要着急，正在回复您' in x.text:
# 					self.browser.quit()
# 				if '本次沟通已结束' in x.text:
# 					self.browser.quit()
# 				if '请等待客服人员应答' in x.text :
# 					self.browser.quit()

# 		return self

# 		# # 是否有新消息
# 		# if if_newmessage[name]:
# 		# 	if_newmessage[name]=0

# 		# 	usersayobj=sayarray[-1]
# 		# 	nname=usersayobj['nickname']
# 		# 	ssay=usersayobj['usersay']

# 		# 	# 保存文本数据
# 		# 	# f.write('医生||'+ssay+'\n')

# 		# 	#保存文本到数据库
# 		# 	# urlprefix='http://liliniao.com.cn/hospital/index.php?m=Api&c=user&a=talklog'
# 		# 	# urll =urlprefix+'&urole='+urllib.quote('医生'.encode('utf8'))+'&usay='+urllib.quote(ssay.encode('utf8'))+'&chatid='+str(userid)+'-'+str(fname)+'&userid='+str(userid)
# 		# 	# reqq = urllib2.Request(urll)
# 		# 	# res_dataa = urllib2.urlopen(reqq)
# 		# 	# ress = res_dataa.read()

# 		# 	# 自动回复

# 		# 	#中文机器人	自有
# 		# 	urll ='http://127.0.0.1:9003/?word='+urllib.quote(ssay.encode('utf8'))+'&group='+urllib.quote(name.encode('utf8'))+'&username='+urllib.quote(nname.encode('utf8'))
# 		# 	reqq = urllib2.Request(urll)
# 		# 	res_dataa = urllib2.urlopen(reqq)
# 		# 	ress = res_dataa.read()

# 		# 	if ress == 'stop to say||stop to say':
# 		# 		print 'stop to say'
# 		# 		pass
# 		# 	else:
# 		# 		pass
# 		# 		saylist=uwords.split('，')
# 		# 		send_massage(name,1,uwords)


# 		# 	# 保存文本数据
# 		# 	# f.write('病人||'+uwords+'\n')

# 		# ress=''#清空上次回答内容






# 		