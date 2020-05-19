#!/opt/anaconda/bin/python
# coding:utf-8
# encoding=utf-8
import httplib, mimetypes, urlparse, json, time
import urllib2
import random


# http://webapi.http.zhimacangku.com/getip?num=1&type=1&pro=&city=0&yys=0&port=1&time=1&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions=
# 芝麻
def changeip(ctname):
  global ip_proxy
  # city=urllib.quote(urllib.quote(ctname))
  # 555527369568174
  # &category=2
  # 唐山0
  # 'http://webapi.http.zhimacangku.com/getip?num=1&type=1&pro=&city=0&yys=0&port=1&time=1&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=2&regions='
  url = "http://webapi.http.zhimacangku.com/getip?num=1&type=1&pro=&city=&yys=0&port=1&time=1&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions="+ctname
  # print(url)
  print('get ip proxy')
  # time.sleep(0.1)
  try:
    req = urllib2.Request(url)
    res_data = urllib2.urlopen(req)
    res = res_data.read()
    ip_proxy=res
  except Exception, e:
    
    ip_proxy=''
    pass
    print('browser.quit() changeip')
    # browser.quit()
    print(str(e))
    # loop()
    print('\n')
    print('\n')
    print('\n')
    # raise e

  # print('ip_proxy')
  print('new proxy ip::'+ip_proxy)
  return ip_proxy


# # 大象
# def changeip(ctname):
#   global ip_proxy
#   # city=urllib.quote(urllib.quote(ctname))
#   # 555527369568174
#   # &category=2
#   url = "http://tvp.daxiangdaili.com/ip/?tid=557160769352451&num=1&delay=1&longlife=5&category=2&area="+ctname+"&foreign=none&filter=on"
#   # print(url)
#   print('get ip proxy')
#   # time.sleep(0.1)
#   try:
#     req = urllib2.Request(url)
#     res_data = urllib2.urlopen(req)
#     res = res_data.read()
#     ip_proxy=res
#   except Exception, e:
    
#     ip_proxy=''
#     pass
#     print('browser.quit() changeip')
#     # browser.quit()
#     print(str(e))
#     # loop()
#     print('\n')
#     print('\n')
#     print('\n')
#     # raise e

#   # print('ip_proxy')
#   print('new proxy ip::'+ip_proxy)
#   return ip_proxy



# # changeipbycityVIP
# def changeipVIP(ctname):
#   global ip_proxy
#   # city=urllib.quote(urllib.quote(ctname))
#   url = "http://vtp.daxiangdaili.com/ip/?tid=556742179509367&num=1&delay=1&area="+ctname+"&filter=on"
#   # print(url)
#   print('get ip proxy')
#   # time.sleep(0.1)
#   try:
#     req = urllib2.Request(url)
#     res_data = urllib2.urlopen(req)
#     res = res_data.read()
#     ip_proxy=res
#   except Exception, e:
    
#     ip_proxy=''
#     pass
#     print('browser.quit() changeip')
#     # browser.quit()
#     print(str(e))
#     # loop()
#     print('\n')
#     print('\n')
#     print('\n')
#     # raise e

#   # print('ip_proxy')
#   print('new proxy ip::'+ip_proxy)
#   return ip_proxy

def genercookies():
  cookiesid=''
  # for i in range(8):
  #   thnum = random.randint(1,7)
  #   cookiesid=cookiesid+str(thnum)
  cookiesid='34309257'
  t = time.time()
  getnowTime = lambda:int(round(t * 1000))
  nowTime=getnowTime()
  totime=nowTime+29153865
  # print(nowTime)
  # print(totime)
  cookielist=['LR_pm0='+cookiesid,'LiveWSPHT'+cookiesid+'='+str(totime)+'54424362','LiveWSPHT'+cookiesid+'sessionid='+str(totime)+'54424362','NPHT'+cookiesid+'fistvisitetime='+str(nowTime),'NPHT'+cookiesid+'lastvisitetime='+str(nowTime),'NPHT'+cookiesid+'visitecounts=1','NPHT'+cookiesid+'visitepages=1']
  return '; '.join(cookielist)



def genewechatid():
    e_userName=[]
    usableName_char ="1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-_1234567890"
    wchatlen=random.choice([5,7,9,11,14])
    for i in range(wchatlen):  
        e_userName.append(random.choice(usableName_char))
    userName = ''.join(e_userName)
    return userName