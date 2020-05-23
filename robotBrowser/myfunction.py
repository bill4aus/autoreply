#!/usr/bin/env python
#coding:utf-8
# -*- coding: utf-8 -*-
import mymodel
import time
from selenium.webdriver.common.keys import Keys	
from selenium.webdriver.common.action_chains import ActionChains


def getmessage(msg_extractor):
	#新建一个信息提取器，用于提取想要的信息
	# msg_extractor=mymodel.msgextractor_for_zoosoft(botchrome)
	return msg_extractor.get()


def send(botchrome,message,which='zoosoft'):
	if which=='zoosoft':
		send_zoosoft(botchrome,message)
	elif which=='kuaishangtong':
		send_kuaishangtong(botchrome,message)
	elif which=='baidu':
		send_baidu(botchrome,message)

def send_zoosoft(botchrome,message):


	def pc(message):
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
			botchrome.javascript(set_wyswyg_js)
		except Exception as e:
			print('parent.f11(event)')
			print(str(e))	

		# 统一输入部分，试一试所有的输入方法
		# js方法
		try:
			# set_wyswyg_js = 'var e = new Event("keypress");e.which = 65;e.altKey=false;e.ctrlKey=false;e.shiftKey=false;e.metaKey=false;e.bubbles=true;parent.f11(e);'
			set_wyswyg_js = 'FreeTextBox1_editor.document.body.innerText="%s"' %(message)
			set_wyswyg_js = set_wyswyg_js+';document.getElementById("FreeTextBox1_editor").contentWindow.document.body.innerHTML="%s"' %(message)
			
			botchrome.javascript(set_wyswyg_js)
		except Exception as e:
			print('#FreeTextBox1_editor')
			print(str(e))

		# try:
		# 	actelem=browser.switch_to.active_element
		# 	actelem.send_keys(message.decode('utf-8'))
		# 	browser.switch_to.default_content()
		# except Exception as e:
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




		# 	except Exception as e:
		# 		# raise e
		# 		print('iframe')
		# 		print(str(e))
		# 		pass






		# # 统一发送部分，试一试所有的发送方法

		# js方法
		try:
			set_wyswyg_js = 'document.getElementById("SendBtn").click();'
			botchrome.javascript(set_wyswyg_js)
		except Exception as e:
			# raise e
			print('SendBtn')
			print(str(e))

		# onclick
		# User_Send()	找到有send的按钮
		iframehtml=botchrome.browser.find_elements_by_xpath("//*[contains(@onclick, 'end')]")
		for x in iframehtml:
			try:
				# print('x.text')
				# print(x.text)
				# print(x.get_attribute('onclick'))
				# print(x.get_attribute('id'))
				if x.is_displayed():
					x.click()
			except Exception as e:
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
		# 	except Exception as e:
		# 		# raise e
		# 		print('Keys.ENTER')
		# 		print(str(e))


		# browser.save_screenshot("/home/wwwroot/default/yiliao.png")

		# #python
		# try:
		# 	browser.find_element_by_xpath("//div[contains(text(), 发送)]").click()
		# 	browser.find_element_by_xpath("//div[contains(text(), 发 送)]").click()
		# except Exception as e:
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

	def mobile(message):
		pass
		try:
			set_wyswyg_js = 'tlist=document.getElementsByTagName("input");for (var i = 0; i < tlist.length; i++) {tlist[i].value="%s"};' %(message)
			botchrome.javascript(set_wyswyg_js)
		except Exception as e:
			print('#texteditor')
			print(str(e))

		# 有可能是多个  后面改
		try:
			inputhtml=botchrome.browser.find_element_by_xpath("//textarea")
			inputhtml.send_keys(message.decode('utf-8'))
		except Exception as e:
			# raise e
			print('message')
			print(str(e))

		# onclick
		# User_Send()	找到有send的按钮
		try:
			iframehtml=botchrome.browser.find_elements_by_xpath("//*[contains(@onclick, 'end')]")
			for x in iframehtml:
				try:
					if x.is_displayed():
						x.click()
				except Exception as e:
					# raise e
					print('onclick')
					print(str(e))
		except Exception as e:
			# raise e
			print('CANT FIND onclick ')
			print(str(e))
		
		#python
		try:
			botchrome.browser.find_element_by_xpath("//div[contains(text(), '发送')]").click()
			botchrome.browser.find_element_by_xpath("//div[contains(text(), '发 送')]").click()
		except Exception as e:
			# raise e
			print('发送')
			print(str(e))

	#发送 调用
	try:
		pc(message)
	except Exception as e:
		raise e
		pass
	# try:
	# 	mobile(message)
	# except Exception as e:
	# 	raise e
	# 	pass



def send_baidu(botchrome,message):

	def sendtry(botchrome,message):
		# 测试
		# imlp-component-typebox-send-btn pc-imlp-component-typebox-send 
		# imlp-component-typebox-send-btn pc-imlp-component-typebox-send pc-imlp-component-typebox-send--disable
		# try:
		# 	set_wyswyg_js = '$(".pc-imlp-component-typebox .pc-imlp-component-typebox-container .imlp-component-typebox-input").innerText="%s";' %(message)
		# 	botchrome.javascript(set_wyswyg_js)
		# except Exception as e:
		# 	print('发送失败')
		# 	print(str(e))
		# time.sleep(1)
		# try:
		# 	set_wyswyg_js = 'onlineChatIns.sendMsg();'
		# 	botchrome.javascript(set_wyswyg_js)
		# except Exception as e:
		# 	print('发送失败')
		# 	print(str(e))

		#


		actions = ActionChains(botchrome.browser)
		try:
			inputiframe = botchrome.browser.find_element_by_css_selector('.pc-imlp-component-typebox .pc-imlp-component-typebox-container .imlp-component-typebox-input ')
			actions.click(inputiframe)
			actions.perform()
			
			
		except Exception as e:
			raise e
			pass
		try:
			inputiframe.clear()
		except Exception as e:
			# raise e
			pass
		try:
			inputiframe.send_keys(message)
		except Exception as e:
			# raise e
			pass
		try:
			botchrome.sendkey(Keys.ENTER)
		except Exception as e:
			print('发送失败')
			print(str(e))
		

	time.sleep(0.5)
	sendtry(botchrome,message)
'''
ksOnlineChat
reConnDialog();
sendMsgAndConn()
sendMsg()
'''

def send_kuaishangtong(botchrome,message):
	# print("send")
	# print(message)
	#不能打字太快

	def sendtry(botchrome,message):
		# 测试
		
		

		try:
			set_wyswyg_js = 'ksEditInstance.innerText="%s";onlineChatIns.sendMsg();' %(message)
			botchrome.javascript(set_wyswyg_js)
		except Exception as e:
			print('发送失败')
			print(str(e))
		time.sleep(1)
		try:
			set_wyswyg_js = 'onlineChatIns.sendMsg();'
			botchrome.javascript(set_wyswyg_js)
		except Exception as e:
			print('发送失败')
			print(str(e))
		


		

		# 	# 保存文本数据
		# 	# f.write('病人||'+uwords+'\n')
		# try:
		# 	edlist=botchrome.browser.find_elements_by_css_selector('#ksEditInstance')

		# 	if len(edlist)>0:

		# 		botchrome.browser.find_element_by_css_selector('#ksEditInstance').send_keys(message)
		# 		time.sleep(1)
		# 		botchrome.browser.find_element_by_css_selector('#ksEditInstance').send_keys(Keys.ENTER)
		# 		pass
		# except Exception as e:
		# 	raise e
		# 	pass
		# finally:
		# 	pass
			
		# 正式

		
		# try:
			

		# 	framebodylist=self.browser.getelementsbycss('iframe body')
		# 	print('framebodylist')
		# 	print(framebodylist)


		# 	framelist=self.browser.getelementsbycss('iframe')
		# 	print('len(framelist)')
		# 	print(len(framelist))
		# 	iframelen=len(framelist)

		# 	iframeeditor=None
		# 	textclassfind=u'ext'
		# 	textclasshidden=u'idden'

		# 	# 得到的元素是原生元素,使用原生方法 操作
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
		# 		self.browser.browser.switch_to.frame(iframeeditor) #'FreeTextBox1_editor'
		# 		self.browser.browser.find_element_by_tag_name('body').send_keys(message.decode('utf-8'))

		# 		if istest:
		# 			pass
		# 			print('test submit')
		# 		else:
		# 			self.browser.browser.find_element_by_tag_name('body').send_keys(Keys.ENTER)
		# 	else:

		# 		# actelem=browser.switch_to.active_element
		# 		# actelem.click()
		# 		# time.sleep(0.2)
		# 		# actelem.click()
		# 		# actelem.send_keys(message.decode('utf-8'))
		# 		# actelem.click()
		# 		# if istest:
		# 		# 	pass
		# 		# 	print('test submit')
		# 		# else:			
		# 		# 	actelem.send_keys(Keys.ENTER)


		# 		edlist=self.browser.browser.find_elements_by_css_selector('#ksEditInstance')

		# 		if len(edlist)>0:

		# 			self.browser.browser.find_element_by_css_selector('#ksEditInstance').send_keys(message.decode('utf-8'))
		# 			time.sleep(1)
		# 			self.browser.browser.find_element_by_css_selector('#ksEditInstance').send_keys(Keys.ENTER)
		# 			pass
		# 		else:

		# 			# actelem=browser.switch_to.active_element
		# 			# actelem.click()
		# 			# time.sleep(0.2)
		# 			# # actelem.click()
		# 			# actelem.send_keys(message.decode('utf-8'))
		# 			# actelem.click()
		# 			# if istest:
		# 			# 	pass
		# 			# 	print('test submit')
		# 			# else:			
		# 			# 	actelem.send_keys(Keys.ENTER)



		# 			print('FreeTextBox1_editor')


		# 			iframeeditor='FreeTextBox1_editor'
		# 			self.browser.browser.switch_to.frame(iframeeditor)
		# 			self.browser.browser.find_element_by_tag_name('body').send_keys(message.decode('utf-8'))
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

	time.sleep(0.5)
	sendtry(botchrome,message)
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
