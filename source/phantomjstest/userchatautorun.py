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

import MySQLdb
import MySQLdb.cursors

conn={}
conn= MySQLdb.connect(
        host='127.0.0.1',
        port = 3306,
        user='root',
        passwd='root',
        db ='botmanager',
        charset="utf8",
        cursorclass=MySQLdb.cursors.DictCursor
        )
print(conn)

tasklist=[]
######################################################
cur = conn.cursor()
# (state =1 or state=0) 
sqli="SELECT * FROM `user` WHERE state =1 and isrun=1"
count=cur.execute(sqli)
# print(conn.commit())
results = cur.fetchall()   
for r in results:
    # print(type(r))
    # print r['id']
    # print r['chaturl']
    # print r['num_online']
    # print r['chattype']
    # print r[3]
    # keywords.append({'chaturl':r[6],'id':r[0]})
    tasklist.append({'id':r['id'],'chaturl':r['chaturl'],'num_online':r['num_online'],'chattype':r['chattype']})
cur.close()




def execCmd(cmd):
 try:
  print("%s start at :%s" % (cmd,datetime.datetime.now()))
  os.system(cmd)
  print("%s stop at :%s" % (cmd,datetime.datetime.now()))
 except Exception, e:
  print('%s\t failed for :\r\n%s' % (cmd,e))




if __name__ == '__main__':
 for x in tasklist:
  print('task start....')
  exceutecommandstr='python run.py'+'  '+str(x['id'])+'  '+str(x['chattype'])+'  '+str(x['num_online'])+'  '+str(x['chaturl'])
  print('exceutecommandstr') 
  print(exceutecommandstr) 
  #线程池
  threads = []
  th = threading.Thread(target=execCmd, args=(exceutecommandstr,))
  # th.setDaemon(True)
  th.setDaemon(False)
  th.start()
  threads.append(th)
  time.sleep(1)
  # time.sleep(60)
exit()


# else:
# 	print('number enough')