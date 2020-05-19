#!/usr/bin/env python
#coding:utf-8
# -*- coding: utf-8 -*-

# 导入工具
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException 
import time
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

import re
from selenium.webdriver.common.keys import Keys  
from PIL import Image	
from user_agent import generate_user_agent, generate_navigator

from supportfunction import changeip
from supportfunction import genewechatid
from supportfunction import genercookies
from supportfunction import geneparamviandtk
import urlparse
import datetime

reload(sys)
sys.setdefaultencoding('utf-8')

import requests
import platform


# with codecs.open('taolu.json',encoding='utf-8') as json_data:
#     taolu = json.load(json_data)
# with codecs.open('bingli.json',encoding='utf-8') as json_data:
#     bingli = json.load(json_data)


fname=random.uniform(1, 10000000000)
f=open('hist/'+str(fname)+'.txt','a')

platstring=platform.platform()

# 基本配置
logging.basicConfig(level=logging.INFO)

with codecs.open('config.json',encoding='utf-8') as json_data:
	config = json.load(json_data)

print(config)


# import damatu

# m2 = hashlib.md5()   


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



# 基本配置
logging.basicConfig(level=logging.INFO)
#精神科
# openurlstring='http://vipu6-szak3.kuaishang.cn/bs/im.htm?cas=57727___181100&fi=68417&ism=1&vi=c84560c7650f495584349836907a1cea&ref=http%3A%2F%2F3g.cdch120.com%2F&dp=http%3A%2F%2F3g.cdch120.com%2F&_tk=9d79f8bc'
# openurlstring='http://pct.zoosnet.net/LR/Chatpre.aspx?id=PCT52081394&cid=1499538353717739194911&lng=cn&sid=1499538353717739194911&p=http%3A//wap.xaxckd.com/jb/yiyu/2017/0228/185.html%23utm_source%3Dbaidu%26utm_medium%3D123456%26utm_term%3D%25E5%25A4%25B1%25E7%259C%25A0%25E6%258A%2591%25E9%2583%2581%25E5%258C%25BB%25E9%2599%25A2%26utm_content%3D%3C%25E5%258C%25BB%3E%25E3%2580%2590%25E5%258C%25BB%25E9%2599%25A2%25E3%2580%2591%25E6%258A%2591%25E9%2583%2581%25E7%2597%2587+%25E7%25B1%25BB%25E5%259E%258B%26utm_campaign%3DM1%3DYYZ&rf1=&rf2=&msg=&d=1499538358059'

#男科
# openurlstring='http://kqi.zoossoft.com/LR/freetel.aspx?siteid=KQI10880110&oname=%e5%80%bc%e7%8f%ad-%e8%ae%b8%e5%8a%a9%e7%90%86'


#皮肤科
# 深圳肤康皮肤病医院  
# http://www.baidu.com/baidu.php?url=kW3K00KdelksEXm36Qnyp2sBpT4rLP-WwVzUs1mkEWdPddqTO0CrB_ZF9-Jaeq-wPonfCuAJ-0zxhV4DE_nDPhSF9iHZWd1axybwpMGcgVRGkM-jkbYdRa5O_JGJhel0BwAXeEFxZeVbQrfy0ccx8S2CRrM4vyFaAV3H_ehByycZ1uaI00.DR_imqIO-osIorU5WdqJc7PHV2XgZJyAp7WGvNq260.U1Yk0ZDqzXeUvoxYEegAGQxY_JZiEIil0A7bTgbqzXeUvoxYEegAGQxY_JZiEIil0A7bTgfqn6KY5TM8vqJLqQSdkJiLqQ29YoLR86KGUHYznjf0u1dBugK1nfKdpHdBmy-bIfKspyfqP0KWpyfqrHn0Ugfqn1D1P-tknjDLg1csPWFxnW0dnNtknjD4g1nvnjD0pvbqn0KzIjYVnfK-pyfqnWndP1wxnHf1n7tznHDzn7tkrjRvn7tznjTkr0KBpHYznjf0UynqnHRvg1mYP1cdPH64nNtknj6snj0knWfkg1D3rjcdn1Rsg1Dsnj7xn0KkTA-b5Hf0TyPGujY4nsKzuLw9u1Ys0AqvUjYknj0knzdbX-tknjcknBdbX-tknjfLPiYkg1Dsrj0YQywlg1DknjDYQH7xnHDsn1cVnH-xnHDsn1bVuZGxnHDsPHcVuZGxnHDkPHDVn-tknHD3ridbX-tknHTdPzYkg1DkP1bdQywlg1DznaYknjPxnHcsnjbVn-tknWcVuZGxnHczn1bVuZGxnHczP1DVuZGxnHczrjTVuZGxnHcvn1nVuZGxnHnknjnVuZGxnHnknWnVuZGxnHnkrjbVuZGxnHnznjcVuZGxnHn1nWnVuZGxnHnYn1RVuZGxnHnvnWTVuZGxnHnvn16VuZGxnHfsnjTVnNtkPj0sriYdg1DYnjnLQywlg1DYnHbkQH7xnHfznjcVuZGxnHfznjnVnNtkPjcsPidbX-tkPjcknBdbX-tkPjcYPidbX-tkPjcvPaYkg1DYnWTvQH7xnHfzP16VuZGxnW0LHadbX-tznjInyadbX-tzPWm4Qywlg1cvPW-mQywl0A7B5HKxn0K-ThTqn0KsTjYs0A4vTjYsQW0snj0snj0s0AdYTjYs0AwbUL0qn0KzpWYs0Aw-IWdsmsKhIjYs0ZKC5H00ULnqn0KBI1Ykn0K8IjYs0ZPl5fKYIgnqPH0znH0LnHDdPjRYrjn3PWfLnsKzug7Y5HDdnjc1PHmsPjT3Pj00Tv-b5H9hnWb3mH7bnj0snj63Phn0mLPV5HD3nbNDfYuKnW7DwbnLfH00mynqnfKsUWYs0Z7VIjYs0Z7VT1Ys0ZGY5H00UyPxuMFEUHYsg1Kxn7tsg1Kxn0Kbmy4dmhNxTAk9Uh-bT1Ysg1Kxn7tsg1Kxn0Ksmgwxuhk9u1Ys0AwYpyfqn0K-IA-b5iYk0A71TAPW5H00IgKGUhPW5H00Tydh5HDv0AuWIgfqn0KhXh6qn0Khmgfqn0KlTAkdT1Ys0A7buhk9u1Yk0Akhm1Ys0APzm1YzrHTLrf
# 和深圳新兴皮肤病医院
# http://www.baidu.com/baidu.php?url=kW3K00jJPmSF4gbo0tImyxKICbM-DkLplhFwaQrotAZCZzuToNvDEeEiK_lrxGFmhOBGrUaaTZQX2nS1UrhI2ZNF93fQKpZBZdtoqZUfF2kvLVVZyw11lB1iavtAQCYxDQDdP7JSKjoE_o4BhLKWuwrvxPo8pSayw2p_x86L9dfINrUge0.Db_iTaUtM-Zsdfd4QDfTPajwCzksIee_TPXi1v43t8XzE5ZslPZgIOO3ktr5gCYxOesOOtlktPNv5gCYIpthz1kLJpMpRt85R_nYQAexY4r-f0.U1Yk0ZDqzXeUvBRznnpbVOizCiRznP2qdQC-nWKhIyV9UhT0IjLFeVEp8_rdknpbVOHiEIil0A-V5HczPsKM5yF-TZnk0ZNG5yF9pywd0ZKGujYY0APGujY3P0KVIjYknjDLg1csPWFxnW0dnNtknjD4g1nvnjD0pvbqn0KzIjYLrjf0uy-b5HDYPHIxnHbsn1PxnHndPH7xnWDsP19xnH6dPWKxnHTsnj7xnW04n100mhbqnW0Yg1DdPfKVm1YvPjmLnWckPHuxnH03nW0vnW6Yn-tknjTvnjb4PNtknj0kg100TgKGujYY0Z7WpyfqrHn0ThIYmyTqnfKEIhsqnH03njDVnNtknj6sPBdbX-tknH0kPaYzg1Dknjf1QH7xnHDsPHcVnNtknH0dPBdbX-tknH0vriY1r7tknH0LPaY1g1DkPH6zQH7xnHDvP16VndtknHm3nBYzg1DkrHT3Qywlg1DznadbX-tknWc3nzdbX-tknWf1niYkg1DzPWndQywlg1DzPW6vQywlg1DzP1bYQywlg1DzrHczQywlg1D1njfzQH7xnHnknjDVrNtkn1D3ridbX-tkn1D4ridbX-tkn1nznzYkg1D1PW61QH7xnHn4rj6VuZGxnHfsnjRVnNtkPj01PzYkg1DYnjfkQywlg1DYnjbLQH7xnHfknjfVuZGxnHfknH6VuZGxnHfknWTVuZGxnHfkPjmVnNtkPjD4nidbX-tkPjcsPBYkg1DYnWfdQH7xnHfzP16VnfK9mWYsg100ugFM5H00TZ0qn0K8IM0qna3snj0snj0sn0KVIZ0qn0KbuAqs5HD0ThCqn0KbugmqTAn0uMfqn0KspjYs0Aq15H00mMTqnH00UMfqn0K1XWY0IZN15HDvnHbsnHTdPHR1njcLP1fznHD10ZF-TgfqnHRsnWndPHfYnH6drfK1pyfqrHf1mWw9nHRsnj0knvnkP6KWTvYqfWPjwW0znbfknWc4nH0knfK9m1Yk0ZK85H00TydY5H00Tyd15H00XMfqn0KVmdqhThqV5HKxn7tsg1Kxn0Kbmy4dmhNxTAk9Uh-bT1Ysg1Kxn7tsg100TA7Ygvu_myTqn0KbIA-b5H00ugwGujYVnfK9TLKWm1Ys0ZNspy4Wm1Ys0Z7VuWYkP6KhmLNY5H00uMGC5H00uh7Y5H00XMK_Ignqn0K9uAu_myTqnfK_uhnqn0KWThnqnHb4Pj0&ck=898.11.152.356.298.534.290.2217&shh=www.baidu.com&sht=baiduhome_pg&us=3.0.1.0.2.1170.0&ie=utf-8&f=8&tn=baiduhome_pg&wd=%E6%B7%B1%E5%9C%B3%20%E7%9A%AE%E8%82%A4%E7%97%85%20%E5%8C%BB%E9%99%A2%20%20fukang&oq=%25E6%25B7%25B1%25E5%259C%25B3%2520%25E7%259A%25AE%25E8%2582%25A4%25E7%2597%2585%2520%25E5%258C%25BB%25E9%2599%25A2&rqlang=cn&inputT=3353
# 这是那个深圳军科的对手
# openurlstring='http://pft.zoosnet.net/LR/Chatpre.aspx?id=PFT49473838&cid=1502245020998669688687&lng=cn&sid=1502245020998669688687&p=http%3A//m.0755gov.com/&rf1=&rf2=&msg=&e=JSdbl-swt&d=1502245038653'

# openurlstring='http://vipw4-szak3.kuaishang.cn/bs/im.htm?cas=57684___621003&fi=68370&e=bdzjtc&p=bdzjtc&ref=http%3A%2F%2Fpfb.fukang-pfk.com%2F&dp=http%3A%2F%2Fpfb.fukang-pfk.com%2F'


# openurlstring ='https://vipz1-hztk5.kuaishang.cn/bs/im.htm?sText=zxzx&cas=59270___700690&fi=67885&ri=18374464750&vi=7890a032d4014b50915fa16113cf718f&dp=http%3A%2F%2Fzt.dy365tj.com%2Fnkzt%2Fdyyyjj171022.html%23baidy365tj-dy-tjpcdytjyy-dytjyyhbh%23dongyingtongjiyiyuanzenmeyang%7C9-9%7Clhgl1024&_d=1515997745948&_tk=d93dc1cf'





# 加密混淆
# https://pyprotect.angelic47.com/

openurlstring=config['url']
keshiname=config['keshi']
userid=config['userid']
swtid=config['swtid']
browsername=config['browser']

maindomain=random.choice(config['domain'])


print(openurlstring)
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


vi,tk,totime=geneparamviandtk()

hosmainpage=maindomain+mainrouter

# openurlstring=url#ceshi
result=list(urlparse.urlparse(openurlstring))
print(result[4]) #param query参数
param=urlparse.parse_qs(result[4],True)

param['dp']=maindomain+mainrouter
param['vi']=vi
param['_d']=totime
param['_tk']=tk


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




#全局变量
#状态变量
lastsay={}
lastsysinfo={}
if_newmessage={}
isayto={}
#改成一个dict 可以处理多个群组
# browser=browser.find_element_by_css_selector('.main')
group_name=''
thisgroup_active_status=0
gstatus={}

#几分钟同步一次群活跃数据
setminutetoupdate=13
# 群组通知时间
setminutetonotice=10

intervaltimes=0

#运行时间
starttime = time.clock()

#是否已经打过招呼
haveyousaidhello=0

msglist_length=0

istest=False

# 获得当前时间时间戳
# 转换为其他日期格式,如:"%Y-%m-%d %H:%M:%S"
starttime=int(time.time())

nowtime = datetime.datetime.now()
print(nowtime.hour)

if nowtime.hour>21	or nowtime.hour<9 :
	# f.close()
	# browser.quit()
	# exit()
	browserquit()


# def waitforlogin():
# 	try:
# 		listele=browser.find_elements_by_css_selector('.chat_item')
# 		# logging.info(u' 联系人长度 : '+str(len(listele)))
# 		if len(listele)>1:
# 			pass
# 			print u'登陆成功'
# 		else:
# 			time.sleep(10)
# 			print u'等待登陆...'
# 			waitforlogin()
# 	except Exception, e:
# 		# raise e
# 		pass
# 		waitforlogin()


# def log_detector():
# 	global browser
# 	try:
# 		waitforlogin()
# 	except Exception, e:
# 		# raise e
# 		print 'error:'
# 		waitforlogin()
	
# waitforlogin()

# 函数定义

       

def get_median(data):
	data.sort()
	half = len(data) // 2
	return (data[half] + data[~half]) / 2


# def get_all_person_message():
# 	global setminutetoupdate
# 	global starttime
# 	count=0
# 	gcount=1

# 	try:
# 		listele=browser.find_elements_by_css_selector('.chat_item')
# 		#count的作用是避免找到太靠页面底下的联系人，导致很多问题。
# 		# 因为页面中联系人是动态生成的
# 		for ele in listele:
# 			gpinfojson=ele.get_attribute('data-cm')
# 			#是联系人才点开
# 			# 顺序在5以内的才点击 越小，处理新消息速度越快
# 			if '@@' not in gpinfojson and count < 8:
# 				gpname=ele.find_element_by_css_selector('.nickname_text').text
# 				# endtime = time.clock()

# 				print '\n'
# 				print '\n'
# 				logging.info(u' 当前朋友名称 : '+gpname)

# 				if u'老-' in gpname:
# 					logging.info(u' 老客户自动跳过 : '+gpname)
# 					# return ''
# 					continue
# 				# 根据运行时间 s  设定聊天数目判断标准
# 				intervaltimes=0

# 				isgoingtoopen=True

# 				if isgoingtoopen:
# 					#是联系人才点开
					
# 					ele.click()
# 					time.sleep(0.2)
					
# 					#还是重新点一下试下
# 					logging.info(u'开始抓取。。。。。')
# 					extract_person_message(gpname,1)
# 					# time.sleep(1.7)
# 					logging.info(u'抓取完毕。。。。。')
# 					# time.sleep(3)
# 				else:
# 					pass
# 					# logging.info(u'跳过：'+gpname)
					
# 			count+=1
# 		#每循环一次列表，清空一次游客发言列表

# 	except Exception, e:
# 		# raise e
# 		logging.info(str(e))


#获取朋友消息
def get_friends_message(name):
	global starttime
	global fname
	global browser
	# time.sleep(10)
	# 获取所有的群组消息
	isfisthello=0
	shorttime=0
	middletime=0
	laragetime=0
	while 1:
	# get_screenshot_as_file
	# browser.save_screenshot("/home/wwwroot/default/yiliao.png")
		nowtime=int(time.time())
		# get_all_person_message() 循环抓取联系人列表
		extract_person_message('gpname',1)	#只抓单个人的消息
		time.sleep(5)
		wechatid_for_play=genewechatid()

		if nowtime-starttime>60*0.2:
			print(nowtime-starttime)
			listele=browser.find_elements_by_css_selector('.msg-box .msg-agent')
			if len(listele)<1 and isfisthello==0:
				slist=['zaime','nihao','还在么？ ','医生你好','你好','在么医生','在么医生。。。','您好','医生您好','在么。。。','你好，我想咨询下']
				random.shuffle(slist)
				send_massage('gpname',1,slist[0])
				# browserquit()
				isfisthello=1



		if nowtime-starttime>60*1.5:
			print(nowtime-starttime)
			listele=browser.find_elements_by_css_selector('.msg-box .msg-agent')
			if len(listele)<2 and shorttime==0:
				slist=['还在么？ ','医生？','咋回事啊？ ','怎么不说话啊？','在么医生。。。','医生你搞什么呢。。','说话啊','等你那么久了呢','快点啊。。。']
				random.shuffle(slist)
				send_massage('gpname',1,slist[0])
				# browserquit()
				shorttime=1

		if nowtime-starttime>60*2:
			print(nowtime-starttime)
			listele=browser.find_elements_by_css_selector('.msg-box .msg-agent')
			if len(listele)<4 and middletime==0:
				slist=['那你联系我下呗','算了。。。那你加我微信吧 ','是要提供我微信号','加我一下','医生。。。麻烦加我微信 ']
				random.shuffle(slist)
				send_massage('gpname',1,slist[0])
				middletime=1
		if nowtime-starttime>60*4:
			print(nowtime-starttime)
			listele=browser.find_elements_by_css_selector('.msg-box .msg-agent')
			if len(listele)<15 and laragetime==0:
				# slist=['你们医院垃圾，客服也是垃圾 ','我看你们医院评价不好啊，太歪了','你们天天坑人是不是缺心眼 ','你们良心不会痛么','傻比客服医生','垃圾啊！','操你大爷！什么玩意','去你老母的，黑心医院','滚你妈的','去你妈的','尼玛傻比么','傻比医生','你们医院垃圾，客服也是垃圾 ','我看你们医院评价不好啊，太歪了','你们天天坑人是不是缺心眼 ','你们良心不会痛么']
				# slist=['我看你们医院评价不好啊，太歪了','我看你们医院评价不好啊，太歪了']
				# random.shuffle(slist)
				# send_massage('gpname',1,slist[0])
				# laragetime=1
				browserquit()
		if nowtime-starttime>60*5:
			print(nowtime-starttime)
			browserquit()
		# nowtime=int(time.time())
		# #8分钟是不是更好？？或者判断下是不是可以关闭了，比如对方一直不说话，出现验证码等等意外情形
		# if nowtime-starttime>60*3:
		#	 pass
		#	 f.close()
		#	 browser.quit()
		#	 exit()
		# browser.save_screenshot("D:/zip/12/"+str(fname)+"screen.png")

		

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



def browserquit():
	global browser
	global f
	global fname

	# if fname:
	# 	browser.save_screenshot("D:/zip/12/"+str(fname)+"screen.png")
	if browser:
		browser.quit()
	if f:
		f.close()
	exit()

#获取朋友消息
def extract_person_message(name,is_already_clicked):
	global thisgroup_active_status
	global gstatus
	global lastsay
	global lastsysinfo
	# global time
	global if_newmessage
	global isayto
	global msglist_length

	name='gpname'

	time.sleep(0.1)
	logging.info(u'----------------开始处理这次循环的消息---------')

	# 是否被对方手动结束对话
	# kschat_enddialog
	# isover=getelements(browser,'#kschat_enddialog')
	# inputhtml=browser.find_element_by_xpath("//div[contains(text(), 次对话已结束)]")
	inputhtml=browser.find_element_by_xpath("//div[@class='kschatphone_enddialog_tips']")

	

	print('isover')
	# print(inputhtml.text)
	if inputhtml!=None:
		if inputhtml.is_displayed():
			browserquit()


	if_newmessage[name]=0
	sayarray=[]
	sysinfoarray=[]

	try:
		# #已经进入该群组消息了 不用重新点击进入了
		# if is_already_clicked:
		# 	pass
		# 	time.sleep(0.1)
		# else:
		# 	find_group_by_name(name)
		# 	time.sleep(0.1)

		groupcode_present=''

		#code没用 会变的 还是以名字为主
		# gpinfojson=browser.find_element_by_css_selector('.chat_list  .active').get_attribute('data-cm')
		# ginfojson=json.loads(gpinfojson)
		# groupcode_present=ginfojson['username']
		# logging.info(u' 当前群组代码 : '+groupcode_present)

		if not lastsay.has_key(name):
			lastsay[name]=u'测试'
			print 'not have key'
			print lastsay[name]

		if not isayto.has_key(name):
			isayto[name]=u'测试'

		# now_name=browser.find_element_by_css_selector('#chatArea .box_hd .title_wrap .title a').text
		# if now_name!=name:
		# 	return 'wrong time'
			# logging.info(u' wrong time : '+gpname)
			# continue
		gpname=name
		logging.info(u' 当前好友名称 : '+gpname)

		time.sleep(0.3)
		#朋友聊天消息
		# .msg_left .msg 
		# listele=browser.find_elements_by_css_selector('#wrapper .content .msg_left')
		listele=browser.find_elements_by_css_selector('.msg_cs')
		# msg_cs msg
		# msg_cus msg

		# #msgArea  .msg-box .text
		#msg-box
		msglist_length=len(listele)
		print(msglist_length)
		print('.msg_left')

		# if msglist_length==0:
		# 	pass
		# 	print('.msg-agent')
		# 	listele=browser.find_elements_by_css_selector('#msgArea .msg-box .msg-agent')
		# 	msglist_length=len(listele)

		print(msglist_length)
		time.sleep(0.1)
		logging.info(u' 该朋友聊天消息长度 : '+str(msglist_length))
		for ele in listele:
			# print ele.text.encode('utf-8')
			nickname= gpname
			usersay= ele.find_element_by_css_selector('.msg').text
			
			# try:
			# 	# usersay= ele.find_element_by_css_selector('table .msg').text
			# 	usersay= ele.find_element_by_css_selector('.msg').text
			# except Exception, e:
			# 	# raise e
			# 	usersay= ele.find_element_by_css_selector('.arrow_box_left .text').text
			
			# time.sleep(0.1)
			logging.info(usersay)
				
			#替换不能识别的字符串  _web  class="emoji emoji1f48e"
			# replace

			# print '\n'
			# print '\n'

			sayarray.append({'nickname':nickname,'usersay':usersay})
		# debug info
		time.sleep(0.2)
		if len(sayarray)>0:
			# print len(sayarray)
			# print sayarray[len(sayarray)-1]['nickname']+sayarray[len(sayarray)-1]['usersay']
			
			logging.info(u'有历史消息')
			# print lastsay[name]
			logging.info(u'判断是否是新消息')

		else:
			logging.info(u'此人暂时无消息')

		# 根据最新的聊天记录，判断上一次聊天记录，是否相同


		if len(sayarray)>0:

			usersayobj=sayarray[-1]
			nname=usersayobj['nickname']
			ssay=usersayobj['usersay'].replace(' ','')
			# print lastsay[name]
			# print (sayarray[-1]['nickname']+sayarray[-1]['usersay'])
			print lastsay[name]==ssay
			if lastsay[name]==ssay:
				pass
			else:
				if ssay=='' and is_img==1:
					# 如果是发图片
					if_newmessage[name]=1
					lastsay[name]=ssay
				elif ssay!='':
					# 如果内容不是为空
					if_newmessage[name]=1
					lastsay[name]=ssay
		# time.sleep(0.1)
		logging.info(if_newmessage[name])
		
		if if_newmessage[name]:
			if_newmessage[name]=0
			# thisgroup_active_status+=1

			#new
			# usersayobj=sayarray.pop()
			usersayobj=sayarray[-1]
			nname=usersayobj['nickname']
			ssay=usersayobj['usersay']
			# usercode=usersayobj['usercode']

			logging.info('***************new message：'+gpname+'******************')
			logging.info(nname+' say : '+ssay)
			logging.info('***************new message：'+gpname+'******************')

			# if is_img or is_file:
			# 	pass
			# 	#用户发的图片，应该比较重要
			# 	ssay='注意：用户-'+nname+' 发照片或者文件，请留意检查相关聊天记录'

			f.write('医生||'+ssay+'\n')

			#保存文本到数据库
			urlprefix='http://39.108.185.27/hospital/index.php?m=Api&c=user&a=talklog'
			urll =urlprefix+'&urole='+urllib.quote('医生'.encode('utf8'))+'&usay='+urllib.quote(ssay.encode('utf8'))+'&chatid='+str(userid)+'-'+str(fname)+'&userid='+str(userid)
			reqq = urllib2.Request(urll)
			res_dataa = urllib2.urlopen(reqq)
			ress = res_dataa.read()

			#中文机器人  自有
			# urll ='http://127.0.0.1:9001/?word='+urllib.quote(ssay.encode('utf8'))+'&group='+urllib.quote(name.encode('utf8'))+'&username='+urllib.quote(nname.encode('utf8'))
			urll ='http://39.108.185.27:9003/?word='+urllib.quote(ssay.encode('utf8'))+'&keshi='+keshiname
			reqq = urllib2.Request(urll)
			res_dataa = urllib2.urlopen(reqq)
			ress = res_dataa.read()

			time.sleep(0.1)
			# print ress
			if ress == 'stop to say||stop to say':
				print 'stop to say'
				pass
			else:
				logging.info('robot will respond with : '+ress.encode('gbk'))
				# print ress
				try:
					#new logic
					usayinfo=ress.split('||')
					uwords=usayinfo[0]
					dintent=usayinfo[1].decode('utf-8')
					myintent=usayinfo[1].decode('utf-8')


					f.write('病人||'+uwords+'\n')

					saylist=uwords.split('，')
					# print('len(saylist)')
					# print(len(saylist))

					# for isayword in saylist:
					# 	print(isayword)
					# 	if isayword!=None:
					# 		send_massage(name,1,isayword)
					# 		time.sleep(0.9)
					# 		# time.sleep(0.8*len(isayword))

					send_massage(name,1,uwords)

					wechatid_for_play=genewechatid()

					if dintent=='医生不爽':
						# slist=['傻比客服医生','垃圾啊！','操你大爷！什么玩意']
						# slist=['拜拜！','再见！','不送！']
						slist=['好的','行','OK']
						random.shuffle(slist)
						send_massage(name,1,slist[0])
						browserquit()
					# if dintent=='安排诊号面诊':
					# 	slist=['那你加我微信吧 '+wechatid_for_play,'我微信号是'+wechatid_for_play,'我不一定有时间，先加我吧 '+wechatid_for_play]
					# 	random.shuffle(slist)
					# 	send_massage(name,1,slist[0])
					# 	browserquit()
					# if dintent=='询问是否有时间过来看病':
					# 	slist=['那你加我微信吧 '+wechatid_for_play,'我微信号是'+wechatid_for_play,'我不一定有时间，先加我吧 '+wechatid_for_play]
					# 	random.shuffle(slist)
					# 	send_massage(name,1,slist[0])
					# 	browserquit()
					# if dintent=='还在么':
					# 	# slist=['你们医院垃圾，客服也是垃圾 ','我看你们医院评价不好啊，太歪了','你们天天坑人是不是缺心眼 ','你们良心不会痛么']
					# 	slist=['你们医院评价不好，太歪了']
					# 	random.shuffle(slist)
					# 	send_massage(name,1,slist[0])
					# 	browserquit()
					# if myintent=='准备过来':
					# 	# slist=['那你加我微信吧 '+wechatid_for_play,'我微信号是'+wechatid_for_play,'我不一定有时间，先加我吧 '+wechatid_for_play]
					# 	slist=['你们医院怎么过去呢 ','坐公交几路比较好','你们没有分院吧 ','我需要准备什么么']
					# 	random.shuffle(slist)
					# 	send_massage(name,1,slist[0])
					# 	browserquit()
					# if myintent=='我考虑下关闭':
					# 	slist=['那你加我微信吧 '+wechatid_for_play,'我微信号是'+wechatid_for_play,'我不一定有时间，先加我吧 '+wechatid_for_play]
					# 	random.shuffle(slist)
					# 	send_massage(name,1,slist[0])
					# 	browserquit()
					if myintent=='愤怒关闭':
						# slist=['去你老母的，黑心医院','滚你妈的','去你妈的','尼玛傻比么','傻比医生','你们医院垃圾，客服也是垃圾 ','我看你们医院评价不好啊，太歪了','你们天天坑人是不是缺心眼 ','你们良心不会痛么']
						# slist=['拜拜！','再见！','不送！']
						# slist=['拜拜！','再见！','不送！']
						slist=['好的','行','OK']
						random.shuffle(slist)
						send_massage(name,1,slist[0])
						browserquit()
					# if myintent=='不方便过来':
					# 	slist=['那你加我微信吧 '+wechatid_for_play,'我微信号是'+wechatid_for_play,'我不一定有时间，先加我吧 '+wechatid_for_play]
					# 	random.shuffle(slist)
					# 	send_massage(name,1,slist[0])
					# 	browserquit()

					# send_massage(name,1,uwords)
				except Exception, e:
					# raise e
					print(str(e))
					pass
		ress=''#清空上次回答内容
		logging.info(u'----------------结束处理这次循环的消息---------')	
	except Exception, e:
		# raise e
		logging.info(str(e))
		pass

	# time.sleep(0.1)
	# get_group_message(name)

# 发送消息
def send_massage(name,is_already_clicked,msgstring):
	global isayto
	global haveyousaidhello
	global istest
	global browser
	global fname
	global userid
	global ismobile
	global msglist_length

	print('send_massage 1')

	if isayto[name]==msgstring:
		logging.info('i already said this before')
		return 'i already said this before'

	isayto[name]=msgstring

	syastring=msgstring

	if haveyousaidhello and '你好' in msgstring:
		pass
		return 'i have already said hello'

	if '你好' in msgstring:
		haveyousaidhello=1
		#已经说过你好了

	#保存文本到数据库
	urlprefix='http://39.108.185.27/hospital/index.php?m=Api&c=user&a=talklog'
	urll =urlprefix+'&urole='+urllib.quote('病人'.encode('utf8'))+'&usay='+urllib.quote(msgstring.encode('utf8'))+'&chatid='+str(userid)+'-'+str(fname)+'&userid='+str(userid)
	reqq = urllib2.Request(urll)
	res_dataa = urllib2.urlopen(reqq)
	ress = res_dataa.read()



	try:
		browser.find_element_by_css_selector('#ksEditInstance').send_keys(syastring.decode('utf-8'))
		time.sleep(1)
		browser.find_element_by_css_selector('#ksEditInstance').send_keys(Keys.ENTER)
	except Exception, e:
		# raise e
		print(str(e))


	# try:
		

	# 	framebodylist=getelements(browser,'iframe body')
	# 	print('framebodylist')
	# 	print(framebodylist)


	# 	framelist=getelements(browser,'iframe')
	# 	print('len(framelist)')
	# 	print(len(framelist))
	# 	iframelen=len(framelist)

	# 	iframeeditor=None
	# 	textclassfind=u'ext'
	# 	textclasshidden=u'idden'


	# 	for thisiframe in framelist:
	# 		# print(thisiframe)
	# 		# print(thisiframe.get_attribute('id'))
	# 		iframeid=thisiframe.get_attribute('id')
	# 		iframeclass=thisiframe.get_attribute('class')
	# 		# iframestyle=thisiframe.get_attribute('style')


	# 		print(iframeid)
	# 		print(iframeclass)

	# 		# if u'none' in iframestyle:
	# 		# 	pass
	# 		# 	iframelen=iframelen-1
			

	# 		# print(iframeid=='')
	# 		if textclassfind in iframeid:
	# 			iframeeditor=thisiframe
	# 			print('ext in this iframe')
	# 			break

	# 		if iframeeditor==None and (textclassfind in iframeclass):
	# 			iframeeditor=thisiframe
	# 			print('ext in this iframe')
	# 			break

	# 		if iframeeditor==None and (textclasshidden in iframeclass  or textclasshidden in iframeid):
	# 			iframelen-=1
	# 			print('hidden iframe')
	# 			break
			


	# 	# print(iframeeditor)
	# 	if iframelen>0:

	# 		if iframeeditor==None:
	# 			# iframeeditor=framelist[0]
	# 			iframeeditor='FreeTextBox1_editor'

	# 		# iframeid=iframeeditor.get_attribute('id')
	# 		# print('iframeid')
	# 		# print(iframeid)
	# 		print(iframeeditor)
	# 		# browser.switch_to.frame(iframeid) #'FreeTextBox1_editor'
	# 		browser.switch_to.frame(iframeeditor) #'FreeTextBox1_editor'
	# 		browser.find_element_by_tag_name('body').send_keys(syastring.decode('utf-8'))

	# 		if istest:
	# 			pass
	# 			print('test submit')
	# 		else:
	# 			browser.find_element_by_tag_name('body').send_keys(Keys.ENTER)
	# 	else:

	# 		# actelem=browser.switch_to.active_element
	# 		# actelem.click()
	# 		# time.sleep(0.2)
	# 		# actelem.click()
	# 		# actelem.send_keys(syastring.decode('utf-8'))
	# 		# actelem.click()
	# 		# if istest:
	# 		# 	pass
	# 		# 	print('test submit')
	# 		# else:			
	# 		# 	actelem.send_keys(Keys.ENTER)


	# 		edlist=browser.find_elements_by_css_selector('#ksEditInstance')

	# 		if len(edlist)>0:

	# 			browser.find_element_by_css_selector('#ksEditInstance').send_keys(syastring.decode('utf-8'))
	# 			time.sleep(1)
	# 			browser.find_element_by_css_selector('#ksEditInstance').send_keys(Keys.ENTER)
	# 			pass
	# 		else:

	# 			# actelem=browser.switch_to.active_element
	# 			# actelem.click()
	# 			# time.sleep(0.2)
	# 			# # actelem.click()
	# 			# actelem.send_keys(syastring.decode('utf-8'))
	# 			# actelem.click()
	# 			# if istest:
	# 			# 	pass
	# 			# 	print('test submit')
	# 			# else:			
	# 			# 	actelem.send_keys(Keys.ENTER)



	# 			print('FreeTextBox1_editor')


	# 			iframeeditor='FreeTextBox1_editor'
	# 			browser.switch_to.frame(iframeeditor)
	# 			browser.find_element_by_tag_name('body').send_keys(syastring.decode('utf-8'))
	# 			# browser.find_element_by_tag_name('body').send_keys(Keys.ENTER)


	# 			time.sleep(1)
	# 			# browser.find_element_by_tag_name('body').send_keys(Keys.ENTER)
	# 			pass
	# except Exception, e:
	# 	# browser.quit()
	# 	# raise e
	# 	#出错就要跳过，不然卡在一个url_id上
	# 	# count+=1
	# 	print(str(e))

	if msglist_length<3:
		browser.save_screenshot("C:/zip/12/"+str(fname)+'s'+"screen.png")
	elif msglist_length<6:
		browser.save_screenshot("C:/zip/12/"+str(fname)+'m'+"screen.png")
	else:
		browser.save_screenshot("C:/zip/12/"+str(fname)+"screen.png")



# 开始运行


# ismobile=True
ismobile=False

starttime=int(time.time())

# 进入浏览器设置
chome_options = webdriver.ChromeOptions()
# 设置中文
chome_options.add_argument('lang=zh_CN.UTF-8')
#设置不显示图片
# ,"profile.managed_default_content_settings.javascript":2
prefs = {"profile.managed_default_content_settings.images":2}
chome_options.add_experimental_option("prefs",prefs)




# 更换头部
# 移动版没有广告地址了，需要点击了
# if ismobile:
# 	chome_options.add_argument('user-agent="Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.23 Mobile Safari/537.36"')


# 适配后再打开
if random.choice([x for x in range(100)])>0:
	uainfo=generate_user_agent(os=('win','win','win','win','win','win','mac'))
	ismobile=False
else:
	uainfo=generate_user_agent(os=('android'))
	ismobile=True


print('ismobile')
print(ismobile)

print('uainfo')
print(uainfo)

chome_options.add_argument('user-agent="'+uainfo+'"')





dcap={}
dcap["phantomjs.page.settings.loadImages"] = True


dcap['phantomjs.page.customHeaders.Accept'] ='text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
dcap['phantomjs.page.customHeaders.Host'] =host
dcap['phantomjs.page.customHeaders.User-Agent'] =uainfo
# dcap['phantomjs.page.customHeaders.Accept-Encoding'] ='gzip, deflate, br'
dcap['phantomjs.page.customHeaders.Referer'] ='https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=0&rsv_idx=1&tn=baidu&wd=%E5%94%90%E5%B1%B1%E5%8C%BB%E9%99%A2'
# dcap['phantomjs.page.customHeaders.Referer'] ='http://www.tstryy.com/jhsy/shengyuzhidao/'
dcap['phantomjs.page.customHeaders.Cookie'] =';'.join(cookielist)
# dcap['phantomjs.page.customHeaders.Cookie'] = ''
dcap['phantomjs.page.customHeaders.Cache-Control'] ='max-age=0'
dcap['phantomjs.page.customHeaders.Connection'] ='keep-alive'
dcap['phantomjs.page.customHeaders.Upgrade-Insecure-Requests'] ='1'
# dcap['phantomjs.page.customHeaders.Accept-Encoding'] ='gzip, deflate'
dcap['phantomjs.page.customHeaders.Accept-Language'] ='zh-CN,zh;q=0.9'



# chome_options.add_argument(('--proxy-server=http://' + ip_proxy))  
# browser = webdriver.Chrome(chrome_options=chome_options)  

# browser = webdriver.PhantomJS()




# 改判断是Linux还是windows 然后再看是xp 还是win7

# xp不需要代理


#win7
if 'XP' not in platstring:
	# cityname=''
	# ip_proxy=changeip(cityname)
	# if len(ip_proxy)>30:
	# 	print('NO IP AVILABLE')
	# 	exit()
	# # chome_options.add_argument(('--proxy-server=http://' + ip_proxy))	



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
	# 	browser = webdriver.Chrome(chrome_options=chome_options)	
	# 	print('Chrome()')
	pass
else:
	#xp

	if browsername==None or browsername=='':
		browsername='phantom'

	if browsername=='phantom':
		# 改为phantom
		# Windows环境下完整路径前加r！！！
		# browser = webdriver.PhantomJS(executable_path=r'D:\phantomjs\bin\phantomjs.exe',desired_capabilities=dcap)
		browser = webdriver.PhantomJS(executable_path=r'C:\phantomjs\phantomjs.exe',desired_capabilities=dcap)
		browser.viewportSize={'width':1824,'height':2200} #重要这句！
		browser.maximize_window()
		print('PhantomJS()')
	if browsername=='chrome':
		# phantom 好像被 识别了 ，所以还是用 chrome
		browser = webdriver.Chrome(chrome_options=chome_options)	
		print('Chrome()')


print('delete_all_cookies()')
browser.delete_all_cookies()


# browser.implicitly_wait(30)
browser.set_script_timeout(30)
browser.set_page_load_timeout(40)
# browser = webdriver.Firefox()
# browser = webdriver.Chrome()




try:
	# browser = webdriver.Chrome(desired_capabilities=capabilities)
	print(hosmainpage)
	browser.get('http://'+hosmainpage)
	print('browser.get()')

	# 注入js跳转 openurlstring

	set_wyswyg_js = 'setTimeout(function(){location.href="'+openurlstring+'";},1500);'
	# set_wyswyg_js='openrightswt();'
	browser.execute_script(set_wyswyg_js)


	time.sleep(3)
except Exception, e:
	pass
	print(str(e))
	# f.close()
	# browser.quit()
	# exit()
	browserquit()
# browser.get(openurlstring)


# 确认没问题 并做网络缓冲
logging.info(u'browser.title:'+browser.title+'.')
logging.info(browser.title)
# time.sleep(5)
browser.save_screenshot("wechat.png")


time.sleep(0.1)



if browser.title=='' or 'kuaishang' in browser.title:
	pass
	f.close()
	browser.quit()
	exit()


# try:
# 	# titleelm=browser.find_element_by_css_selector('#kw')
# 	titleelm=browser.find_element_by_css_selector('iframe')
# 	print(titleelm)
# except Exception, e:
# 	# raise e
# 	print(str(e))
# 	print('browser.quit() cant find .chat_item')
# 	f.close()
# 	browser.quit()
# 	print('page opend error ,quit quit quit')
# 	print('page opend error ,quit quit quit')
# 	exit()


# # 定时器
# scheduler = BackgroundScheduler()
# scheduler.add_job(log_detector,'cron',minute='*/15')
# scheduler.start()


# get_all_group_info()


# waitforlogin()





# nname='dd'
# name='cc'
# ssay='您好.这里是上海九龙男子医院- 预约咨询中心，我是刘医生助理，有什么可以帮您，请讲！'
# #中文机器人  自有
# # urll ='http://127.0.0.1:9001/?word='+urllib.quote(ssay.encode('utf8'))+'&group='+urllib.quote(name.encode('utf8'))+'&username='+urllib.quote(nname.encode('utf8'))
# urll ='http://127.0.0.1:9003/?word='+urllib.quote(ssay.encode('utf8'))+'&group='+urllib.quote(name.encode('utf8'))+'&username='+urllib.quote(nname.encode('utf8'))
# reqq = urllib2.Request(urll)
# res_dataa = urllib2.urlopen(reqq)
# ress = res_dataa.read()

# time.sleep(0.1)
# # print ress
# if ress == 'stop to say||stop to say':
# 	print 'stop to say'
# 	pass
# else:
# 	logging.info('robot will respond with : '+ress.encode('gbk'))
# 	# print ress
# 	try:
# 		pass
# 		# isayto[name]=ress

# 		usayinfo=ress.split('||')
# 		uwords=usayinfo[0]
# 		dintent=usayinfo[1].decode('utf-8')

# 		print('dintent')
# 		print(dintent)
		
# 		replyintent=taolu[dintent].split(',')
# 		print('replyintent')
# 		print(replyintent)
# 		random.shuffle(replyintent)
# 		print('taolu[dintent]')
# 		print(taolu[dintent])

# 		print(bingli[replyintent[0]])
# 		print('bingli[replyintent[0]]')
# 		send_massage(name,1,uwords)

# 		saylist=uwords.split('，')
# 		print('len(saylist)')
# 		print(len(saylist))
# 		# for isayword in saylist:
# 		# 	print(isayword)
# 		# 	send_massage(name,1,isayword)
# 		# 	time.sleep(0.5)


# 		if uwords[1]=='医生不爽':
# 			browser.quit()
# 		if uwords[1]=='安排诊号面诊':
# 			browser.quit()
# 		if uwords[1]=='询问是否有时间过来看病':
# 			browser.quit()
# 		if uwords[1]=='还在么':
# 			browser.quit()
# 	except:
# 		pass




# #yzmimg
# 验证码判断
iscode=0
# modalDiv_Chatpreobj
# modalDiv_ChatpreobjN

coderobot=browser.find_elements_by_css_selector('#modalDiv_ChatpreobjN')
if len(coderobot)>0:
	iscode=1
	print 'newcode'
	print 'newcode'

	#截图
	# yzmimgN
	imgelement=browser.find_element_by_css_selector('#yzmimgN')
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


	#拖拽滑块到相应位置
	widthheight=codestr.split(',')
	print('widthheight')
	print(widthheight)
	# browser.actions()
	# .mouseMove(
	# 	element(by.css('.material-dialog-container')), -20, -20) #pixel offset from top left
	# .click()
	# .perform();
	above = browser.find_element_by_css_selector("#yzmimgN")
	ActionChains(browser).click_and_hold(above).drag_and_drop_by_offset(above,float(widthheight[0])*size['width'],float(widthheight[1])*size['height']).perform()







get_friends_message('')