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


# #云打码api
# import sys
# import os
# from ctypes import *
# YDMApi = windll.LoadLibrary('yundamaAPI-x64')
# appId = 3035   # 软件ＩＤ，开发者分成必要参数。登录开发者后台【我的软件】获得！
# appKey = '0856355e1dd686e7819093bcd2843176'     # 软件密钥，开发者分成必要参数。登录开发者后台【我的软件】获得！
# username ='cdsbtest'# raw_input('用户账号：')
# password ='cdsb123456'# raw_input('用户密码：')

# # 例：1004表示4位字母数字，不同类型收费不同。请准确填写，否则影响识别率。在此查询所有类型 http://www.yundama.com/price.html
# codetype = 1004

# # 分配30个字节存放识别结果
# result = c_char_p("                              ")     

# # 识别超时时间 单位：秒
# timeout = 60

# # 验证码文件路径
# # filename = 'getimage.jpg'
# filename = 'code.jpg'

# run()
#####

# #1.实例化类型 参数是打码兔用户账号和密码	
# dmt=DamatuApi("cdsbtest","cdsb123456")
# print 'damatu:'
# print(dmt.getBalance()) #查询余额 


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

cur = conn.cursor()
# sqli="select * from ad where chaturl is null and isuser is null and isdealwith=0 and id>16950"

# sqli="select * from ad where chaturl is null and id>0 and id <7000 and title like '%http%' "
# sqli="select * from ad where chaturl is null and id>7000 and id <13000  and title like '%http%' "
# sqli="select * from ad where chaturl is null and id>13000 and id <24000  and title like '%http%' "
# sqli="select * from ad where chaturl is null and id>24000 and id <30000  and title like '%http%' "
sqli="select * from ad where id>70258 and exclusive=0 and chaturl is null and title like '%http%' and ismobile=1 "
count=cur.execute(sqli)
# print(conn.commit())
results = cur.fetchall()   
for r in results:
    # print(type(r))
    print r[0]
    print r[3]
    keywords.append({'adurl':r[3],'id':r[0]})
cur.close()




# cur = conn.cursor()
# # sqli="insert into ad values(%s,%s,%s,%s)"
# sqli="update ad set chaturl='"+'thishref' +"' where id ="+'1'
# print(sqli)
# print(cur.execute(sqli))
# print(conn.commit())
# cur.close()



# keywords_bak=[]
count=0

ip_proxy_list=[

]
ip_count=0


# qq=Image.open('code.jpg')
# print qq
# text=pytesseract.image_to_string(qq,lang="eng") #使用image_to_string识别验证码
# print pytesseract
# print 'code:'
# print text

keywordlist=keywords

# 基本配置
# logging.basicConfig(level=logging.INFO)
openurlstring=''
# openurlstring='http://www.ipip.net/'


def settimeout(timeset,func):
	global isfinished
	global threading
	global browser
	timer = threading.Timer(timeset,func)
	timer.start()


def getelement(source,selector):
	global browser
	# browser.implicitly_wait(10)
	
	# res=WebDriverWait(source,3).until(lambda source:source.find_elements_by_css_selector(selector) , " open fail")
	res=True
	try:
		res=WebDriverWait(source,0.5).until(lambda source:source.find_element_by_css_selector(selector) , " open fail")
		# print(res)
		if res==False:
			return None
		else:
			# print(selector)
			elem=source.find_element_by_css_selector(selector)
			# elem=source.find_elements_by_css_selector(selector)
			return elem
	except Exception, e:
		return None

	# try:
	# 	WebDriverWait()
	# 	elem=source.find_element_by_css_selector(selector)
	# 	return elem
	# except Exception, e:
	# 	# raise e
	# 	print(str(e))
	# 	print(str(selector))
	# 	return None

def getelements(source,selector):
	global browser
	# browser.implicitly_wait(10)
	# res=WebDriverWait(source,3).until(lambda source:source.find_elements_by_css_selector(selector) , " open fail")
	res=True
	try:
		res=WebDriverWait(source,0.5).until(lambda source:source.find_elements_by_css_selector(selector) , " open fail")
		
		# print(res)
		if res==False:
			return []
		else:
			elem=source.find_elements_by_css_selector(selector)
			# print(selector)
			# elem=source.find_elements_by_css_selector(selector)
			return elem
	except Exception, e:
		return []

	# try:
	# 	elem=source.find_elements_by_css_selector(selector)
	# 	return elem
	# except Exception, e:
	# 	# raise e
	# 	print(str(e))
	# 	print(str(selector))
	# 	return []

def sendkeyto(selector,keycode):
	pass




def openbrowser():
	pass
	global browser
	global ip_proxy_list
	global ip_count
	global count



	chome_options = webdriver.ChromeOptions()  
	#设置不显示图片
	prefs = {"profile.managed_default_content_settings.images":2}
	chome_options.add_experimental_option("prefs",prefs)

	# 通过代理打开网页

	# prox=Proxy()
	# prox.proxy_type=ProxyType.MANUAL
	# prox.http_proxy=ip_proxy

	useproxy=False
	# useproxy=True

	if useproxy:
		#1
		# capabilities=webdriver.DesiredCapabilities.CHROME
		# prox.add_to_capabilities(capabilities)
		# browser = webdriver.Chrome(desired_capabilities=capabilities)

		#2
		chome_options.add_argument(('--proxy-server=http://' + ip_proxy))  
		# os.environ["webdriver.chrome.driver"] = chromedriver  
		browser = webdriver.Chrome(chrome_options=chome_options)  
	else:
		browser = webdriver.Chrome(chrome_options=chome_options)



	# browser.implicitly_wait(20)
	# browser.set_script_timeout(20)
	browser.set_page_load_timeout(60)
	try:
		# browser = webdriver.Chrome(desired_capabilities=capabilities)
		browser.get(openurlstring)
	except Exception, e:
		# raise e
		
		# count-=1

		browser.quit()
	# 确认没问题 并做网络缓冲
	# logging.info(u'browser.title:')
	# logging.info(browser.title)

	# time.sleep(20)

	time.sleep(2)
	# time.sleep(1)


	# # weibo_top_public
	# weibo_top_public=getelements(browser,'.help_link .ico_service')
	# # weibo_top_public = browser.find_elements_by_css_selector('.help_link .ico_service')
	# # print weibo_top_public
	# if len(weibo_top_public)<1:
	# 	closebrowser()
	# if len(browser.title)<3:
	# 	closebrowser()
	# time.sleep(1)

	# browser.save_screenshot("s.weibo.com.png")

def closebrowser():
	pass
	global browser
	global ip_count
	# 关闭chrome 重新换IP代理
	# browser.close()
	browser.quit()
	openbrowser()
	ip_count+=1



def dealwithurl(urlstring):
	rr = urlparse.urlparse(urlstring)
	new_url_list=[]
	new_query=[]
	for x in rr:
		new_url_list.append(x)


	url_query_list=new_url_list[4].split('&')
	for param in url_query_list:
		paramlist=param.split('=')

		if len(paramlist)==2:
			param_key=paramlist[0]
			param_value=paramlist[1]

			#kuaishang
			if 'kuaishang' in urlstring:
				print('kuaishang')
				if not('did' in param_key) and not('sid' in param_key) and not('cas' in param_key) and not('fi' in param_key):
					param_value=''
				else:
					new_query.append(param_key+'='+param_value)
			# chatpre.aspx 网 zoo
			if 'hatpre' in urlstring:
				if not('id' == param_key):
					param_value=''
				else:
					new_query.append(param_key+'='+param_value)

			# 53kf.com
			if '53kf.' in urlstring:
				if not('arg' == param_key):
					param_value=''
				else:
					new_query.append(param_key+'='+param_value)
			#qiao.baidu.com
			if 'qiao.baidu.com' in urlstring:
				if not('siteid' == param_key):
					param_value=''
				else:
					new_query.append(param_key+'='+param_value)


	new_url_list[4]='&'.join(new_query)

	msgstring = urlparse.urlunparse(new_url_list)
	return msgstring
	

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


	url_id=0

	# 关键词列表是否循环完毕
	if len(keywordlist)<=count:
		# time.sleep(30)
		ip_count+=1
		time.sleep(10)
		try:
			# 关闭所有窗口
			
			browser.close()

		except Exception, e:
			# raise e
			# print(str(e))
			pass
		
		time.sleep(30)

		pass
		count=0
		msgstring=keywordlist[count]['adurl']
		url_id=keywordlist[count]['id']
	else:
		# 获取下一个关键词
		msgstring=keywordlist[count]['adurl']
		url_id=keywordlist[count]['id']

	count+=1
	# print count
	# print '\n'
	# print '\n'

	# time.sleep(0.5)


	# 打开浏览器
	# a=urllib.quote(urllib.quote(msgstring))
	# openurlstring='http://www.baidu.com/s?wd='+msgstring+'&rsv_spt=1&issp=1&f=3&rsv_bp=0&rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_enter=1&rsv_sug3=8&rsv_sug1=6&rsv_sug7=100&rsv_sug2=0&prefixsug=shaoer&rsp=0&inputT=2051&rsv_sug4=12425'
	openurlstring=msgstring
	openbrowser()



	print('real web url:')
	print(msgstring)

	# https://my.oschina.net/guol/blog/95699
	domainurl=urlparse.urlparse(msgstring).netloc
	domainurl=domainurl.replace('www.','')

	print('domain:')
	print(domainurl)
	# time.sleep(0.5)
	# time.sleep(1)

	# # 寻找验证码代码

	# 该页面向下滑动，获取ajax内容

	# 寻找搜索框，进行下一个关键词搜索

	try:
		htmltitle=browser.title
	except Exception, e:
		# raise e
		htmltitle=''
	print(htmltitle)
	# 打印关键词
	# print msgstring
	print('url_id')
	print(url_id)

	time.sleep(5)

	shangwutong=[]
	cur = conn.cursor()

	# 默认有js函数
	ishaveopenjsfunction=1
	# 默认有Href
	ishavehref=1

	try:
		browser.execute_script('openZoosUrl();')
	except Exception, e:
		ishaveopenjsfunction=0
	print('ishaveopenjsfunction')
	print(ishaveopenjsfunction)
	time.sleep(1)
	if ishaveopenjsfunction==0:
		ad_list=getelements(browser,'a')
		# time.sleep(1)
		for url in ad_list:
			href_text=str(url.get_attribute('title'))+str(url.text)
			click_url=str(url.get_attribute('href'))+str(url.get_attribute('onclick'))
			# print('a')
			


			# if click_url!=None:
			# 	if 'open' in click_url:
			# 		try:
			# 			url.click()

			# 			try:
			# 				alert = browser.switch_to_alert()
			# 				alert.accept()
			# 			except Exception, e:
			# 				# raise e
			# 				pass
			# 				print('no alert ')

			# 		except Exception, e:
			# 			print('cant click')
			# 			print(str(e))

			if href_text!=None:
				if '免费' in href_text or '回复' in href_text or '咨询' in href_text or '提问' in href_text :
					try:
						print(href_text.encode('gbk'))
						url.click()

						try:
							alert = browser.switch_to_alert()
							alert.accept()
						except Exception, e:
							# raise e
							pass
							print('no alert ')
						break
					except Exception, e:
						print('cant click')
						print(str(e))
				else:
					ishavehref=0

			# time.sleep(2)
			# click_url=url.get_attribute('onclick')
	print('ishavehref')
	print(ishavehref)
	print(1)
	if ishavehref==0:
		div_list=getelements(browser,'button')
		for elem in div_list:
			title_text=str(elem.get_attribute('title'))+str(elem.text)
			# print(title_text)
			if title_text!=None:
				if '免费' in title_text or '回复' in title_text or '咨询' in title_text or '提问' in title_text :
					try:
						elem.click()
						break
					except Exception, e:
						# raise e
						print('cant click')
						print(str(e))
	# print('time.sleep(5)')
	# time.sleep(5)
	print('start to craw chat window')
	# 统一在此抓取地址
	handles = browser.window_handles
	time.sleep(5)

	for hnumber in xrange(0,len(handles)):
		print('hnumber')
		print(hnumber)
		browser.switch_to_window(handles[hnumber])

		# time.sleep(1)
		print(' js.current_url  ')
		newwindowurl=browser.current_url
		print(newwindowurl)

		thishref=newwindowurl
		time.sleep(1)

		ifiswellknow=False
		wellknowwebsite=['baidu.com','alicdn.c','1688.c','qq.com','taobao.com','tmall.com','gov.cn','amazon.cn','jd.com','javascript','cnzz.com','bshare.cn','nuomi.com','51.la','weibo.com','dwz.cn']
		for x in wellknowwebsite:
			if (x in thishref):
				ifiswellknow=True
				break
		print('ifiswellknow')
		print(ifiswellknow)
		if not(ifiswellknow):

			# thishrefdomainurl=urlparse.urlparse(thishref).netloc
			# thishrefdomainurl=thishrefdomainurl.replace('www.','')
			# if thishrefdomainurl!='' and thishrefdomainurl!=domainurl:
			# if thishrefdomainurl!='' :
			if thishref!='' :
				pass
				print('first chat url:')
				print(thishref)

				#判断  是否包含 chat im. 等特定聊天标志

				ischat=False
				chatsign=['chat','CHAT','Chat','/im.','/IM.','/Im.','client','call','kefu','tel']
				for x in chatsign:
					if (x in thishref):
						ischat=True
						break

				if ischat:
					print(url_id)
					print('real chat url:')
					print(thishref)

					new_thishref=dealwithurl(thishref)

					# url_id  这回导致多次更新
					sqli="update ad set   title='"+htmltitle+"',isdealwith=1, chaturl='"+new_thishref +"' where id ="+str(url_id)
					print(sqli)
					print(cur.execute(sqli))
					print(conn.commit())
					# cur.close()
					# conn.close()
					break
			else:
				pass

				# if thishrefdomainurl=='javascript:':
					# url.click()
				# 	# return False
				print('chat url not found')

		# print(domainurl)

		# if url.get_attribute('onclick'):
		# 	# url.click()




	# if len(handles)>1:
	# 	time.sleep(0.2)
	# 	browser.switch_to_window(handles[1]) #切换回百度窗口
	# 	time.sleep(0.2)
	# 	print(' js.current_url  ')
	# 	newwindowurl=browser.current_url
	# 	print(newwindowurl)
	# 	# url_id  这回导致多次更新
	# 	sqli="update ad set  title='"+htmltitle+"',isdealwith=1, chaturl='"+newwindowurl +"' where id ="+str(url_id)
	# 	print(sqli)
	# 	print(cur.execute(sqli))
	# 	print(conn.commit())
	# time.sleep(0.5)
	# ActionChains(browser).move_by_offset(400,400).perform()
			

	# browser.find_element_by_css_selector('.code_input .W_inputStp').send_keys(codestr.encode('utf-8'))

	# time.sleep(0.5)


	try:
		pass
	except Exception, e:
		ad_list=[]
		browser.quit()
		raise e
		print(str(e))

		# print wb.text
	cur.close()
	time.sleep(1)
	browser.quit()

while 1:
	try:

		print('\n')
		print('\n')
		print('\n')
		print('\n')
		print('\n')

		print('loop start')
		loop()
		print('loop over')
	except Exception, e:
		# raise e
		print(str(e))

		try:
			browser.quit()
			loop()
		except Exception, e:
			# raise e
			print(str(e))
			pass
		pass
