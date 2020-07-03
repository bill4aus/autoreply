# coding:utf-8

import browserBot
import json
import myfunction
import mymodel
import time
import random










'''


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



# # 加密混淆
# # https://pyprotect.angelic47.com/



#kuaishangtong



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



'''



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
# botchrome = browserBot.firefox()
# url="http://kqi.zoossoft.com/LR/freetel.aspx?siteid=KQI10880110&oname=%e5%80%bc%e7%8f%ad-%e8%ae%b8%e5%8a%a9%e7%90%86"
# url="http://kefu8.kuaishang.com.cn/bs/im/33908/29881/753511/sText_%E4%BC%98%E5%8C%96%E7%82%B9%E5%87%BB.htm"
# url="https://ada.baidu.com/site/qianhu.wejianzhan.com/xyl?imid=8aa44b4ceda14518603c8535b1de40a6&utm_source=baidu_wc3&utm_medium=cpc&utm_term=%E7%94%B7%E7%A7%91%E5%8C%BB%E9%99%A2&utm_content=%E7%94%B7%E7%A7%91&utm_campaign=A_B02_%E7%94%B7%E7%A7%91_%E5%8C%BB%E9%99%A2_%E5%AF%B9%E8%AF%9D%5B-nk%5D&key=nankeyiyuan&e_adposition=cl4&e_keywordid=165598555817&bd_vid=nH6sPHcLPWfYnWR3Pj0kn1TYrjwxnWcdg1wxnH0s#back1590229671057"
# url = "https://ada.baidu.com/site/120czxh.com/xyl?imid=e9540f5f450dcf8520d795f4903fca54#back1590314513287"
# url="https://ada.baidu.com/site/88308006.com/xyl?imid=5f7b6feec59f8e155675b82a253975b8&zh=NAAAAABP&bz=hyc&jh=nkyy&k=148122326017&&bd_vid=nHDzPHcdn1TkPj61rHRYrHnsn1KxnWcdg17xnH0s#back1590315603493"
url="https://ada.baidu.com/site/120hztjyy.com/xyl?imid=37eda5f886ea77c6f772251d0e6f8d8b#back1590315956526"
# url="https://ada.baidu.com/site/120czxh.com/xyl?imid=e9540f5f450dcf8520d795f4903fca54#back1590316919481"
# url="https://ada.baidu.com/site/shch120.net/xyl?imid=4998e7e3acdfa4787b3f53f59760c2d7&bd21pc-N28-004-01571&bd_vid=nHf3PjbzrHfdrjf3PWRznWcdnjwxnWcLg17xnH0s&renqun_youhua=716503#back1590318157388"
# url="https://ada.baidu.com/site/cq-nk.cn/xyl?imid=29b4c335ce287ee072a7e9bfa5b96d63#back1590318396077"
# url="http://lbs.zoosnet.net/LR/Chatpre.aspx?id=LBS31671888&cid=1524380007409445977319&lng=cn&sid=1524380007409445977319&p=http%3A//hzaboluo-mtbd.cn/pc/yypp/%3Fbd-hzabl06%3DCC-%28pp%29pp-795/%3Futm_source%3D%25E6%259D%25AD%25E5%25B7%259E%25E9%2598%25BF%25E6%25B3%25A2%25E7%25BD%259706%26utm_medium%3D%25E7%25AB%259E%25E4%25BB%25B7%26utm_term%3D%25E6%259D%25AD%25E5%25B7%259E%25E9%2598%25BF%25E6%25B3%25A2%25E7%25BD%2597%25E7%2594%25B7%25E7%25A7%2591%26utm_content%3D002%252D%25E6%259D%25AD%25E5%25B7%259E%25E9%2598%25BF%25E6%25B3%25A2%25E7%25BD%2597%26utm_campaign%3DCC%252D%25EF%25BC%2588pp%25EF%25BC%2589%25E5%2593%2581%25E7%2589%258C&rf1=https%3A//www.baidu&rf2=.com/s%3Fie%3Dutf-8%26f%3D8%26rsv_bp%3D0%26rsv_idx%3D1%26tn%3Dbaidu%26wd%3D%25E6%259D%25AD%25E5%25B7%259E%2520%25E7%2594%25B7%25E7%25A7%2591%26rsv_pq%3Df13bbd920003e228%26rsv_t%3Dc8ffPqs0X%252F%252FPFur077XE3JFvGlU42pmIXq3i64qF6nh1SR8tdGYT%252BIoXlcw%26rqlang%3Dcn%26rsv_enter%3D1%26rsv_sug3%3D18%26rsv_sug1%3D9%26rsv_sug7%3D100%26rsv_sug2%3D0%26inputT%3D6033%26rsv_sug4%3D154656&e=%25u6765%25u81EA%25u9996%25u9875%25u81EA%25u52A8%25u9080%25u8BF7%25u7684%25u5BF9%25u8BDD&msg=&d=1524380017081"
# 登陆
# time.sleep(10)
# botchrome.open(url,waittime=1)
botchrome.openwithsource(url,refferurl,waittime=8)
# botchrome.save_cookie('./cookie.broswer')

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
wechatid_for_play=myfunction.genewechatid()


# 'kuaishangtong'/'zoosoft' /baidu 目前两种

if 'baidu' in url:
	talktype = 'baidu'
elif 'zoossoft' in url:
	talktype = 'zoosoft'
elif 'kuaishang' in url:
	talktype = 'kuaishangtong'


if talktype=='zoosoft':
	msg_extractor=mymodel.msgextractor_for_zoosoft(botchrome)
elif talktype=='kuaishangtong':
	msg_extractor=mymodel.msgextractor_for_kuaishangtong(botchrome)
elif talktype=='baidu':
	msg_extractor=mymodel.msgextractor_for_baidu(botchrome)
	


# myfunction.send(botchrome,'iamtosaystring',which=talktype)


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
