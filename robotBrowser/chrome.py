# coding:utf-8

import browserBot
import json
import myfunction
import mymodel
import time

# def faceButton(startx,starty):
# 	face_dict = {
# 		'dianzan':(startx-110,starty+110),
# 		'tiaopi':(startx-110,starty+80),
# 		'weixiao':(startx-210,starty+80),
# 		'daxiao':(startx-160,starty+80),
# 		'kaixin':(startx-60,starty+130),
# 		'weisuo':(startx,starty+130),
# 		'hua':(startx+50,starty+170),
# 		'ku':(startx,starty+50),
# 		}
# 	facelist = ['dianzan','tiaopi','weixiao','daxiao','kaixin','weisuo','hua','ku']
# 	return face_dict,facelist


refferurl = "https://www.baidu.com/s?ie=utf-8&f=3&rsv_bp=1&rsv_idx=1&tn=baidu&wd=%E7%94%B7%E7%A7%91&fenlei=256&oq=%25E7%2594%25B7%25E7%25A7%2591&rsv_pq=9c21b5200003eca7&rsv_t=a9517qIjZoZkvrDBI0xxeCTZY7yTzt2GO%2B88TGGGDOqPvnRbFInVHHpXEq0&rqlang=cn&rsv_enter=0&rsv_dl=ts_0&rsv_btype=t&prefixsug=%25E7%2594%25B7%25E7%25A7%2591&rsp=0&rsv_sug=1"


botchrome = browserBot.chrome()
# url="http://kqi.zoossoft.com/LR/freetel.aspx?siteid=KQI10880110&oname=%e5%80%bc%e7%8f%ad-%e8%ae%b8%e5%8a%a9%e7%90%86"
# url="http://kefu8.kuaishang.com.cn/bs/im/33908/29881/753511/sText_%E4%BC%98%E5%8C%96%E7%82%B9%E5%87%BB.htm"
url="https://ada.baidu.com/site/qianhu.wejianzhan.com/xyl?imid=8aa44b4ceda14518603c8535b1de40a6&utm_source=baidu_wc3&utm_medium=cpc&utm_term=%E7%94%B7%E7%A7%91%E5%8C%BB%E9%99%A2&utm_content=%E7%94%B7%E7%A7%91&utm_campaign=A_B02_%E7%94%B7%E7%A7%91_%E5%8C%BB%E9%99%A2_%E5%AF%B9%E8%AF%9D%5B-nk%5D&key=nankeyiyuan&e_adposition=cl4&e_keywordid=165598555817&bd_vid=nH6sPHcLPWfYnWR3Pj0kn1TYrjwxnWcdg1wxnH0s#back1590229671057"
	
# 登陆
# botchrome.open(url,waittime=1)
botchrome.openwithsource(url,refferurl,waittime=15)
botchrome.save_cookie('./cookie.broswer')

# corpus = bot.dataload_by_line('./corpus.txt')



# # 如果没有权限发帖，跳过
# if bot.trytofind('.poster_warning'):
# 	continue
# bot.scroll('document.body.clientHeight')
# bot.msleep(0.5)
# bot.sendkey(bot.Keys.CONTROL + bot.Keys.ENTER)
# bot.close()





# 开始时间
starttime=int(time.time())
# 标志状态
shorttime=0
middletime=0
laragetime=0

# 机器人
keshi = 'xinggongnengzhangai'
mybot=mymodel.robot(keshi,"userid")
# wechatid_for_play=genewechatid()


# 'kuaishangtong'/'zoosoft' 目前两种
talktype = 'baidu'

if talktype=='zoosoft':
	msg_extractor=mymodel.msgextractor_for_zoosoft(botchrome)
elif talktype=='kuaishangtong':
	msg_extractor=mymodel.msgextractor_for_kuaishangtong(botchrome)
elif talktype=='baidu':
	msg_extractor=mymodel.msgextractor_for_baidu(botchrome)
	



#while 循环
while True:
	print('.......this time loop.......')
	# 基本规则验证
	nowtime=int(time.time())
	if nowtime-starttime>60*1.5:
		print(nowtime-starttime)
		listele=botchrome.getelementsbycss('.msg-box .msg-agent')
		if len(listele)<2 and shorttime==0:
			slist=['还在么？ ','医生？','咋回事啊？ ','怎么不说话啊？','在么医生。。。','医生你搞什么呢。。','说话啊','等你那么久了呢','快点啊。。。']
			# self.browser.send(random.choice(slist))
			# browserquit()
			shorttime=1

	if nowtime-starttime>60*4:
		print(nowtime-starttime)
		listele=botchrome.getelementsbycss('.msg-box .msg-agent')
		if len(listele)<4 and middletime==0:
			slist=['那你联系我一下吧 。。'+wechatid_for_play,'医生。。。你加我微信吧 '+wechatid_for_play,'是要提供我微信号？','麻烦加我一下可以么。。。'+wechatid_for_play,'医生。。。麻烦加我微信 '+wechatid_for_play]
			# self.browser.send(random.choice(slist))
			middletime=1
	if nowtime-starttime>60*6:
		print(nowtime-starttime)
		listele=botchrome.getelementsbycss('.msg-box .msg-agent')
		if len(listele)<15 and laragetime==0:
			# slist=['你们医院垃圾，客服也是垃圾 ','我看你们医院评价不好啊，太歪了','你们天天坑人是不是缺心眼 ','你们良心不会痛么','傻比客服医生','垃圾啊！','操你大爷！什么玩意','去你老母的，黑心医院','滚你妈的','去你妈的','尼玛傻比么','傻比医生','你们医院垃圾，客服也是垃圾 ','我看你们医院评价不好啊，太歪了','你们天天坑人是不是缺心眼 ','你们良心不会痛么']
			# slist=['我看你们医院评价不好啊，太歪了','我看你们医院评价不好啊，太歪了']
			# self.browser.send(random.choice(slist))
			# laragetime=1
			# self.browser.quit()
			pass
	if nowtime-starttime>60*8:
		print(nowtime-starttime)
		# self.browser.quit()
	# nowtime=int(time.time())
	# #8分钟是不是更好？？或者判断下是不是可以关闭了，比如对方一直不说话，出现验证码等等意外情形
	# if nowtime-starttime>60*3:
		# self.browser.quit()
	# self.browser.screen("D:/zip/12/"+str(fname)+"screen.png")



	# 消息循环
	# 获取消息
	#get message
	# messenger=self.browser.getmessage()

	messenger = myfunction.getmessage(msg_extractor)

	print('messenger.new:')
	print(messenger.new)

	if messenger.new:
		print('new message:')
		print(messenger.newmsg)


		replay=mybot.get_respone(messenger.newmsg)
		# print(replay)
		
		# .decode('utf-8')
		if replay == 'stop':
			print ('stop to say')
			# return ;
		else:
			iamtosaystring,doctor_intent,my_intent=replay.split("||")
			# saylist=uwords.split('，')
			# send_massage(name,1,uwords)
			pass
			#send message	

			#new logic
			# wechatid_for_play=genewechatid()
			dintent=doctor_intent
			myintent=my_intent


			if dintent=='医生不爽':
				# slist=['傻比客服医生','垃圾啊！','操你大爷！什么玩意']
				# slist=['拜拜！','再见！','不送！']
				slist=['好的','行','OK']
				myfunction.send(botchrome,random.choice(slist))
				botchrome.quit()
			# if dintent=='安排诊号面诊':
			#	 slist=['那你加我微信吧 '+wechatid_for_play,'我微信号是'+wechatid_for_play,'我不一定有时间，先加我吧 '+wechatid_for_play]
				# self.browser.send(random.choice(slist))
				# self.browser.quit()
			# if dintent=='询问是否有时间过来看病':
			#	 slist=['那你加我微信吧 '+wechatid_for_play,'我微信号是'+wechatid_for_play,'我不一定有时间，先加我吧 '+wechatid_for_play]
				# self.browser.send(random.choice(slist))
				# self.browser.quit()
			# if dintent=='还在么':
			#	 # slist=['你们医院垃圾，客服也是垃圾 ','我看你们医院评价不好啊，太歪了','你们天天坑人是不是缺心眼 ','你们良心不会痛么']
			#	 slist=['你们医院评价不好，太歪了']
				# self.browser.send(random.choice(slist))
				# self.browser.quit()
			# if myintent=='准备过来':
			#	 # slist=['那你加我微信吧 '+wechatid_for_play,'我微信号是'+wechatid_for_play,'我不一定有时间，先加我吧 '+wechatid_for_play]
			#	 slist=['你们医院怎么过去呢 ','坐公交几路比较好','你们没有分院吧 ','我需要准备什么么']
				# self.browser.send(random.choice(slist))
				# self.browser.quit()
			# if myintent=='我考虑下关闭':
			#	 slist=['那你加我微信吧 '+wechatid_for_play,'我微信号是'+wechatid_for_play,'我不一定有时间，先加我吧 '+wechatid_for_play]
				# self.browser.send(random.choice(slist))
				# self.browser.quit()
			if myintent=='愤怒关闭':
				# slist=['去你老母的，黑心医院','滚你妈的','去你妈的','尼玛傻比么','傻比医生','你们医院垃圾，客服也是垃圾 ','我看你们医院评价不好啊，太歪了','你们天天坑人是不是缺心眼 ','你们良心不会痛么']
				# slist=['拜拜！','再见！','不送！']
				# slist=['拜拜！','再见！','不送！']
				slist=['好的','行','OK']
				myfunction.send(botchrome,random.choice(slist))
				botchrome.quit()

			myfunction.send(botchrome,iamtosaystring,which=talktype)



			# if myintent=='不方便过来':
			#	 slist=['那你加我微信吧 '+wechatid_for_play,'我微信号是'+wechatid_for_play,'我不一定有时间，先加我吧 '+wechatid_for_play]
			# self.browser.send(random.choice(slist))
				# self.browser.quit()
	else:
		pass
		# noting happened
	time.sleep(3)
