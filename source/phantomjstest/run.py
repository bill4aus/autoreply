#!/opt/anaconda/bin/python
# coding:utf-8
# encoding=utf-8
# Filename: put_files_hdfs.py
# 让多条命令并发执行,如让多条scp,ftp,hdfs上传命令并发执行,提高程序运行效率
import datetime
import os
import threading
import time
import sys
 
def execCmd(cmd):
 try:
  print("%s start at :%s" % (cmd,datetime.datetime.now()))
  os.system(cmd)
  print("%s stop at :%s" % (cmd,datetime.datetime.now()))
 except Exception, e:
  print('%s\t failed for :\r\n%s' % (cmd,e))
 
if __name__ == '__main__':

 starttime=int(time.time())
 #url chat
 openurlstring=sys.argv[4]
 print('openurlstring')
 print(openurlstring)
 #number to online
 number_online=sys.argv[3]
 print('number_online')
 print(number_online)
 # 需要执行的命令列表
 cmds = []
 #并发数目
 theadnum=int(number_online)
 #分类目录
 # illclass='erke'
 #number to online
 illclass=sys.argv[2]
 print('illclass')
 print(illclass)

 userid=sys.argv[1]
 print('userid')
 print(userid)
 #持续时间
 # duration
 # 科室列表
 # keshi_list=['chuanranbingke','pifuke','guke','jingshenxinlike','neike','qitakeshi','waike','wuguanke','zhongyike','erke','erkezonghe','fuchanke','pifuxingbingke','yanke','yijike','yixueyingxiangxue','zhongliuke']
 
 # cd /usr/application/autoreplay/phantomjstest
 # python run.py 1 fuchanke 5 http://boai.zoossoft.com/LR/Chatpre.aspx?id=LCE66634992&lng=cn

 if 'zoossoft' in openurlstring or '/LR/' in openurlstring :
  pass
  pyfilename='zoosoft_run.py'+'  '+userid+'  '+illclass+'  '+openurlstring
 elif 'kuaishang' in openurlstring or '/bs/im' in openurlstring:
  pass
  pyfilename='kuaishangtong_run.py'+'  '+userid+'  '+'  '+illclass+'  '+openurlstring
 else:
  print('url error')
  exit()

 # pyfilename='run_zoosoft.py'+'  '+openurlstring
 # pyfilename='run_kuaishangtong.py'
 # pyfilename='testbot.py'
 # for x in xrange(1,theadnum):
 # 	cmds.append('python '+pyfilename)
 exceutecommandstr='python '+pyfilename
 print('exceutecommandstr') 
 print(exceutecommandstr) 
 #线程池
 threads = []
 while True:

  nowtime=int(time.time())
  #持续 监控 时间 默认10分钟
  # duration=60*60*0.5
  # duration=60*2
  duration=60*120*4
  # duration=60*2
  if nowtime-starttime>duration:
    exit()

  # print(threading.active_count())
  active_countt=threading.active_count()
  print('active_countt')
  print(active_countt)
  print(type(active_countt))
  for thid in range(0,(theadnum-active_countt)):
    print('thid')
    print(thid)
    th = threading.Thread(target=execCmd, args=(exceutecommandstr,))
    th.setDaemon(True)
    th.start()
    threads.append(th)
    time.sleep(40)
  time.sleep(60*3)


# else:
# 	print('number enough')