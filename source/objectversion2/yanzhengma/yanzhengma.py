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
from yundama import YDMHttp


# 上级目录
# sys.path.append('../')
# import robot.robot as robot
class yanzhengma(object):
	"""docstring for yanzhengma"""
	def __init__(self,browser):
		super(yanzhengma, self).__init__()
		# self.arg = arg
		self.browser=browser


		# 用户名
		username	= 'cdsbtest'
		# 密码
		password	= 'cdsb123456'							
		# 软件ＩＤ，开发者分成必要参数。登录开发者后台【我的软件】获得！
		appid		 = 3035									 
		# 软件密钥，开发者分成必要参数。登录开发者后台【我的软件】获得！
		appkey		= '0856355e1dd686e7819093bcd2843176'	
		# 图片文件
		# filename	= 'getimage.jpg'						
		# 验证码类型，# 例：1004表示4位字母数字，不同类型收费不同。请准确填写，否则影响识别率。在此查询所有类型 http://www.yundama.com/price.html
		# codetype	= 1004
		self.codetype	= 5000
		# 超时时间，秒
		self.timeout	 = 60	 

		# 初始化
		self.yundama = YDMHttp(username, password, appid, appkey)

		# 登陆云打码
		uid = self.yundama.login();
		print 'uid: %s' % uid
		# 查询余额
		balance = self.yundama.balance();
		print 'balance: %s' % balance

	def recognise(self,imgfilename):

		# 开始识别，图片路径，验证码类型ID，超时时间（秒），识别结果
		cid, result = self.yundama.decode(imgfilename, self.codetype, self.timeout);
		print 'cid: %s, result: %s' % (cid, result)
		result=str(result)
		# print result
		result=result.replace('c_char_p','')
		result=result.replace('(','')
		result=result.replace(')','')
		result=result.replace('\'','')

		img_to_text=result

		#得到的是原始对象,使用原始的send_keys方法发送消息
		self.browser.getelementbycss('#ccode').send_keys(img_to_text.decode())
		time.sleep(0.3)
		self.browser.getelementbycss('#Button1').send_keys(Keys.ENTER)
		time.sleep(0.3)