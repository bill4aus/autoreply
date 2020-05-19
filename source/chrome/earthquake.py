#!/usr/bin/env python
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

from user_agent import generate_user_agent, generate_navigator

from selenium.webdriver.common.keys import Keys	

reload(sys)
sys.setdefaultencoding('utf-8')

import requests
import json,urllib2


# 设置代理
# service_args = ['--proxy='+ip_proxy,'--proxy-type=socks5']
service_args = []




dcap={}
#从USER_AGENTS列表中随机选一个浏览器头，伪装浏览器
uainfo=generate_user_agent()
print(type(uainfo))
print(uainfo)

dcap["phantomjs.page.settings.userAgent"] = (
	uainfo
)
dcap["phantomjs.page.settings.loadImages"] = False

browser = webdriver.PhantomJS(desired_capabilities=dcap)

browser.viewportSize={'width':824,'height':2200} #重要这句！
browser.maximize_window()

# chome_options.add_argument(('--proxy-server=http://' + ip_proxy))	
# browser = webdriver.Chrome(chrome_options=chome_options)	


browser.implicitly_wait(30)
browser.set_script_timeout(30)
browser.set_page_load_timeout(40)


while 1:

	openurlstring='https://weibo.cn/365ICL?p=r&rand=9598&p=r'
	try:
		# browser = webdriver.Chrome(desired_capabilities=capabilities)
		browser.get(openurlstring)
		time.sleep(10)
	except Exception, e:
		pass
		browser.quit()
		exit()
	# browser.save_screenshot("/home/wwwroot/default/wechat.png")
	time.sleep(0.1)

	try:
		# titleelm=browser.find_element_by_css_selector('#kw')
		titleelm=browser.find_elements_by_css_selector('.c')
		# print(titleelm)
		for x in titleelm:
			# print(x.text.encode('gbk'))
			
			if x.get_attribute('id')=='':
				continue
			print(x)
			print(x.get_attribute('id'))

			# .ctt
			twitter=x.find_element_by_tag_name('span').text
			# print(twitter.encode('gbk'))
			category='地震'
			# category='政府'
			# weibolink=x.find_element_by_css_selector('div a:nth-child(1)').get_attribute('href')#'https://weibo.cn/365ICL?p=r&rand=9598&p=r'
			weibolink=x.find_element_by_css_selector('a.cc').get_attribute('href')#'https://weibo.cn/365ICL?p=r&rand=9598&p=r'
			# weibolink=x.find_element_by_xpath("//a[contains(text(),'评论')]") 
			# print(weibolink)
			timestr=x.find_element_by_css_selector('span.ct').text
			# print(timestr.encode('gbk'))
			author='成都高新减灾研究所-专用爬虫'

			is_quake='四川' in twitter and	'发生' in twitter and	'级' in twitter and	'预警' in twitter
			# is_quake='装备与技术展' in twitter

			# if '今天' in timestr or '分钟前' in timestr	:
			is_today='今天' in timestr or '分钟前' in timestr or '秒前' in timestr
			if is_quake and is_today :
				print('******************************* earthquake **************************************')
				textmod={"twitter":twitter.encode('utf-8'),"category":category.encode('utf-8'),"weibolink":weibolink,"timestr": timestr,"author":author}
				# textmod = json.dumps(textmod)
				# textmod=urllib.urlencode(textmod)
				# headers = {'Content-type':"application/json"}
				# url='http://tongji.cdsb.mobi/micropub/addtwitter/'
				# req = urllib2.Request(url=url,data=json.dumps(textmod),headers=headers)
				# res = urllib2.urlopen(req)
				# res = res.read()
				# print(res)

				url='http://tongji.cdsb.mobi/micropub/addtwitter/'
				r = requests.post(url, data = textmod);


	except Exception, e:
		# raise e
		print(str(e))
		# browser.quit()
		# exit()
	print('next time......wait for 10 seconds')
	time.sleep(30)

