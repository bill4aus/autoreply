#!/opt/anaconda/bin/python
#coding:utf-8
# -*- coding: utf-8 -*-


# 导入工具
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException 
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.proxy import ProxyType 
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



# changeipbycityUNVIP
def changeip(ctname):
  global ip_proxy
  # city=urllib.quote(urllib.quote(ctname))
  # 555527369568174
  url = "http://tvp.daxiangdaili.com/ip/?tid=556742179509367&num=1&delay=1&area="+ctname+"&foreign=none&exclude_ports=80,22&filter=on"
  # print(url)
  print('get ip proxy')
  # time.sleep(0.1)
  try:
    req = urllib2.Request(url)
    res_data = urllib2.urlopen(req)
    res = res_data.read()
    ip_proxy=res
  except Exception, e:
    
    ip_proxy=''
    pass
    print('browser.quit() changeip')
    # browser.quit()
    print(str(e))
    # loop()
    print('\n')
    print('\n')
    print('\n')
    # raise e

  # print('ip_proxy')
  print('new proxy ip::'+ip_proxy)
  return ip_proxy





# # 浏览器设置

# service_args = []
# dcap={}
# #从USER_AGENTS列表中随机选一个浏览器头，伪装浏览器
# uainfo=generate_user_agent()
# print(type(uainfo))
# print(uainfo)

# dcap["phantomjs.page.settings.userAgent"] = (
#   uainfo
# )
# dcap["phantomjs.page.settings.loadImages"] = False

# browser = webdriver.PhantomJS(desired_capabilities=dcap,service_args=service_args)

# browser.viewportSize={'width':800,'height':1200} #重要这句！
# browser.maximize_window()

# browser.implicitly_wait(30)
# browser.set_script_timeout(30)
# browser.set_page_load_timeout(40)


# url 数组  组装

urllist=[]

# 数据量大
# # neike
# for talkid in range(getnumberpage_start,9395):
# 	urlstr='http://www.120ask.com/shilu/online/1?p='+str(talkid)
# 	urllist.append(urlstr)
# # waike
# for talkid in range(getnumberpage_start,5263):
# 	urlstr='http://www.120ask.com/shilu/online/2?p='+str(talkid)
# 	urllist.append(urlstr)
# # fuke
# for talkid in range(getnumberpage_start,11235):
# 	urlstr='http://www.120ask.com/shilu/online/3?p='+str(talkid)
# 	urllist.append(urlstr)
# # erke
# for talkid in range(getnumberpage_start,5395):
# 	urlstr='http://www.120ask.com/shilu/online/4?p='+str(talkid)
# 	urllist.append(urlstr)
# # zhongyike
# for talkid in range(getnumberpage_start,1729):
# 	urlstr='http://www.120ask.com/shilu/online/51?p='+str(talkid)
# 	urllist.append(urlstr)
# # wuguanke
# for talkid in range(getnumberpage_start,2069):
# 	urlstr='http://www.120ask.com/shilu/online/60?p='+str(talkid)
# 	urllist.append(urlstr)
# # pifuke
# for talkid in range(getnumberpage_start,3617):
# 	urlstr='http://www.120ask.com/shilu/online/7?p='+str(talkid)
# 	urllist.append(urlstr)
# # yangsheng
# for talkid in range(getnumberpage_start,218):
# 	urlstr='http://www.120ask.com/shilu/online/100?p='+str(talkid)
# 	urllist.append(urlstr)
# # shiliao
# for talkid in range(getnumberpage_start,213):
# 	urlstr='http://www.120ask.com/shilu/online/101?p='+str(talkid)
# 	urllist.append(urlstr)


# 数据全面 量少  
# 最高500页
npage=1 #500 
perpagenumber=500#每次翻页3页


getnumberpage_start=(npage-1)*perpagenumber #500 
getnumberpage=npage*perpagenumber #500 

if getnumberpage_start==0:
	getnumberpage_start=1


# 男科相关
for talkid in range(getnumberpage_start,getnumberpage):
	urlstr='http://www.120ask.com/shilu/list/31?p='+str(talkid)
	urllist.append(urlstr)
for talkid in range(getnumberpage_start,getnumberpage):
	urlstr='http://www.120ask.com/shilu/list/239?p='+str(talkid)
	urllist.append(urlstr)
for talkid in range(getnumberpage_start,getnumberpage):
	urlstr='http://www.120ask.com/shilu/list/240?p='+str(talkid)
	urllist.append(urlstr)
for talkid in range(getnumberpage_start,getnumberpage):
	urlstr='http://www.120ask.com/shilu/list/241?p='+str(talkid)
	urllist.append(urlstr)
for talkid in range(getnumberpage_start,getnumberpage):
	urlstr='http://www.120ask.com/shilu/list/463?p='+str(talkid)
	urllist.append(urlstr)




# neike
for talkid in range(getnumberpage_start,getnumberpage):
	urlstr='http://www.120ask.com/shilu/list/1?p='+str(talkid)
	urllist.append(urlstr)
# waike
for talkid in range(getnumberpage_start,getnumberpage):
	urlstr='http://www.120ask.com/shilu/list/2?p='+str(talkid)
	urllist.append(urlstr)
# fuke
for talkid in range(getnumberpage_start,getnumberpage):
	urlstr='http://www.120ask.com/shilu/list/3?p='+str(talkid)
	urllist.append(urlstr)
# erke
for talkid in range(getnumberpage_start,getnumberpage):
	urlstr='http://www.120ask.com/shilu/list/4?p='+str(talkid)
	urllist.append(urlstr)
# pifuke
for talkid in range(getnumberpage_start,getnumberpage):
	urlstr='http://www.120ask.com/shilu/list/7?p='+str(talkid)
	urllist.append(urlstr)
# fuke
for talkid in range(getnumberpage_start,getnumberpage):
	urlstr='http://www.120ask.com/shilu/list/40?p='+str(talkid)
	urllist.append(urlstr)
# zhongyike
for talkid in range(getnumberpage_start,getnumberpage):
	urlstr='http://www.120ask.com/shilu/list/51?p='+str(talkid)
	urllist.append(urlstr)
# xingbing
for talkid in range(getnumberpage_start,getnumberpage):
	urlstr='http://www.120ask.com/shilu/list/59?p='+str(talkid)
	urllist.append(urlstr)# wuguanke
for talkid in range(getnumberpage_start,getnumberpage):
	urlstr='http://www.120ask.com/shilu/list/60?p='+str(talkid)
	urllist.append(urlstr)
# chuanranke
for talkid in range(getnumberpage_start,getnumberpage):
	urlstr='http://www.120ask.com/shilu/list/63?p='+str(talkid)
	urllist.append(urlstr)
# xinlijiankang
for talkid in range(getnumberpage_start,getnumberpage):
	urlstr='http://www.120ask.com/shilu/list/67?p='+str(talkid)
	urllist.append(urlstr)
# zhengxingmeirong
for talkid in range(getnumberpage_start,getnumberpage):
	urlstr='http://www.120ask.com/shilu/list/68?p='+str(talkid)
	urllist.append(urlstr)
# zhongliuke
for talkid in range(getnumberpage_start,getnumberpage):
	urlstr='http://www.120ask.com/shilu/list/69?p='+str(talkid)
	urllist.append(urlstr)
# baojian yangsheng
for talkid in range(getnumberpage_start,getnumberpage):
	urlstr='http://www.120ask.com/shilu/list/100?p='+str(talkid)
	urllist.append(urlstr)
# yaoping
for talkid in range(getnumberpage_start,getnumberpage):
	urlstr='http://www.120ask.com/shilu/list/203?p='+str(talkid)
	urllist.append(urlstr)
# zinv jiaoyu
for talkid in range(getnumberpage_start,getnumberpage):
	urlstr='http://www.120ask.com/shilu/list/104?p='+str(talkid)
	urllist.append(urlstr)
# jiaju huanjing
for talkid in range(getnumberpage_start,getnumberpage):
	urlstr='http://www.120ask.com/shilu/list/121?p='+str(talkid)
	urllist.append(urlstr)
# yichuan 
for talkid in range(getnumberpage_start,getnumberpage):
	urlstr='http://www.120ask.com/shilu/list/234?p='+str(talkid)
	urllist.append(urlstr)
# qita 
for talkid in range(getnumberpage_start,getnumberpage):
	urlstr='http://www.120ask.com/shilu/list/94?p='+str(talkid)
	urllist.append(urlstr)

pfile=open('urllist.txt','a+')



for url in urllist:
	try:
		# searchinput=browser.find_element_by_css_selector('#kw')
		# searchinput.send_keys(msgstring)
		# searchinput.send_keys(Keys.DOWN)

		# 浏览器设置

		# cityname=''
		# ip_proxy=changeip(cityname)

		service_args = []
		dcap={}
		#从USER_AGENTS列表中随机选一个浏览器头，伪装浏览器
		uainfo=generate_user_agent()
		print(type(uainfo))
		print(uainfo)

		# dcap["phantomjs.page.settings.userAgent"] = (
		#   uainfo
		# )
		# dcap["phantomjs.page.settings.loadImages"] = False

		# # IP代理
		# proxy = webdriver.Proxy()  
		# proxy.proxy_type = ProxyType.MANUAL  
		# proxy.http_proxy = ip_proxy
		# proxy.add_to_capabilities(dcap)  

		# browser = webdriver.PhantomJS(desired_capabilities=dcap,service_args=service_args)

		chome_options = webdriver.ChromeOptions()
		# 设置中文
		chome_options.add_argument('lang=zh_CN.UTF-8')
		
		#设置不显示图片
		# ,"profile.managed_default_content_settings.javascript":2
		# prefs = {"profile.managed_default_content_settings.images":2}
		prefs = {}
		chome_options.add_experimental_option("prefs",prefs)

		browser = webdriver.Chrome(chrome_options=chome_options)

		browser.viewportSize={'width':800,'height':1200} #重要这句！
		browser.maximize_window()

		browser.implicitly_wait(30)
		browser.set_script_timeout(30)
		browser.set_page_load_timeout(40)




		print(url)
		browser.get(url)
		time.sleep(15)
		ad_list=[]
		try:
			q_list=getelements(browser,'.cla_left .cla_list li')
			time.sleep(5)
		except Exception, e:
			pass
			print(str(e))
			q_list=[]
			browser.quit()

		print(len(q_list))
		contenttext=''
		for qus in q_list:
			try:
				print(qus)
				hrefstr=qus.find_element_by_css_selector('a').get_attribute('href')
				classtext=qus.find_element_by_css_selector('em').text
				classtext=classtext.replace("[", "");
				classtext=classtext.replace("]", "");
				# hrefstr='http://www.120ask.com'+hrefstr
				# hrefstr='http://www.120ask.com'+hrefstr
				print(hrefstr)
				contenttext=contenttext+hrefstr+'||'+classtext+'\n'
			except Exception, e:
				# raise e
				print(str(e))
				browser.quit()

		pfile.write(contenttext)
		time.sleep(2)
		browser.quit()


	except Exception, e:
		print(str(e))
		# browser.quit()
		browser.quit()
		pass
	time.sleep(15)

pfile.close()
browser.quit()
exit()