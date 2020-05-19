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
import urllib2
import threading
import json
import random
import math
import codecs
import os
from selenium.webdriver.common.keys import Keys	
from PIL import Image	
from user_agent import generate_user_agent, generate_navigator

reload(sys)
sys.setdefaultencoding('utf-8')

import requests

class MyBrowder(object):
	"""docstring for MyBrowder"""
	def __init__(self, arg):
		super(MyBrowder, self).__init__()
		self.arg = arg



		# 如果是chrome
		# 浏览器设置 # setting
		self.chome_options = webdriver.ChromeOptions()
		# 设置中文
		self.chome_options.add_argument('lang=zh_CN.UTF-8')
		
		#设置不显示图片
		# ,"profile.managed_default_content_settings.javascript":2
		# prefs = {"profile.managed_default_content_settings.images":2}
		prefs = {}
		self.chome_options.add_experimental_option("prefs",prefs)
		

		

		# ip代理
		# cityname='广东'
		# cityname=''
		# ip_proxy=changeip(cityname)
		# # ip_proxy='zghbtsyt.eatuo.com:23157'
		# # ip_proxy='124.237.131.63:9999'
		# # ip_proxy='123.180.68.176:11896'

		# if len(ip_proxy)>20:
		# 	print('NO IP AVILABLE')
		# 	exit()

		# chome_options.add_argument(('--proxy-server=http://' + ip_proxy))	

	def screen(self,screen_file):
		self.browser.save_screenshot(screen_file)

	def getelementbycss(self,css_selector):
		# try:
		# 	res=WebDriverWait(source,0.5).until(lambda source:self.browser.find_element_by_css_selector(css_selector) , " open fail")

		# 	if res==False:
		# 		return None
		# 	else:
		# 		elem=self.browser.find_element_by_css_selector(css_selector)
		# 		return elem
		# except Exception, e:
		# 	return None
		elem=self.browser.find_element_by_css_selector(css_selector)
		return elem
	def getelementsbycss(self,css_selector):
		# try:
		# 	res=WebDriverWait(source,0.5).until(lambda source:self.browser.find_elements_by_css_selector(css_selector) , " open fail")
		# 	if res==False:
		# 		return []
		# 	else:
		# 		elem=self.browser.find_elements_by_css_selector(css_selector)
		# 		return elem
		# except Exception, e:
		# 	return []
		elem=self.browser.find_elements_by_css_selector(css_selector)
		if elem:
			return elem
		else:
			return []
	def openwithsource(self,openurlstring,hospitalsite):
		
		self.browser = webdriver.Chrome(chrome_options=self.chome_options)
		self.browser.delete_all_cookies()
		# # 带跳转的打开方式
		try:
			self.browser.get(hospitalsite)
		except Exception, e:
			# raise e
			self.browser.quit()
		
		time.sleep(3)
		set_wyswyg_js = 'location.href="'+openurlstring+'";'
		self.javascript(set_wyswyg_js)
		time.sleep(3)
		self.screen("./wechat.png")
		time.sleep(3)

		try:
			self.check_website()
		except Exception, e:
			# raise e
			self.browser.quit()

	def open(self,openurlstring):

		self.browser = webdriver.Chrome(chrome_options=self.chome_options)
		self.browser.delete_all_cookies()
		# 超时设置
		self.browser.implicitly_wait(30)
		self.browser.set_script_timeout(30)
		self.browser.set_page_load_timeout(40)


		try:
			self.browser.get(openurlstring)
		except Exception, e:
			# raise e
			self.browser.quit()
		time.sleep(5)
		self.screen("./wechat.png")
		# self.browser.save_screenshot("wechat.png")
		try:
			self.check_website()
		except Exception, e:
			# raise e
			self.browser.quit()
		
		
	def quit(self):
		# 关闭文件
		# f.close()
		# 关闭浏览器 好像退出后,进程还在?需要确认,占用内存
		self.browser.quit()
		# 退出python进程
		exit()
	def check_website(self):
		# 检查标题是否为空
		if self.browser.title=='' or '.com' in self.browser.title or '.cn' in self.browser.title or '.net' in self.browser.title:
			self.browser.quit()
		# 暂停
		# 检查页面是否包含iframe 
		# try:
		# 	titleelm=self.browser.find_element_by_css_selector('iframe')
		# except Exception, e:
		# 	# raise e
		# 	print('cant find iframe , page opend error ,quit quit quit')
		# 	self.browser.quit()
		
		
		# 高级验证码  # 验证码判断
		iscode=0
		# modalDiv_Chatpreobj
		# modalDiv_ChatpreobjN

		coderobot=self.browser.find_elements_by_css_selector('#modalDiv_ChatpreobjN')
		if len(coderobot)>0:
			iscode=1
			print 'newcode'
			print 'newcode'

			#截图
			# yzmimgN
			imgelement=self.browser.find_element_by_css_selector('#yzmimgN')
			location = imgelement.location	#获取验证码x,y轴坐标
			size=imgelement.size	#获取验证码的长宽
			print('size')
			print(size)
			rangle=(int(location['x']),int(location['y']),int(location['x']+size['width']),int(location['y']+size['height'])) #写成我们需要截取的位置坐标

			i=Image.open("wechat.png") #打开截图
			frame4=i.crop(rangle)	#使用Image的crop函数，从截图中再次截取我们需要的区域
			frame4.save("newcode.jpg")

			imgid=None

			#提交识别请求，获取图片ID
			url="http://www.liliniao.com.cn/dama/index.php?m=UserAdmin&c=Fileupload&a=upload"
			files={'Filedata':('newcode.jpg',open('newcode.jpg','rb'),'image/jpeg')}
			sdata={'type': 'Image'}
			res=requests.post(url,data=sdata,files=files)
			print res.text
			imginfo=json.loads(res.text)
			imgid=imginfo['id']
			print('imgid')
			print(imgid)

			#等待识别结果
			# 定时请求该图片ID结果
			codestr=''
			reststat=0
			if imgid!=None:
				while reststat==0:
					print('wait')
					imgcoderesinfo=requests.get('http://www.liliniao.com.cn/dama/index.php?m=UserAdmin&c=Api&a=index&id='+str(imgid))
					imgcoderes=json.loads(imgcoderesinfo.text)
					if imgcoderes['status']==1:
						reststat=1
						codestr=imgcoderes['result']
					time.sleep(1)
				print('img code ok')
				print('code sovled')


			#输入识别结果  或者  根据结果 点击相应位置
			widthheight=codestr.split(',')
			print('widthheight')
			print(widthheight)
			# browser.actions()
			# .mouseMove(
			# 	element(by.css('.material-dialog-container')), -20, -20) #pixel offset from top left
			# .click()
			# .perform();
			above = self.browser.find_element_by_css_selector("#yzmimgN")
			ActionChains(self.browser).move_to_element_with_offset(above,float(widthheight[0])*size['width'],float(widthheight[1])*size['height']).click().perform()








		#是否出现验证码  普通
		# 请点击正确的答案开始对话  text   xpath 改为
		iscode=0
		# print(self.browser.find_element_by_css_selector('title'))
		# print(self.browser.find_element_by_css_selector('#modalDiv_ChatpreobjN'))
		coderobot=self.browser.find_elements_by_css_selector('#modalDiv_Chatpreobj')
		if len(coderobot)>0:
			print 'robot'
			print 'robot'
			print 'robot'
			print 'robot'
			iscode=1

			# 验证码模块
			# browser.save_screenshot('web.jpg')
			imgelement=self.browser.find_element_by_css_selector('#yzmimg')
			location = imgelement.location	#获取验证码x,y轴坐标
			size=imgelement.size	#获取验证码的长宽
			rangle=(int(location['x']),int(location['y']),int(location['x']+size['width']),int(location['y']+size['height'])) #写成我们需要截取的位置坐标

			i=Image.open("wechat.png") #打开截图
			frame4=i.crop(rangle)	#使用Image的crop函数，从截图中再次截取我们需要的区域
			frame4.save("code.jpg")

			imgfilename="code.jpg"

			self.vertify.recognise(imgfilename)
			# img_to_text=

		return False



	
	# 手机 PC  ipad
	def setua(self,useragent):
		# self.useragent=useragent
		# uainfo=self.useragent.get()
		uainfo=useragent.get()
		# useraget
		self.chome_options.add_argument("user-agent="+uainfo)

	def setsender(self,sender):
		print("set sender")
		self.sender=sender

	def send(self,message):
		print("send message")
		# print(message)
		self.sender.send(message)

	# def setschedule(self,schedule):
	# 	pass
	# 	self.schedule=schedule
	
	def setextractor(self,msg_extractor):
		self.extractor=msg_extractor
	def getmessage(self):
		return self.extractor.get()
	def javascript(self,jsfunction):
		self.browser.execute_script(jsfunction)

	def setyanzhengma(self,vertify):
		self.vertify=vertify
	# def listen(self,message_extractor):
	# 	# 一直运行
	# 	while True:
	# 		pass
	# 		message_extractor.run()
	# 		time.sleep(5)

	# 	# 保存截图
	# 	# browser.save_screenshot("D:/zip/12/"+str(fname)+"screen.png")

	# # 执行schedule
	# def start(self):
	# 	pass

	# 	self.schedule.run()
		