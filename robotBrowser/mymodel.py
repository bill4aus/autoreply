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
		




class msgextractor_for_kuaishangtong(object):
	"""docstring for msgextractor_for_kuaishangtong"""
	def __init__(self, botchrome):
		super(msgextractor_for_kuaishangtong, self).__init__()
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
		# inputhtml=self.botchrome.getelementbycss("#kw")
		# if inputhtml:
		# 	self.new=True
		# 	self.newmsg="new message"
		# return self


		# 开始提取

		# 判断 是  PC  还是  移动端

		# .msg_cs .msg  PC
		# .msg_left mobile


		# #wrapper .content .msg_left
		# #msgArea .msg-box .msg-agent
		# msg_left
		#msgArea .msg-box .msg-agent
		listele=self.botchrome.getelementsbycss('.msg_cs .msg')
		msglist_length=len(listele)
		for ele in listele:
			try:
				# ele不是自定义browser 只有原生方法
				usersay= ele.text
			except Exception as e:
				# raise e
				# usersay= ele.find_element_by_css_selector('.arrow_box_left .text').text
				usersay=""
			# try:
			# 	# ele不是自定义browser 只有原生方法
			# 	usersay= ele.find_element_by_css_selector('.msg').text
			# except Exception, e:
			# 	# raise e
			# 	# usersay= ele.find_element_by_css_selector('.arrow_box_left .text').text
			# 	usersay=""
				
			self.sayarray.append({'nickname':self.name,'usersay':usersay})
		
		# 判断聊天长度
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

			# 过滤
			if self.newmsg=="正在输入":
				self.new=False


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
			self.botchrome.screen("C:/zip/"+str(fname)+'s'+"screen.png")
		elif msglist_length<6:
			self.botchrome.screen("C:/zip/"+str(fname)+'m'+"screen.png")
		else:
			self.botchrome.screen("C:/zip/"+str(fname)+"screen.png")


		# 没起作用
		# 没起作用
		# 是否被对方手动结束对话
		# kschat_enddialog
		# inputhtml=self.browser.getelementsbycss('.other_msg')
		inputhtml=self.botchrome.getelementsbycss('.msg')
		# inputhtml=browser.find_element_by_xpath("//div[contains(text(), '次对话已经结束! 如果您还')]")
		# inputhtml=browser.find_element_by_xpath("//div[@class='other_msg']")

		# print('isover')
		if inputhtml!=None:
			for x in inputhtml:
				print(x.text)
				if '次对话已经结束! 如果您还' in x.text:
					self.botchrome.quit()
				if '请您耐心等待' in x.text:
					self.botchrome.quit()
				if '在线咨询患者较多，回复较慢，请不要着急，正在回复您' in x.text:
					self.botchrome.quit()
				if '本次沟通已结束' in x.text:
					self.botchrome.quit()
				if '请等待客服人员应答' in x.text :
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

		# 	#中文机器人	自有
		# 	urll ='http://127.0.0.1:9003/?word='+urllib.quote(ssay.encode('utf8'))+'&group='+urllib.quote(name.encode('utf8'))+'&username='+urllib.quote(nname.encode('utf8'))
		# 	reqq = urllib2.Request(urll)
		# 	res_dataa = urllib2.urlopen(reqq)
		# 	ress = res_dataa.read()

		# 	if ress == 'stop to say||stop to say':
		# 		print 'stop to say'
		# 		pass
		# 	else:
		# 		pass
		# 		saylist=uwords.split('，')
		# 		send_massage(name,1,uwords)


		# 	# 保存文本数据
		# 	# f.write('病人||'+uwords+'\n')

		# ress=''#清空上次回答内容







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







class msgextractor_for_baidu(object):
	"""docstring for msgextractor_for_zoosoft"""
	def __init__(self, botchrome):
		super(msgextractor_for_baidu, self).__init__()
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
		listele=self.botchrome.getelementsbycss('.pc-component-chatview-wrapper .pc-chatviewbase .pc-chatviewbase-bubble')
		msglist_length=len(listele)
		for ele in listele:
			try:
				# ele不是自定义browser 只有原生方法
				usersay= ele.find_element_by_css_selector('.imlp-component-text').text
			except Exception as e:
				# raise e
				# usersay= ele.find_element_by_css_selector('.text').text
				usersay=''
			self.sayarray.append({'nickname':self.name,'usersay':usersay})
		
		# 判断聊天长度
		print("len(self.sayarray)")
		print(len(self.sayarray))
		print(self.sayarray)
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





#lib

from user_agent import generate_user_agent, generate_navigator
class ua(object):
	"""docstring for ua"""
	def __init__(self, ismobile):
		super(ua, self).__init__()
		self.ismobile = ismobile


	# http://www.fynas.com/ua/search?b=&d=%E5%8D%8E%E4%B8%BA
	def mobile(self):
		pass
		ua=[
		'Mozilla/5.0 (Linux; Android 7.0; STF-AL10 Build/HUAWEISTF-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043508 Safari/537.36 V1_AND_SQ_7.2.0_730_YYB_D QQ/7.2.0.3270 NetType/4G WebP/0.3.0 Pixel/1080',
		'Mozilla/5.0 (Linux; Android 5.1.1; vivo Xplay5A Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.3 baiduboxapp/9.3.0.10 (Baidu; P1 5.1.1)',
		'Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; STF-AL00 Build/HUAWEISTF-AL00) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.9 Mobile Safari/537.36',
		'Mozilla/5.0 (Linux; Android 6.0; LEX626 Build/HEXCNFN5902606111S) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/35.0.1916.138 Mobile Safari/537.36 T7/7.4 baiduboxapp/8.3.1 (Baidu; P1 6.0)',
		'Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; SM-C7000 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.6.2.948 Mobile Safari/537.36',
		'MQQBrowser/5.3/Mozilla/5.0 (Linux; Android 6.0; TCL 580 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.98 Mobile Safari/537.36',
		'Mozilla/5.0 (Linux; U; Android 5.1.1; zh-cn; MI 4S Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.1.3',
		'Mozilla/5.0 (Linux; Android 5.1; OPPO R9tm Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.3 baiduboxapp/9.3.0.10 (Baidu; P1 5.1)',
		'Mozilla/5.0 (Linux; Android 5.1; OPPO R9m Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043508 Safari/537.36 V1_AND_SQ_7.2.0_730_YYB_D QQ/7.2.0.3270 NetType/4G WebP/0.3.0 Pixel/1080',
		'Mozilla/5.0 (Linux; Android 5.1.1; OPPO R7sPlus Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.3 baiduboxapp/9.3.0.10 (Baidu; P1 5.1.1)',
		'Mozilla/5.0 (Linux; Android 6.0.1; OPPO A57 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043508 Safari/537.36 V1_AND_SQ_7.2.0_730_YYB_D QQ/7.2.0.3270 NetType/WIFI WebP/0.3.0 Pixel/720',
		'Mozilla/5.0 (Linux; Android 5.1; OPPO A37m Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.3 baiduboxapp/9.3.0.10 (Baidu; P1 5.1)',
		'Mozilla/5.0 (Linux; U; Android 4.4.4; zh-CN; N5209 Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.0.953 Mobile Safari/537.36',
		'Mozilla/5.0 (Linux; Android 5.1; OPPO A59s Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.3 baiduboxapp/9.3.0.10 (Baidu; P1 5.1)',
		'Mozilla/5.0 (Linux; Android 5.1.1; vivo Xplay5A Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.3 baiduboxapp/9.3.0.10 (Baidu; P1 5.1.1)',
		'Mozilla/5.0 (Linux; Android 5.0.2; vivo X6A Build/LRX22G; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.3 baiduboxapp/9.3.0.10 (Baidu; P1 5.0.2)',
		'Mozilla/5.0 (Linux; Android 5.1; vivo X6Plus D Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043508 Safari/537.36 V1_AND_SQ_7.2.0_730_YYB_D QQ/7.2.0.3270 NetType/4G WebP/0.3.0 Pixel/1080',
		'Mozilla/5.0 (Linux; Android 6.0; vivo Y67A Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/35.0.1916.138 Mobile Safari/537.36 T7/7.4 baiduboxapp/8.5 (Baidu; P1 6.0)',
		'Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; vivo Y67 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.5.6.946 Mobile Safari/537.36',
		'Mozilla/5.0 (Linux; Android 5.1.1; vivo X7Plus Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/35.0.1916.138 Mobile Safari/537.36 T7/7.1 baiduboxapp/8.0 (Baidu; P1 5.1.1)',
		'Mozilla/5.0 (Linux; U; Android 5.0.2; zh-CN; vivo X6Plus A Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.3) WindVane/8.3.0 1080X1920',
		'Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; Redmi Note 4X Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.1.3',
		'Mozilla/5.0 (Linux; U; Android 6.0.1; zh-cn; Redmi Note 3 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.8 Mobile Safari/537.36',
		'Mozilla/5.0 (Linux; U; Android 4.4.4; zh-cn; HM NOTE 1LTE Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/42.0.2311.153 Mobile Safari/537.36 XiaoMi/MiuiBrowser/2.1.1',
		'Mozilla/5.0 (Linux; U; Android 6.0; zh-cn; Redmi Pro Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/8.7.7',
		'Mozilla/5.0 (Linux; U; Android 5.1.1; zh-cn; Redmi 3 Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.8 Mobile Safari/537.36',
		'Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; SM-C7000 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.6.2.948 Mobile Safari/537.36',
		'Mozilla/5.0 (Linux; Android 6.0.1; SM-A7100 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/35.0.1916.138 Mobile Safari/537.36 T7/7.4 baiduboxapp/8.1 (Baidu; P1 6.0.1)',
		'Mozilla/5.0 (Linux; Android 4.4.4; SM-N935F Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/33.0.0.0 Safari/537.36 baidubrowser/7.13.13.0 (Baidu; P1 4.4.4)',
		'Mozilla/5.0 (Linux; Android 6.0.1; SM-C9000 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.1 baidubrowser/7.15.15.0 (Baidu; P1 6.0.1)',
		'Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; SM-G9300 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.2 Mobile Safari/537.36',
		'Mozilla/5.0 (Linux; Android 7.0; FRD-AL00 Build/HUAWEIFRD-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043508 Safari/537.36 V1_AND_SQ_7.1.0_0_TIM_D TIM2.0/1.2.0.1692 QQ/6.5.5 NetType/2G WebP/0.3.0 Pixel/1080 IMEI/869953022249635',
		'Mozilla/5.0 (Linux; Android 6.0; HUAWEI NXT-AL10 Build/HUAWEINXT-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.3 baiduboxapp/9.3.0.10 (Baidu; P1 6.0)',
		'Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.23 Mobile Safari/537.36'
		]
		# random.shuffle(ua)
		# return ua[0]
		return random.choice(ua)

	# 手机 PC  ipad
	def get(self):
		# 更换头部
		# 移动版没有广告地址了，需要点击了
		# if ismobile:
		# 	chome_options.add_argument('user-agent="Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.23 Mobile Safari/537.36"')

		# generate_user_agent(os=('android'))

		if self.ismobile:
			uainfo=self.mobile()
		else:
			uainfo=generate_user_agent(os=('win'))
		return uainfo


from yundama import YDMHttp


import httplib, mimetypes, urlparse, json, time

class YDMHttp:

    apiurl = 'http://api.yundama.com/api.php'
    
    username = ''
    password = ''
    appid = ''
    appkey = ''

    def __init__(self, username, password, appid, appkey):
        self.username = username  
        self.password = password
        self.appid = str(appid)
        self.appkey = appkey

    def request(self, fields, files=[]):
        try:
            response = post_url(self.apiurl, fields, files)
            response = json.loads(response)
        except Exception as e:
            response = None
        return response
    
    def balance(self):
        data = {'method': 'balance', 'username': self.username, 'password': self.password, 'appid': self.appid, 'appkey': self.appkey}
        response = self.request(data)
        if (response):
            if (response['ret'] and response['ret'] < 0):
                return response['ret']
            else:
                return response['balance']
        else:
            return -9001
    
    def login(self):
        data = {'method': 'login', 'username': self.username, 'password': self.password, 'appid': self.appid, 'appkey': self.appkey}
        response = self.request(data)
        if (response):
            if (response['ret'] and response['ret'] < 0):
                return response['ret']
            else:
                return response['uid']
        else:
            return -9001

    def upload(self, filename, codetype, timeout):
        data = {'method': 'upload', 'username': self.username, 'password': self.password, 'appid': self.appid, 'appkey': self.appkey, 'codetype': str(codetype), 'timeout': str(timeout)}
        file = {'file': filename}
        response = self.request(data, file)
        if (response):
            if (response['ret'] and response['ret'] < 0):
                return response['ret']
            else:
                return response['cid']
        else:
            return -9001

    def result(self, cid):
        data = {'method': 'result', 'username': self.username, 'password': self.password, 'appid': self.appid, 'appkey': self.appkey, 'cid': str(cid)}
        response = self.request(data)
        return response and response['text'] or ''

    def decode(self, filename, codetype, timeout):
        cid = self.upload(filename, codetype, timeout)
        if (cid > 0):
            for i in range(0, timeout):
                result = self.result(cid)
                if (result != ''):
                    return cid, result
                else:
                    time.sleep(1)
            return -3003, ''
        else:
            return cid, ''

    def report(self, cid):
        data = {'method': 'report', 'username': self.username, 'password': self.password, 'appid': self.appid, 'appkey': self.appkey, 'cid': str(cid), 'flag': '0'}
        response = self.request(data)
        if (response):
            return response['ret']
        else:
            return -9001

######################################################################

def post_url(url, fields, files=[]):
    urlparts = urlparse.urlsplit(url)
    return post_multipart(urlparts[1], urlparts[2], fields, files)

def post_multipart(host, selector, fields, files):
    content_type, body = encode_multipart_formdata(fields, files)
    h = httplib.HTTP(host)
    h.putrequest('POST', selector)
    h.putheader('Host', host)
    h.putheader('Content-Type', content_type)
    h.putheader('Content-Length', str(len(body)))
    h.endheaders()
    h.send(body)
    errcode, errmsg, headers = h.getreply()
    return h.file.read()

def encode_multipart_formdata(fields, files=[]):
    BOUNDARY = 'WebKitFormBoundaryJKrptX8yPbuAJLBQ'
    CRLF = '\r\n' 
    L = [] 
    for field in fields:
        key = field
        value = fields[key]
        L.append('--' + BOUNDARY) 
        L.append('Content-Disposition: form-data; name="%s"' % key) 
        L.append('') 
        L.append(value) 
    for field in files:
        key = field
        filepath = files[key]
        L.append('--' + BOUNDARY) 
        L.append('Content-Disposition: form-data; name="%s"; filename="%s"' % (key, filepath))
        L.append('Content-Type: %s' % get_content_type(filepath)) 
        L.append('')
        L.append(open(filepath, 'rb').read())
    L.append('--' + BOUNDARY + '--') 
    L.append('') 
    body = CRLF.join(L)
    content_type = 'multipart/form-data; boundary=%s' % BOUNDARY 
    return content_type, body 

def get_content_type(filename):
    return mimetypes.guess_type(filename)[0] or 'application/octet-stream'


# 上级目录
# sys.path.append('../')
# import robot.robot as robot
class yanzhengma(object):
	"""docstring for yanzhengma"""
	def __init__(self,browser):
		super(yanzhengma, self).__init__()
		# self.arg = arg
		self.browser=browser


		# 用户名
		username	= 'cdsbtest'
		# 密码
		password	= 'cdsb123456'							
		# 软件ＩＤ，开发者分成必要参数。登录开发者后台【我的软件】获得！
		appid		 = 3035									 
		# 软件密钥，开发者分成必要参数。登录开发者后台【我的软件】获得！
		appkey		= '0856355e1dd686e7819093bcd2843176'	
		# 图片文件
		# filename	= 'getimage.jpg'						
		# 验证码类型，# 例：1004表示4位字母数字，不同类型收费不同。请准确填写，否则影响识别率。在此查询所有类型 http://www.yundama.com/price.html
		# codetype	= 1004
		self.codetype	= 5000
		# 超时时间，秒
		self.timeout	 = 60	 

		# 初始化
		self.yundama = YDMHttp(username, password, appid, appkey)

		# 登陆云打码
		uid = self.yundama.login();
		print 'uid: %s' % uid
		# 查询余额
		balance = self.yundama.balance();
		print 'balance: %s' % balance

	def recognise(self,imgfilename):

		# 开始识别，图片路径，验证码类型ID，超时时间（秒），识别结果
		cid, result = self.yundama.decode(imgfilename, self.codetype, self.timeout);
		print 'cid: %s, result: %s' % (cid, result)
		result=str(result)
		# print result
		result=result.replace('c_char_p','')
		result=result.replace('(','')
		result=result.replace(')','')
		result=result.replace('\'','')

		img_to_text=result

		#得到的是原始对象,使用原始的send_keys方法发送消息
		self.browser.getelementbycss('#ccode').send_keys(img_to_text.decode())
		time.sleep(0.3)
		self.browser.getelementbycss('#Button1').send_keys(Keys.ENTER)
		time.sleep(0.3)