#!/usr/bin/python
# encoding=utf-8
# Filename: put_files_hdfs.py
# 让多条命令并发执行,如让多条scp,ftp,hdfs上传命令并发执行,提高程序运行效率
import datetime
import os
import threading
import time
 
def execCmd(cmd):
 try:
  print("%s start at :%s" % (cmd,datetime.datetime.now()))
  os.system(cmd)
  print("%s stop at :%s" % (cmd,datetime.datetime.now()))
 except Exception, e:
  print('%s\t failed for :\r\n%s' % (cmd,e))
 
if __name__ == '__main__':
 # 需要执行的命令列表
 cmds = []
 theadnum=2
 pyfilename='kuaishangtong.py'
 # pyfilename='bot_for_zoosoft.pyc'
 # pyfilename='zoosoft.py'
 # pyfilename='testbot.py'
 # 从1开始
 for x in xrange(1,theadnum+1):
 	pass
 	cmds.append('python '+pyfilename)

  
 #线程池
 threads = []
  
 print("start:%s" % datetime.datetime.now())
 
 for cmd in cmds:
  th = threading.Thread(target=execCmd, args=(cmd,))
  th.start()
  threads.append(th)
  time.sleep(90)
	  
 # 等待线程运行完毕
 for th in threads:
  # th.setDaemon(True)
  th.join(1)
  print("stop :%s" % datetime.datetime.now())

time.sleep(40)
while True:
  # print(threading.active_count())
  active_countt=threading.active_count()
  print("active_countt")
  print(active_countt)
  # print(type(active_countt))
  if int(active_countt)<theadnum:
	 for cmd in cmds:
	  th = threading.Thread(target=execCmd, args=(cmd,))
	  th.start()
	  threads.append(th)
	  time.sleep(90)
	 # 等待线程运行完毕
	 for th in threads:
	  # th.setDaemon(True)
	  th.join(5)
	  print("stop :%s" % datetime.datetime.now())
	 threads=[]
	 time.sleep(3)
  time.sleep(120)


else:
	print('number enough')