#!/usr/bin/env python
#coding:utf-8
# -*- coding: utf-8 -*-


# 导入工具
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException 
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.proxy import ProxyType 
import time
import datetime
# from bs4 import BeautifulSoup
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
from selenium.webdriver.common.keys import Keys	
from PIL import Image	
from user_agent import generate_user_agent, generate_navigator

from supportfunction import changeip
from supportfunction import genewechatid
from supportfunction import genercookies
from supportfunction import geneparamviandtk
from supportfunction import geneurlrouter

import re
import urlparse

reload(sys)
sys.setdefaultencoding('utf-8')

import requests
import platform

from supportfunction import keywordslist


import browser.MyBrowser as browser
import useragent.ua as ua
import schedule.schedule_for_kuaishangtong as schedule
import sender.msgsender as msgsender
import messageextractor.msgextractor as msgextractor
import yanzhengma.yanzhengma as vertificator


import platform

# # openurlstring="http://ie.icoa.cn/"

# # 加密混淆
# # https://pyprotect.angelic47.com/

# platstring=platform.platform()



# fname=random.uniform(1, 10000000000)
# f=open('hist/'+str(fname)+'.txt','a')


with codecs.open('config.json',encoding='utf-8') as json_data:
	config = json.load(json_data)

# 搜索关键词列表
keywordlist=keywordslist()
usearchword=random.choice(keywordlist)


openurlstring=config['url']
keshiname=random.choice(config['keshi'])
userid=config['userid']
swtid=config['swtid']

# 目前先暂定chrome 
# phantom后面再写
browsername=config['browser']




# 不能带http://
baidurl="www.baidu.com/s?ie=utf-8&f=8&rsv_bp=0&rsv_idx=1&tn=baidu&"+urllib.urlencode({"wd":usearchword})+"&rsv_pq=8be423541abda&rsv_t=d532oXG7fdsiwYlno&rqlang=cn&rsv_enter=1&rsv_sug3=2&rsv_sug1=1&rsv_sug7=100&rsv_sug2=0&inputT=2031&rsv_sug4=2513"

if len(config['domain'])>0:
	# 医院地址
	maindomain=random.choice(config['domain'])
	if not len(maindomain)>0:
		pass
		maindomain=baidurl
else:
	# 模拟百度跳转过去
	maindomain=baidurl
	# maindomain="www.baidu.com"

# try:
# 	mainrouter=random.choice(config['router'])
# except Exception, e:
# 	# raise e
# 	mainrouter=geneurlrouter(1)+'/'+geneurlrouter(2)+'/'+geneurlrouter(3)+'html?=' +geneurlrouter(15)#'s=g&bd=4&ids=kdjsc'


# #cookie
# cookielist=genercookies(str(swtid))
# print(cookielist)
# cidforzoosoft=cookielist[1].split('=')[1]
# print(cidforzoosoft)

# #替换为cookie里面的cid sid
# openurlstring=re.sub('cid=\d{5,}','cid='+str(cidforzoosoft),openurlstring)
# openurlstring=re.sub('sid=\d{5,}','sid='+str(cidforzoosoft),openurlstring)


# # openurlstring=url#ceshi
# result=list(urlparse.urlparse(openurlstring))
# print(result[4]) #param query参数
# param=urlparse.parse_qs(result[4],True)


# hospitalsite='http://'+maindomain+''+mainrouter

# param['p']=hospitalsite



# param['wd']=usearchword

# result[4]=urllib.urlencode(param, True)

# openurlstring=urlparse.urlunparse(result)
# print(urlparse.urlunparse(result))



# protocol, s1 = urllib.splittype(openurlstring)  
# host, s2=  urllib.splithost(s1)  
# host, port = urllib.splitport(host)  

# print('host')
# print(host)




# 加密混淆
# https://pyprotect.angelic47.com/

# openurlstring=config['url']
# keshiname=config['keshi']
# userid=config['userid']
# swtid=config['swtid']
# browsername=config['browser']

# maindomain=random.choice(config['domain'])


print(openurlstring)
try:
	mainrouter=random.choice(config['router'])
except Exception, e:
	# raise e
	mainrouter=geneurlrouter(1)+'/'+geneurlrouter(2)+'/'+geneurlrouter(3)+'html?=' +geneurlrouter(15)#'s=g&bd=4&ids=kdjsc'


#cookie
# cookielist=genercookies(str(swtid))
# print(cookielist)
# cidforzoosoft=cookielist[1].split('=')[1]
# print(cidforzoosoft)

# #替换为cookie里面的cid sid
# openurlstring=re.sub('cid=\d{5,}','cid='+str(cidforzoosoft),openurlstring)
# openurlstring=re.sub('sid=\d{5,}','sid='+str(cidforzoosoft),openurlstring)


vi,tk,totime=geneparamviandtk()

hospitalsite='http://'+maindomain+mainrouter

# openurlstring=url#ceshi
result=list(urlparse.urlparse(openurlstring))
print(result[4]) #param query参数
param=urlparse.parse_qs(result[4],True)

# param['dp']=maindomain+mainrouter
# param['vi']=vi
# param['_d']=totime
# param['_tk']=tk


result[4]=urllib.urlencode(param, True)




openurlstring=urlparse.urlunparse(result)
print(urlparse.urlunparse(result))



protocol, s1 = urllib.splittype(openurlstring)  
host, s2=  urllib.splithost(s1)  
host, port = urllib.splitport(host)  

print('host')
print(host)


# 参数研究
# 2017-12-13 10:54:15 从[搜索引擎,搜索关键词:未提供]:m.baidu.com 进入:/a/nxby/512.html
# https://vipz1-hztk5.kuaishang.cn/bs/im.htm
# ?sText=zxzx
# &cas=59270___700690
# &fi=67885
# &ri=18374871175
# &vi=7890a032d4014b50915fa16113cf718f
# &dp=http%3A%2F%2Fzt.dy365tj.com%2Fnkzt%2Fdyyyjj171022.html%23baidy365tj-dy-tjpcdytjyy-dytj%23dongyingtongji%7C9-9%7Clhgl1024
# &_d=1516067310982
# &_tk=3aad58bb






if __name__ == '__main__':


	# 获得当前时间时间戳
	# 转换为其他日期格式,如:"%Y-%m-%d %H:%M:%S"
	starttime=int(time.time())

	nowtime = datetime.datetime.now()
	print(nowtime.hour)

	# if nowtime.hour>22	or nowtime.hour<9 :
	# 	exit()


	# 新建浏览器
	mybrowser=browser.MyBrowder(browsername)

	#新建一个代理器
	# mybrowser.setproxy()

	# 新建一个UA库
	useragent=ua.ua(False)
	mybrowser.setua(useragent)

	# 新建一个验证码识别器
	myvertify=vertificator.yanzhengma(mybrowser)
	mybrowser.setyanzhengma(myvertify)

	#新建一个信息提取器，用于提取想要的信息
	msg_extractor=msgextractor.msgextractor_for_kuaishangtong(mybrowser)
	mybrowser.setextractor(msg_extractor)

	# 新建一个发送器，用于发送消息  操作浏览器
	mysender=msgsender.msgsender_for_kuaishangtong(mybrowser)
	mybrowser.setsender(mysender)


	#开始监听事件  执行计划  
	# mybrowser.listen(msg_extractor,msg_sender)
	# mybrowser.start()
	# 新建一个执行计划   schedule
	myschedule=schedule.schedule(mybrowser)
	# mybrowser.setschedule(myschedule)

	# url="http://lbs.zoosnet.net/LR/Chatpre.aspx?id=LBS31671888&cid=1524380007409445977319&lng=cn&sid=1524380007409445977319&p=http%3A//hzaboluo-mtbd.cn/pc/yypp/%3Fbd-hzabl06%3DCC-%28pp%29pp-795/%3Futm_source%3D%25E6%259D%25AD%25E5%25B7%259E%25E9%2598%25BF%25E6%25B3%25A2%25E7%25BD%259706%26utm_medium%3D%25E7%25AB%259E%25E4%25BB%25B7%26utm_term%3D%25E6%259D%25AD%25E5%25B7%259E%25E9%2598%25BF%25E6%25B3%25A2%25E7%25BD%2597%25E7%2594%25B7%25E7%25A7%2591%26utm_content%3D002%252D%25E6%259D%25AD%25E5%25B7%259E%25E9%2598%25BF%25E6%25B3%25A2%25E7%25BD%2597%26utm_campaign%3DCC%252D%25EF%25BC%2588pp%25EF%25BC%2589%25E5%2593%2581%25E7%2589%258C&rf1=https%3A//www.baidu&rf2=.com/s%3Fie%3Dutf-8%26f%3D8%26rsv_bp%3D0%26rsv_idx%3D1%26tn%3Dbaidu%26wd%3D%25E6%259D%25AD%25E5%25B7%259E%2520%25E7%2594%25B7%25E7%25A7%2591%26rsv_pq%3Df13bbd920003e228%26rsv_t%3Dc8ffPqs0X%252F%252FPFur077XE3JFvGlU42pmIXq3i64qF6nh1SR8tdGYT%252BIoXlcw%26rqlang%3Dcn%26rsv_enter%3D1%26rsv_sug3%3D18%26rsv_sug1%3D9%26rsv_sug7%3D100%26rsv_sug2%3D0%26inputT%3D6033%26rsv_sug4%3D154656&e=%25u6765%25u81EA%25u9996%25u9875%25u81EA%25u52A8%25u9080%25u8BF7%25u7684%25u5BF9%25u8BDD&msg=&d=1524380017081"
	# url="http://webservice.zoosnet.net/LR/Chatpre.aspx?id=LZA77086339&cid=1524404285946652349178&lng=cn&sid=1524404285946652349178&p=http%3A//wap.022sayy.com/&rf1=&rf2=&msg=&e=tanchuang&d=1524404293741"
	
	url=openurlstring
	print(openurlstring)

	# url='http://vipu6-szak3.kuaishang.cn/bs/im.htm?cas=57727___181100&fi=68417&ism=1&vi=c84560c7650f495584349836907a1cea&ref=http%3A%2F%2F3g.cdch120.com%2F&dp=http%3A%2F%2F3g.cdch120.com%2F&_tk=9d79f8bc'


	# 启动 schedule
	myschedule.start(url,hospitalsite,keshiname)

	