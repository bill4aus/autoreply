#!/usr/bin/env python
#coding:utf-8
# -*- coding: utf-8 -*-

# 导入工具
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.proxy import Proxy,ProxyType

from selenium.common.exceptions import NoSuchElementException 
import time
from bs4 import BeautifulSoup
import sys
import io
import logging
from apscheduler.schedulers.background import BackgroundScheduler
import urllib
import urllib2
import threading
import json
import random
import math
import urlparse

import MySQLdb
reload(sys)
sys.setdefaultencoding('utf-8')

import requests

import hashlib   
from selenium.webdriver.common.keys import Keys  

# from PIL import Image
from PIL import Image

# import pytesseract
# from kmeans import invokefunc

import threading
from selenium.webdriver.support.wait import WebDriverWait

# import damatu




# 进入浏览器设置
chome_options = webdriver.ChromeOptions()
# 设置中文
chome_options.add_argument('lang=zh_CN.UTF-8')
#设置不显示图片
# ,"profile.managed_default_content_settings.javascript":2
prefs = {"profile.managed_default_content_settings.images":2}
chome_options.add_experimental_option("prefs",prefs)
chome_options.add_argument('user-agent="Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.23 Mobile Safari/537.36"')
browser = webdriver.Chrome(chrome_options=chome_options)
# browser.implicitly_wait(30)
# browser.set_script_timeout(30)
# browser.set_page_load_timeout(40)

time.sleep(1)

fo = open("comm.txt", "w")



openurlstring='http://xw.qq.com/m/news/index.htm'
browser.get(openurlstring)


# for x in xrange(1,30):
#     browser.find_element_by_css_selector('.more .gomore').click()
#     time.sleep(3)


time.sleep(60*3)


hreflist=browser.find_elements_by_css_selector('a')

clicklist=[]

print(len(hreflist))
for hreff in hreflist:
    print(hreff)
    clicklist.append(hreff.get_attribute('href'))
    # time.sleep(5)




print(len(clicklist))
for hrefurl in clicklist:
    print(hrefurl)
    browser.get(hrefurl)
    time.sleep(1)


    try:

        itemtext=''

        # find elem
        thistitle=browser.title
        itemtext=thistitle+'||'
        
        browser.find_element_by_css_selector('.fixnav  .rpl').click()
        commlist=browser.find_elements_by_css_selector('.comment .content')
        for commhtml in commlist:
            itemtext=itemtext+commhtml.text+',,'

        browser.back()
        browser.back()

        # print(itemtext.encode('gbk'))

        fo.writelines(itemtext.encode('utf-8')+'\n')

        time.sleep(5)
    except Exception, e:
        # raise e
        print(str(e))



# while 1:
#     pass

#     try:
#         itemtext=''
#         # find elem
#         thistitle=browser.title
#         itemtext=thistitle+'||'

#         browser.find_element_by_css_selector('.fixnav  .rpl').click()
#         commlist=browser.find_elements_by_css_selector('.comment .content')
#         for commhtml in commlist:
#             itemtext=itemtext+commhtml.text+',,'
#         print(itemtext.encode('gbk'))
#     except Exception, e:
#         # raise e
#         print(str(e))


#     time.sleep(3)





