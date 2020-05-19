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


class msgsender_for_zoosoft(object):
	"""docstring for msgsender_for_zoosoft"""
	def __init__(self, browser):
		super(msgsender_for_zoosoft, self).__init__()
		self.browser = browser
		


	def send(self,message):
		# print("send")
		# print(message)
		#不能打字太快
		time.sleep(3)

		# 参数未传
		# if ismobile:
		try:
			self.pc(message)
		except Exception, e:
			# raise e
			pass
		
		try:
			self.mobile(message)
		except Exception, e:
			# raise e
			pass
		# if isayto[name]==msgstring:
		# 	# logging.info('i already said this before')
		# 	return 'i already said this before'
		# # 保存这一次发送的消息
		# isayto[name]=msgstring

		# if haveyousaidhello and '你好' in msgstring:
		# 	return 'i have already said hello'
		
		# #已经说过你好了
		# if '你好' in msgstring:
		# 	haveyousaidhello=1
		

		#保存文本到数据库
		# urlprefix='http://liliniao.com.cn/hospital/index.php?m=Api&c=user&a=talklog'
		# urll =urlprefix+'&urole='+urllib.quote('病人'.encode('utf8'))+'&usay='+urllib.quote(msgstring.encode('utf8'))+'&chatid='+str(userid)+'-'+str(fname)+'&userid='+str(userid)
		# reqq = urllib2.Request(urll)
		# res_dataa = urllib2.urlopen(reqq)
		# ress = res_dataa.read()
		# self.sendtry()

	def mobile(self,message):
		pass
		# if ismobile:
		#模拟点击输入框
		# try:
		# 	set_wyswyg_js = 'inputclick();'
		# 	browser.execute_script(set_wyswyg_js)
		# except Exception, e:
		# 	print('inputclick();')
		# 	print(str(e))	
		# textarea #texteditor
		try:
			set_wyswyg_js = 'tlist=document.getElementsByTagName("input");for (var i = 0; i < tlist.length; i++) {tlist[i].value="%s"};' %(message)
			self.browser.javascript(set_wyswyg_js)
		except Exception, e:
			print('#texteditor')
			print(str(e))

		# 有可能是多个  后面改
		try:
			inputhtml=self.browser.browser.find_element_by_xpath("//textarea")
			inputhtml.send_keys(message.decode('utf-8'))
		except Exception, e:
			# raise e
			print('message')
			print(str(e))

		# onclick
		# User_Send()	找到有send的按钮
		try:
			iframehtml=self.browser.browser.find_elements_by_xpath("//*[contains(@onclick, 'end')]")
			for x in iframehtml:
				try:
					if x.is_displayed():
						x.click()
				except Exception, e:
					# raise e
					print('onclick')
					print(str(e))
		except Exception, e:
			# raise e
			print('CANT FIND onclick ')
			print(str(e))
		
		#python
		try:
			self.browser.browser.find_element_by_xpath("//div[contains(text(), '发送')]").click()
			self.browser.browser.find_element_by_xpath("//div[contains(text(), '发 送')]").click()
		except Exception, e:
			# raise e
			print('发送')
			print(str(e))

	def pc(self,message):
		# 测试
		# # 输入 文本
		# # inputhtml=self.browser.browser.find_element_by_css_selector("#kw")
		# inputhtml=self.browser.getelementbycss("#kw")
		# inputhtml.send_keys(message)

		# # 点击发送
		# inputhtml.send_keys(Keys.ENTER)


		# 	# 保存文本数据
		# 	# f.write('病人||'+uwords+'\n')

		# 正式

		#这个函数模拟输入，使字体变黑，看起来正常
		# document.dispatchEvent(e);
		# var e=document.createEvent("KeyboardEvents");e.initKeyboardEvent("keydown",true,true,window,"65");parent.f11(e)
		try:
			set_wyswyg_js = 'parent.f11(event);'
			self.browser.javascript(set_wyswyg_js)
		except Exception, e:
			print('parent.f11(event)')
			print(str(e))	

		# 统一输入部分，试一试所有的输入方法
		# js方法
		try:
			# set_wyswyg_js = 'var e = new Event("keypress");e.which = 65;e.altKey=false;e.ctrlKey=false;e.shiftKey=false;e.metaKey=false;e.bubbles=true;parent.f11(e);'
			set_wyswyg_js = 'FreeTextBox1_editor.document.body.innerText="%s"' %(message)
			set_wyswyg_js = set_wyswyg_js+';document.getElementById("FreeTextBox1_editor").contentWindow.document.body.innerHTML="%s"' %(message)
			
			self.browser.browser.execute_script(set_wyswyg_js)
		except Exception, e:
			print('#FreeTextBox1_editor')
			print(str(e))

		# try:
		# 	actelem=browser.switch_to.active_element
		# 	actelem.send_keys(message.decode('utf-8'))
		# 	browser.switch_to.default_content()
		# except Exception, e:
		# 	# raise e
		# 	print('active_element')
		# 	print(str(e))
		# 	browser.switch_to.default_content()
		# #python方法
		# # 找到iframe里面有body div 输入 editor 等字样	
		# iframehtml=browser.find_elements_by_xpath("//iframe")
		# for x in iframehtml:
		# 	try:
		# 		print('xxxxxxx')
		# 		# inputhtml=x.find_element_by_xpath("//body[contains(text(), 在此输入)]")
		# 		inputhtml=x.find_element_by_xpath("//body")
		# 		# print(inputhtml)
		# 		# print('inputhtml.text')
		# 		# print(inputhtml.text)
		# 		# if inputhtml!=None:
		# 		# print('x.text')
		# 		# print(x.text)
		# 		# print(x.get_attribute('id'))
		# 		# print(x.get_attribute('class'))
		# 		# print(inputhtml.text)

		# 		actions = ActionChains(browser)
		# 		inputiframe = browser.find_element_by_css_selector("#"+x.get_attribute('id'))
		# 		actions.click(inputiframe)
		# 		actions.perform()
		# 		# inputhtml.send_keys(message.decode('utf-8'))
		# 		# set_wyswyg_js = 'document.getElementById("'+x.get_attribute('id')+'").contentWindow.document.body.click();'
		# 		set_wyswyg_js = ''
		# 		set_wyswyg_js = set_wyswyg_js+'document.getElementById("'+x.get_attribute('id')+'").contentWindow.document.body.innerHTML="%s"' %(message)
		# 		# set_wyswyg_js = set_wyswyg_js+';document.getElementById("FreeTextBox1_editor").contentWindow.document.body.innerHTML="%s"' %(message)
		# 		browser.execute_script(set_wyswyg_js)

		# 		# 不能发，不然要发2次
		# 		# #send
		# 		# inputhtml.send_keys(Keys.ENTER)

		# 		# inputiframe = browser.find_element_by_css_selector("#"+x.get_attribute('id'))
		# 		# actions = ActionChains(browser)
		# 		# actions.move_to_element(inputiframe)
		# 		# actions.click(inputiframe)
		# 		# actions.perform()
		# 		# inputhtml.send_keys(message.decode('utf-8'))




		# 	except Exception, e:
		# 		# raise e
		# 		print('iframe')
		# 		print(str(e))
		# 		pass






		# # 统一发送部分，试一试所有的发送方法

		# js方法
		try:
			set_wyswyg_js = 'document.getElementById("SendBtn").click();'

			self.browser.browser.execute_script(set_wyswyg_js)
		except Exception, e:
			# raise e
			print('SendBtn')
			print(str(e))

		# onclick
		# User_Send()	找到有send的按钮
		iframehtml=self.browser.browser.find_elements_by_xpath("//*[contains(@onclick, 'end')]")
		for x in iframehtml:
			try:
				# print('x.text')
				# print(x.text)
				# print(x.get_attribute('onclick'))
				# print(x.get_attribute('id'))
				if x.is_displayed():
					x.click()
			except Exception, e:
				# raise e
				print('onclick')
				print(str(e))
				pass
				
		# iframehtml=browser.find_elements_by_xpath("//iframe")
		# for x in iframehtml:
		# 	try:
		# 		inputhtml=x.find_element_by_xpath("//body[contains(text(), 在此输入)]")
		# 		# #send
		# 		inputhtml.send_keys(Keys.ENTER)
		# 	except Exception, e:
		# 		# raise e
		# 		print('Keys.ENTER')
		# 		print(str(e))


		# browser.save_screenshot("/home/wwwroot/default/yiliao.png")

		# #python
		# try:
		# 	browser.find_element_by_xpath("//div[contains(text(), 发送)]").click()
		# 	browser.find_element_by_xpath("//div[contains(text(), 发 送)]").click()
		# except Exception, e:
		# 	# raise e
		# 	print('发送')
		# 	print(str(e))


		# # or	终极大招	暂不做
		# # chain = ActionChains(driver)
		# # chain.context_click(implement).perform()

		# # menu = driver.find_element_by_css_selector(".nav")
		# # hidden_submenu =		driver.find_element_by_css_selector(".nav #submenu1")

		# # actions = ActionChains(browser)
		# # actions.move_to_element(menu)
		# # actions.click(hidden_submenu)
		# # actions.perform()
















class msgsender_for_kuaishangtong(object):
	"""docstring for msgsender_for_kuaishangtong"""
	def __init__(self, browser):
		super(msgsender_for_kuaishangtong, self).__init__()
		self.browser = browser
		


	def send(self,message):
		# print("send")
		# print(message)
		#不能打字太快
		time.sleep(1.5)
		self.sendtry(message)
		# if isayto[name]==msgstring:
		# 	# logging.info('i already said this before')
		# 	return 'i already said this before'
		# # 保存这一次发送的消息
		# isayto[name]=msgstring

		# if haveyousaidhello and '你好' in msgstring:
		# 	return 'i have already said hello'
		
		# #已经说过你好了
		# if '你好' in msgstring:
		# 	haveyousaidhello=1
		

		#保存文本到数据库
		# urlprefix='http://liliniao.com.cn/hospital/index.php?m=Api&c=user&a=talklog'
		# urll =urlprefix+'&urole='+urllib.quote('病人'.encode('utf8'))+'&usay='+urllib.quote(msgstring.encode('utf8'))+'&chatid='+str(userid)+'-'+str(fname)+'&userid='+str(userid)
		# reqq = urllib2.Request(urll)
		# res_dataa = urllib2.urlopen(reqq)
		# ress = res_dataa.read()
		# self.sendtry()

	def sendtry(self,message):
		# 测试
		# # 输入 文本
		# # inputhtml=self.browser.browser.find_element_by_css_selector("#kw")
		# inputhtml=self.browser.getelementbycss("#kw")
		# inputhtml.send_keys(message)

		# # 点击发送
		# inputhtml.send_keys(Keys.ENTER)


		# 	# 保存文本数据
		# 	# f.write('病人||'+uwords+'\n')

		# 正式

		
		try:
			

			framebodylist=self.browser.getelementsbycss('iframe body')
			print('framebodylist')
			print(framebodylist)


			framelist=self.browser.getelementsbycss('iframe')
			print('len(framelist)')
			print(len(framelist))
			iframelen=len(framelist)

			iframeeditor=None
			textclassfind=u'ext'
			textclasshidden=u'idden'

			# 得到的元素是原生元素,使用原生方法 操作
			for thisiframe in framelist:
				# print(thisiframe)
				# print(thisiframe.get_attribute('id'))
				iframeid=thisiframe.get_attribute('id')
				iframeclass=thisiframe.get_attribute('class')
				# iframestyle=thisiframe.get_attribute('style')


				print(iframeid)
				print(iframeclass)

				# if u'none' in iframestyle:
				# 	pass
				# 	iframelen=iframelen-1
				

				# print(iframeid=='')
				if textclassfind in iframeid:
					iframeeditor=thisiframe
					print('ext in this iframe')
					break

				if iframeeditor==None and (textclassfind in iframeclass):
					iframeeditor=thisiframe
					print('ext in this iframe')
					break

				if iframeeditor==None and (textclasshidden in iframeclass  or textclasshidden in iframeid):
					iframelen-=1
					print('hidden iframe')
					break
				


			# print(iframeeditor)
			if iframelen>0:

				if iframeeditor==None:
					# iframeeditor=framelist[0]
					iframeeditor='FreeTextBox1_editor'

				# iframeid=iframeeditor.get_attribute('id')
				# print('iframeid')
				# print(iframeid)
				print(iframeeditor)
				# browser.switch_to.frame(iframeid) #'FreeTextBox1_editor'
				self.browser.browser.switch_to.frame(iframeeditor) #'FreeTextBox1_editor'
				self.browser.browser.find_element_by_tag_name('body').send_keys(message.decode('utf-8'))

				if istest:
					pass
					print('test submit')
				else:
					self.browser.browser.find_element_by_tag_name('body').send_keys(Keys.ENTER)
			else:

				# actelem=browser.switch_to.active_element
				# actelem.click()
				# time.sleep(0.2)
				# actelem.click()
				# actelem.send_keys(message.decode('utf-8'))
				# actelem.click()
				# if istest:
				# 	pass
				# 	print('test submit')
				# else:			
				# 	actelem.send_keys(Keys.ENTER)


				edlist=self.browser.browser.find_elements_by_css_selector('#ksEditInstance')

				if len(edlist)>0:

					self.browser.browser.find_element_by_css_selector('#ksEditInstance').send_keys(message.decode('utf-8'))
					time.sleep(1)
					self.browser.browser.find_element_by_css_selector('#ksEditInstance').send_keys(Keys.ENTER)
					pass
				else:

					# actelem=browser.switch_to.active_element
					# actelem.click()
					# time.sleep(0.2)
					# # actelem.click()
					# actelem.send_keys(message.decode('utf-8'))
					# actelem.click()
					# if istest:
					# 	pass
					# 	print('test submit')
					# else:			
					# 	actelem.send_keys(Keys.ENTER)



					print('FreeTextBox1_editor')


					iframeeditor='FreeTextBox1_editor'
					self.browser.browser.switch_to.frame(iframeeditor)
					self.browser.browser.find_element_by_tag_name('body').send_keys(message.decode('utf-8'))
					# browser.find_element_by_tag_name('body').send_keys(Keys.ENTER)


					time.sleep(1)
					# browser.find_element_by_tag_name('body').send_keys(Keys.ENTER)
					pass


		except Exception, e:
			# browser.quit()
			# raise e
			#出错就要跳过，不然卡在一个url_id上
			# count+=1
			print(str(e))