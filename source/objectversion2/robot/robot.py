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

class robot(object):
	"""docstring for robot"""
	def __init__(self,keshi,userid):
		super(robot, self).__init__()
		# self.arg = arg

		# 构建url
		# 科室
		# %E4%BD%A0%E5%A5%BD&keshi=xinggongnengzhangai
		self.keshi=keshi

	def get_respone(self,messagegot):
		# pass
		# #中文机器人	自有
		urll ='http://39.108.185.27:9003/?word='+urllib.quote(messagegot.encode('utf8'))+'&keshi='+self.keshi
		print(urll)
		reqq = urllib2.Request(urll)
		res_dataa = urllib2.urlopen(reqq)
		ress = res_dataa.read()
		# return "respone test"

		# 	if ress == 'stop to say||stop to say':
		# 		print 'stop to say'
		# 		pass
		# 	else:
		# 		pass
		# 		saylist=uwords.split('，')
		# 		send_massage(name,1,uwords)
		return ress
		