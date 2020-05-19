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
import re
import urlparse

reload(sys)
sys.setdefaultencoding('utf-8')

import requests
import platform

from supportfunction import keywordslist


import browser.MyBrowser as browser
import useragent.ua as ua
import schedule.schedule as schedule
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

try:
	mainrouter=random.choice(config['router'])
except Exception, e:
	# raise e
	mainrouter=geneurlrouter(1)+'/'+geneurlrouter(2)+'/'+geneurlrouter(3)+'html?=' +geneurlrouter(15)#'s=g&bd=4&ids=kdjsc'


#cookie
cookielist=genercookies(str(swtid))
print(cookielist)
cidforzoosoft=cookielist[1].split('=')[1]
print(cidforzoosoft)

#替换为cookie里面的cid sid
openurlstring=re.sub('cid=\d{5,}','cid='+str(cidforzoosoft),openurlstring)
openurlstring=re.sub('sid=\d{5,}','sid='+str(cidforzoosoft),openurlstring)


# openurlstring=url#ceshi
result=list(urlparse.urlparse(openurlstring))
print(result[4]) #param query参数
param=urlparse.parse_qs(result[4],True)


hospitalsite='http://'+maindomain+''+mainrouter

param['p']=hospitalsite



param['wd']=usearchword

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

# http://BYT.zoosnet.net/LR/Chatpre.aspx
# ?id=BYT56031954
# &cid=1513132589268454686813
# &lng=cn
# &sid=1513132589268454686813
#起作用了
# 初次访问网址http://3g.buyunw.com/a/nxby/512.html?JJBD-BY1-ppc_tangshantongrenbuyunbuyuyiyuan
# 当前网页:http://3g.buyunw.com/a/nxby/512.html?JJBD-BY1-ppc_tangshantongrenbuyunbuyuyiyuan 
# &p=http://3g.buyunw.com/a/nxby/512.html?JJBD-BY1-ppc_tangshantongrenbuyunbuyuyiyuan
# 来源网页:https://m.baidu.com/baidu.php 
# &rf1=https://m.baidu.com/baidu.php?url=K600000-SwTdAzCGTImKFE_J8oWYqe22TUsEwbwo0nISN0pK9NxyvgwG71JVAmNysuIcXXGuzwdApg4GtNWl2BRGjp59M7JPG2GTiU8RrTBTBtYORCmXuPUwQqzc2VGFwLiNxiN3BIOcXDcFon95HFkaUJWRvYINOJx1zPmGdtj9-Hg7nf.7R_iTIg-x6Ymc8KDjnDgwxC6LN4rxxOpOvEg4uOgO_N4tXrZ-Cn4ClhmJj_YzmotAWK7x6YmPjqAKhFmhPMuvgtEKA_nYQ7IMu8LJ0.U1Yk0ZDq1nUFETv_znJz8qHfYoLR86Kspynqn0KY5T1AzULPonW2_oERYQ2eYOLiEIil0A-V5Hczn6KM5gI-rH00Iybq0ZKGujYknsKWpyfqn1c40AdY5HckrH-xnH0kPdt1PW0kg1csPHD0pvbqnfKzIjY1nWR0uy-b5HDznjbvP7tknHfdPHFxnH04P1Tvg1DkrH0YP-tknHb3njFxnHcsnHmvg1Dznjc4P-tknW0snW-xnHD4n161g1Dkrj63n7tknH63PWwxnHD3rjR1g1Dkrj61P7tknH6LrH-xnH0Ln1Ddg1DznjTLnsKBpHYznjuxnW0snjFxnW0sn1D0Uynqn10YPHb3PH6sn7tLnjfYnWbzPH-xn7tzn1nvPHnkP0KkTA-b5HD10Z7Wpyfqn1c40ZFMIA7M5H00mycqn7ts0ANzu1Ys0ZKs5H00UMus5H08nj0snj0snj00Ugws5H00uAwETjYk0ZFJ5H00uANv5gIGTvR0uMfqn6KspjYdPjDkPfKET1Yz0AFL5Hf0UMfqnsK1XWY1nWKxnH0snfKYIgnqPWnznH6YrjTLnWmdPHTznHR3r0Kzug7Y5HDdnHnkn1cdPjc4PHT0Tv-b5ycYuAwbnycsrHfvnWTsrHR0mLPV5HIKf1IAf1R3fYf1nYnYrDn0mynqnfKsUWYs0Z7VIjYs0Z7VT1Ys0ZGY5H00UyPxuMFEUHYsg1Kxn7ts0Aw9UMNBuNqsUA78pyw15HKxn7tsg100TA7Ygvu_myTqn0Kbmv-b5H00ugwGujYVnfK9TLKWm1Ys0ZNspy4Wm1Ys0Z7VuWYkP6KhmLNY5H00uMGC5H00uh7Y5H00XMK_Ignqn0K9uAu_myTqnfK_uhnqn0KLuMFEUHY3PjwB0APzm1YYn1nYr0
# &qid=b4ddd1b094627095
# &sourceid=160
# &placeid=1
# &rank=1
# 访问者来源友情链接:https://m.baidu.com
# &shh=m.baidu.com
# &word=%E5%94%90%E5%B1%B1%E5%90%8C%E4%BB%81%E4%B8%8D%E5%AD%95%E5%8C%BB%E9%99%A2
# &sht=844b
# &ck=803.132.194.343.400.264.1.0.0.194
# &rf2=.343
# &msg=
# 说明: tiaozhuan 
# &e=tiaozhuan
# &d=1513132670581




if __name__ == '__main__':


	# 获得当前时间时间戳
	# 转换为其他日期格式,如:"%Y-%m-%d %H:%M:%S"
	starttime=int(time.time())

	nowtime = datetime.datetime.now()
	print(nowtime.hour)

	if nowtime.hour>22	or nowtime.hour<9 :
		# f.close()
		# browser.quit()
		exit()
		# browserquit()


	# 新建浏览器
	mybrowser=browser.MyBrowder('MyBrowder')

	#新建一个代理器
	# mybrowser.setproxy()

	# 新建一个UA库
	useragent=ua.ua(False)
	mybrowser.setua(useragent)

	# 新建一个验证码识别器
	myvertify=vertificator.yanzhengma(mybrowser)
	mybrowser.setyanzhengma(myvertify)

	#新建一个信息提取器，用于提取想要的信息
	msg_extractor=msgextractor.msgextractor_for_zoosoft(mybrowser)
	mybrowser.setextractor(msg_extractor)

	# 新建一个发送器，用于发送消息  操作浏览器
	mysender=msgsender.msgsender_for_zoosoft(mybrowser)
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


	# 启动 schedule
	myschedule.start(url,hospitalsite,keshiname)

	