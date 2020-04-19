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
import os

from pypinyin import lazy_pinyin,pinyin

from user_agent import generate_user_agent, generate_navigator

from selenium.webdriver.common.keys import Keys  

reload(sys)
sys.setdefaultencoding('utf-8')

import requests
import uuid




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
    browserquit()
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
    browserquit()
    return []
    

def browserquit():
	global browser
	global pfile
	try:
		if browser:
			browser.quit()
	except Exception, e:
		# raise e
		
		pass
	
	try:
		if pfile:
			pfile.close()
	except Exception, e:
		# raise e
		pass

	# 不能退，因为没有守护进程
	# exit()


# changeipbycityUNVIP
def changeip(ctname):
  global ip_proxy
  # city=urllib.quote(urllib.quote(ctname))
  # url = "http://webapi.http.zhimacangku.com/getip?num=1&type=1&pro=&city=&yys=0&port=1&time=1&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions="+ctname
  url = "http://tvp.daxiangdaili.com/ip/?tid=558273526620959&num=1&delay=1&area="+ctname+"&foreign=none&exclude_ports=80,22&filter=on"
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
    # browserquit()
    # raise e

  # print('ip_proxy')
  print('new proxy ip::'+ip_proxy)
  return ip_proxy



# # 浏览器设置

# service_args = []
# dcap={}
# #从USER_AGENTS列表中随机选一个浏览器头，伪装浏览器
# uainfo=generate_user_agent(os=('mac','win'))
# print(type(uainfo))
# print(uainfo)

# dcap["phantomjs.page.settings.userAgent"] = (
#   uainfo
# )
# dcap["phantomjs.page.settings.loadImages"] = False


# cityname=''
# ip_proxy=changeip(cityname)
# # IP代理
# proxy = webdriver.Proxy()  
# proxy.proxy_type = ProxyType.MANUAL  
# proxy.http_proxy = ip_proxy
# proxy.add_to_capabilities(dcap)  

# browser = webdriver.PhantomJS(desired_capabilities=dcap,service_args=service_args)

# browser.viewportSize={'width':800,'height':1200} #重要这句！
# browser.maximize_window()

# browser.implicitly_wait(30)
# browser.set_script_timeout(30)
# browser.set_page_load_timeout(40)


# url 数组  组装

# urllist=['http://www.120ask.com/shilu/00jovpnknlwg3h09.html']
urllist=[]

ulistfile=open('./'+'urllist'+'.txt')
ulistfile=codecs.open('./'+'urllist'+'.txt','r','utf-8')

for newurl in ulistfile:
	print(newurl)
	try:
		urlbody=newurl.split('||')
		urllist.append({'url':urlbody[0],'classtext':urlbody[1]})
	except Exception, e:
		# raise e
		print(str(e))



random.shuffle(urllist)



for urlinfo in urllist:
	browserquit()
	try:
		# searchinput=browser.find_element_by_css_selector('#kw')
		# searchinput.send_keys(msgstring)
		# searchinput.send_keys(Keys.DOWN)
		# time.sleep(2)
		browserquit()
		browserquit()
		browserquit()

		url=urlinfo['url']
		classtext=urlinfo['classtext']
		classtext=classtext.replace("[", "");
		classtext=classtext.replace("]", "");
		classtext=classtext.replace("\n", "");



		protocol, s1 = urllib.splittype(url)  
		host, s2=  urllib.splithost(s1)  
		host, port = urllib.splitport(host)  

		print('host')
		print(host)

		print(classtext)
		print(type(classtext))

		# 浏览器设置

		service_args = []
		dcap={}
		#从USER_AGENTS列表中随机选一个浏览器头，伪装浏览器
		uainfo=generate_user_agent(os=('mac','win'))
		print(type(uainfo))
		print(uainfo)

		dcap["phantomjs.page.settings.loadImages"] = False

		#### new ####  是不是还缺头
		# dcap['phantomjs.page.customHeaders.Host'] =host
		dcap['phantomjs.page.customHeaders.User-Agent'] =uainfo
		# dcap['phantomjs.page.customHeaders.Accept-Language'] ='zh-CN,en-US;q=0.7,en;q=0.3'




		# cityname=''
		# ip_proxy=changeip(cityname)
		
		# # IP代理
		# proxy = webdriver.Proxy()  
		# proxy.proxy_type = ProxyType.MANUAL  
		# proxy.http_proxy = ip_proxy
		# proxy.add_to_capabilities(dcap)  

		# service_args=service_args
		# browser = webdriver.PhantomJS(desired_capabilities=dcap)

		# 如果是chrome
		# 浏览器设置 # setting
		chome_options = webdriver.ChromeOptions()
		# 设置中文
		chome_options.add_argument('lang=zh_CN.UTF-8')
		
		#设置不显示图片
		# ,"profile.managed_default_content_settings.javascript":2
		# prefs = {"profile.managed_default_content_settings.images":2}
		prefs = {}
		chome_options.add_experimental_option("prefs",prefs)

		browser = webdriver.Chrome(chrome_options=chome_options)
		#new
		# browser.start_session(dcap) 

		browser.viewportSize={'width':800,'height':1200} #重要这句！
		browser.maximize_window()

		browser.implicitly_wait(30)
		browser.set_script_timeout(30)
		browser.set_page_load_timeout(40)



		print(url)
		browser.get(url)
		time.sleep(1)
		ad_list=[]



		# # 老分类
		# keshistr=browser.find_element_by_css_selector('.cla_ans dl .d1').text
		# keshi_pinyin= lazy_pinyin(keshistr.split(' ')[1].split('-')[0])


		# 新的分类
		
		keshi_pinyin= lazy_pinyin(classtext)

		flodername=''.join(keshi_pinyin)

		print('flodername')
		print(flodername)
		print('flodername')

		if os.path.exists('./'+flodername):
			pass
		else:
			os.makedirs('./'+flodername)



		# print(keshistr.encode('gbk'))
		print(''.join(keshi_pinyin))
		filename=str(uuid.uuid4())
		pfile=codecs.open('./'+flodername+'/'+filename+'.txt','w+','utf-8')

		

		q_list=getelements(browser,'.p_zixunbox p span')
		print(len(q_list))
		contenttext=''
		for qus in q_list:
			try:
				print(qus.text.encode('gbk'))
				sayinfo=qus.text.split('\n')
				if len(sayinfo)!=2:
					sayinfo=qus.text.split(' ')
				# print(sayinfo[0])
				# print('says:')
				# print(sayinfo[1])
				# p_chatliface
				# chat_role=qus.find_element_by_css_selector('.p_chatliface')
				# chat_content=qus.find_element_by_css_selector('.p_chatcont')
				# contenttext=contenttext+chat_role+'||'+chat_content+'\n'
				contenttext=contenttext+sayinfo[0]+'||'+sayinfo[1]+'\n'
				# contenttext=qus.text
				print('***********')
			except Exception, e:
				# raise e
				print(str(e))
				browserquit()
		try:
			pfile.write(contenttext)
		except Exception, e:
			# raise e
			browserquit()
			browserquit()

		
		time.sleep(2)
		# browser.quit()
		# pfile.close()
		# browser.quit()
		browserquit()
		browserquit()


	except Exception, e:
		print(str(e))
		# browser.quit()
		browserquit()
		browserquit()
		browserquit()
		pass
	time.sleep(2)
	browserquit()
	browserquit()
	browserquit()

