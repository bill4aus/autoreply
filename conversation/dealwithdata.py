#!/usr/bin/env python
#coding:utf-8
# -*- coding: utf-8 -*-
import urllib
import requests

import json
import os

# 9001  病人
# 9002  医生患者判断
# 9003  医生


# ctname=u'白天输液退了，晚上洗澡就出来了'

# url = "http://127.0.0.1:9002/?word="+urllib.quote(ctname.encode('utf8'))
# req = urllib2.Request(url)
# res_data = urllib2.urlopen(req)
# res = res_data.read()
# print(res)

def get_intent(role,keshi,words):
	pass
	# if role==0:
	# 	pass
	# 	# print('doctor')
	# 	# 医生
	# 	# ctname=u'白天输液退了，晚上洗澡就出来了'
	# 	url = "http://127.0.0.1:9003/?word="+urllib.quote(words)
	# 	req = urllib2.Request(url)
	# 	res_data = urllib2.urlopen(req)
	# 	res = res_data.read()
	# 	# res=res.decode('utf-8')
	# 	# print(res)

	# 	if res=='stop':
	# 		return 'stop'
	# 	return res.split('||')
	# else:
	# 	# 病人
	# 	# print('patient')
	# 	pass
	# 	url = "http://127.0.0.1:9001/?word="+urllib.quote(words)
	# 	print(url)
	# 	req = urllib2.Request(url)
	# 	res_data = urllib2.urlopen(req)
	# 	res = res_data.read()
	# 	# res=res.decode('utf-8')
	# 	# print(res)
	# 	if res=='stop':
	# 		return 'stop'
	# 	return res.split('||')

	#new api
	# http://127.0.0.1:9003/?role=patient&word=%E4%BD%A0%E5%A5%BD&keshi=xinggongnengzhangai
	url = "http://127.0.0.1:9003/?role=patient&keshi="+keshi+"&word="+urllib.parse.quote(words)
	print(url)
	r = requests.get(url)
	res = r.text

	# req = urllib2.Request(url)
	# res_data = urllib2.urlopen(req)
	# res = res_data.read()
	# res=res.decode('utf-8')
	# print(res)
	if res=='stop':
		return 'stop'
	return res



# 对病人回复意图进行分类

# 科室列表
# keshi_list=['xinggongnengzhangai','qianliexianjibing','niaodaoxialie','miniaowaike','baopibaojing','chuanranbingke','pifuke','guke','jingshenxinlike','neike','qitakeshi','waike','wuguanke','zhongyike','erke','erkezonghe','fuchanke','pifuxingbingke','yanke','yijike','yixueyingxiangxue','zhongliuke']
keshi_list=['xinggongnengzhangai','qianliexianjibing','niaodaoxialie','miniaowaike','baopibaojing','fuchanke','pifuxingbingke']


# ./zhongyike
# []
# cb60713d-cb38-4f00-a252-cffb119f8309.txt				




for ke_name in keshi_list:
	flodername=ke_name

	for root, dirs, files in os.walk('./corpus/'+flodername):
		for nfile in files:
			if os.path.splitext(nfile)[1] == '.txt':
				print(root)
				print(dirs)
				print(nfile)

				# pifuke
				# flodername='pifuke'
				# filename='b6c1771b-3fa2-4036-b040-d87736ec1d05'
				# print(os.path.splitext(nfile))
				# sx

				# flodername=flodername
				filename=os.path.splitext(nfile)[0]


				talklist=[]
				for line in open('./corpus/'+flodername+'/'+filename+'.txt',encoding='utf-8').readlines():  
					print(line)
					wordsinfo=line.split('||')

					if len(wordsinfo)!=2:
						continue

					# 过滤平台不适合的词句
					# 息只有医生及用户本
					# 健康币
					if '健康币' in wordsinfo[1] or '息只有医生及用户本' in wordsinfo[1]:
						continue


					# print(len(wordsinfo))
					#角色
					# print(wordsinfo[0])
					# 内容
					# print(wordsinfo[1])

					# if wordsinfo[0]=='医生':
						# pass
						# responseword,wordsintent=get_intent(0,wordsinfo[1])
						# # # print(wordsinfo[1].replace('\n','')+'=>'+wordsintent)
						# # print(wordsinfo[0]+'=>'+wordsintent)
						# # # print('\n')
						# # 如果是医生
						# talklist.append((wordsinfo[0],wordsintent))
					if wordsinfo[0]=='患者':
						# responseword,wordsintent=get_intent(1,wordsinfo[1].replace('\n',''))
						# talklist.append((wordsintent,wordsinfo[1].replace('\n','')))
						wdlist=wordsinfo[1].replace('\n','').split(' ')

						if len(wdlist)>1:
							for ww in wdlist:
								wdtiny=ww.split('，')
								if len(wdtiny)>1:
									for xwd in wdtiny:
										pass
										patientintent=get_intent(1,ke_name,xwd)
										print(patientintent)
										if patientintent!='stop':
											# doctorresponse,patientintent,doctorintent=rp
											talklist.append((patientintent,xwd))

								else:
									patientintent=get_intent(1,ke_name,wdtiny[0])
									print(patientintent)
									if patientintent!='stop':
										# doctorresponse,patientintent,doctorintent=rp
										talklist.append((patientintent,wdtiny[0]))
						else:
							patientintent=get_intent(1,ke_name,wdlist[0])
							print(patientintent)
							if patientintent!='stop':
								# doctorresponse,patientintent,doctorintent=rp
								talklist.append((patientintent,wdlist[0]))
						

				uintent=''
				intent_deal={}


				for uintent,talk in talklist:
					if intent_deal.get(uintent)==None:
						intent_deal[uintent]=[]
					else:
						intent_deal[uintent].append(talk)

				# print(json.dumps(intent_deal,ensure_ascii=False,indent=2))
				# 写入文件
				newjsonfile=open('./bingli/'+flodername+'/'+filename+'.json','w+')
				# newjsonfile.write(json.dumps(intent_deal,ensure_ascii=False,indent=2))
				json.dump(intent_deal,newjsonfile,ensure_ascii=False,indent=4)
				newjsonfile.close()

				#读取
				# myjsonfile=open('./'+flodername+'/'+filename+'.json')
				# jstr=myjsonfile.read()
				# print(jstr)
				# newjstr=''.join(jstr.split('\n'))

				# load_dict = json.loads(newjstr)
				# for x in load_dict:
				# 	print(x)
				# 	print(load_dict[x])