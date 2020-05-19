#!/usr/bin/env python
#coding:utf-8
# -*- coding: utf-8 -*-

# 导入工具
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException 
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.proxy import ProxyType 
from selenium.webdriver.common.action_chains import ActionChains
import time
import datetime
from bs4 import BeautifulSoup
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
from PIL import Image  
from yundama import YDMHttp


from supportfunction import changeip
from supportfunction import genercookies
from supportfunction import genewechatid



from user_agent import generate_user_agent, generate_navigator
from selenium.webdriver.common.keys import Keys  
reload(sys)
sys.setdefaultencoding('utf-8')
import requests



# 加载默认套路
with codecs.open('taolu.json',encoding='utf-8') as json_data:
    taolu = json.load(json_data)
with codecs.open('bingli.json',encoding='utf-8') as json_data:
    bingli = json.load(json_data)


# 随机生成一个用户聊天记录代号
fname=random.uniform(1, 10000000000)
f=open('hist/'+str(fname)+'.txt','a')



# 基本配置
logging.basicConfig(level=logging.INFO)
#精神科
# openurlstring='http://vipu6-szak3.kuaishang.cn/bs/im.htm?cas=57727___181100&fi=68417&ism=1&vi=c84560c7650f495584349836907a1cea&ref=http%3A%2F%2F3g.cdch120.com%2F&dp=http%3A%2F%2F3g.cdch120.com%2F&_tk=9d79f8bc'
# openurlstring='http://pct.zoosnet.net/LR/Chatpre.aspx?id=PCT52081394&cid=1499538353717739194911&lng=cn&sid=1499538353717739194911&p=http%3A//wap.xaxckd.com/jb/yiyu/2017/0228/185.html%23utm_source%3Dbaidu%26utm_medium%3D123456%26utm_term%3D%25E5%25A4%25B1%25E7%259C%25A0%25E6%258A%2591%25E9%2583%2581%25E5%258C%25BB%25E9%2599%25A2%26utm_content%3D%3C%25E5%258C%25BB%3E%25E3%2580%2590%25E5%258C%25BB%25E9%2599%25A2%25E3%2580%2591%25E6%258A%2591%25E9%2583%2581%25E7%2597%2587+%25E7%25B1%25BB%25E5%259E%258B%26utm_campaign%3DM1%3DYYZ&rf1=&rf2=&msg=&d=1499538358059'



#男科
# openurlstring='http://kqi.zoossoft.com/LR/freetel.aspx?siteid=KQI10880110&oname=%e5%80%bc%e7%8f%ad-%e8%ae%b8%e5%8a%a9%e7%90%86'
# openurlstring='http://kqi.zoossoft.com/LR/freetel.aspx?siteid=KQI10880110'


# openurlstring='http://com.zoosnet.net/LR/Chatpre.aspx?id=COM49756704&cid=1499335611282792024686&lng=cn&sid=1499335611282792024686&p=http%3A//www.12079.com/index.html&rf1=&rf2=&msg=&d=1499335614626'



#皮肤科
# 深圳肤康皮肤病医院  
# http://www.baidu.com/baidu.php?url=kW3K00KdelksEXm36Qnyp2sBpT4rLP-WwVzUs1mkEWdPddqTO0CrB_ZF9-Jaeq-wPonfCuAJ-0zxhV4DE_nDPhSF9iHZWd1axybwpMGcgVRGkM-jkbYdRa5O_JGJhel0BwAXeEFxZeVbQrfy0ccx8S2CRrM4vyFaAV3H_ehByycZ1uaI00.DR_imqIO-osIorU5WdqJc7PHV2XgZJyAp7WGvNq260.U1Yk0ZDqzXeUvoxYEegAGQxY_JZiEIil0A7bTgbqzXeUvoxYEegAGQxY_JZiEIil0A7bTgfqn6KY5TM8vqJLqQSdkJiLqQ29YoLR86KGUHYznjf0u1dBugK1nfKdpHdBmy-bIfKspyfqP0KWpyfqrHn0Ugfqn1D1P-tknjDLg1csPWFxnW0dnNtknjD4g1nvnjD0pvbqn0KzIjYVnfK-pyfqnWndP1wxnHf1n7tznHDzn7tkrjRvn7tznjTkr0KBpHYznjf0UynqnHRvg1mYP1cdPH64nNtknj6snj0knWfkg1D3rjcdn1Rsg1Dsnj7xn0KkTA-b5Hf0TyPGujY4nsKzuLw9u1Ys0AqvUjYknj0knzdbX-tknjcknBdbX-tknjfLPiYkg1Dsrj0YQywlg1DknjDYQH7xnHDsn1cVnH-xnHDsn1bVuZGxnHDsPHcVuZGxnHDkPHDVn-tknHD3ridbX-tknHTdPzYkg1DkP1bdQywlg1DznaYknjPxnHcsnjbVn-tknWcVuZGxnHczn1bVuZGxnHczP1DVuZGxnHczrjTVuZGxnHcvn1nVuZGxnHnknjnVuZGxnHnknWnVuZGxnHnkrjbVuZGxnHnznjcVuZGxnHn1nWnVuZGxnHnYn1RVuZGxnHnvnWTVuZGxnHnvn16VuZGxnHfsnjTVnNtkPj0sriYdg1DYnjnLQywlg1DYnHbkQH7xnHfznjcVuZGxnHfznjnVnNtkPjcsPidbX-tkPjcknBdbX-tkPjcYPidbX-tkPjcvPaYkg1DYnWTvQH7xnHfzP16VuZGxnW0LHadbX-tznjInyadbX-tzPWm4Qywlg1cvPW-mQywl0A7B5HKxn0K-ThTqn0KsTjYs0A4vTjYsQW0snj0snj0s0AdYTjYs0AwbUL0qn0KzpWYs0Aw-IWdsmsKhIjYs0ZKC5H00ULnqn0KBI1Ykn0K8IjYs0ZPl5fKYIgnqPH0znH0LnHDdPjRYrjn3PWfLnsKzug7Y5HDdnjc1PHmsPjT3Pj00Tv-b5H9hnWb3mH7bnj0snj63Phn0mLPV5HD3nbNDfYuKnW7DwbnLfH00mynqnfKsUWYs0Z7VIjYs0Z7VT1Ys0ZGY5H00UyPxuMFEUHYsg1Kxn7tsg1Kxn0Kbmy4dmhNxTAk9Uh-bT1Ysg1Kxn7tsg1Kxn0Ksmgwxuhk9u1Ys0AwYpyfqn0K-IA-b5iYk0A71TAPW5H00IgKGUhPW5H00Tydh5HDv0AuWIgfqn0KhXh6qn0Khmgfqn0KlTAkdT1Ys0A7buhk9u1Yk0Akhm1Ys0APzm1YzrHTLrf
# 和深圳新兴皮肤病医院
# http://www.baidu.com/baidu.php?url=kW3K00jJPmSF4gbo0tImyxKICbM-DkLplhFwaQrotAZCZzuToNvDEeEiK_lrxGFmhOBGrUaaTZQX2nS1UrhI2ZNF93fQKpZBZdtoqZUfF2kvLVVZyw11lB1iavtAQCYxDQDdP7JSKjoE_o4BhLKWuwrvxPo8pSayw2p_x86L9dfINrUge0.Db_iTaUtM-Zsdfd4QDfTPajwCzksIee_TPXi1v43t8XzE5ZslPZgIOO3ktr5gCYxOesOOtlktPNv5gCYIpthz1kLJpMpRt85R_nYQAexY4r-f0.U1Yk0ZDqzXeUvBRznnpbVOizCiRznP2qdQC-nWKhIyV9UhT0IjLFeVEp8_rdknpbVOHiEIil0A-V5HczPsKM5yF-TZnk0ZNG5yF9pywd0ZKGujYY0APGujY3P0KVIjYknjDLg1csPWFxnW0dnNtknjD4g1nvnjD0pvbqn0KzIjYLrjf0uy-b5HDYPHIxnHbsn1PxnHndPH7xnWDsP19xnH6dPWKxnHTsnj7xnW04n100mhbqnW0Yg1DdPfKVm1YvPjmLnWckPHuxnH03nW0vnW6Yn-tknjTvnjb4PNtknj0kg100TgKGujYY0Z7WpyfqrHn0ThIYmyTqnfKEIhsqnH03njDVnNtknj6sPBdbX-tknH0kPaYzg1Dknjf1QH7xnHDsPHcVnNtknH0dPBdbX-tknH0vriY1r7tknH0LPaY1g1DkPH6zQH7xnHDvP16VndtknHm3nBYzg1DkrHT3Qywlg1DznadbX-tknWc3nzdbX-tknWf1niYkg1DzPWndQywlg1DzPW6vQywlg1DzP1bYQywlg1DzrHczQywlg1D1njfzQH7xnHnknjDVrNtkn1D3ridbX-tkn1D4ridbX-tkn1nznzYkg1D1PW61QH7xnHn4rj6VuZGxnHfsnjRVnNtkPj01PzYkg1DYnjfkQywlg1DYnjbLQH7xnHfknjfVuZGxnHfknH6VuZGxnHfknWTVuZGxnHfkPjmVnNtkPjD4nidbX-tkPjcsPBYkg1DYnWfdQH7xnHfzP16VnfK9mWYsg100ugFM5H00TZ0qn0K8IM0qna3snj0snj0sn0KVIZ0qn0KbuAqs5HD0ThCqn0KbugmqTAn0uMfqn0KspjYs0Aq15H00mMTqnH00UMfqn0K1XWY0IZN15HDvnHbsnHTdPHR1njcLP1fznHD10ZF-TgfqnHRsnWndPHfYnH6drfK1pyfqrHf1mWw9nHRsnj0knvnkP6KWTvYqfWPjwW0znbfknWc4nH0knfK9m1Yk0ZK85H00TydY5H00Tyd15H00XMfqn0KVmdqhThqV5HKxn7tsg1Kxn0Kbmy4dmhNxTAk9Uh-bT1Ysg1Kxn7tsg100TA7Ygvu_myTqn0KbIA-b5H00ugwGujYVnfK9TLKWm1Ys0ZNspy4Wm1Ys0Z7VuWYkP6KhmLNY5H00uMGC5H00uh7Y5H00XMK_Ignqn0K9uAu_myTqnfK_uhnqn0KWThnqnHb4Pj0&ck=898.11.152.356.298.534.290.2217&shh=www.baidu.com&sht=baiduhome_pg&us=3.0.1.0.2.1170.0&ie=utf-8&f=8&tn=baiduhome_pg&wd=%E6%B7%B1%E5%9C%B3%20%E7%9A%AE%E8%82%A4%E7%97%85%20%E5%8C%BB%E9%99%A2%20%20fukang&oq=%25E6%25B7%25B1%25E5%259C%25B3%2520%25E7%259A%25AE%25E8%2582%25A4%25E7%2597%2585%2520%25E5%258C%25BB%25E9%2599%25A2&rqlang=cn&inputT=3353
# 这是那个深圳军科的对手
# openurlstring='http://pft.zoosnet.net/LR/Chatpre.aspx?id=PFT49473838&cid=1502245020998669688687&lng=cn&sid=1502245020998669688687&p=http%3A//m.0755gov.com/&rf1=&rf2=&msg=&e=JSdbl-swt&d=1502245038653'
# openurlstring='http://www.baidu.com/baidu.php?url=kW3K00KdelksEXm36Qnyp2sBpT4rLP-WwVzUs1mkEWdPddqTO0CrB_ZF9-Jaeq-wPonfCuAJ-0zxhV4DE_nDPhSF9iHZWd1axybwpMGcgVRGkM-jkbYdRa5O_JGJhel0BwAXeEFxZeVbQrfy0ccx8S2CRrM4vyFaAV3H_ehByycZ1uaI00.DR_imqIO-osIorU5WdqJc7PHV2XgZJyAp7WGvNq260.U1Yk0ZDqzXeUvoxYEegAGQxY_JZiEIil0A7bTgbqzXeUvoxYEegAGQxY_JZiEIil0A7bTgfqn6KY5TM8vqJLqQSdkJiLqQ29YoLR86KGUHYznjf0u1dBugK1nfKdpHdBmy-bIfKspyfqP0KWpyfqrHn0Ugfqn1D1P-tknjDLg1csPWFxnW0dnNtknjD4g1nvnjD0pvbqn0KzIjYVnfK-pyfqnWndP1wxnHf1n7tznHDzn7tkrjRvn7tznjTkr0KBpHYznjf0UynqnHRvg1mYP1cdPH64nNtknj6snj0knWfkg1D3rjcdn1Rsg1Dsnj7xn0KkTA-b5Hf0TyPGujY4nsKzuLw9u1Ys0AqvUjYknj0knzdbX-tknjcknBdbX-tknjfLPiYkg1Dsrj0YQywlg1DknjDYQH7xnHDsn1cVnH-xnHDsn1bVuZGxnHDsPHcVuZGxnHDkPHDVn-tknHD3ridbX-tknHTdPzYkg1DkP1bdQywlg1DznaYknjPxnHcsnjbVn-tknWcVuZGxnHczn1bVuZGxnHczP1DVuZGxnHczrjTVuZGxnHcvn1nVuZGxnHnknjnVuZGxnHnknWnVuZGxnHnkrjbVuZGxnHnznjcVuZGxnHn1nWnVuZGxnHnYn1RVuZGxnHnvnWTVuZGxnHnvn16VuZGxnHfsnjTVnNtkPj0sriYdg1DYnjnLQywlg1DYnHbkQH7xnHfznjcVuZGxnHfznjnVnNtkPjcsPidbX-tkPjcknBdbX-tkPjcYPidbX-tkPjcvPaYkg1DYnWTvQH7xnHfzP16VuZGxnW0LHadbX-tznjInyadbX-tzPWm4Qywlg1cvPW-mQywl0A7B5HKxn0K-ThTqn0KsTjYs0A4vTjYsQW0snj0snj0s0AdYTjYs0AwbUL0qn0KzpWYs0Aw-IWdsmsKhIjYs0ZKC5H00ULnqn0KBI1Ykn0K8IjYs0ZPl5fKYIgnqPH0znH0LnHDdPjRYrjn3PWfLnsKzug7Y5HDdnjc1PHmsPjT3Pj00Tv-b5H9hnWb3mH7bnj0snj63Phn0mLPV5HD3nbNDfYuKnW7DwbnLfH00mynqnfKsUWYs0Z7VIjYs0Z7VT1Ys0ZGY5H00UyPxuMFEUHYsg1Kxn7tsg1Kxn0Kbmy4dmhNxTAk9Uh-bT1Ysg1Kxn7tsg1Kxn0Ksmgwxuhk9u1Ys0AwYpyfqn0K-IA-b5iYk0A71TAPW5H00IgKGUhPW5H00Tydh5HDv0AuWIgfqn0KhXh6qn0Khmgfqn0KlTAkdT1Ys0A7buhk9u1Yk0Akhm1Ys0APzm1YzrHTLrf&ck=5385.2.135.245.149.269.142.1256&shh=www.baidu.com&sht=baiduhome_pg'

# 深圳新兴皮肤病医院
# openurlstring='http://www.baidu.com/baidu.php?url=kW3K00jJPmSF4gbo0tImyxKICbM-DkLplhFwaQrotAZCZzuToNvDEeEiK_lrxGFmhOBGrUaaTZQX2nS1UrhI2ZNF93fQKpZBZdtoqZUfF2kvLVVZyw11lB1iavtAQCYxDQDdP7JSKjoE_o4BhLKWuwrvxPo8pSayw2p_x86L9dfINrUge0.Db_iTaUtM-Zsdfd4QDfTPajwCzksIee_TPXi1v43t8XzE5ZslPZgIOO3ktr5gCYxOesOOtlktPNv5gCYIpthz1kLJpMpRt85R_nYQAexY4r-f0.U1Yk0ZDqzXeUvBRznnpbVOizCiRznP2qdQC-nWKhIyV9UhT0IjLFeVEp8_rdknpbVOHiEIil0A-V5HczPsKM5yF-TZnk0ZNG5yF9pywd0ZKGujYY0APGujY3P0KVIjYknjDLg1csPWFxnW0dnNtknjD4g1nvnjD0pvbqn0KzIjYLrjf0uy-b5HDYPHIxnHbsn1PxnHndPH7xnWDsP19xnH6dPWKxnHTsnj7xnW04n100mhbqnW0Yg1DdPfKVm1YvPjmLnWckPHuxnH03nW0vnW6Yn-tknjTvnjb4PNtknj0kg100TgKGujYY0Z7WpyfqrHn0ThIYmyTqnfKEIhsqnH03njDVnNtknj6sPBdbX-tknH0kPaYzg1Dknjf1QH7xnHDsPHcVnNtknH0dPBdbX-tknH0vriY1r7tknH0LPaY1g1DkPH6zQH7xnHDvP16VndtknHm3nBYzg1DkrHT3Qywlg1DznadbX-tknWc3nzdbX-tknWf1niYkg1DzPWndQywlg1DzPW6vQywlg1DzP1bYQywlg1DzrHczQywlg1D1njfzQH7xnHnknjDVrNtkn1D3ridbX-tkn1D4ridbX-tkn1nznzYkg1D1PW61QH7xnHn4rj6VuZGxnHfsnjRVnNtkPj01PzYkg1DYnjfkQywlg1DYnjbLQH7xnHfknjfVuZGxnHfknH6VuZGxnHfknWTVuZGxnHfkPjmVnNtkPjD4nidbX-tkPjcsPBYkg1DYnWfdQH7xnHfzP16VnfK9mWYsg100ugFM5H00TZ0qn0K8IM0qna3snj0snj0sn0KVIZ0qn0KbuAqs5HD0ThCqn0KbugmqTAn0uMfqn0KspjYs0Aq15H00mMTqnH00UMfqn0K1XWY0IZN15HDvnHbsnHTdPHR1njcLP1fznHD10ZF-TgfqnHRsnWndPHfYnH6drfK1pyfqrHf1mWw9nHRsnj0knvnkP6KWTvYqfWPjwW0znbfknWc4nH0knfK9m1Yk0ZK85H00TydY5H00Tyd15H00XMfqn0KVmdqhThqV5HKxn7tsg1Kxn0Kbmy4dmhNxTAk9Uh-bT1Ysg1Kxn7tsg100TA7Ygvu_myTqn0KbIA-b5H00ugwGujYVnfK9TLKWm1Ys0ZNspy4Wm1Ys0Z7VuWYkP6KhmLNY5H00uMGC5H00uh7Y5H00XMK_Ignqn0K9uAu_myTqnfK_uhnqn0KWThnqnHb4Pj0&ck=898.11.152.356.298.534.290.2217&shh=www.baidu.com&sht=baiduhome_pg&us=3.0.1.0.2.1170.0&ie=utf-8&f=8&tn=baiduhome_pg&wd=%E6%B7%B1%E5%9C%B3%20%E7%9A%AE%E8%82%A4%E7%97%85%20%E5%8C%BB%E9%99%A2%20%20fukang&oq=%25E6%25B7%25B1%25E5%259C%25B3%2520%25E7%259A%25AE%25E8%2582%25A4%25E7%2597%2585%2520%25E5%258C%25BB%25E9%2599%25A2&rqlang=cn&inputT=3353'
# openurlstring='http://swt.25661122.com/LR/Chatpre.aspx?id=MER82816861&cid=1502328019013621756183&lng=cn&sid=1502328019013621756183&p=http%3A//sja.gdqcd.com/&rf1=&rf2=&e=%25u6765%25u81EA%25u9996%25u9875%25u7684%25u5BF9%25u8BDD&d=1502353815671 '


# openurlstring='http://kud.zoossoft.com/LR/Chatpre.aspx?id=KUD85656095&cid=1499324268340680160915&lng=cn&sid=1499324268340680160915&p=http%3A//bddhs.smfukang.com/%3Fbdpc17-hsyy-fsh%3Dtt00008%23zhidao&rf1=&rf2=&msg=&d=1499324271710'

# test
# openurlstring='http://put.zoosnet.net/LR/Chatpre.aspx?id=PUT80510025&cid=1499332913275483612857&lng=cn&sid=1499332913275483612857&p=http%3A//www.4001120777.cn/%23BD-PC-B005-bh00562&rf1=&rf2=&msg=&d=1499332916461'
# openurlstring='https://www.baidu.com/s?wd=ip&rsv_spt=1&rsv_iqid=0xec4120a80003642d&issp=1&f=3&rsv_bp=0&rsv_idx=2&ie=utf-8&rqlang=&tn=baiduhome_pg&ch=&rsv_enter=1&inputT=2044'

#url chat
openurlstring=sys.argv[3]
illclass=sys.argv[2]
userid=sys.argv[1]

print(openurlstring)
if openurlstring == '':
  # openurlstring='http://kud.zoossoft.com/LR/Chatpre.aspx?id=KUD85656095&cid=1499324268340680160915&lng=cn&sid=1499324268340680160915&p=http%3A//bddhs.smfukang.com/%3Fbdpc17-hsyy-fsh%3Dtt00008%23zhidao&rf1=&rf2=&msg=&d=1499324271710'
  print('missing argc:chat url')
  exit()


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
starttime=int(time.time())


nowtime = datetime.datetime.now()
print(nowtime.hour)

if nowtime.hour>22  or nowtime.hour<9 :
  f.close()
  # browser.quit()
  exit()


#是否已经打过招呼
haveyousaidhello=0

istest=False


protocol, s1 = urllib.splittype(openurlstring)  
host, s2=  urllib.splithost(s1)  
host, port = urllib.splitport(host)  

print('host')
print(host)




def getelement(source,selector):
  global browser
  # browser.implicitly_wait(10)
  # res=WebDriverWait(source,3).until(lambda source:source.find_elements_by_css_selector(selector) , " open fail")
  res=True
  try:
    res=WebDriverWait(source,0.5).until(lambda source:source.find_element_by_css_selector(selector) , " open fail")
    # print(res)
    if res==False:
      return None
    else:
      # print(selector)
      elem=source.find_element_by_css_selector(selector)
      # elem=source.find_elements_by_css_selector(selector)
      return elem
  except Exception, e:
    return None


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


# 获取相应的疾病目录数据
bingli_id_list=[]
bingliflodername='/usr/application/autoreplay/conversation/'
keshi_='pifuxingbingke'
keshi_=illclass
for root, dirs, files in os.walk(bingliflodername+keshi_):
    for nfile in files:
      if os.path.splitext(nfile)[1] == '.json':
        bingli_id_list.append(os.path.splitext(nfile)[0])

# 函数定义
print(bingli_id_list)
print('bingli_id_list')
       
def check_exists_by_xpath(ele,css_selector):
    try:
        ele.find_element_by_css_selector(css_selector)
    except NoSuchElementException:
        return False
    return True

#group selector  根据群名字找到群，并进入群聊天
#缺点是 只能找11个以内的群 ，其他的群取不到   需要以后调试

def find_group_by_name(name):
  time.sleep(0.2)

  #遍历的方法。。好像更可靠些呢？
  listele=browser.find_elements_by_css_selector('.chat_item')
  # logging.info(u' 联系人长度 : '+str(len(listele)))
  for ele in listele:
    if name in ele.text:
      ele.click()
      #要不要全局保留一个当前是哪一个群组的变量？？
    # time.sleep(0.1)

def get_median(data):
  data.sort()
  half = len(data) // 2
  return (data[half] + data[~half]) / 2


#获取朋友消息
def get_friends_message(name):
  global starttime
  global browser
  # time.sleep(10)
  # 是否发了消息
  shorttime=0
  middletime=0
  laragetime=0
  while 1:
    # get_screenshot_as_file
    # browser.save_screenshot("/home/wwwroot/default/yiliao.png")
    
    # get_all_person_message() 循环抓取联系人列表
    extract_person_message('gpname',1)  #只抓单个人的消息
    time.sleep(5)

    nowtime=int(time.time())
    wechatid_for_play=genewechatid()
    #8分钟是不是更好？？
    # 或者判断下是不是可以关闭了，
    # 比如对方一直不说话，出现验证码、聊天不能发送、出现联系表单等等意外情形
    if nowtime-starttime>30:
      listele=browser.find_elements_by_css_selector('.msg-box .msg-agent')
      if len(listele)<1 and shorttime==0:
        send_massage('gpname',1,'你好，医生在么？我等了好久了，什么时候能跟医生聊天啊？我很着急')
        shorttime=1
    if nowtime-starttime>50:
      listele=browser.find_elements_by_css_selector('.msg-box .msg-agent')
      if len(listele)<1 and middletime==0:
        slist=['还在么？ ','医生？','咋回事啊？ ','怎么不说话啊？','在么医生。。。','医生你搞什么呢。。','说话啊','你妹啊，等你那么久','快点啊。。。']
        random.shuffle(slist)
        middletime=1
        send_massage('gpname',1,slist[0])
    if nowtime-starttime>60*1.5:
      listele=browser.find_elements_by_css_selector('.msg-box .msg-agent')
      if len(listele)<3 and laragetime==0:
        # slist=['那你联系我下呗'+wechatid_for_play,'算了。。。那你加我微信吧 '+wechatid_for_play,'我微信号是'+wechatid_for_play+'，加我一下','我擦，医生。。。加我微信 '+wechatid_for_play]
        slist=['那你联系我下呗','算了。。。那你加我微信吧 ','是要提供我微信号','加我一下','医生。。。麻烦加我微信 ']
        random.shuffle(slist)
        laragetime=1
        send_massage('gpname',1,slist[0])
    if nowtime-starttime>60*3:
      listele=browser.find_elements_by_css_selector('.msg-box .msg-agent')
      if len(listele)<10:
        slist=['你们医院垃圾，客服也是垃圾 ','我看你们医院评价不好啊，太歪了','你们天天坑人是不是缺心眼 ','你们良心不会痛么','傻比客服医生','垃圾啊！','操你大爷！什么玩意','去你老母的，黑心医院','滚你妈的','去你妈的','尼玛傻比么','傻比医生','你们医院垃圾，客服也是垃圾 ','我看你们医院评价不好啊，太歪了','你们天天坑人是不是缺心眼 ','你们良心不会痛么']
        random.shuffle(slist)
        send_massage('gpname',1,slist[0])
        browserquit()
    if nowtime-starttime>60*5:
      browserquit()
    browser.save_screenshot("/home/wwwroot/default/yiliao.png")



def browserquit():
  global browser
  global f
  global fname
  global userid

  browser.save_screenshot("/home/wwwroot/default/yiliao.png")

  if fname and userid:
    browser.save_screenshot("/usr/application/autoreplay/phantomjstest/screen/"+str(userid)+'/'+str(fname)+"screen.png")
    # browser.save_screenshot("D:/zip/12/"+str(fname)+"screen.png")
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
  global browser
  global bingli_id_list
  global keshi_


  time.sleep(0.1)
  logging.info(u'----------------开始处理这次循环的消息---------')


  try:
    # 里面包括我自己的聊天条数
    listele=browser.find_elements_by_css_selector('.msg-box')
    print('all talk number:')
    print(len(listele))

  except Exception, e:
    # raise e
    print(str(e))

  time.sleep(1)


  if_newmessage[name]=0
  sayarray=[]
  sysinfoarray=[]

  # try:

  if not lastsay.has_key(name):
    lastsay[name]=u'测试'
    print 'not have key'
    print lastsay[name]

  if not isayto.has_key(name):
    isayto[name]=u'测试'

  gpname=name
  # logging.info(u' 当前好友名称 : '+gpname)

  # send_massage(name,1,'医生你好，我这边网络不好')
  # time.sleep(1)
  # browser.save_screenshot("/home/wwwroot/default/yiliao.png")
  # time.sleep(1)
  # ss

  time.sleep(0.3)
  #获取聊天消息记录
  #获取聊天消息记录
   # .msg_left .msg 
  listele=browser.find_elements_by_css_selector('.msg-box .msg-agent')
  # #msgArea  .msg-box .text
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
      # 找不到对方聊天的元素 则结束
      print(str(e))
      print('text cant find')
      # usersay= ele.find_element_by_css_selector('.text').text
      usersay=''
      exit()
    
    # time.sleep(0.1)
    logging.info(usersay)
      
    #替换不能识别的字符串  _web  class="emoji emoji1f48e"
    # replace

    # print '\n'
    # print '\n'
    # 保存对方说的话
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

  is_img=0
  if len(sayarray)>0:

    usersayobj=sayarray[-1]
    nname=usersayobj['nickname']
    ssay=usersayobj['usersay'].replace(' ','')
    # print lastsay[name]
    # print (sayarray[-1]['nickname']+sayarray[-1]['usersay'])

    # 判断是不是跟上次一样
    print lastsay[name]==ssay
    if lastsay[name]==ssay:
      pass
    else:
      if ssay=='' and is_img==1:
        # 如果新消息是发图片
        if_newmessage[name]=1
        lastsay[name]=ssay
      elif ssay!='':
        # 如果新消息是文本
        if_newmessage[name]=1
        lastsay[name]=ssay
  # time.sleep(0.1)
  logging.info(if_newmessage[name])
  
  # 如果是新消息
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
    urlprefix='http://liliniao.com.cn/hospital/index.php?m=Api&c=user&a=talklog'
    urll =urlprefix+'&urole='+urllib.quote('医生'.encode('utf8'))+'&usay='+urllib.quote(ssay.encode('utf8'))+'&chatid='+str(userid)+'-'+str(fname)+'&userid='+str(userid)
    reqq = urllib2.Request(urll)
    res_dataa = urllib2.urlopen(reqq)
    ress = res_dataa.read()


    logging.info('***************new message：'+gpname+'******************')
    logging.info(nname+' say : '+ssay)
    logging.info('***************new message：'+gpname+'******************')


    #中文机器人  自有
    urll ='http://127.0.0.1:9003/?word='+urllib.quote(ssay.encode('utf8'))+'&group='+urllib.quote(name.encode('utf8'))+'&username='+urllib.quote(nname.encode('utf8'))
    reqq = urllib2.Request(urll)
    res_dataa = urllib2.urlopen(reqq)
    ress = res_dataa.read()

    time.sleep(0.1)
    # print ress  如果是设定的不说话
    if ress == 'stop to say||stop to say':
      print 'stop to say'
      pass
    else:
      logging.info('robot will respond with : '+ress.encode('gbk'))
      try:
        # isayto[name]=ress

        usayinfo=ress.split('||')
        uwords=usayinfo[0]
        dintent=usayinfo[1].decode('utf-8')

        print('医生意图dintent')
        print(dintent)

        replyintent=taolu[dintent].split(',')
        print('回复套路replyintent')
        print(replyintent)
        # print('replyintent')
        # print(replyintent)
        
        print('此套路的回复套路taolu[dintent]')
        print(taolu[dintent])

        print('第一个回复套路replyintent[0]')
        print(replyintent[0])

        # 随机选一个意图
        random.shuffle(replyintent)
        myintent=replyintent[0]
        print('随机选的一个意图myintent')
        print(myintent)
        #在已有意图里面，找一个符合的意图，剔除没有对话的意图
        #to do
        flodername='pifuxingbingke'#病种
        flodername=keshi_ #病种
        myjsonfile=open('/usr/application/autoreplay/conversation/'+flodername+'/'+bingli_id_list[0]+'.json')
        jstr=myjsonfile.read()
        print('jstr')
        newjstr=''.join(jstr.split('\n'))
        print(newjstr)
        new_bingli_dict = json.loads(newjstr)

        avilabe_intent=[]
        for intentstr in new_bingli_dict:
          if new_bingli_dict.get(intentstr):
            if len(new_bingli_dict[intentstr])!=0:
              avilabe_intent.append(intentstr)
        print('可用的意图avilabe_intent')
        print(avilabe_intent)
        for xinten in avilabe_intent:
          print(xinten+',')
        # print('replyintent[0]')
        # print(replyintent[0])
        for mintent in replyintent:
          if mintent in avilabe_intent:
            if myintent=='打招呼':
              break
            else:
              myintent=mintent
              logging.info(u'----------------找到一个可用的意图---------') 
              print(myintent)
              break
        #*************************************************************
        # 随机选一个默认回复
        # print('bingli[replyintent[0]]')

        random.shuffle(bingli[myintent])
        # print(bingli[replyintent[0]][0])
        #  (name,1,uwords)
        # myintent=replyintent[0]
        random_uwords=bingli[myintent][0]
        print('随机选的默认回复文本 random_uwords')
        print(random_uwords)


        #现在，换一个方法。随机找一个用户，取出该用户的，该意图的回复用于返回
        random.shuffle(bingli_id_list)
        
        # keshi_ 是否需要定义全局变量 pifuke

        # filename='b6c1771b-3fa2-4036-b040-d87736ec1d05'#随机选择一个用户文件
        filename=bingli_id_list[0]
        print('patient_id')
        print(filename)

        # myjsonfile=open('/usr/application/autoreplay/conversation/'+flodername+'/'+filename+'.json')
        # jstr=myjsonfile.read()
        # print('jstr')
        # newjstr=''.join(jstr.split('\n'))
        # print(newjstr)
        # new_bingli_dict = json.loads(newjstr)
        # print('json.dumps(new_bingli_dict)')
        # print(json.dumps(new_bingli_dict))
        print('最终的意图选择 myintent')
        print(myintent)

        if myintent=='打招呼':
          uwordslist=None
        else:
          # uwords=new_bingli_dict[myintent]
          uwordslist=new_bingli_dict.get(myintent)
          print('新病例中的该意图文本uwordslist')
          print(uwordslist)
          random.shuffle(uwordslist)


        #在已有意图里面，找一个符合的意图，剔除没有对话的意图

        #直到选出一个有该意图的对话  太耗费资源
        # trytimes=0
        # # uwordslist=''
        # while uwordslist=='' or uwordslist==None :
        #   if trytimes>100:
        #     exit()
        #   # random.shuffle(bingli_id_list)
        #   if trytimes>=len(bingli_id_list):
        #     exit()
        #     # random.shuffle(bingli_id_list)
        #   filename=bingli_id_list[trytimes]
        #   myjsonfile=open('/usr/application/autoreplay/conversation/'+flodername+'/'+filename+'.json')
        #   jstr=myjsonfile.read()
        #   myjsonfile.close()
        #   newjstr=''.join(jstr.split('\n'))
        #   new_bingli_dict = json.loads(newjstr)
        #   uwordslist=new_bingli_dict.get(myintent)
        #   trytimes=trytimes+1

        #如果该病人没有此意图，则随机找个该意图的对话
        if uwordslist==None:
          # 默认是皮肤科的对话，不妥
          # 默认改为中性对话了
          uwords=random_uwords
          print('默认病例的回复uwords')
          # uwords=''
        elif len(uwordslist)==0:
          # 默认是皮肤科的对话，不妥
          # 默认改为中性对话了
          uwords=random_uwords
          # uwords=''
          print('默认病例的回复uwords')
        else:
          random.shuffle(uwordslist)
          print('新病例的回复uwords')
          print(uwords)
          if len(uwordslist)>0:
            uwords=uwordslist[0]

        #*************************************************************

        f.write('病人||'+uwords+'\n')

        saylist=uwords.split('，')
        # print(len(saylist))

        # # 分散发送，模拟人工
        # for isayword in saylist:
        #   print(isayword)
        #   if isayword!=None:
        #     send_massage(name,1,isayword)
        #     time.sleep(0.8)
        #     # time.sleep(0.1*len(isayword))
        # print(uwords)
        # send_massage(name,1,uwords)
        print('doc dintent')
        print(dintent)
        browser.save_screenshot("/home/wwwroot/default/yiliao.png")




        #保存截图到文件夹
        #用户ID的文件夹不存在怎么办
        try:
          if os.path.exists('/usr/application/autoreplay/phantomjstest/screen/'+str(userid)):
            pass
          else:
            os.makedirs('/usr/application/autoreplay/phantomjstest/screen/'+str(userid))
          browser.save_screenshot("/usr/application/autoreplay/phantomjstest/screen/"+str(userid)+'/'+str(fname)+"screen.png")

        except Exception, e:
          # raise e
          print(str(e))



        wechatid_for_play=genewechatid()
        # 若干条主动关闭的情形
        if dintent=='医生不爽':
          slist=['傻比客服医生','垃圾啊！','操你大爷！什么玩意']
          random.shuffle(slist)
          send_massage(name,1,slist[0])
          browserquit()
        if dintent=='安排诊号面诊':
          slist=['那你加我微信吧 '+wechatid_for_play,'我微信号是'+wechatid_for_play,'我不一定有时间，先加我吧 '+wechatid_for_play]
          random.shuffle(slist)
          send_massage(name,1,slist[0])
          browserquit()
        if dintent=='询问是否有时间过来看病':
          slist=['那你加我微信吧 '+wechatid_for_play,'我微信号是'+wechatid_for_play,'我不一定有时间，先加我吧 '+wechatid_for_play]
          random.shuffle(slist)
          send_massage(name,1,slist[0])
          browserquit()
        if dintent=='还在么':
          slist=['你们医院垃圾，客服也是垃圾 ','我看你们医院评价不好啊，太歪了','你们天天坑人是不是缺心眼 ','你们良心不会痛么']
          random.shuffle(slist)
          send_massage(name,1,slist[0])
          browserquit()

        if myintent=='准备过来':
          slist=['那你加我微信吧 '+wechatid_for_play,'我微信号是'+wechatid_for_play,'我不一定有时间，先加我吧 '+wechatid_for_play]
          random.shuffle(slist)
          send_massage(name,1,slist[0])
          browserquit()
        if myintent=='我考虑下关闭':
          slist=['那你加我微信吧 '+wechatid_for_play,'我微信号是'+wechatid_for_play,'我不一定有时间，先加我吧 '+wechatid_for_play]
          random.shuffle(slist)
          send_massage(name,1,slist[0])
          browserquit()
        if myintent=='愤怒关闭':
          slist=['去你老母的，黑心医院','滚你妈的','去你妈的','尼玛傻比么','傻比医生','你们医院垃圾，客服也是垃圾 ','我看你们医院评价不好啊，太歪了','你们天天坑人是不是缺心眼 ','你们良心不会痛么']
          random.shuffle(slist)
          send_massage(name,1,slist[0])
          browserquit()
        if myintent=='不方便过来':
          slist=['那你加我微信吧 '+wechatid_for_play,'我微信号是'+wechatid_for_play,'我不一定有时间，先加我吧 '+wechatid_for_play]
          random.shuffle(slist)
          send_massage(name,1,slist[0])
          browserquit()

        # 分散发送，模拟人工
        for isayword in saylist:
          print(isayword)
          if isayword!=None:
            send_massage(name,1,isayword)
            time.sleep(0.8)
            # time.sleep(0.1*len(isayword))
        print(uwords)
        # #保存文本到数据库
        # urlprefix='http://liliniao.com.cn/hospital/index.php?m=Api&c=user&a=talklog'
        # urll =urlprefix+'&urole='+urllib.quote('病人'.encode('utf8'))+'&usay='+urllib.quote(uwords.encode('utf8'))+'&chatid='+str(userid)+'-'+str(fname)+'&userid='+str(userid)
        # reqq = urllib2.Request(urll)
        # res_dataa = urllib2.urlopen(reqq)
        # ress = res_dataa.read()

      except Exception, e:
        # raise e
        pass
        print(str(e))
  ress=''#清空上次回答内容

  logging.info(u'----------------结束处理这次循环的消息---------') 
  time.sleep(5)

# 发送消息

def send_massage(name,is_already_clicked,msgstring):
  global isayto
  global haveyousaidhello
  global istest
  global browser
  global fname
  global userid

  print('send_massage 1')

  # 如果之前说过一样的话 返回
  if isayto[name]==msgstring:
    logging.info('i already said this before')
    return 'i already said this before'

  isayto[name]=msgstring
  syastring=msgstring

  # 如果已经说过你好，打过招呼，则不打招呼了，避免看起来很傻
  if haveyousaidhello and '你好' in msgstring:
    return 'i have already said hello'

  #已经说过你好了
  if '你好' in msgstring:
    haveyousaidhello=1
    #已经说过你好了
  print(syastring)
  print('send_massage 2')



  #保存文本到数据库
  urlprefix='http://liliniao.com.cn/hospital/index.php?m=Api&c=user&a=talklog'
  urll =urlprefix+'&urole='+urllib.quote('病人'.encode('utf8'))+'&usay='+urllib.quote(syastring.encode('utf8'))+'&chatid='+str(userid)+'-'+str(fname)+'&userid='+str(userid)
  reqq = urllib2.Request(urll)
  res_dataa = urllib2.urlopen(reqq)
  ress = res_dataa.read()


  #这个函数模拟输入，使字体变黑，看起来正常
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
    # document.dispatchEvent(e);
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
  # User_Send()  找到有send的按钮
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


  browser.save_screenshot("/home/wwwroot/default/yiliao.png")

  #python
  try:
    browser.find_element_by_xpath("//div[contains(text(), 发送)]").click()
    browser.find_element_by_xpath("//div[contains(text(), 发 送)]").click()
  except Exception, e:
    # raise e
    print('发送')
    print(str(e))


  # or  终极大招  暂不做
  # chain = ActionChains(driver)
  # chain.context_click(implement).perform()

  # menu = driver.find_element_by_css_selector(".nav")
  # hidden_submenu =    driver.find_element_by_css_selector(".nav #submenu1")

  # actions = ActionChains(browser)
  # actions.move_to_element(menu)
  # actions.click(hidden_submenu)
  # actions.perform()



# 开始运行
ismobile=True


# # 进入浏览器设置
# chome_options = webdriver.ChromeOptions()
# # 设置中文
# chome_options.add_argument('lang=zh_CN.UTF-8')
# #设置不显示图片
# # ,"profile.managed_default_content_settings.javascript":2
# prefs = {"profile.managed_default_content_settings.images":2}
# chome_options.add_experimental_option("prefs",prefs)

# 更换头部
# 移动版没有广告地址了，需要点击了
# if ismobile:
#   chome_options.add_argument('user-agent="Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.23 Mobile Safari/537.36"')

cityname=''
ip_proxy=changeip(cityname)
# ip_proxy=''
# ip_proxy='1.82.216.135:80'
# ip_proxy='58.59.68.91:9797'

if len(ip_proxy)>20:
  print('NO IP AVILABLE')
  exit()

# 设置代理
# service_args = ['--proxy='+ip_proxy,'--proxy-type=socks5']
service_args = []




dcap={}
#从USER_AGENTS列表中随机选一个浏览器头，伪装浏览器
uainfo=generate_user_agent(os=('mac','win'))
print(type(uainfo))
print(uainfo)

# uainfo='Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36'

# dcap["phantomjs.page.settings.userAgent"] = (
#   uainfo
# )
# dcap["phantomjs.page.settings.loadImages"] = False
dcap["phantomjs.page.settings.loadImages"] = True



#### new ####  是不是还缺头
# text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8


# LiveWSKFT18569041=149877776756740603027; NKFT18569041fistvisitetime=1498748668041; NKFT18569041lastvisitetime=1498748668041; NKFT18569041visitecounts=1; NKFT18569041visitepages=1; LiveWSPGT23396196=149892222924837505454; NPGT23396196fistvisitetime=1498893132947; NPGT23396196lastvisitetime=1498893132947; NPGT23396196visitecounts=1; NPGT23396196visitepages=1; Hm_lvt_7060bc8bac6b843rfw353fb03c3d34e87=1498893133; LiveWSLZS21891916=149892238170925221131; NLZS21891916fistvisitetime=1498893279728; NLZS21891916lastvisitetime=1498893279728; NLZS21891916visitecounts=1; NLZS21891916visitepages=1; Hm_lvt_09a7d8e17be9c34a1eafcea17976202a=1498893280; LiveWSLUT29936309=149892926523469673288; NLUT29936309fistvisitetime=1498900163122; NLUT29936309lastvisitetime=1498900163122; NLUT29936309visitecounts=1; NLUT29936309visitepages=1; Hm_lvt_f5ea3e973d420d95a3999d557930d6fa=1498900163; LiveWSDDT80624187=149947419836708459718; NDDT80624187fistvisitetime=1499445085599; NDDT80624187lastvisitetime=1499445085600; NDDT80624187visitecounts=1; NDDT80624187visitepages=1; LiveWSPET20637501=149947421177398028329; NPET20637501fistvisitetime=1499445099514; NPET20637501lastvisitetime=1499445099515; NPET20637501visitecounts=1; NPET20637501visitepages=1; LiveWSDCT52464796=149990463545371455122; NDCT52464796fistvisitetime=1499875514444; NDCT52464796lastvisitetime=1499875514444; NDCT52464796visitecounts=1; NDCT52464796visitepages=1; UM_distinctid=15d378c1e4bf5b-05792607ssd2cd-5393662-100300-15d37s8e4cbb5; LiveWSPHT34309257=1512222296346446442351; LiveWSPHT34309257sessionid=1512222296346446442351; NPHT34309257fistvisitetime=1512193145022; LR_pm0=34309257; NPHT34309257lastvisitetime=1512193332482; NPHT34309257visitecounts=2; NPHT34309257visitepages=2
# Upgrade-Insecure-Requests:1
# Accept-Encoding:gzip, deflate, br
# Accept-Language:zh-CN,zh;q=0.9
# Cache-Control:max-age=0
# Connection:keep-alive


random.shuffle(bingli_id_list)

dcap['phantomjs.page.customHeaders.Accept'] ='text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
dcap['phantomjs.page.customHeaders.Host'] =host
dcap['phantomjs.page.customHeaders.User-Agent'] =uainfo
# dcap['phantomjs.page.customHeaders.Accept-Encoding'] ='gzip, deflate, br'

# dcap['phantomjs.page.customHeaders.Referer'] ='https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=0&rsv_idx=1&tn=baidu&wd=%E5%94%90%E5%B1%B1%E5%8C%BB%E9%99%A2'
dcap['phantomjs.page.customHeaders.Referer'] ='http://www.tstryy.com/jhsy/shengyuzhidao/'



dcap['phantomjs.page.customHeaders.Cookie'] =genercookies()

# dcap['phantomjs.page.customHeaders.Cookie'] = ''
dcap['phantomjs.page.customHeaders.Cache-Control'] ='max-age=0'
dcap['phantomjs.page.customHeaders.Connection'] ='keep-alive'
dcap['phantomjs.page.customHeaders.Upgrade-Insecure-Requests'] ='1'


# dcap['phantomjs.page.customHeaders.Accept-Encoding'] ='gzip, deflate'
dcap['phantomjs.page.customHeaders.Accept-Language'] ='zh-CN,zh;q=0.9'



# IP代理
proxy = webdriver.Proxy()  
proxy.proxy_type = ProxyType.MANUAL  
proxy.http_proxy = ip_proxy
proxy.add_to_capabilities(dcap)  

# service_args=service_args
browser = webdriver.PhantomJS(desired_capabilities=dcap)


browser.viewportSize={'width':824,'height':2200} #重要这句！
browser.maximize_window()

# chome_options.add_argument(('--proxy-server=http://' + ip_proxy))  
# browser = webdriver.Chrome(chrome_options=chome_options)  


browser.implicitly_wait(30)
browser.set_script_timeout(30)
browser.set_page_load_timeout(40)




try:
  # browser = webdriver.Chrome(desired_capabilities=capabilities)
  browser.get(openurlstring)
  time.sleep(20)
except Exception, e:
  pass
  print(str(e))
  f.close()
  browser.quit()
  exit()
# browser.get(openurlstring)


# 确认没问题 并做网络缓冲
logging.info(u'browser.title:'+browser.title+'.')
logging.info(browser.title)
# time.sleep(5)

# get_screenshot_as_file
browser.save_screenshot("/home/wwwroot/default/yiliao.png")


browser.save_screenshot("/usr/application/autoreplay/phantomjstest/screen/"+str(userid)+'/'+str(fname)+"screen.png")



time.sleep(0.1)


# 如果页面没有正常打开就关闭
if browser.title=='' or '.com' in browser.title or '.cn' in browser.title or '.net' in browser.title:
  pass
  print('page load failed  title:.com.net')
  f.close()
  browser.quit()
  exit()


# 如果页面没有正常打开就关闭
try:
  # titleelm=browser.find_element_by_css_selector('#kw')
  titleelm=browser.find_element_by_css_selector('iframe')
  print(titleelm)
except Exception, e:
  # raise e
  print(str(e))
  print('browser.quit() cant find iframe')
  f.close()
  browser.quit()
  print('page opend error ,quit quit quit')
  print('page opend error ,quit quit quit')
  exit()






# 验证码识别
# import damatu
# m2 = hashlib.md5()   

# # #云打码api
# from ctypes import *
# # YDMApi = windll.LoadLibrary('yundamaAPI-x64')

# #yzmimg
# 验证码判断
iscode=0
coderobot=browser.find_elements_by_css_selector('#modalDiv_Chatpreobj')
if len(coderobot)>0:
  print 'robot'
  print 'robot'
  print 'robot'
  print 'robot'
  iscode=1
  # pass
  # f.close()
  # browser.quit()
  # exit()
  # 验证码模块
  # browser.save_screenshot('web.jpg')
  imgelement=browser.find_element_by_css_selector('#yzmimg')
  location = imgelement.location  #获取验证码x,y轴坐标
  size=imgelement.size  #获取验证码的长宽
  rangle=(int(location['x']),int(location['y']),int(location['x']+size['width']),int(location['y']+size['height'])) #写成我们需要截取的位置坐标

  i=Image.open("/usr/application/autoreplay/phantomjstest/screen/"+str(userid)+'/'+str(fname)+"screen.png") #打开截图
  frame4=i.crop(rangle)  #使用Image的crop函数，从截图中再次截取我们需要的区域
  frame4.save("/usr/application/autoreplay/phantomjstest/code/"+str(userid)+str(fname)+"code.jpg")


  # qq=Image.open('code.jpg')
  # text=pytesseract.image_to_string(qq).strip() #使用image_to_string识别验证码
  # print 'code:'
  # print text


  # 用户名
  username    = 'cdsbtest'
  # 密码
  password    = 'cdsb123456'                            
  # 软件ＩＤ，开发者分成必要参数。登录开发者后台【我的软件】获得！
  appid       = 3035                                     
  # 软件密钥，开发者分成必要参数。登录开发者后台【我的软件】获得！
  appkey      = '0856355e1dd686e7819093bcd2843176'    
  # 图片文件
  # filename    = 'getimage.jpg'                        
  # 验证码类型，# 例：1004表示4位字母数字，不同类型收费不同。请准确填写，否则影响识别率。在此查询所有类型 http://www.yundama.com/price.html
  codetype    = 1004
  # 超时时间，秒
  timeout     = 60     

  imgfilename="/usr/application/autoreplay/phantomjstest/code/"+str(userid)+str(fname)+"code.jpg"

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

  time.sleep(0.5)
  browser.find_element_by_css_selector('#ccode').send_keys(codestr.encode('utf-8'))
  time.sleep(0.5)
  browser.find_element_by_css_selector('#Button1').send_keys(Keys.ENTER)
  time.sleep(0.5)





# 在呼叫在线客服人
isrobot=0
callforchathtml=browser.find_element_by_xpath("//div[contains(text(), 在呼叫在线客服人)]")
if callforchathtml.is_displayed():
  isrobot=1

if isrobot and not(iscode):
  pass
  logging.info(u'robot loop')
  f.close()
  browser.quit()
  exit()





get_friends_message('')