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

fname=random.uniform(1, 10000000000)
f=open('hist/'+str(fname)+'.txt','a')

platstring=platform.platform()

# 基本配置
logging.basicConfig(level=logging.INFO)



with codecs.open('config.json',encoding='utf-8') as json_data:
	config = json.load(json_data)



# #唐山
# openurlstring='http://pht.zoosnet.net/LR/Chatpre.aspx?siteid=PHT34309257&lng=cn'
# # openurlstring='http://pjn.zoossoft.net/LR/Chatpre.aspx?siteid=PJN73715361&lng=cn'
# openurlstring='http://BYT.zoossoft.net/LR/Chatpre.aspx?siteid=BYT56031954&lng=cn'
# keshiname='xinggongnengzhangai'
# userid='18136'


# 测试
# MBC59176407
# openurlstring='http://mbc.zoossoft.cn/LR/Chatpre.aspx?id=MBC59176407&lng=cn'
# http://mbc.zoossoft.cn/LR/Chatpre.aspx?id=MBC59176407&cid=1513130425171560507210&lng=cn&sid=1513130425171560507210&p=http%3A//www.nanjiannanke.com/%23bd_njyyppc_00198_nanjianyiyuan&rf1=&rf2=&msg=&d=1513130601615

# http://mbc.zoossoft.cn/LR/Chatpre.aspx?id=MBC59176407&cid=1513132589268454686813&lng=cn&sid=1513132589268454686813&p=http://3g.buyunw.com/a/nxby/512.html?JJBD-BY1-ppc_tangshantongrenbuyunbuyuyiyuan&rf1=https://m.baidu.com/baidu.php?url=K600000-SwTdAzCGTImKFE_J8oWYqe22TUsEwbwo0nISN0pK9NxyvgwG71JVAmNysuIcXXGuzwdApg4GtNWl2BRGjp59M7JPG2GTiU8RrTBTBtYORCmXuPUwQqzc2VGFwLiNxiN3BIOcXDcFon95HFkaUJWRvYINOJx1zPmGdtj9-Hg7nf.7R_iTIg-x6Ymc8KDjnDgwxC6LN4rxxOpOvEg4uOgO_N4tXrZ-Cn4ClhmJj_YzmotAWK7x6YmPjqAKhFmhPMuvgtEKA_nYQ7IMu8LJ0.U1Yk0ZDq1nUFETv_znJz8qHfYoLR86Kspynqn0KY5T1AzULPonW2_oERYQ2eYOLiEIil0A-V5Hczn6KM5gI-rH00Iybq0ZKGujYknsKWpyfqn1c40AdY5HckrH-xnH0kPdt1PW0kg1csPHD0pvbqnfKzIjY1nWR0uy-b5HDznjbvP7tknHfdPHFxnH04P1Tvg1DkrH0YP-tknHb3njFxnHcsnHmvg1Dznjc4P-tknW0snW-xnHD4n161g1Dkrj63n7tknH63PWwxnHD3rjR1g1Dkrj61P7tknH6LrH-xnH0Ln1Ddg1DznjTLnsKBpHYznjuxnW0snjFxnW0sn1D0Uynqn10YPHb3PH6sn7tLnjfYnWbzPH-xn7tzn1nvPHnkP0KkTA-b5HD10Z7Wpyfqn1c40ZFMIA7M5H00mycqn7ts0ANzu1Ys0ZKs5H00UMus5H08nj0snj0snj00Ugws5H00uAwETjYk0ZFJ5H00uANv5gIGTvR0uMfqn6KspjYdPjDkPfKET1Yz0AFL5Hf0UMfqnsK1XWY1nWKxnH0snfKYIgnqPWnznH6YrjTLnWmdPHTznHR3r0Kzug7Y5HDdnHnkn1cdPjc4PHT0Tv-b5ycYuAwbnycsrHfvnWTsrHR0mLPV5HIKf1IAf1R3fYf1nYnYrDn0mynqnfKsUWYs0Z7VIjYs0Z7VT1Ys0ZGY5H00UyPxuMFEUHYsg1Kxn7ts0Aw9UMNBuNqsUA78pyw15HKxn7tsg100TA7Ygvu_myTqn0Kbmv-b5H00ugwGujYVnfK9TLKWm1Ys0ZNspy4Wm1Ys0Z7VuWYkP6KhmLNY5H00uMGC5H00uh7Y5H00XMK_Ignqn0K9uAu_myTqnfK_uhnqn0KLuMFEUHY3PjwB0APzm1YYn1nYr0&qid=b4ddd1b094627095&sourceid=160&placeid=1&rank=1&shh=m.baidu.com&word=%E5%94%90%E5%B1%B1%E5%90%8C%E4%BB%81%E4%B8%8D%E5%AD%95%E5%8C%BB%E9%99%A2&sht=844b&ck=803.132.194.343.400.264.1.0.0.194&rf2=.343&msg=&e=tiaozhuan&d=1513132670581
# http://mbc.zoossoft.cn/LR/Chatpre.aspx?id=MBC59176407&cid=1513132589268454686813&lng=cn&sid=1513132589268454686813&p=http://3g.buyunw.com/a/nxby/512.html?JJBD-BY1-ppc_tangshantongrenbuyunbuyuyiyuan&rf1=https://m.baidu.com/baidu.php?url=K600000-SwTdAzCGTImKFE_J8oWYqe22TUsEwbwo0nISN0pK9NxyvgwG71JVAmNysuIcXXGuzwdApg4GtNWl2BRGjp59M7JPG2GTiU8RrTBTBtYORCmXuPUwQqzc2VGFwLiNxiN3BIOcXDcFon95HFkaUJWRvYINOJx1zPmGdtj9-Hg7nf.7R_iTIg-x6Ymc8KDjnDgwxC6LN4rxxOpOvEg4uOgO_N4tXrZ-Cn4ClhmJj_YzmotAWK7x6YmPjqAKhFmhPMuvgtEKA_nYQ7IMu8LJ0.U1Yk0ZDq1nUFETv_znJz8qHfYoLR86Kspynqn0KY5T1AzULPonW2_oERYQ2eYOLiEIil0A-V5Hczn6KM5gI-rH00Iybq0ZKGujYknsKWpyfqn1c40AdY5HckrH-xnH0kPdt1PW0kg1csPHD0pvbqnfKzIjY1nWR0uy-b5HDznjbvP7tknHfdPHFxnH04P1Tvg1DkrH0YP-tknHb3njFxnHcsnHmvg1Dznjc4P-tknW0snW-xnHD4n161g1Dkrj63n7tknH63PWwxnHD3rjR1g1Dkrj61P7tknH6LrH-xnH0Ln1Ddg1DznjTLnsKBpHYznjuxnW0snjFxnW0sn1D0Uynqn10YPHb3PH6sn7tLnjfYnWbzPH-xn7tzn1nvPHnkP0KkTA-b5HD10Z7Wpyfqn1c40ZFMIA7M5H00mycqn7ts0ANzu1Ys0ZKs5H00UMus5H08nj0snj0snj00Ugws5H00uAwETjYk0ZFJ5H00uANv5gIGTvR0uMfqn6KspjYdPjDkPfKET1Yz0AFL5Hf0UMfqnsK1XWY1nWKxnH0snfKYIgnqPWnznH6YrjTLnWmdPHTznHR3r0Kzug7Y5HDdnHnkn1cdPjc4PHT0Tv-b5ycYuAwbnycsrHfvnWTsrHR0mLPV5HIKf1IAf1R3fYf1nYnYrDn0mynqnfKsUWYs0Z7VIjYs0Z7VT1Ys0ZGY5H00UyPxuMFEUHYsg1Kxn7ts0Aw9UMNBuNqsUA78pyw15HKxn7tsg100TA7Ygvu_myTqn0Kbmv-b5H00ugwGujYVnfK9TLKWm1Ys0ZNspy4Wm1Ys0Z7VuWYkP6KhmLNY5H00uMGC5H00uh7Y5H00XMK_Ignqn0K9uAu_myTqnfK_uhnqn0KLuMFEUHY3PjwB0APzm1YYn1nYr0&qid=b4ddd1b094627095&sourceid=160&placeid=1&rank=1&shh=m.baidu.com&word=wordtest&sht=844b&ck=803.132.194.343.400.264.1.0.0.194&rf2=.343&msg=&e=tiaozhuan&d=1513132670581

# https://m.baidu.com/baidu.php?url=K600000-SwTdAzCGTImKFE_J8oWYqe22TUsEwbwo0nISN0pK9NxyvgwG71JVAmNysuIcXXGuzwdApg4GtNWl2BRGjp59M7JPG2GTiU8RrTBTBtYORCmXuPUwQqzc2VGFwLiNxiN3BIOcXDcFon95HFkaUJWRvYINOJx1zPmGdtj9-Hg7nf.7R_iTIg-x6Ymc8KDjnDgwxC6LN4rxxOpOvEg4uOgO_N4tXrZ-Cn4ClhmJj_YzmotAWK7x6YmPjqAKhFmhPMuvgtEKA_nYQ7IMu8LJ0.U1Yk0ZDq1nUFETv_znJz8qHfYoLR86Kspynqn0KY5T1AzULPonW2_oERYQ2eYOLiEIil0A-V5Hczn6KM5gI-rH00Iybq0ZKGujYknsKWpyfqn1c40AdY5HckrH-xnH0kPdt1PW0kg1csPHD0pvbqnfKzIjY1nWR0uy-b5HDznjbvP7tknHfdPHFxnH04P1Tvg1DkrH0YP-tknHb3njFxnHcsnHmvg1Dznjc4P-tknW0snW-xnHD4n161g1Dkrj63n7tknH63PWwxnHD3rjR1g1Dkrj61P7tknH6LrH-xnH0Ln1Ddg1DznjTLnsKBpHYznjuxnW0snjFxnW0sn1D0Uynqn10YPHb3PH6sn7tLnjfYnWbzPH-xn7tzn1nvPHnkP0KkTA-b5HD10Z7Wpyfqn1c40ZFMIA7M5H00mycqn7ts0ANzu1Ys0ZKs5H00UMus5H08nj0snj0snj00Ugws5H00uAwETjYk0ZFJ5H00uANv5gIGTvR0uMfqn6KspjYdPjDkPfKET1Yz0AFL5Hf0UMfqnsK1XWY1nWKxnH0snfKYIgnqPWnznH6YrjTLnWmdPHTznHR3r0Kzug7Y5HDdnHnkn1cdPjc4PHT0Tv-b5ycYuAwbnycsrHfvnWTsrHR0mLPV5HIKf1IAf1R3fYf1nYnYrDn0mynqnfKsUWYs0Z7VIjYs0Z7VT1Ys0ZGY5H00UyPxuMFEUHYsg1Kxn7ts0Aw9UMNBuNqsUA78pyw15HKxn7tsg100TA7Ygvu_myTqn0Kbmv-b5H00ugwGujYVnfK9TLKWm1Ys0ZNspy4Wm1Ys0Z7VuWYkP6KhmLNY5H00uMGC5H00uh7Y5H00XMK_Ignqn0K9uAu_myTqnfK_uhnqn0KLuMFEUHY3PjwB0APzm1YYn1nYr0

# openurlstring="http://ie.icoa.cn/"


# 加密混淆
# https://pyprotect.angelic47.com/


keywordlist=[
"男科医院哪家最好",
"正规男科",
" 男科 排名",
"最权威的男科医院",
"男科医院",
"前列腺最好的医院",
"前列腺炎 治",
"中医治疗前列腺炎",
"年轻人 前列腺炎 ",
"前列腺炎相关检查",
"早射的调理小窍门",
"前列腺炎症状",
"龟头脱皮",
"男人一般几分钟射",
"早泄",
"男科医院",
"龟头有红斑",
"阴囊潮湿是怎么回事",
"湿疹图片",
"肾虚的症状有哪些",
"尿液浑浊",
"龟头炎",
"持久不射的方法",
"正常的性生活",
"早射是什么原因引起的",
"前列腺炎吃什么药",
"前列腺按摩",
"尿频尿急是怎么回事",
"睾丸疼痛",
"睾丸静脉",
"包皮过长的危害",
"珍珠疹",
"早泄怎么办",
"早泄的症状",
"阴虱是怎么引起的",
"性生活多长时间正常",
"小便刺痛",
"太敏感了怎么办",
"尿路感染",
"男人的功能",
"男科医院哪家好",
"男科哪家好",
"龟头炎图片大全",
"龟头上有红点",
"灌南男科医院",
"割包皮要多久恢复",
"睾丸炎",
"蛋疼咋回事",
"不持久怎么办",
"补肾壮阳的最佳方法",
"包皮炎早期图片",
"正常性生活",
"正常男人的阳茎图片",
"怎么样才能忍住不射",
"怎么射快",
"怎么控制射精",
"早谢是什么原因引起的",
"早谢能治好吗",
"早泄怎么治疗",
"早泄费用",
"在线咨询",
"阴囊瘙痒",
"阴囊潮湿",
"一直想上厕所但尿只有一点",
"阳痿吃什么药",
"阳萎可以做手术吗",
"阳萎",
"性兴奋",
"性生活娱乐网",
"小肚子坠痛怎么回事",
"小便有泡沫",
"小便时尿道刺痛",
"小便浑浊",
"提高勃起硬度的方法",
"生殖器疱疹图片初期",
"生殖器疱疹",
"肾虚的表现",
"什么是滑精",
"射得太快怎么办",
"蛇胆疮",
"前列腺炎",
"前列腺病自我按摩图解",
"疱疹图片",
"尿尿分叉怎么回事",
"尿黄是什么原因引起的",
"尿分叉是怎么回事",
"尿多是什么原因",
"尿道炎",
"尿不尽是怎么回事",
"男性霉菌感染症状",
"男科医院",
"老公勃起一会就软",
"尖锐",
"龟头隐隐作痛",
"龟头痒",
"龟头炎用什么软膏",
"龟头炎会自己康复吗",
"龟头上有小红点",
"龟头上有红斑是什么病",
"龟头敏感",
"龟头发紫怎么回事啊",
"灌南男泌尿外科",
"功能性",
"割包皮最佳年龄",
"割包皮一般要多少钱",
"睾丸疼痛是怎么回事",
"肚子胀疼怎么回事",
"持久",
"吃什么补肾",
"勃起功能障碍怎么锻炼",
"包皮炎用什么药膏",
"包皮系带手术",
"包皮手术最佳年龄",
"包皮手术",
"包皮切除后悔了图片",
"包皮过长的图片",
"百度",
"3年没有性生活",
"1001问夫妻性生活",
"做完包皮手术",
"做完包茎手术怎么降低龟头敏感度",
"做完爱下面痛怎么回事",
"做了包皮手术后要注意什么",
"做爱一般多长时间",
"做爱一般多久算正常",
"做爱时间短怎么调理",
"做爱时间短怎么回事",
"做爱时间短",
"做爱后下面痒怎么办",
"做爱龟头裂了出血",
"做爱多久好呢",
"做爱多久",
"左右腹部疼痛是啥原因",
"左侧睾丸肿大疼痛是怎么回事",
"左边睾丸疼痛是什么原因",
"最近硬不起来怎么回事",
"最近性功能不行怎么办",
"最近老是感觉有尿意",
"足跟痛是怎么回事",
"壮阳食物",
"中医男科性功能障碍",
"中年男人怎样提高性能力",
"治早射最好的药",
"治前列腺炎要注意什么",
"治疗早泄的手术叫什么",
"治疗早泄吃什么药",
"治疗早泄",
"治疗早射吃什么西药",
"治疗阳痿早泄的药",
"治疗阳瘘最佳西药",
"治疗前列腺有哪些仪器",
"治疗皮炎湿疹的偏方",
"值是什么意思",
"直不起来怎么办",
"支原体阳性是什么意思",
"支原体感染症状",
"正常性生活一次多长时间正常",
"正常男生阴囊的图片",
"正常男人几分钟",
"正常龟头图片",
"正常龟头的表面图片",
"正常的尿液是什么颜色的",
"正常的男人一次多长时间",
"正常的包皮图片",
"正常包皮图片",
"正常包皮图",
"真菌感染怎么治",
"真的阳痿",
"珍珠疹和尖锐湿区分图",
"长期手淫",
"增粗的方法",
"怎样做龟头按摩",
"怎样自检睾丸是否坏死",
"怎样知道自己是不是肾虚",
"怎样让阴痉快速硬起来",
"怎样可以延长做爱时间",
"怎样解决早射",
"怎样过性生活",
"怎样防止包皮创伤",
"怎么知道自己人阳虚还是阴虚",
"怎么增加硬度",
"怎么样的包皮正常图片",
"怎么样才能提高性功能",
"怎么样才能让老婆高潮",
"怎么样才能不早泄",
"怎么提高勃起硬度",
"怎么取前列腺液",
"怎么能持久不射",
"怎么锻炼勃起功能",
"怎么锻炼",
"早泄症状的具体表现",
"早泄怎样治",
"早泄咋办",
"早泄有哪些症状",
"早泄是怎么引起",
"早泄如何治疗",
"早泄可以手术治疗吗",
"早泄会影响生育吗",
"早泄多吃什么",
"早泄的调理",
"早泄吃什么药",
"早射吃什么最好",
"早上尿绿色怎么回事",
"早期症状图片",
"在学校便秘怎么办",
"在线医生免费咨询",
"在做割包皮手术要多少钱",
"幼儿白细胞高的原因及危害",
"有前列腺炎要注意什么",
"有尿意却尿不出来",
"游泳池的面积",
"硬度不足",
"硬度",
"硬的时间不长怎么办",
"硬的慢软的快",
"引起早泄的主要原因",
"阴虚和阳虚的区别",
"阴襄潮湿是什么原因引起的",
"阴囊湿怎么办",
"阴囊上面肿了怎么消炎",
"阴囊破个口子",
"阴囊里有个小疙瘩是怎么回事",
"阴囊冷的是怎么回事",
"阴囊潮湿怎么回事",
"阴囊潮湿用什么药最好",
"阴囊潮湿瘙痒用什么药",
"阴痉珍珠状丘疹",
"阴痉长小疙瘩图片",
"阴痉向左弯曲怎么矫正",
"阴痉冠状沟里那个小颗粒",
"阴痉短小怎么办",
"阴胫痒有白色分泌物",
"阴胫敏感",
"阴茎珍珠疹",
"阴茎珍珠样丘疹病",
"阴茎又上方疼痛",
"阴茎有时觉得痒有时又不痒是怎么回事",
"阴茎弯曲的初期症状",
"阴茎弯曲",
"阴茎头有点裂",
"阴茎痛",
"阴茎上做个伤口有影响吗",
"阴茎上的包皮痒痒怎么回事",
"阴茎皮长了硬硬的包",
"阴茎疱疹",
"阴茎敏感神经真皮植入隔离术",
"阴茎敏感",
"阴茎毛囊炎图片",
"阴茎麻木",
"阴茎过长",
"阴茎短小",
"阴茎勃起无力",
"阴茎勃起很快就软了",
"阴道外面阴毛上面痒痒痒怎么回事",
"医生在线咨询",
"一直有尿意怎么回事",
"一直都有尿意",
"一个睾丸影响性功能吗",
"一搬泌尿炎症治疗多少钱",
"一般化验血多少钱",
"一般夫妻生活多久一次",
"一般多久射精才正常",
"叶剑飞鸡巴有多大",
"尧利专注男性健康",
"腰椎间盘突出",
"腰痛怎么治疗",
"阳痿怎么治",
"阳痿早泄怎么治",
"阳痿早泄可以治愈吗",
"阳痿早泄吃肾宝行吗",
"阳痿早泄",
"阳痿有什么症状",
"阳痿是什么原因",
"阳痿如何",
"阳痿会对身体有什么危害",
"阳痿费用",
"阳痿的症状",
"阳痿吃伟哥管用吗",
"阳痿吃什么食物",
"阳萎早谢吃什么药最好",
"阳萎早期症状表现图",
"阳萎都43岁了能治好吗",
"阳萎勃不起来吃什么药好",
"阳具溃烂",
"羊睾丸",
"验尿能验出什么",
"厌氧菌感染症状",
"延长性",
"修正壮阳药哪个效果好",
"胸前背后长痘痘是什么原因",
"性时间多久是正常",
"性生活中变",
"性生活一般多长时间为宜",
"性生活一般多长时间",
"性生活一般多久一次",
"性生活问题",
"性生活图片",
"性生活时间短治疗",
"性生活时间短怎么调理",
"性生活时",
"性生活后有异味是怎么回事",
"性生活过多吃什么补",
"性生活龟头敏感度",
"性生活多长时间最合适",
"性生活不勃起困难",
"性神经衰弱怎么检查",
"性神经衰弱的症状",
"性冷淡",
"性功能障碍探查术什么意思",
"性功能障碍术费用",
"性功能减退是什么原因",
"性功能减退什么原因",
"性功能检查大概多少钱",
"性多长时间",
"性持久的锻炼方法",
"新浦哪家医院查男科好",
"心理医生免费咨询",
"心理性性冷淡",
"小孩说尿尿尿出血了怎么办",
"小孩包皮过长怎么清洗",
"小腹胀胀的",
"小腹痛是怎么回事",
"小腹大是什么原因",
"小肚子左下角隐隐作痛",
"小肚子胀痛咋回事",
"小便有白色浑浊物图片",
"小便有白色浑浊物",
"小便味道重是什么原因",
"小便疼痛是怎么回事",
"小便酸碱度正常值多少",
"小便频繁如何治疗",
"小便尿道刺痛能自愈么",
"小便尿不出来",
"小便难排",
"小便量少次数多",
"小便经常黄是什么原因",
"小便混浊有白色沉淀物",
"小便浑浊是什么原因",
"小便会刺痛吃什么药",
"小便带血",
"小便带精液",
"小便带白色混浊物",
"小便刺痛吃什么药",
"小便次数多是怎么回事",
"小便不出来还痛怎么办",
"现在市场上那种补肾壮阳效果好",
"夏天手上起小水泡痒怎么办",
"下体总是痒",
"下身长水泡",
"下面长了疙瘩什么原因",
"下面痒带点血怎么办",
"下腹痛",
"系带断了有什么影响",
"息肉",
"吸烟对性功能的危害",
"我想看男科",
"为什么做爱时间长",
"为什么阴囊总是湿的",
"为什么小便会有血",
"为什么手淫很快射精",
"为什么射完精之后睾丸就会发冷",
"为什么射得很快",
"为什么会得前列腺炎",
"网上预约门诊",
"外阴瘙痒有小疙瘩图片",
"外国人的阴茎和图片",
"头疼怎么办最快最有效吃什么",
"同房后出血为什么呢",
"体寒怎么调理",
"淘宝",
"损人不利己",
"搜索蛇胆疮",
"搜狗",
"睡醒了口甘什么原因",
"水花和湿疹一样吗",
"水痘的症状和治疗",
"手淫早泄怎么治疗",
"手淫有害吗",
"手淫引起的早泄怎么办",
"手脱皮怎么办",
"手上起小疙瘩很痒怎么回事",
"世界上最粗的阴茎",
"时间短怎么治",
"石家庄平山县哪家医院治肾虚好",
"十岁男孩阴茎勃起多大",
"湿疹锌软膏",
"湿疹的症状",
"湿疹",
"虱子怎么去除",
"虱子是怎么产生的",
"生殖器图片",
"生殖器疱疹图片",
"生殖感染疱疹用什么消炎药",
"生虱子的原因",
"肾阴虚影响性功能吗",
"肾阴虚的表现",
"肾阴虚吃啥好",
"肾炎症状",
"肾虚怎么调理",
"肾虚会影响怀孕吗",
"肾虚吃什么食物能补",
"肾亏",
"肾不好不能吃什么东西",
"什么药治早射最好",
"什么药补肾效果最好",
"什么样龟头正常",
"什么延迟喷剂好",
"什么是尖锐湿庞图片",
"什么是病毒疣",
"什么是包皮手术过程",
"什么是包茎过长",
"什么食物能补肾",
"什么叫阳痿",
"身上起红疙瘩很痒怎么办",
"射完尿尿疼",
"射精有血是什么",
"射精延迟",
"射精无力",
"射精太快有什么办法",
"射精时射出一小块固体",
"射精什么颜色正常",
"射精困难症",
"射精快的原因",
"射精过快",
"蛇胆疮怎么治",
"蛇胆疮初期图片",
"三级彩超什么时候做",
"撒尿有白色沉淀物",
"撒尿时尿道刺痛",
"乳头疼怎么回事",
"乳头上的小疙瘩叫什么",
"如何提高性生活",
"如何让阴径变长",
"如何快速锻炼腹肌",
"如何快速勃起",
"如何降低龟冠敏感度",
"如何改善早泄",
"如何锻炼性功能",
"如何持久",
"如何补肾壮阳小方法",
"如果有炎症做性生活男性会不会有龟头炎",
"人乳头瘤病毒45阴性",
"去医院挂号怎么挂",
"去包皮多少钱",
"丘疹",
"轻度阳痿吃什么",
"青少年早泄的调理",
"切完包皮有什么好处",
"切包皮对薄起有影响吗",
"前列腺注射疗法",
"前列腺肿瘤",
"前列腺增生用什么药",
"前列腺增生吃什么药",
"前列腺怎么治疗的方法",
"前列腺怎么检查",
"前列腺有灼热感",
"前列腺溢液",
"前列腺液怎么取出来的",
"前列腺炎治疗仪",
"前列腺炎原因是什么",
"前列腺炎有什么症状",
"前列腺炎有哪些症状",
"前列腺炎有哪些危害",
"前列腺炎需要注意哪些",
"前列腺炎手术大概多少钱",
"前列腺炎能彻底治愈吗",
"前列腺炎会自愈吗",
"前列腺炎发病原因",
"前列腺炎的自我疗法",
"前列腺炎的治疗需要多少钱",
"前列腺炎吃中药好还是西药好",
"前列腺炎艾灸什么穴位",
"前列腺需要做什么检查",
"前列腺性生活会传染吗",
"前列腺小囊肿手术费用",
"前列腺腔道介入治疗法",
"前列腺脓细胞",
"前列腺能过性生活",
"前列腺内部回声不均匀",
"前列腺囊肿吃什么药",
"前列腺挂水有用吗",
"前列腺感染什么症状",
"前列腺肥大是什么样子图片",
"前列腺肥大会疼吗",
"前列腺肥大吃什么食物",
"前列腺大会影响生育吗",
"前列腺吃什么药最管用",
"前列腺吃什么药",
"前列腺吃什么好",
"前列腺超声检查疼吗",
"前列腺曾生公鸡能吃吗",
"前列腺闭通片治疗什么的",
"前列腺癌",
"前列腺",
"前列线癌",
"前列什么闭通",
"前列倍喜胶囊多少钱",
"普乐安片",
"苹果有哪些营养",
"频繁小便是怎么回事",
"屁股沟上长个疙瘩",
"皮炎湿疹",
"皮肤科专家在线",
"盆腔积液有哪些症状",
"疱疹怎么引起的",
"疱疹图片初期症状",
"疱疹是怎么引起的图片",
"疱疹是怎么引起的",
"疱疹能彻底治愈吗",
"膀子上长了好多小红点",
"膀胱炎的症状",
"膀胱炎",
"膀胱过度活动必须做输尿管扩张吗",
"排卵期多长时间同房一次最好",
"啪啪一半软了的原因",
"欧式包皮手术恢复需要拆线吗",
"女医生的男科病诊所",
"女人性交水多是什么原因",
"女人尿带红色怎么回事",
"女人怀孕的前兆",
"尿隐血阳性是什么意思",
"尿隐血1十是什么",
"尿液里有白色沉淀物",
"尿液混浊有白色沉淀",
"尿液发黄而且尿痛尿频",
"尿液发黄",
"尿无力尿不尽是怎么回事",
"尿完尿后有白色液体",
"尿少尿黄什么原因",
"尿频是怎么回事",
"尿频尿急小腹胀痛是怎么回事",
"尿频尿急尿痛吃什么药",
"尿频尿不尽",
"尿频吃西药好的快还是中药",
"尿泡沫",
"尿尿有灼热感",
"尿尿有一点微痛",
"尿尿有血怎么回事而且疼",
"尿尿疼怪什么",
"尿尿的时候疼",
"尿路系统感染",
"尿路感染怎么造成的",
"尿路感染怎么回事",
"尿路感染怎么办",
"尿路感染的症状",
"尿路感染吃什么消炎药",
"尿检时候有白细胞高为啥",
"尿检查什么",
"尿急是怎么回事",
"尿急憋不住",
"尿管疼还有分泌物",
"尿感染吃什么药可以治",
"尿分叉是怎么回事男性",
"尿分叉吃什么药比较好",
"尿发红",
"尿多去医院看什么科",
"尿多屁多怎么回事",
"尿毒症早期小便症状",
"尿滴白是怎么回事",
"尿等待是怎么回事",
"尿道痒怎么回事",
"尿道痒痒",
"尿道炎症状",
"尿道炎怎样引起的",
"尿道炎什么症状男性",
"尿道炎吃什么药最好",
"尿道微疼怎么了",
"尿道流脓是什么病",
"尿道口有白色分泌物还尿痛",
"尿道口发红的原因",
"尿道口",
"尿道黄色脓状物",
"尿道很痒很痒怎么回事",
"尿道感染的症状图片",
"尿道感染的症状",
"尿道感染",
"尿道发炎什么症状",
"尿道发炎吃什么药最好",
"尿到最后有精液滑出",
"尿出白色浑浊液体",
"尿常规是查什么的",
"尿常规挂什么科",
"尿常规多久出结果",
"念珠菌感染",
"年轻人早泄的原因",
"能勃起到时间不长",
"脑梗塞的症状",
"南京最好治早泄专家",
"南京军区总医院护士照",
"南京鼓楼医院生殖中心",
"男子医院mbaiducom",
"男子哪里好",
"男子检查不育",
"男孕前检查项目baiduresults",
"男姓生殖器包皮图片",
"男性珍珠疹初期图片",
"男性早些泄怎么治疗",
"男性一般多大岁数性功能开始减退",
"男性性生活",
"男性小便痛怎么回事",
"男性小便后擦拭有血",
"男性生殖图像",
"男性生殖器水肿怎么办",
"男性生殖器起红点图片",
"男性生殖器官多少公分才算正常图",
"男性生殖器多大才正常",
"男性生殖器",
"男性生育体检",
"男性膀胱炎怎么检查",
"男性尿频吃什么药",
"男性尿尿暗红色",
"男性尿道痒吃什么药",
"男性尿道刺痛吃什么药",
"男性念路菌",
"男性内分泌六项检查就抽血",
"男性科疾病",
"男性健康论谈",
"男性疾病咨询",
"男性疾病挂什么科",
"男性患有白色念珠菌到哪科看",
"男性龟头敏感容易射",
"男性感染霉菌有什么症状",
"男性感染霉菌的症状",
"男性多长时间正常",
"男性滴虫怎么治疗",
"男性滴虫病的治疗",
"男性晨勃图片",
"男性勃起不能随心所欲",
"男性包皮图片",
"男性白色念珠菌感染",
"男下面痒红肿",
"男士有没有感染霉菌怎么检查",
"男士阴茎疼是什么原因",
"男士性",
"男士前列腺炎有哪些症状",
"男士得霉菌有什么症状",
"男士b超检查什么",
"男牲生殖器",
"男生殖器疱疹图",
"男生殖器",
"男生私处痒是怎么回事",
"男生尿道痒怎么回事",
"男什么时候不长高了",
"男上厕所尿道疼",
"男人做多长时间算正常",
"男人正常多大尺寸",
"男人硬不起来怎么办",
"男人硬不起的七大原因",
"男人阴囊潮湿怎么办",
"男人阴经标准多长",
"男人一天最多射几次",
"男人性方面性不起来是怎么回事",
"男人小腹胀痛尿频尿急",
"男人小便有白汁什么原因",
"男人小便多是什么原因",
"男人下体瘙痒怎么回事",
"男人为何疲软",
"男人私处",
"男人时间短是怎么回事",
"男人生殖照片",
"男人生殖器",
"男人肾虚症状有哪些",
"男人肾虚什么表现",
"男人肾虚吃什么补得快",
"男人射精快怎么调理",
"男人如何延长时间",
"男人容易射",
"男人尿频尿急的原因",
"男人尿尿开叉",
"男人胯部瘙痒",
"男人可以射多少次精",
"男人喝蜂蜜对性功能",
"男人鬼头起个泡吃什么药",
"男人龟头炎是什么原因",
"男人睾丸一个大一个小",
"男人多长时间算持久",
"男人多少岁性功能开始下降",
"男人的性功能最强年龄",
"男人的尿到痒痒咋了",
"男人的包皮正常图片",
"男人床上多久才算正常",
"男人持续射精会怎么样",
"男人吃什么对身体好",
"男人吃什么补品比较好",
"男人吃什么",
"男人晨勃是什么原因",
"男人晨勃到多大年龄段",
"男人不举",
"男人不行的原因",
"男人被感染霉菌怎么办",
"男人保养性功能",
"男人包皮图片",
"男朋友早射是什么原因",
"男朋友射太快怎么办",
"男朋友射的太快怎么办",
"男科疾病",
"男科都是私立医院吗",
"男科病查询",
"男科",
"男方孕前检查",
"男的生殖器官痒痒怎么回事",
"男的射的快",
"男的尿道炎原因是什么",
"奶子好吃吗",
"那些中草药补肾",
"那些食品有助于伤口愈合",
"哪些龟头最好",
"目前狐臭最好的是哪个手术",
"摩擦龟头降低敏感度",
"免费在线咨询",
"泌尿系统感染的原因",
"泌尿系感染治疗方法",
"泌尿外科医生",
"霉菌性包皮龟头炎用什么药",
"霉菌感染用什么药",
"霉菌",
"玫瑰糠疹",
"没有性",
"没有精子怎么办",
"慢性前列腺炎",
"罗红霉素附睾炎",
"卵巢皮痒男性",
"炉甘石洗剂",
"六味地黄丸治早迣吗",
"六味地黄丸哪个牌子好",
"六味地黄丸",
"淋菌性尿道炎的症状",
"淋巴发炎怎么办",
"良性前列腺增生的典型症状是",
"最知名男科医生",
"有哪些医院",
"一医",
"市第一人民医院病房图片",
"市第一人民医院",
"人民医院男科怎么样",
"人民医院妇科",
"男性医院有哪些医院",
"男科中医",
"男科医院收费贵吗",
"男科医院排名榜",
"哪家医院治疗阳痿早泄比较好",
"哪几家男性医院最好",
"哪个医院男科医院",
"哪个男科不坑人",
"哪个男科",
"泌尿科",
"看中医肾虚哪个医院好",
"看男科哪家好",
"人民医院怎么样",
"人民收费合理",
"人民男科医院",
"割包皮多少钱啊",
"第一人民医院泌尿科什么时候可以挂门诊",
"比较好的男性医院有哪些",
"老中医壮阳药",
"老男人包皮图",
"老急尿尿怎么回事",
"老公时间短怎么办",
"老公很快就射了",
"裤裆潮湿是怎么回事",
"空乘专业有本科吗",
"看性功能障碍挂什么科",
"皲裂性湿疹",
"人民男科医院好不好",
"靖边泌尿专科医院好不好",
"精子活力不够怎么调理",
"精子红色的严重后果",
"精子发黄",
"精子多会胀痛吗",
"精子带血是什么原因",
"精子成块",
"精子不液化",
"精液检查多长时间出结果",
"精索静脉手术是皋丸做手术",
"精索静脉曲张会导致阳痿早泄吗",
"精囊炎吃什么药",
"精毫炎",
"经常闹肚子拉稀怎么办",
"进口玛卡和国产玛卡的区别",
"今天紫铜价格",
"疥疮是什么病",
"芥疮的症状及图片",
"结晶尿",
"轿车提速时有点抖怎么回事",
"脚后跟疼是肾虚吗",
"酱豆腐的功效",
"降低龟头敏感度",
"降低龟头灵敏度的方法",
"江苏省东海县人民医院泌尿外科的专家",
"健康的正常的龟头图片",
"坚而不久是什么原因",
"坚而不久",
"尖锐湿尤图",
"尖锐湿庞怎么治疗",
"尖锐湿庞早期图片",
"尖锐湿庞图片",
"假性尖锐疣",
"几天同一次房才正常的",
"急性浅表性龟头炎图",
"急性前列腺怎么得的",
"鸡巴小感觉自卑而且射精快有什么可以调理",
"婚检都检查什么项目",
"汇仁肾宝片效果怎么样",
"汇仁肾宝片",
"黄色液体",
"环状肉芽肿",
"环切术",
"环切包皮手术后恢复图",
"化脓性阴囊皮炎",
"滑精是怎么回事",
"滑精和溢精",
"后背长痘痘是什么原因",
"韩式包皮环切术",
"海绵体修复",
"过夫妻生活",
"国建医院",
"鬼头痒痒有白色物",
"鬼头脱皮发白",
"鬼头上有红点不痛不痒怎么回事",
"龟头皱",
"龟头周围有小颗粒图片",
"龟头正常肉粒图片",
"龟头长红点子",
"龟头长疙瘩图片",
"龟头怎么白色东西",
"龟头有异味",
"龟头有小红点还脱皮",
"龟头有小红点不痛不痒",
"龟头有小红点",
"龟头有红疙瘩挂什么科",
"龟头有红点是什么病症",
"龟头有白色的小泡图片",
"龟头疣图片初期图片",
"龟头痒是什么引起的",
"龟头痒的图片",
"龟头炎怎么治疗",
"龟头炎用什么药好的快",
"龟头炎要怎么治疗",
"龟头炎图片",
"龟头下面的筋断图片",
"龟头污垢洗不干净",
"龟头脱皮有点肿痒",
"龟头痛是什么原因引起",
"龟头疼痛流脓吃什么药",
"龟头疼是什么原因引起",
"龟头疼",
"龟头太敏感容易射精怎么办",
"龟头水肿",
"龟头上长小肉疙瘩",
"龟头上有小红点痒痒的",
"龟头上小红点",
"龟头上起红色点点图片",
"龟头上面长小肉刺怎么回事",
"龟头起了一块一块的红",
"龟头破",
"龟头那里隐隐作痛",
"龟头敏感度高吃什么药",
"龟头糜烂的症状和图片",
"龟头没感觉",
"龟头毛囊炎传染吗",
"龟头流出黄液什么原因",
"龟头会分泌粘液",
"龟头冠状沟",
"龟头沟里有白色分泌物",
"龟头分泌物很多包皮痒痒",
"龟头放墙上摩擦好嘛",
"龟头出现红点",
"龟头边缘有红点",
"龟头边上起来疙瘩是咋回事",
"龟头包皮炎初期图片",
"龟头包皮炎",
"龟头包茎可以剪了吗",
"灌云专业男科医院",
"灌云县医院",
"灌云县那家医院治男性专科",
"灌云男科医院",
"灌南医院刘静恩",
"灌南新中医院",
"灌南新区医院",
"灌南仁慈医院",
"灌南哪家看男科病的",
"灌南华山医院电话",
"灌南华山医院",
"骨折哪家医院好",
"佝偻病的早期症状",
"功能性障碍",
"公鸡睾丸的作用与功效",
"割完包皮注意事项",
"割完包皮需要换什么药",
"割完包皮图片",
"割完包皮会比以前的大吗",
"割完包皮多久消肿",
"割了包皮有什么好处和坏处",
"割包皮有什么用",
"割包皮要住院多久",
"割包皮要多少钱呀",
"割包皮要多久才能过性生活",
"割包皮五天伤口要勤换沙布吗",
"割包皮图片",
"割包皮是什么意思",
"割包皮视频",
"割包皮全过程",
"割包皮麻醉药打在哪",
"割包皮几天可以拆纱布",
"割包皮环切器多久会掉",
"割包皮后能让它勃起吗",
"割包皮后悔死了",
"割包皮后多久能过性生活",
"割包皮后多久可以同房",
"割包皮后吃什么好得快",
"割包皮好不好",
"割包皮多少钱多久康复",
"割包皮多久不包沙布",
"割包皮的利与弊",
"割包皮的坏处",
"割包皮",
"睾丸胀痛是怎么回事",
"睾丸胀痛是什么原因",
"睾丸胀痛",
"睾丸有筋小腹有点疼",
"睾丸一大一小正常吗",
"睾丸痒越挠越痒还褪皮",
"睾丸炎症状",
"睾丸炎是怎么引起的",
"睾丸炎的症状",
"睾丸图片",
"睾丸疼挂什么科",
"睾丸疼吃什么药最有效",
"睾丸特别痒",
"睾丸上有小疙瘩",
"睾丸上有个小硬疙瘩",
"睾丸上有白色疙瘩图片",
"睾丸起皮图片",
"睾丸起皮的症状图片",
"睾丸扭转容易复发吗",
"睾丸扭转",
"睾丸很黏",
"睾丸肥大是什么情况",
"睾丸发肿是什么原因",
"睾丸出汗潮湿是怎么回事",
"睾丸潮湿怎么回事",
"睾丸",
"睾酮",
"肛门周围长了很多小疙瘩",
"肛门湿疹怎么治",
"肛门很疼是什么原因",
"刚进去就射了",
"赣榆县中医院男科",
"赣榆县医院",
"赣榆男科医院哪个好",
"赣榆男科医院",
"腹部胀痛是什么原因",
"腹部胀痛",
"附睾炎图片",
"附睾炎是怎么引起的",
"附睾炎能根治吗",
"附睾炎吃什么中药调理",
"附睾炎吃什么药最有效",
"妇科检查项目",
"夫妻多久一次性生活",
"夫妻保健",
"多少时间射算正常",
"多少秒达不到属于早泄",
"对男人性功能好的方法",
"锻炼身体可以延长性生活时间吗",
"锻炼可以治疗肾虚吗",
"锻炼龟头不敏感的方法",
"肚子右侧疼怎么回事",
"东海医院",
"东海新人民医院治男科好吗",
"东海县同济医院",
"东海县仁慈医院",
"东海县人民医院男科好不好",
"东海县人民医院男科",
"东海县人民医院泌尿科几点上班",
"东海县人民医院官网",
"东海县男科医院有哪些",
"东海县地图",
"东海同济医院割包皮多少钱",
"东海玛丽亚",
"滴虫性阴炎症状",
"滴虫病男性",
"得前列腺都有什么症状",
"到了夏天为什么会尿急尿频",
"蛋蛋一大一小正常吗",
"蛋蛋潮湿是什么原因",
"蛋白尿怎么引起的",
"单纯疱疹是怎么引起的",
"带状疱疹怎么治疗",
"大阴茎射精",
"大便时阴道流血是怎么回事",
"刺激",
"春天什么汤补肾",
"传染性软疣",
"处女真人照片放大提醒",
"抽烟影响性功能吗",
"宠物在线医生免费咨询",
"吃什么壮阳延长时间",
"吃什么中药补肾效果最好",
"吃什么药对肝有损伤",
"吃什么药不射精",
"吃什么能增强性功能",
"吃什么能马上壮阳",
"吃什么能持久不射",
"吃什么可以冶疗早泄",
"吃什么对前烈腺炎有好处",
"吃什么对勃起硬度好",
"吃什么补肾壮阳最快",
"吃啥药管闪腰",
"成年人尿床怎么回事",
"藏药阳痿早泄",
"菜花病早期症状",
"不举是什么原因",
"不持久是怎么回事",
"博爱医院",
"勃起硬度",
"勃起心里障碍怎么治疗",
"勃起时龟头上有小丘疹正常吗",
"勃起久了睾丸会痛坠痛",
"勃起后为什么很快就软",
"勃起后出来透明的液体",
"勃起的时候疼是怎么了",
"勃起不硬还短是怎么回事",
"勃起不坚吃些什么好",
"病前列腺炎怎么治疗",
"病毒性疱疹图片大全",
"病毒性感染的症状",
"标准的包皮后的图片",
"必利劲官网",
"北京男科医院那强",
"宝宝包皮过长图片",
"包皮肿了一圈",
"包皮有什么用",
"包皮炎症状",
"包皮炎用什么药最有效",
"包皮炎用什么药",
"包皮系带",
"包皮水肿",
"包皮术后水肿怎样消除",
"包皮手术要多少钱左右",
"包皮手术视频全过程",
"包皮手术十天后图片",
"包皮手术后龟头水肿图",
"包皮手术后勃起系带疼",
"包皮手术后勃起",
"包皮手术过程",
"包皮手术多长时间可以做爱",
"包皮手术多少钱一般多少钱",
"包皮手术多少钱",
"包皮手术多久可以洗澡",
"包皮手术10天能洗澡吗",
"包皮是不是必须要切掉",
"包皮上长痘痘",
"包皮上有小红点",
"包皮切除后的图片欣赏",
"包皮尿垢多",
"包皮内侧破了流血",
"包皮裂口",
"包皮里面破了怎么回事",
"包皮拉伤会不会有事",
"包皮会引起早泄吗",
"包皮环切一六天啦有一个点出血",
"包皮环切术脱落前图片",
"包皮环切手术愈合图片",
"包皮环切后多久能同房",
"包皮和没包皮的区别图",
"包皮过长是什么样子",
"包皮过长不割好吗",
"包皮龟头炎怎么治",
"包皮垢增多",
"包皮垢图片",
"包皮垢",
"包皮割了多久可以康复",
"包皮割多了怎么办",
"包皮割多了",
"包皮割掉后龟头敏感",
"包皮割掉后龟头干",
"包皮缝合器钉子脱落原理",
"包皮发炎",
"包皮多久可以同房",
"包皮不割有事吗",
"包茎手术恢复过程图",
"包茎手术多少钱",
"包茎",
"办过事鸡巴红肿什么原因",
"百度搜索",
"百度男人尿频尿急的原因",
"白细胞正常值范围",
"白细胞高的原因及危害",
"白色念珠菌怎么治疗",
"白色念珠菌感染龟头",
"白带异常的症状图片"
]



openurlstring=config['url']
keshiname=random.choice(config['keshi'])
userid=config['userid']
swtid=config['swtid']
browsername=config['browser']

maindomain=random.choice(config['domain'])

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

usearchword=random.choice(keywordlist)

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

if nowtime.hour>22	or nowtime.hour<0 :
	# f.close()
	# browser.quit()
	# exit()
	browserquit()



# # 函数定义


# 函数定义

#获取朋友消息
def get_friends_message(name):
	global starttime
	global fname
	global browser
	# time.sleep(10)
	# 获取所有的群组消息
	shorttime=0
	middletime=0
	laragetime=0
	while 1:
	# get_screenshot_as_file
	# browser.save_screenshot("/home/wwwroot/default/yiliao.png")
		try:
			nowtime=int(time.time())
			# get_all_person_message() 循环抓取联系人列表
			extract_person_message('gpname',1)	#只抓单个人的消息
			time.sleep(5)
			wechatid_for_play=genewechatid()



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
					slist=['那你联系我一下吧 。。'+wechatid_for_play,'医生。。。你加我微信吧 '+wechatid_for_play,'是要提供我微信号？','麻烦加我一下可以么。。。'+wechatid_for_play,'医生。。。麻烦加我微信 '+wechatid_for_play]
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
		except Exception, e:
			# raise e
			browserquit()


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

	# global browser

	name='gpname'

	# 获取所有的群组消息
	# while 1:
	# 	# get_all_person_message() 循环抓取联系人列表
	# 	# extract_person_message('gpname',1)	#只抓单个人的消息


	time.sleep(0.1)
	logging.info(u'----------------开始处理这次循环的消息---------')


	# 是否被对方手动结束对话
	# kschat_enddialog
	inputhtml=getelements(browser,'.other_msg')
	# inputhtml=browser.find_element_by_xpath("//div[contains(text(), '次对话已经结束! 如果您还')]")
	# inputhtml=browser.find_element_by_xpath("//div[@class='other_msg']")

	print('isover')
	for x in inputhtml:
		print(x.text)
		if '次对话已经结束! 如果您还' in x.text:
			browserquit()
	# if inputhtml!=None:
	# 	if inputhtml.is_displayed():
	# 		browserquit()

	# if len(inputhtml)>3:
	# 	pass
	# 	browserquit()


	try:
		listele=browser.find_elements_by_css_selector('.msg-box')
		# print(len(listele))
	except Exception, e:
		# raise e
		print(str(e))



	time.sleep(1)


	if_newmessage[name]=0
	sayarray=[]
	sysinfoarray=[]
	is_img=0

	try:

		if not lastsay.has_key(name):
			lastsay[name]=u'测试'
			print 'not have key'
			print lastsay[name]

		if not isayto.has_key(name):
			isayto[name]=u'测试'

		gpname=name
		logging.info(u' 当前好友名称 : '+gpname)

		time.sleep(0.3)
		#朋友聊天消息
		 # .msg_left .msg 
		listele=browser.find_elements_by_css_selector('.msg-box .msg-agent')
		# #msgArea	.msg-box .text
		#msg-box
		msglist_length=len(listele)
		print('msglist_length')
		print(msglist_length)

		time.sleep(0.1)
		logging.info(u' 该朋友聊天消息长度 : '+str(msglist_length))
		

		for ele in listele:
			# print ele.text.encode('utf-8')
			nickname= gpname

			try:
				usersay= ele.find_element_by_css_selector('.arrow_box_left .text').text
			except Exception, e:
				# raise e
				usersay= ele.find_element_by_css_selector('.text').text
			
			# time.sleep(0.1)
			logging.info(usersay)
				
			#替换不能识别的字符串	_web	class="emoji emoji1f48e"
			# replace

			# print '\n'
			# print '\n'

			sayarray.append({'nickname':nickname,'usersay':usersay})
		# print(sayarray)
		# # debug info
		# time.sleep(0.2)
		if len(sayarray)>0:
			# print len(sayarray)
			# print sayarray[len(sayarray)-1]['nickname']+sayarray[len(sayarray)-1]['usersay']
			
			logging.info(u'有历史消息')
			# print lastsay[name]
			logging.info(u'判断是否是新消息')

		else:
			logging.info(u'此人暂时无消息')

		# # 根据最新的聊天记录，判断上一次聊天记录，是否相同


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

			f.write('医生||'+ssay+'\n')


			#保存文本到数据库
			urlprefix='http://39.108.185.27/hospital/index.php?m=Api&c=user&a=talklog'
			urll =urlprefix+'&urole='+urllib.quote('医生'.encode('utf8'))+'&usay='+urllib.quote(ssay.encode('utf8'))+'&chatid='+str(userid)+'-'+str(fname)+'&userid='+str(userid)
			reqq = urllib2.Request(urll)
			res_dataa = urllib2.urlopen(reqq)
			ress = res_dataa.read()

			logging.info('***************new message：'+gpname+'******************')
			logging.info(nname+' say : '+ssay)
			logging.info('***************new message：'+gpname+'******************')

		# 	# if is_img or is_file:
		# 	# 	pass
		# 	# 	#用户发的图片，应该比较重要
		# 	# 	ssay='注意：用户-'+nname+' 发照片或者文件，请留意检查相关聊天记录'

			#中文机器人	自有
			# +'&group='+urllib.quote(name.encode('utf8'))+'&username='+urllib.quote(nname.encode('utf8'))
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
					pass
					print(str(e))
		ress=''#清空上次回答内容



		logging.info(u'----------------结束处理这次循环的消息---------')	
	except Exception, e:
		# raise e
		logging.info(str(e))
		pass

	# time.sleep(0.1)
	# get_group_message(name)


	time.sleep(5)

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

	print(syastring)
	print('send_massage 2')

	if not ismobile:
		#这个函数模拟输入，使字体变黑，看起来正常
		# document.dispatchEvent(e);
		# var e=document.createEvent("KeyboardEvents");e.initKeyboardEvent("keydown",true,true,window,"65");parent.f11(e)
		try:
			set_wyswyg_js = 'parent.f11(event);'
			browser.execute_script(set_wyswyg_js)
		except Exception, e:
			print('parent.f11(event)')
			print(str(e))	

		# 统一输入部分，试一试所有的输入方法
		# js方法
		try:
			# set_wyswyg_js = 'var e = new Event("keypress");e.which = 65;e.altKey=false;e.ctrlKey=false;e.shiftKey=false;e.metaKey=false;e.bubbles=true;parent.f11(e);'
			set_wyswyg_js = 'FreeTextBox1_editor.document.body.innerText="%s"' %(syastring)
			set_wyswyg_js = set_wyswyg_js+';document.getElementById("FreeTextBox1_editor").contentWindow.document.body.innerHTML="%s"' %(syastring)
			browser.execute_script(set_wyswyg_js)
		except Exception, e:
			print('#FreeTextBox1_editor')
			print(str(e))

		try:
			actelem=browser.switch_to.active_element
			actelem.send_keys(syastring.decode('utf-8'))
			browser.switch_to.default_content()
		except Exception, e:
			# raise e
			print('active_element')
			print(str(e))
			browser.switch_to.default_content()
		#python方法
		# 找到iframe里面有body div 输入 editor 等字样	
		iframehtml=browser.find_elements_by_xpath("//iframe")
		for x in iframehtml:
			try:
				print('xxxxxxx')
				# inputhtml=x.find_element_by_xpath("//body[contains(text(), 在此输入)]")
				inputhtml=x.find_element_by_xpath("//body")
				# print(inputhtml)
				# print('inputhtml.text')
				# print(inputhtml.text)
				# if inputhtml!=None:
				# print('x.text')
				# print(x.text)
				# print(x.get_attribute('id'))
				# print(x.get_attribute('class'))
				# print(inputhtml.text)

				actions = ActionChains(browser)
				inputiframe = browser.find_element_by_css_selector("#"+x.get_attribute('id'))
				actions.click(inputiframe)
				actions.perform()
				# inputhtml.send_keys(syastring.decode('utf-8'))
				# set_wyswyg_js = 'document.getElementById("'+x.get_attribute('id')+'").contentWindow.document.body.click();'
				set_wyswyg_js = ''
				set_wyswyg_js = set_wyswyg_js+'document.getElementById("'+x.get_attribute('id')+'").contentWindow.document.body.innerHTML="%s"' %(syastring)
				# set_wyswyg_js = set_wyswyg_js+';document.getElementById("FreeTextBox1_editor").contentWindow.document.body.innerHTML="%s"' %(syastring)
				browser.execute_script(set_wyswyg_js)

				# 不能发，不然要发2次
				# #send
				# inputhtml.send_keys(Keys.ENTER)

				# inputiframe = browser.find_element_by_css_selector("#"+x.get_attribute('id'))
				# actions = ActionChains(browser)
				# actions.move_to_element(inputiframe)
				# actions.click(inputiframe)
				# actions.perform()
				# inputhtml.send_keys(syastring.decode('utf-8'))




			except Exception, e:
				# raise e
				print('iframe')
				print(str(e))
				pass


		# 统一发送部分，试一试所有的发送方法

		# js方法
		try:
			set_wyswyg_js = 'document.getElementById("SendBtn").click();'
			browser.execute_script(set_wyswyg_js)
		except Exception, e:
			# raise e
			print('SendBtn')
			print(str(e))

		# onclick
		# User_Send()	找到有send的按钮
		iframehtml=browser.find_elements_by_xpath("//*[contains(@onclick, 'end')]")
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
				
		iframehtml=browser.find_elements_by_xpath("//iframe")
		for x in iframehtml:
			try:
				inputhtml=x.find_element_by_xpath("//body[contains(text(), 在此输入)]")
				# #send
				inputhtml.send_keys(Keys.ENTER)
			except Exception, e:
				# raise e
				print('Keys.ENTER')
				print(str(e))


		#python
		try:
			browser.find_element_by_xpath("//div[contains(text(), 发送)]").click()
			browser.find_element_by_xpath("//div[contains(text(), 发 送)]").click()
		except Exception, e:
			# raise e
			print('发送')
			print(str(e))


		# or	终极大招	暂不做
		# chain = ActionChains(driver)
		# chain.context_click(implement).perform()

		# menu = driver.find_element_by_css_selector(".nav")
		# hidden_submenu =		driver.find_element_by_css_selector(".nav #submenu1")

		# actions = ActionChains(browser)
		# actions.move_to_element(menu)
		# actions.click(hidden_submenu)
		# actions.perform()




	if ismobile:
		#模拟点击输入框
		# try:
		# 	set_wyswyg_js = 'inputclick();'
		# 	browser.execute_script(set_wyswyg_js)
		# except Exception, e:
		# 	print('inputclick();')
		# 	print(str(e))	
		# textarea #texteditor
		try:
			set_wyswyg_js = 'tlist=document.getElementsByTagName("input");for (var i = 0; i < tlist.length; i++) {tlist[i].value="%s"};' %(syastring)
			browser.execute_script(set_wyswyg_js)
		except Exception, e:
			print('#texteditor')
			print(str(e))

		# 有可能是多个  后面改
		try:
			inputhtml=browser.find_element_by_xpath("//textarea")
			inputhtml.send_keys(syastring.decode('utf-8'))
		except Exception, e:
			# raise e
			print('syastring')
			print(str(e))

		# onclick
		# User_Send()	找到有send的按钮
		try:
			iframehtml=browser.find_elements_by_xpath("//*[contains(@onclick, 'end')]")
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
			browser.find_element_by_xpath("//div[contains(text(), '发送')]").click()
			browser.find_element_by_xpath("//div[contains(text(), '发 送')]").click()
		except Exception, e:
			# raise e
			print('发送')
			print(str(e))

	if msglist_length<3:
		browser.save_screenshot("C:/zip/12/"+str(fname)+'s'+"screen.png")
	elif msglist_length<6:
		browser.save_screenshot("C:/zip/12/"+str(fname)+'m'+"screen.png")
	else:
		browser.save_screenshot("C:/zip/12/"+str(fname)+"screen.png")
# 开始运行


# ismobile=True
ismobile=False

# 进入浏览器设置
chome_options = webdriver.ChromeOptions()
# chome_options.set_binary("C:\Program Files\Google\Chrome\chrome.exe");
# 设置中文
chome_options.add_argument('lang=zh_CN.UTF-8')


# 适配后再打开
# if random.choice([x for x in range(100)])>0:
# 	uainfo=generate_user_agent(os=('win','win','win','win','win','win','mac'))
# 	ismobile=False
# else:
# 	uainfo=generate_user_agent(os=('android'))
# 	ismobile=True

# uainfo=generate_user_agent(os=('win','win','mac'))
uainfo=generate_user_agent(os=('android'))
ismobile=True

print('ismobile')
print(ismobile)

print('uainfo')
print(uainfo)

# uainfo='User-Agent: MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'
# chome_options.add_argument("user-agent='"+uainfo+"'")
# chome_options.add_argument('user-agent="Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1"')
chome_options.add_argument('user-agent="'+uainfo+'"')

# can not  set the request header 'Referer' 
#设置不显示图片
# ,"profile.managed_default_content_settings.javascript":2
# prefs = {"profile.managed_default_content_settings.images":2}
prefs = {}
chome_options.add_experimental_option("prefs",prefs)
# 更换头部
# 移动版没有广告地址了，需要点击了
# if ismobile:
# 	chome_options.add_argument('user-agent="Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.23 Mobile Safari/537.36"')

dcap={}
dcap["phantomjs.page.settings.loadImages"] = True


dcap['phantomjs.page.customHeaders.Accept'] ='text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
dcap['phantomjs.page.customHeaders.Host'] =host
dcap['phantomjs.page.customHeaders.User-Agent'] =uainfo
# dcap['phantomjs.page.customHeaders.Accept-Encoding'] ='gzip, deflate, br'
dcap['phantomjs.page.customHeaders.Referer'] ='https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=0&rsv_idx=1&tn=baidu&wd='+urllib.quote(usearchword)
# dcap['phantomjs.page.customHeaders.Referer'] ='http://www.tstryy.com/jhsy/shengyuzhidao/'
dcap['phantomjs.page.customHeaders.Cookie'] =';'.join(cookielist)
# dcap['phantomjs.page.customHeaders.Cookie'] = ''
dcap['phantomjs.page.customHeaders.Cache-Control'] ='max-age=0'
dcap['phantomjs.page.customHeaders.Connection'] ='keep-alive'
dcap['phantomjs.page.customHeaders.Upgrade-Insecure-Requests'] ='1'
# dcap['phantomjs.page.customHeaders.Accept-Encoding'] ='gzip, deflate'
dcap['phantomjs.page.customHeaders.Accept-Language'] ='zh-CN,zh;q=0.9'





# 改判断是Linux还是windows 然后再看是xp 还是win7

# xp不需要代理


#win7
if 'XP' not in platstring:
	cityname=''
	ip_proxy=changeip(cityname)
	if len(ip_proxy)>30:
		print('NO IP AVILABLE')
		exit()
	# chome_options.add_argument(('--proxy-server=http://' + ip_proxy))	



	# IP代理
	proxy = webdriver.Proxy()  
	proxy.proxy_type = ProxyType.MANUAL  
	proxy.http_proxy = ip_proxy
	proxy.add_to_capabilities(dcap)  

	if browsername==None or browsername=='':
		browsername='phantom'

	if browsername=='phantom':
		# 改为phantom
		# Windows环境下完整路径前加r！！！
		browser = webdriver.PhantomJS(executable_path=r'E:\python\phantom\phantomjs\bin\phantomjs.exe',desired_capabilities=dcap)
		browser.viewportSize={'width':824,'height':2200} #重要这句！
		browser.maximize_window()
		print('PhantomJS()')
	if browsername=='chrome':
		# chrome ua修改失败，所以还是用phantom
		browser = webdriver.Chrome(chrome_options=chome_options)	
		print('Chrome()')
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

# for coostr in cookielist:
# 	coo=coostr.split('=')
# 	browser.add_cookie({'name':coo[0],'value':coo[1]})

# browser.implicitly_wait(30)
browser.set_script_timeout(30)
browser.set_page_load_timeout(40)
# browser = webdriver.Firefox()
# browser = webdriver.Chrome()

print('cookie')
try:
	# browser = webdriver.Chrome(desired_capabilities=capabilities)
	# browser.get(openurlstring)
	print(hospitalsite)
	browser.get(hospitalsite)
	print('browser.get()')
	time.sleep(3)
	set_wyswyg_js = 'location.href="'+openurlstring+'";'
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

# browser.delete_all_cookies()
# 确认没问题 并做网络缓冲
logging.info(u'browser.title:'+browser.title+'.')
logging.info(browser.title)
# time.sleep(5)
browser.save_screenshot("wechat.png")

# time.sleep(60*10*2)
# time.sleep(10)


if browser.title=='' or '.com' in browser.title or '.cn' in browser.title or '.net' in browser.title:
	pass
	# f.close()
	# browser.quit()
	# exit()
	browserquit()


# set_wyswyg_js = "document.write('<script>window.location.href = \""+'http://trnanke120.com/'+"\";</script>')"
# browser.execute_script(set_wyswyg_js)
# time.sleep(5)

# set_wyswyg_js = "document.write('<script>window.location.href = \""+openurlstring+"\";</script>')"
# browser.execute_script(set_wyswyg_js)
# time.sleep(5)


if browser.title=='' or '.com' in browser.title or '.cn' in browser.title or '.net' in browser.title:
	pass
	# f.close()
	# browser.quit()
	# exit()
	browserquit()



# servicekindlist

# testclick(1,"%u5305%u76ae%u6574%u5f62");
# onclick="testclick(2,"%u6027%u529f%u80fd%u969c%u788d");"
# testclick(2,"%u6027%u529f%u80fd%u969c%u788d");

set_wyswyg_js = 'testclick(2,"%u6027%u529f%u80fd%u969c%u788d");'
browser.execute_script(set_wyswyg_js)

# 断点
# d 

# #移动端没有iframe
# try:
# 	# titleelm=browser.find_element_by_css_selector('#kw')
# 	titleelm=browser.find_element_by_css_selector('iframe')
# 	print(titleelm)
# except Exception, e:
# 	# raise e
# 	print(str(e))
# 	print('browser.quit() cant find .chat_item')
# 	# f.close()
# 	# browser.quit()
# 	print('page opend error ,quit quit quit')
# 	print('page opend error ,quit quit quit')
# 	# exit()
# 	browserquit()

from yanma import YDMHttp



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


	#输入识别结果  或者  根据结果 点击相应位置
	widthheight=codestr.split(',')
	print('widthheight')
	print(widthheight)
	# browser.actions()
	# .mouseMove(
	# 	element(by.css('.material-dialog-container')), -20, -20) #pixel offset from top left
	# .click()
	# .perform();
	above = browser.find_element_by_css_selector("#yzmimgN")
	ActionChains(browser).move_to_element_with_offset(above,float(widthheight[0])*size['width'],float(widthheight[1])*size['height']).click().perform()

# tes

coderobot=browser.find_elements_by_css_selector('#modalDiv_Chatpreobj')
if len(coderobot)>0:
	print 'code'
	print 'code'
	iscode=1
	# pass
	# f.close()
	# browser.quit()
	# exit()
	# 验证码模块
	# browser.save_screenshot('web.jpg')
	imgelement=browser.find_element_by_css_selector('#yzmimg')
	location = imgelement.location	#获取验证码x,y轴坐标
	size=imgelement.size	#获取验证码的长宽
	rangle=(int(location['x']),int(location['y']),int(location['x']+size['width']),int(location['y']+size['height'])) #写成我们需要截取的位置坐标

	i=Image.open("wechat.png") #打开截图
	frame4=i.crop(rangle)	#使用Image的crop函数，从截图中再次截取我们需要的区域
	frame4.save("code.jpg")


	# qq=Image.open('code.jpg')
	# text=pytesseract.image_to_string(qq).strip() #使用image_to_string识别验证码
	# print 'code:'
	# print text


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
	codetype	= 1004
	# codetype	= 5000
	# 超时时间，秒
	timeout	 = 60	 

	imgfilename="code.jpg"

	# # 一键识别函数，无需调用 YDM_SetAppInfo 和 YDM_Login，适合脚本调用
	# captchaId = YDMApi.YDM_EasyDecodeByPath(username, password, appId, appKey, imgfilename, codetype, timeout, result)
	# result=str(result)
	# print result
	# result=result.replace('c_char_p','')
	# result=result.replace('(','')
	# result=result.replace(')','')
	# result=result.replace('\'','')

	# codestr=result
	# print codestr

	# 初始化
	yundama = YDMHttp(username, password, appid, appkey)

	# 登陆云打码
	uid = yundama.login();
	print 'uid: %s' % uid

	# 查询余额
	balance = yundama.balance();
	print 'balance: %s' % balance

	# 开始识别，图片路径，验证码类型ID，超时时间（秒），识别结果
	cid, result = yundama.decode(imgfilename, codetype, timeout);
	print 'cid: %s, result: %s' % (cid, result)
	result=str(result)
	print result
	result=result.replace('c_char_p','')
	result=result.replace('(','')
	result=result.replace(')','')
	result=result.replace('\'','')

	codestr=result
	print codestr

	# codestr=dmt.decode('code.jpg',200) #上传打码

	# 除非试了很多次不行才换代理
	# 关闭chrome 重新换IP代理
	# closebrowser()

	# time.sleep(0.5)
	# browser.find_element_by_css_selector('#ccode').send_keys(codestr.encode('utf-8'))
	browser.find_element_by_css_selector('#ccode').send_keys(codestr.decode())
	time.sleep(0.3)
	browser.find_element_by_css_selector('#Button1').send_keys(Keys.ENTER)
	time.sleep(0.3)



# 在呼叫在线客服人
isrobot=0
# #headerBox
# 呼叫在线客服
# @id='prompttop' and 
# callforchathtml=browser.find_element_by_xpath("//p[contains(text(), 呼叫在线客)]")
# nowforchathtml=browser.find_element_by_xpath("//p[contains(text(), 正在和您进行对话)]")
# prompttop
# 正在和您进行对话
# 在呼叫在线客服人
time.sleep(0.3)
try:
	callforchathtml=browser.find_element_by_xpath("//p[@id='prompttop']")
	callforchathtmltext=callforchathtml.text
except Exception, e:
	# raise e
	callforchathtml=None
	callforchathtmltext='移动端'

# print(callforchathtml.text)

# callforchathtml=browser.find_element_by_css_selector('#headerBox')
# if callforchathtml.is_displayed() and not nowforchathtml.is_displayed():
if callforchathtml:
	if '在呼叫在线客服' in callforchathtmltext:
		isrobot=1

# print('isrobot and not(iscode)')
print('isrobot')
print(isrobot)
print(not(iscode))
# if isrobot and not(iscode):
if isrobot:
	pass
	logging.info(u'robot loop')
	# f.close()
	# browser.quit()
	# exit()

	browserquit()

get_friends_message('')