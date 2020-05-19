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
import platform
reload(sys)
sys.setdefaultencoding('utf-8')


platstring=platform.platform()

import requests

class MyBrowder(object):
	"""docstring for MyBrowder"""
	def __init__(self, browsername):
		super(MyBrowder, self).__init__()
		self.browsername = browsername


		self.vertifycodeimgsize=None;
		self.isuseful=0

		# 如果是chrome
		# 浏览器设置 # setting
		self.chrome_options = webdriver.ChromeOptions()
		# 设置中文
		# self.chrome_options.add_argument('lang=zh_CN.UTF-8')

		username = os.getenv("USERNAME")
		userProfile = "C:\\Users\\" + username + "\\AppData\\Local\\Google\\Chrome\\User Data\\Default"
		
		self.chrome_options.add_argument("user-data-dir={}".format(userProfile))
		# "excludeSwitches",["ignore-certificate-errors"]
		self.chrome_options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors", "safebrowsing-disable-download-protection", "safebrowsing-disable-auto-update", "disable-client-side-phishing-detection"])

		self.chrome_options.add_argument('--disable-extensions')
		self.chrome_options.add_argument('--profile-directory=Default')
		self.chrome_options.add_argument("--incognito")
		self.chrome_options.add_argument("--disable-plugins-discovery");
		self.chrome_options.add_argument("--start-maximized")
		
		#设置不显示图片
		# ,"profile.managed_default_content_settings.javascript":2
		# prefs = {"profile.managed_default_content_settings.images":2}
		prefs = {}
		self.chrome_options.add_experimental_option("prefs",prefs)


		# 如果是phantom


		self.dcap={}
		self.dcap["phantomjs.page.settings.loadImages"] = True


		self.dcap['phantomjs.page.customHeaders.Accept'] ='text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
		# self.dcap['phantomjs.page.customHeaders.Host'] =host
		
		self.dcap['phantomjs.page.customHeaders.Accept-Encoding'] ='gzip, deflate, sdch'
		# self.dcap['phantomjs.page.customHeaders.Referer'] ='https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=0&rsv_idx=1&tn=baidu&wd=%E5%94%90%E5%B1%B1%E5%8C%BB%E9%99%A2'
		# # dcap['phantomjs.page.customHeaders.Referer'] ='http://www.tstryy.com/jhsy/shengyuzhidao/'
		# self.dcap['phantomjs.page.customHeaders.Cookie'] =';'.join(cookielist)
		self.dcap['phantomjs.page.customHeaders.Cookie'] = 'JSESSIONID=D41B9AB30144CDCCDB8F7E7479E53D0D; 59270___700690_KS_59270___700690=ab2e820fa35d47fb978a598e742cee7c; gdxidpyhxdE=vRay0bA0aLpjcs6IB0Q8CaaEDx0dEY%2FnprC2NLavdyjtIa1ghW06kXCqg9je6BPk5p%2FY4i6eZL7g2IpfzYQusTIt1mvl%5C2kmtwQqO7cHAmmAgQXZKr%2B9ad%2FlkCnaptSD5YpMLhE0eHYW%5C9qNr1x%2F1JVZK7oycCA87Hbn7uLmOckD%2Bs8X%3A1527175534004; _9755xjdesxxd_=32; 59270___700690_KS_isvca=; recordCheck=1527177693298'
		self.dcap['phantomjs.page.customHeaders.Cache-Control'] ='max-age=0'
		self.dcap['phantomjs.page.customHeaders.Connection'] ='keep-alive'
		self.dcap['phantomjs.page.customHeaders.Upgrade-Insecure-Requests'] ='1'
		self.dcap['phantomjs.page.customHeaders.Accept-Encoding'] ='gzip, deflate'
		self.dcap['phantomjs.page.customHeaders.Accept-Language'] ='zh-CN,zh;q=0.9'



		

		

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

		# chrome_options.add_argument(('--proxy-server=http://' + ip_proxy))	

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
		
		self.browser = webdriver.Chrome(chrome_options=self.chrome_options)
		self.browser.delete_all_cookies()
		# # 带跳转的打开方式
		try:
			self.browser.get(hospitalsite)
		except Exception, e:
			raise e
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

		while True:
			print('code check and  recognise .......')

			if self.check_vertifycode()==None:
				pass
				print("cotinune")
				time.sleep(5)
				self.screen("./wechat.png")
			else:
				break;
			

	def open(self,openurlstring):

		#win7
		if 'XP' not in platstring:
			# cityname=''
			# ip_proxy=changeip(cityname)
			# if len(ip_proxy)>30:
			# 	print('NO IP AVILABLE')
			# 	exit()
			# # chrome_options.add_argument(('--proxy-server=http://' + ip_proxy))	



			# # IP代理
			# proxy = webdriver.Proxy()  
			# proxy.proxy_type = ProxyType.MANUAL  
			# proxy.http_proxy = ip_proxy
			# proxy.add_to_capabilities(dcap)  

			# if browsername==None or browsername=='':
			# 	browsername='phantom'

			# if browsername=='phantom':
			# 	# 改为phantom
			# 	# Windows环境下完整路径前加r！！！
			# 	browser = webdriver.PhantomJS(executable_path=r'E:\python\phantom\phantomjs\bin\phantomjs.exe',desired_capabilities=dcap)
			# 	browser.viewportSize={'width':824,'height':2200} #重要这句！
			# 	browser.maximize_window()
			# 	print('PhantomJS()')
			# if browsername=='chrome':
			# 	# chrome ua修改失败，所以还是用phantom
			# 	browser = webdriver.Chrome(chrome_options=chrome_options)	
			# 	print('Chrome()')


			tbrowser=webdriver.Chrome(chrome_options=self.chrome_options)
			pass
		else:
			#xp

			if self.browsername==None or self.browsername=='':
				self.browsername='phantom'

			if self.browsername=='phantom':
				# 改为phantom
				# Windows环境下完整路径前加r！！！
				# browser = webdriver.PhantomJS(executable_path=r'D:\phantomjs\bin\phantomjs.exe',desired_capabilities=dcap)
				tbrowser = webdriver.PhantomJS(executable_path=r'C:\phantomjs\phantomjs.exe',desired_capabilities=self.dcap)
				tbrowser.viewportSize={'width':1824,'height':2200} #重要这句！
				tbrowser.maximize_window()
				print('PhantomJS()')
				pass
			if self.browsername=='chrome':
				# phantom 好像被 识别了 ，所以还是用 chrome
				tbrowser=webdriver.Chrome(chrome_options=self.chrome_options)
				print('Chrome()')



		self.browser = tbrowser
		self.browser.delete_all_cookies()
		# 超时设置
		# self.browser.implicitly_wait(30)
		# self.browser.set_script_timeout(30)
		self.browser.set_page_load_timeout(10)


		try:
			self.browser.get(openurlstring)
		except Exception, e:
			raise e
			self.browser.quit()
		time.sleep(3)
		self.screen("./wechat.png")
		time.sleep(3)

		# self.browser.save_screenshot("wechat.png")
		try:
			self.check_website()
		except Exception, e:
			# raise e
			self.browser.quit()

		while True:
			print('code check and  recognise .......')

			if self.check_vertifycode()==None:
				pass
				print("cotinune")
				time.sleep(5)
				self.screen("./wechat.png")
			else:
				break;
		
		
	def quit(self):
		# 关闭文件
		# f.close()
		# 关闭浏览器 好像退出后,进程还在?需要确认,占用内存
		try:
			self.browser.quit()
		except Exception as e:
			# raise e
			pass
		# self.browser.quit()
		# 退出python进程
		exit()

	def if_element(self,elementstring):
		coderobot=self.browser.find_elements_by_css_selector(elementstring)
		if len(coderobot)>0:
			return True
		else:
			return False
	def if_vertifycode_showup(self):
		# 高级验证码  
		# iscodeforclick=0
		# modalDiv_Chatpreobj
		# modalDiv_ChatpreobjN
		if self.if_element('#modalDiv_ChatpreobjN'):
			return 'click'
		elif self.if_element('.oc_comm_win_verify'):
			return 'drag'
		elif self.if_element('#putongyanzhengma'):
			# 普通验证码判断
			return 'putongyanzhengma'
		else:
			return None

		
	def check_vertifycode(self):

		vertifycodetype=self.if_vertifycode_showup()
		if vertifycodetype==None:
			return None

		
		isdeal=0
		# #是否出现普通验证码  普通
		# # 请点击正确的答案开始对话  text   xpath 改为
		# iscode=0
		# # print(self.browser.find_element_by_css_selector('title'))
		# # print(self.browser.find_element_by_css_selector('#modalDiv_ChatpreobjN'))
		# coderobot=self.browser.find_elements_by_css_selector('#modalDiv_Chatpreobj')
		# if len(coderobot)>0:
		# 	print 'robot'
		# 	print 'robot'
		# 	print 'robot'
		# 	print 'robot'
		# 	iscode=1

		# 	# 验证码模块
		# 	# browser.save_screenshot('web.jpg')
		# 	imgelement=self.browser.find_element_by_css_selector('#yzmimg')
		# 	location = imgelement.location	#获取验证码x,y轴坐标
		# 	size=imgelement.size	#获取验证码的长宽
		# 	rangle=(int(location['x']),int(location['y']),int(location['x']+size['width']),int(location['y']+size['height'])) #写成我们需要截取的位置坐标

		# 	i=Image.open("wechat.png") #打开截图
		# 	frame4=i.crop(rangle)	#使用Image的crop函数，从截图中再次截取我们需要的区域
		# 	frame4.save("code.jpg")

		# 	imgfilename="code.jpg"

		# 	self.vertify.recognise(imgfilename)
		# 	# img_to_text=

		# return False

		print('image deal')

		# 高级验证码  # 验证码判断

		# modalDiv_ChatpreobjN
		# modalDiv_Chatpreobj
		# iscodeforclick=0
		if vertifycodetype=='click':
			pass
			# iscodeforclick=1
			print 'click code'

			#截图
			# yzmimgN
			imgelement=self.browser.find_element_by_css_selector('#yzmimgN')
			location = imgelement.location	#获取验证码x,y轴坐标
			if self.vertifycodeimgsize==None:
				pass
				self.vertifycodeimgsize=imgelement.size	#获取验证码的长宽
			print('size')
			print(size)
			rangle=(int(location['x']),int(location['y']),int(location['x']+self.vertifycodeimgsize['width']),int(location['y']+self.vertifycodeimgsize['height'])) #写成我们需要截取的位置坐标

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
			time.sleep(1)
			# float(widthheight[1])*self.vertifycodeimgsize['height']
			ActionChains(self.browser).move_to_element_with_offset(above,float(widthheight[0])*self.vertifycodeimgsize['width'],float(widthheight[1])*self.vertifycodeimgsize['height']).click().perform()



		# 高级拖拽验证码
		# isdragcode=0
		if vertifycodetype=='drag':
			print 'drag code'
			print(self.isuseful)
			if (not self.isuseful):
				pass
				#截图
				# oc_comm_win_verify
				# ncpt_puzzle_bg
				# ncpt_puzzle_bg
				imgelement=self.browser.find_element_by_css_selector('.ncpt_puzzle_bg')
				location = imgelement.location	#获取验证码x,y轴坐标
				if self.vertifycodeimgsize==None:
					self.vertifycodeimgsize=imgelement.size	#获取验证码的长宽
				print('size')
				print(self.vertifycodeimgsize)
				rangle=(int(location['x']),int(location['y']),int(location['x']+self.vertifycodeimgsize['width']),int(location['y']+self.vertifycodeimgsize['height'])) #写成我们需要截取的位置坐标

				i=Image.open("wechat.png") #打开截图
				frame4=i.crop(rangle)	#使用Image的crop函数，从截图中再次截取我们需要的区域
				frame4.save("newcode.jpg")

				imgid=None

				#提交识别请求，获取图片ID
				url="http://www.liliniao.com.cn/dama/index.php?m=UserAdmin&c=Fileupload&a=upload"
				files={'Filedata':('newcode.jpg',open('newcode.jpg','rb'),'image/jpeg')}
				sdata={'type': 'Image'}
				res=requests.post(url,data=sdata,files=files)
				# print res.text
				imginfo=json.loads(res.text)
				imgid=imginfo['id']
				print('imgid')
				print(imgid)

			#等待识别结果
			# 定时请求该图片ID结果
			codestr=''
			
			
			if imgid!=None:
				while (isdeal==0 and self.isuseful==0):
					time.sleep(5)
					imgcoderesinfo=requests.get('http://www.liliniao.com.cn/dama/index.php?m=UserAdmin&c=Api&a=index&id='+str(imgid))
					imgcoderes=json.loads(imgcoderesinfo.text)
					if imgcoderes['status']==1:
						codestr=imgcoderes['result']
						#输入识别结果  或者  根据结果 点击相应位置
						widthheight=codestr.split(',')
						print('widthheight')
						print(widthheight)
						
						dragger = self.browser.find_element_by_css_selector(".ncpt_slide_fg img")
						# ActionChains(self.browser).move_to_element_with_offset(above,float(widthheight[0])*size['width'],float(widthheight[1])*size['height']).click().perform()
						# float(widthheight[1])*self.vertifycodeimgsize['height']
						ActionChains(self.browser).click_and_hold(dragger).move_by_offset(float(widthheight[0])*self.vertifycodeimgsize['width']-35,0).release().perform()
						isdeal=1
						time.sleep(3)

						vertifycodetype=self.if_vertifycode_showup()
						if vertifycodetype==None:
							return None

					else:
						print('wait')
						print(str(imgid))
					


		return True



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
		
		

	
	# 手机 PC  ipad
	def setua(self,useragent):
		# self.useragent=useragent
		# uainfo=self.useragent.get()
		self.uainfo=useragent.get()
		# useraget
		self.chrome_options.add_argument("user-agent="+self.uainfo)
		self.dcap['phantomjs.page.customHeaders.User-Agent'] =self.uainfo

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
		