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
import uuid

# 上级目录
sys.path.append('../')
import robot.robot as robot
from supportfunction import genewechatid

class schedule(object):
  """docstring for schedule"""
  def __init__(self, browser):
    super(schedule, self).__init__()
    self.browser = browser
    


  # 具体要做的事情
  def run(self,url,source,keshi):
    # open
    # http://lbs.zoosnet.net/LR/Chatpre.aspx?id=LBS31671888&cid=1524380007409445977319&lng=cn&sid=1524380007409445977319&p=http%3A//hzaboluo-mtbd.cn/pc/yypp/%3Fbd-hzabl06%3DCC-%28pp%29pp-795/%3Futm_source%3D%25E6%259D%25AD%25E5%25B7%259E%25E9%2598%25BF%25E6%25B3%25A2%25E7%25BD%259706%26utm_medium%3D%25E7%25AB%259E%25E4%25BB%25B7%26utm_term%3D%25E6%259D%25AD%25E5%25B7%259E%25E9%2598%25BF%25E6%25B3%25A2%25E7%25BD%2597%25E7%2594%25B7%25E7%25A7%2591%26utm_content%3D002%252D%25E6%259D%25AD%25E5%25B7%259E%25E9%2598%25BF%25E6%25B3%25A2%25E7%25BD%2597%26utm_campaign%3DCC%252D%25EF%25BC%2588pp%25EF%25BC%2589%25E5%2593%2581%25E7%2589%258C&rf1=https%3A//www.baidu&rf2=.com/s%3Fie%3Dutf-8%26f%3D8%26rsv_bp%3D0%26rsv_idx%3D1%26tn%3Dbaidu%26wd%3D%25E6%259D%25AD%25E5%25B7%259E%2520%25E7%2594%25B7%25E7%25A7%2591%26rsv_pq%3Df13bbd920003e228%26rsv_t%3Dc8ffPqs0X%252F%252FPFur077XE3JFvGlU42pmIXq3i64qF6nh1SR8tdGYT%252BIoXlcw%26rqlang%3Dcn%26rsv_enter%3D1%26rsv_sug3%3D18%26rsv_sug1%3D9%26rsv_sug7%3D100%26rsv_sug2%3D0%26inputT%3D6033%26rsv_sug4%3D154656&e=%25u6765%25u81EA%25u9996%25u9875%25u81EA%25u52A8%25u9080%25u8BF7%25u7684%25u5BF9%25u8BDD&msg=&d=1524380017081
    
    # url="http://lbs.zoosnet.net/LR/Chatpre.aspx?id=LBS31671888&cid=1524380007409445977319&lng=cn&sid=1524380007409445977319&p=http%3A//hzaboluo-mtbd.cn/pc/yypp/%3Fbd-hzabl06%3DCC-%28pp%29pp-795/%3Futm_source%3D%25E6%259D%25AD%25E5%25B7%259E%25E9%2598%25BF%25E6%25B3%25A2%25E7%25BD%259706%26utm_medium%3D%25E7%25AB%259E%25E4%25BB%25B7%26utm_term%3D%25E6%259D%25AD%25E5%25B7%259E%25E9%2598%25BF%25E6%25B3%25A2%25E7%25BD%2597%25E7%2594%25B7%25E7%25A7%2591%26utm_content%3D002%252D%25E6%259D%25AD%25E5%25B7%259E%25E9%2598%25BF%25E6%25B3%25A2%25E7%25BD%2597%26utm_campaign%3DCC%252D%25EF%25BC%2588pp%25EF%25BC%2589%25E5%2593%2581%25E7%2589%258C&rf1=https%3A//www.baidu&rf2=.com/s%3Fie%3Dutf-8%26f%3D8%26rsv_bp%3D0%26rsv_idx%3D1%26tn%3Dbaidu%26wd%3D%25E6%259D%25AD%25E5%25B7%259E%2520%25E7%2594%25B7%25E7%25A7%2591%26rsv_pq%3Df13bbd920003e228%26rsv_t%3Dc8ffPqs0X%252F%252FPFur077XE3JFvGlU42pmIXq3i64qF6nh1SR8tdGYT%252BIoXlcw%26rqlang%3Dcn%26rsv_enter%3D1%26rsv_sug3%3D18%26rsv_sug1%3D9%26rsv_sug7%3D100%26rsv_sug2%3D0%26inputT%3D6033%26rsv_sug4%3D154656&e=%25u6765%25u81EA%25u9996%25u9875%25u81EA%25u52A8%25u9080%25u8BF7%25u7684%25u5BF9%25u8BDD&msg=&d=1524380017081"
    
    # 直接打开目标
    self.browser.open(url)
    # 跳转到目标
    # self.browser.openwithsource(url,source)

    # 开始时间
    starttime=int(time.time())
    # 标志状态
    shorttime=0
    middletime=0
    laragetime=0
    
    # 生成用户id
    thisuserid=uuid.uuid1()

    # 机器人
    mybot=robot.robot(keshi,thisuserid)
    wechatid_for_play=genewechatid()
    #while 循环
    while True:
      print('.......this time loop.......')
      # 基本规则验证
      nowtime=int(time.time())
      if nowtime-starttime>60*1.5:
        time.sleep(2)
        print(nowtime-starttime)
        listele=self.browser.getelementsbycss('.msg-box .msg-agent')
        if len(listele)<2 and shorttime==0:
          slist=['还在么？ ','医生？','咋回事啊？ ','怎么不说话啊？','在么医生。。。','医生你搞什么呢。。','说话啊','等你那么久了呢','快点啊。。。']
          self.browser.send(random.choice(slist))
          # browserquit()
          shorttime=1

      if nowtime-starttime>60*4:
        print(nowtime-starttime)
        listele=self.browser.getelementsbycss('.msg-box .msg-agent')
        if len(listele)<4 and middletime==0:
          slist=['那你联系我一下吧 。。'+wechatid_for_play,'医生。。。你加我微信吧 '+wechatid_for_play,'是要提供我微信号？','麻烦加我一下可以么。。。'+wechatid_for_play,'医生。。。麻烦加我微信 '+wechatid_for_play]
          self.browser.send(random.choice(slist))
          middletime=1
      if nowtime-starttime>60*6:
        print(nowtime-starttime)
        listele=self.browser.getelementsbycss('.msg-box .msg-agent')
        if len(listele)<15 and laragetime==0:
          # slist=['你们医院垃圾，客服也是垃圾 ','我看你们医院评价不好啊，太歪了','你们天天坑人是不是缺心眼 ','你们良心不会痛么','傻比客服医生','垃圾啊！','操你大爷！什么玩意','去你老母的，黑心医院','滚你妈的','去你妈的','尼玛傻比么','傻比医生','你们医院垃圾，客服也是垃圾 ','我看你们医院评价不好啊，太歪了','你们天天坑人是不是缺心眼 ','你们良心不会痛么']
          # slist=['我看你们医院评价不好啊，太歪了','我看你们医院评价不好啊，太歪了']
          # self.browser.send(random.choice(slist))
          # laragetime=1
          self.browser.quit()
      if nowtime-starttime>60*8:
        print(nowtime-starttime)
        self.browser.quit()
      # nowtime=int(time.time())
      # #8分钟是不是更好？？或者判断下是不是可以关闭了，比如对方一直不说话，出现验证码等等意外情形
      # if nowtime-starttime>60*3:
        # self.browser.quit()
      # self.browser.screen("D:/zip/12/"+str(fname)+"screen.png")



      # 消息循环
      # 获取消息
      #get message
      print("get message")

      messenger=self.browser.getmessage()
      print("get message done")

      print(messenger.new)
      if messenger.new:
        print('new message:')
        print(messenger.newmsg)
        replay=mybot.get_respone(messenger.newmsg)
        # print(replay)
        
        # .decode('utf-8')
        if replay == 'stop':
          print 'stop to say'
          # return ;
        else:
          iamtosaystring,doctor_intent,my_intent=replay.split("||")
          # saylist=uwords.split('，')
          # send_massage(name,1,uwords)
          pass
          #send message
          print('send message') 
          print('my_intent')
          print(my_intent)

          #new logic
          # wechatid_for_play=genewechatid()
          dintent=doctor_intent
          myintent=my_intent


          if dintent=='医生不爽':
            # slist=['傻比客服医生','垃圾啊！','操你大爷！什么玩意']
            # slist=['拜拜！','再见！','不送！']
            slist=['好的','行','OK']
            self.browser.send(random.choice(slist))
            self.browser.quit()
          # if dintent=='安排诊号面诊':
          #   slist=['那你加我微信吧 '+wechatid_for_play,'我微信号是'+wechatid_for_play,'我不一定有时间，先加我吧 '+wechatid_for_play]
            # self.browser.send(random.choice(slist))
            # self.browser.quit()
          # if dintent=='询问是否有时间过来看病':
          #   slist=['那你加我微信吧 '+wechatid_for_play,'我微信号是'+wechatid_for_play,'我不一定有时间，先加我吧 '+wechatid_for_play]
            # self.browser.send(random.choice(slist))
            # self.browser.quit()
          # if dintent=='还在么':
          #   # slist=['你们医院垃圾，客服也是垃圾 ','我看你们医院评价不好啊，太歪了','你们天天坑人是不是缺心眼 ','你们良心不会痛么']
          #   slist=['你们医院评价不好，太歪了']
            # self.browser.send(random.choice(slist))
            # self.browser.quit()
          # if myintent=='准备过来':
          #   # slist=['那你加我微信吧 '+wechatid_for_play,'我微信号是'+wechatid_for_play,'我不一定有时间，先加我吧 '+wechatid_for_play]
          #   slist=['你们医院怎么过去呢 ','坐公交几路比较好','你们没有分院吧 ','我需要准备什么么']
            # self.browser.send(random.choice(slist))
            # self.browser.quit()
          # if myintent=='我考虑下关闭':
          #   slist=['那你加我微信吧 '+wechatid_for_play,'我微信号是'+wechatid_for_play,'我不一定有时间，先加我吧 '+wechatid_for_play]
            # self.browser.send(random.choice(slist))
            # self.browser.quit()
          if myintent=='愤怒关闭':
            # slist=['去你老母的，黑心医院','滚你妈的','去你妈的','尼玛傻比么','傻比医生','你们医院垃圾，客服也是垃圾 ','我看你们医院评价不好啊，太歪了','你们天天坑人是不是缺心眼 ','你们良心不会痛么']
            # slist=['拜拜！','再见！','不送！']
            # slist=['拜拜！','再见！','不送！']
            slist=['好的','行','OK']
            self.browser.send(random.choice(slist))
            self.browser.quit()
          # if myintent=='不方便过来':
          #   slist=['那你加我微信吧 '+wechatid_for_play,'我微信号是'+wechatid_for_play,'我不一定有时间，先加我吧 '+wechatid_for_play]
          # self.browser.send(random.choice(slist))
            # self.browser.quit()
          
          # 回答问题
          if '有没有'  in iamtosaystring:
              iamtosaystring='有的'
              return
              self.browser.send(random.choice(slist))
          if '是不是'  in iamtosaystring:
              iamtosaystring='嗯嗯，对的'
              self.browser.send(random.choice(slist))
              return
          if '对吧'  in iamtosaystring:
              iamtosaystring='嗯嗯，是的'
              self.browser.send(random.choice(slist))
              return


          if myintent=='打招呼':
            if ('你好' not in iamtosaystring) or ('您好' not in iamtosaystring):
              iamtosaystring='你好,'+iamtosaystring


          self.browser.send(iamtosaystring)
      else:
        pass
        # noting happened
      time.sleep(1)
    # shut down
    # time.sleep(30)
    # self.browser.quit()

    

  # 执行schedule
  def start(self,url,source,keshi):
    # self.run(url,source,keshi)
    try:
      # self.run()
      self.run(url,source,keshi)
    except Exception, e:
      print(url,source,keshi)
      print(str(e))
      # raise e
      self.browser.quit()
    