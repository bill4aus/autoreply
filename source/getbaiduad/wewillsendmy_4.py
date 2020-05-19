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
# from apscheduler.schedulers.background import BackgroundScheduler
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

from user_agent import generate_user_agent, generate_navigator

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

conn={}
conn= MySQLdb.connect(
        host='127.0.0.1',
        port = 3306,
        user='root',
        passwd='root',
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


cur = conn.cursor()
# and chaturl like '%hatpre.%'
# sqli="select * from ad where chaturl is not null and redundant=0  and id>21475 and id<23000"
# sqli="select * from ad where status=0 and chaturl is not null and redundant=0  and id>23607 and id<26000"

# status=0
# `chaturl` LIKE '%kuaishang%'
# `chaturl` LIKE '%atpre.aspx%'
# chaturl is not null 
# and ismobile=1 不是移动端 也可以做这个业务
# id<100  and

#以前的
pagesize=100
page=18
# pagesize=500
# page=1

# #阿斌的
# # 承接商务通防御 一次性收费 永久防护。总有用的上的时候！加QQ 3566691
# pagesize=400
# page=1



sqli="SELECT * FROM `ad` WHERE  chaturl LIKE '%atpre.aspx%'  and redundant=0 and isuser =0 and exclusive=0  limit "+str(pagesize*(page-1))+","+str(pagesize)
# SELECT * FROM `ad` WHERE status=0 and chaturl is not null and ismobile=1 and redundant=0
count=cur.execute(sqli)
# print(conn.commit())
results = cur.fetchall()   
for r in results:
    # print(type(r))
    # print r[0]
    # print r[3]
    keywords.append({'chaturl':r[6],'id':r[0]})
cur.close()


# http://www.120huaxi.com/chat.php?sText=%E5%BA%95%E9%83%A8%E6%82%AC%E6%B5%AE-%E5%9C%A8%E7%BA%BF%E5%92%A8%E8%AF%A2&ri=656046727&vi=237622837a104ff78cff3bb55affa4b3&dp=http%3A%2F%2Fwww.120huaxi.com%2F%23bd&_d=1498742054747
# http://vip3-kf9.kuaishang.cn/bs/im.htm?cas=56275___699169&fi=64942&dp=http%3A%2F%2Fwww.bjfynjk.com%2Fzt%2Fhospital%2F%23baidu-fynjk-353&_d=1498660538465&


# keywords_bak=[]
count=0

ip_proxy_list=[

]

ip_proxy=''
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




def changeip(cityname):
	global ip_proxy
	cityname=''
	# city=urllib.quote(urllib.quote(ctname))
	# &ports=8080
	url = 'http://tvp.daxiangdaili.com/ip/?tid=556798197808597&num=1&operator=1&area='+cityname+'&delay=1'
	# url = "http://tvp.daxiangdaili.com/ip/?tid=555527369568174&num=1&delay=1&area="+cityname+"&foreign=none&exclude_ports=80,8080,22&filter=on"
	# print(url)
	req = urllib2.Request(url)
	res_data = urllib2.urlopen(req)
	res = res_data.read()
	ip_proxy=res
	print('ip_proxy')
	print(ip_proxy)
	return ip_proxy

	# #new
	# # {"ERRORCODE":"0","RESULT":{"wanIp":"115.209.9.0","proxyport":"23098"}}
	# url = 'http://www.xdaili.cn/ipagent//privateProxy/getDynamicIP/DD2017757426QjI7RV/710612c8fcdd11e6942200163e1a31c0?returnType=2'
	# req = urllib2.Request(url)
	# res_data = urllib2.urlopen(req)
	# res = res_data.read()
	# ip_proxy=res
	# iipp=ip_proxy['RESULT']['wanIp']
	# portport=ip_proxy['RESULT']['proxyport']
	# print('ip_proxy')
	# print(iipp+':'+portport)
	# return iipp+':'+portport


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
	global ip_proxy
	global url_id
	# 通过代理打开网页


	citynamelist=[
	'北京',
	'上海',
	'天津',
	'重庆',
	'深圳',
	'广州',
	'成都',
	'昆明',
	'石家庄',
	'沈阳',
	'长春',
	'哈尔滨',
	'呼和浩特',
	'乌鲁木齐 ',
	'兰州',
	'西宁',
	'武汉',
	'长沙',
	'南京',
	'南昌',
	'太原',
	'济南',
	'合肥',
	'杭州',
	'福州',
	'银川',
	'南宁',
	'青岛',
	'珠海',
	'贵阳',
	'无锡',
	'东莞',
	'厦门',
	'苏州',
	]

	# ip_proxy='123.145.14.12:8889'

	# useproxy=False
	useproxy=True



	# service_args = ['--proxy='+ip_proxy]
	service_args = []
	dcap={}

	# chome_options = webdriver.ChromeOptions()  
	# #设置不显示图片
	# prefs = {"profile.managed_default_content_settings.images":2}
	# chome_options.add_experimental_option("prefs",prefs)
	

	if useproxy:

		random.shuffle(citynamelist)
		cityname=citynamelist[0]
		print(cityname)

		if ip_proxy=='':
			cityname=''
			ip_proxy=changeip(cityname)
			# ip_proxy='110.87.25.106:808'

		print('ip_proxy')
		print(ip_proxy)

		if 'ERROR' in ip_proxy:
			print('change city name')
			print('change city name')
			print('change city name')
			print('change city name')
			# ip_count+=1

			# 没有代理就重新打开刚才的网页
			if count==0:
				pass
			else:
				count-=1
			ip_proxy=''
			loop()

		#2
		# chome_options.add_argument(('--proxy-server=http://' + ip_proxy))  
		# # os.environ["webdriver.chrome.driver"] = chromedriver  
		# browser = webdriver.Chrome(chrome_options=chome_options)  


		# IP代理
		proxy = webdriver.Proxy()  
		proxy.proxy_type = ProxyType.MANUAL  
		proxy.http_proxy = ip_proxy
		proxy.add_to_capabilities(dcap)  

		cityname=''
		ip_proxy=changeip(cityname)
		# ip_proxy=''
		# ip_proxy='1.82.216.135:80'
		# ip_proxy='58.59.68.91:9797'

		# 设置代理


	else:
		# browser = webdriver.Chrome(chrome_options=chome_options)
		pass



	################ phantomjs ################
	
	#从USER_AGENTS列表中随机选一个浏览器头，伪装浏览器
	uainfo=generate_user_agent(os=('mac','win'))
	print(type(uainfo))
	print(uainfo)

	# dcap["phantomjs.page.settings.userAgent"] = (
	#   uainfo
	# )
	# dcap["phantomjs.page.settings.acceptLanguage"]='zh-CN,en-US;q=0.7,en;q=0.3'
	# dcap["phantomjs.page.settings.acceptEncoding"]='utf-8'
	dcap["phantomjs.page.settings.loadImages"] = False
	# dcap["phantomjs.page.settings.loadImages"] = True

	#### new ####
	# 最重要的host字段，如果没有host值，http1.1协议会认为这是一个不规范的请求从而直接丢弃。
	# 'Accept-Encoding':'gzip, deflate',#会乱码  看实际情况决定是否自动解压
	# 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
	headers = {
	# 'Accept': '*/*',
	'Accept-Language': 'zh-CN,zh;q=0.8',
	# 'Cache-Control': 'max-age=0',
	# 'Connection': 'keep-alive',
	'User-Agent': uainfo,#这种修改 UA 也有效
	'Referer':'https://www.baidu.com/s?wd=%E5%8C%BB%E9%99%A2&rsv_spt=1&rsv_iqid=0xd9a7643a000377cd&issp=1&f=8&rsv_bp=0&rsv_idx=2&ie=utf-8&rqlang=&tn=baiduhome_pg&ch=&rsv_enter=1&inputT=1602'
	}

	for key, value in headers.iteritems():
		dcap['phantomjs.page.customHeaders.{}'.format(key)] = value


	print(dcap)
	# service_args=service_args
	#liunx
	browser = webdriver.PhantomJS(desired_capabilities=dcap)
	#windows
	# browser = webdriver.PhantomJS(desired_capabilities=dcap,executable_path="D:\weibo\node_modules\phantomjs\lib\phantom\phantomjs.exe")

	

	browser.viewportSize={'width':824,'height':2200} #重要这句！
	browser.maximize_window()

	# chome_options.add_argument(('--proxy-server=http://' + ip_proxy))  
	# browser = webdriver.Chrome(chrome_options=chome_options)  


	browser.implicitly_wait(30)
	browser.set_script_timeout(30)
	browser.set_page_load_timeout(40)


	############### phantomjs ################


	browser.delete_all_cookies()
	browser.delete_all_cookies()
	# browser.implicitly_wait(20)
	# browser.set_script_timeout(20)
	browser.set_page_load_timeout(60)
	try:
		# browser = webdriver.Chrome(desired_capabilities=capabilities)
		browser.get(openurlstring)
	except Exception, e:
		# raise e
		
		# count-=1

		count+=1

		print('timeout')
		print('timeout')
		print('timeout')
		print('timeout')
		print('timeout')
		print('url_id')
		print(url_id)

		# keywordlist.append()
		keywordlist.append({'chaturl':openurlstring,'id':url_id})

		browser.quit()
	# 确认没问题 并做网络缓冲
	# logging.info(u'browser.title:')
	# logging.info(browser.title)

	# time.sleep(20)

	time.sleep(2)
	# time.sleep(1)

	# browser.save_screenshot("/home/wwwroot/default/ad.png")
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



	saylist=[
	# 'hi~你好',
	# '你好',
	# '医生你好',
	# '你好啊',
	# '承接商务通防御 一次性收费 永久防护。总有用的上的时候！加QQ 3566691',
	# '承接商务通防御 一次性收费 永久防护。总有用的上的时候！加QQ 1556901',
	# '你好，真人骚扰对手商务通，防屏蔽，提升竞争软实力，费用低廉，可测试体验。联系QQ:1043550026',
	# '对话框被骚扰？我们帮您还击！真人刷对手商务通，安全放心，防屏蔽。费用低廉,可测试体验。联系：QQ 1043550026',
	# '亲，你好，最新独家产品，商务通恶聊反击，帮您提高竞争力，可免费测试体验，欢迎咨询 QQ1043550026',
	# '代刷商务通，帮你提高竞争力，防屏蔽，防验证码，安全放心，费用低廉。可免费测试体验。详情咨询：QQ1043550026',
	'代刷商务通，破三防，真实、专业，安全放心！可免费测试体验 。联系QQ 1043550026',
	'被恶意聊天影响工作？我们帮您还击，短时间促成和谈！破三防，真实、专业，安全放心。可免费测试体验。咨询QQ 1043550026',
	]


	if istest:
		syastring='你好'
	else:
		# syastring=saylist[0]
		syastring=random.choice(saylist)
	# syastring='hello~'

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
		
		time.sleep(60)

		pass
		stop 
		# 通过 未命名 变量 报错 退出


		# count=0
		# msgstring=keywordlist[count]['chaturl']
		# url_id=keywordlist[count]['id']
	else:
		# 获取下一个关键词
		msgstring=keywordlist[count]['chaturl']
		url_id=keywordlist[count]['id']

	
	# 打开浏览器
	# a=urllib.quote(urllib.quote(msgstring))
	
	if istest:
		# msgstring='http://plt.zoosnet.net/LR/Chatpre.aspx?id=PLT34973142&cid=1498654119737755989143&lng=cn&sid=1498654119737755989143&p=http%3A//www.gcw028.com/yiyuangk/11260.html%3FK-PC-E-gcH-BD5&rf1=http%3A//www.gcw028.com/yiyuangk/11260&rf2=.html%3FK-PC-E-gcH-BD5%26WebSh'
		msgstring='https://www.baidu.com/s?wd=ip&rsv_spt=1&rsv_iqid=0xc995f90f0000e7f4&issp=1&f=8&rsv_bp=0&rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_enter=1&rsv_sug3=3&rsv_sug1=3&rsv_sug7=101&rsv_sug2=0&inputT=627&rsv_sug4=1300'
	# msgstring='http://plt.zoosnet.net/LR/Chatpre.aspx?id=PLT34973142&cid=1498654119737755989143&lng=cn&sid=1498654119737755989143&p=http%3A//www.gcw028.com/yiyuangk/11260.html%3FK-PC-E-gcH-BD5&rf1=http%3A//www.gcw028.com/yiyuangk/11260&rf2=.html%3FK-PC-E-gcH-BD5%26WebSh'
	
	
	rr = urlparse.urlparse(msgstring)
	# print (rr) 
	# print (rr.port)
	# print (rr.hostname)  
	# print (rr.query)
	new_url_list=[]
	new_query=[]

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

			# 百度 IP 测试 需要IP关键词
	 		if 'wd' in param_key:
				param_value='ip'

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


	new_url_list[4]='&'.join(new_query)

	msgstring = urlparse.urlunparse(new_url_list)
	
	
	print(msgstring)

	openurlstring=msgstring
	# openurlstring='http://jngb120.zoossoft.com/LR/Chatpre.aspx?id=LGW31671888'
	openbrowser()


	# time.sleep(30)

	print('url_id')
	print(url_id)
	print('allurl left:')
	print(len(keywordlist)-count)

	browser.save_screenshot("/home/wwwroot/default/ad.png")
	time.sleep(1)
	# time.sleep(4)
	# # 寻找验证码代码
	# 该页面向下滑动，获取ajax内容
	# 寻找搜索框，进行下一个关键词搜索

	# inputelems=getelements(browser,'input')
	# buttonelems=getelements(browser,'button')

	# cur = conn.cursor()
	try:
		# # inputelems=getelements(browser,'input')
		# # print(inputelems)
		# # for inputelem in inputelems:
		# # 	pass
		# # 	print(inputelem.get_attribute('name'))
		# # 	print(inputelem.get_attribute('style'))
		# 	# inputelem.send_keys(syastring)
		# # browser.send_keys(syastring)
		# # pageagref.send_keys(Keys.ENTER)


		# # actelem=browser.switch_to.active_element
		# # print(actelem.get_attribute('id'))
		# # print(actelem.get_attribute('name'))
		# # print(actelem.get_attribute('class'))
		# # print(actelem.get_attribute('id'))
		# # actelem.click()
		# # time.sleep(0.5)
		# # actelem.click()
		# # actelem.send_keys(syastring.decode('utf-8'))
		# # actelem.click()
		# # # actelem.send_keys(Keys.ENTER)

		# framebodylist=getelements(browser,'iframe body')
		# print('framebodylist')
		# print(framebodylist)


		# framelist=getelements(browser,'iframe')
		# print('len(framelist)')
		# print(len(framelist))
		# iframelen=len(framelist)

		# iframeeditor=None
		# textclassfind=u'ext'
		# textclasshidden=u'idden'


		# for thisiframe in framelist:
		# 	# print(thisiframe)
		# 	# print(thisiframe.get_attribute('id'))
		# 	iframeid=thisiframe.get_attribute('id')
		# 	iframeclass=thisiframe.get_attribute('class')
		# 	# iframestyle=thisiframe.get_attribute('style')


		# 	print(iframeid)
		# 	print(iframeclass)

		# 	# if u'none' in iframestyle:
		# 	# 	pass
		# 	# 	iframelen=iframelen-1
			

		# 	# print(iframeid=='')
		# 	if textclassfind in iframeid:
		# 		iframeeditor=thisiframe
		# 		print('ext in this iframe')
		# 		break

		# 	if iframeeditor==None and (textclassfind in iframeclass):
		# 		iframeeditor=thisiframe
		# 		print('ext in this iframe')
		# 		break

		# 	if iframeeditor==None and (textclasshidden in iframeclass  or textclasshidden in iframeid):
		# 		iframelen-=1
		# 		print('hidden iframe')
		# 		break
			


		# # print(iframeeditor)
		# if iframelen>0:

		# 	if iframeeditor==None:
		# 		# iframeeditor=framelist[0]
		# 		iframeeditor='FreeTextBox1_editor'

		# 	# iframeid=iframeeditor.get_attribute('id')
		# 	# print('iframeid')
		# 	# print(iframeid)
		# 	print(iframeeditor)
		# 	# browser.switch_to.frame(iframeid) #'FreeTextBox1_editor'
		# 	browser.switch_to.frame(iframeeditor) #'FreeTextBox1_editor'
		# 	browser.find_element_by_tag_name('body').send_keys(syastring.decode('utf-8'))

		# 	if istest:
		# 		pass
		# 		print('test submit')
		# 	else:
		# 		browser.find_element_by_tag_name('body').send_keys(Keys.ENTER)
		# else:

		# 	actelem=browser.switch_to.active_element
		# 	actelem.click()
		# 	time.sleep(0.2)
		# 	actelem.click()
		# 	actelem.send_keys(syastring.decode('utf-8'))
		# 	actelem.click()
		# 	if istest:
		# 		pass
		# 		print('test submit')
		# 	else:			
		# 		actelem.send_keys(Keys.ENTER)



		# # try:
		# # 	browser.switch_to.active_element.send_keys(syastring.decode('utf-8'))
		# # except Exception, e:
		# # 	# raise e
		# # 	browser.switch_to.frame('FreeTextBox1_editor')
		# # 	browser.find_element_by_tag_name('body').send_keys(syastring.decode('utf-8'))




		# # # url_id  更新是否发送的字段  发送次数
		# # sqli="update ad set  isdealwith=1, chaturl='"+thishref +"' where id ="+str(url_id)
		# # print(sqli)
		# # print(cur.execute(sqli))
		# # print(conn.commit())
		# # # cur.close()
		# # # conn.close()






		#python
		# 找到iframe里面有body div 输入 editor 等字样  
		iframehtml=browser.find_elements_by_xpath("//iframe")
		for x in iframehtml:
			try:
				pass
				print('xxxxxxx')
				inputhtml=x.find_element_by_xpath("//body[contains(text(), 在此输入)]")
				print(inputhtml)
				print('inputhtml.text')
				print(inputhtml.text)
				# if inputhtml!=None:
				# print('x.text')
				# print(x.text)
				print(x.get_attribute('id'))
				print(x.get_attribute('class'))
				print(inputhtml.text)
				# inputhtml.send_keys(syastring.decode('utf-8'))
				set_wyswyg_js = 'document.getElementById("'+x.get_attribute('id')+'").contentWindow.document.body.click();'
				set_wyswyg_js = set_wyswyg_js+'document.getElementById("'+x.get_attribute('id')+'").contentWindow.document.body.innerHTML="%s"' %(syastring)
				# set_wyswyg_js = set_wyswyg_js+';document.getElementById("FreeTextBox1_editor").contentWindow.document.body.innerHTML="%s"' %(syastring)
				browser.execute_script(set_wyswyg_js)

				#send
				inputhtml.send_keys(Keys.ENTER)

			except Exception, e:
				# raise e
				print(str(e))
				pass
			
		edlist=browser.find_elements_by_css_selector('#ksEditInstance')
		print(len(edlist))
		if len(edlist)>0:
			browser.find_element_by_css_selector('#ksEditInstance').send_keys(syastring.decode('utf-8'))
			time.sleep(1)
			browser.find_element_by_css_selector('#ksEditInstance').send_keys(Keys.ENTER)


		try:
			set_wyswyg_js = 'document.getElementById("ksEditInstance").innerHTML="%s"' %(syastring)
			browser.execute_script(set_wyswyg_js)
			browser.find_element_by_css_selector('#ksEditInstance').send_keys(Keys.ENTER)
		except Exception, e:
			# raise e
			print(str(e))
			pass


			
		
		# inputhtml=browser.find_element_by_xpath("//body[contains(text(), 在此输入)]")
		# # inputhtml=browser.find_element_by_xpath("//div[contains(text(), 发送)]")
		# print('inputhtml')
		# print(inputhtml)
		# print('inputhtml.text')
		# print(inputhtml.text)
		# print(inputhtml.get_attribute('id'))
		# print(inputhtml.get_attribute('class'))


		
		# onclick
		# User_Send()
		iframehtml=browser.find_elements_by_xpath("//*[contains(@onclick, 'end')]")
		for x in iframehtml:
			try:
				print('x.text')
				print(x.text)
				print(x.get_attribute('onclick'))
				print(x.get_attribute('id'))
				x.click()
			except Exception, e:
				# raise e
				print(str(e))
				pass
			

		# 找到send()函数名，直接js调用
		# 找到发送按钮，点击
		# 找到href="javascript:void(0)"的按钮，依次点击

		time.sleep(1)
		# get_screenshot_as_file
		# browser.save_screenshot("ad.png")
		browser.save_screenshot("/home/wwwroot/default/ad.png")
		count+=1

		if istest:
			time.sleep(5)
		else:
			time.sleep(1.2)


	except Exception, e:
		# browser.quit()
		# raise e
		#出错就要跳过，不然卡在一个url_id上
		count+=1
		print(str(e))

		# print wb.text
	# cur.close()
	# time.sleep(1)
	browser.quit()


# time.sleep(60*12)
while 1:
	try:
		print('loop start')
		loop()
		print('loop over')
	except Exception, e:
		# raise e
		# print(str(e))
		# loop()
		pass
