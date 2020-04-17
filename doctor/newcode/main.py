# coding=utf-8

import re
from src.person import person
from src.msg import msgInstance
from src.handleMsg import handleMsg
from src.handleTaolu import handleTaolu
from src.util import logInfo
import json

from flask import Flask,request
app = Flask(__name__)


default = "--"
threadList = {}
personList = {}

def mainLoop(doctalk, keshi, userid):
    if userid in personList.keys():
        telangpu = personList[userid]
    else:
        telangpu = person(userid)
        personList.setdefault(userid, telangpu)     
    requestMsg = re.sub(r'[\s\.?,。，]', '', doctalk)
    msg = msgInstance(requestMsg)
    handleMsg(telangpu, msg)       
    taolu = telangpu.getTaolu()
    if taolu != 0 and taolu < 5:
        print("begin taolu:", taolu)
        handleTaolu(msg, taolu)
    
    respose = msg.getRespose()
    if len (respose["list"]) == 0:
        for val in respose["list"]:
            logInfo((msg.seq, val.get("word") + "time:",val.get("time")))
    return respose
@app.route('/')
def api_article():
    print('')
    doctalk = request.args.get('doctalk')
    keshi = request.args.get('keshi')
    userid = request.args.get('userid')
    myresponse = mainLoop(doctalk,keshi,userid)
    return  json.dumps(myresponse,ensure_ascii=False)

@app.route('/colse')
def close_dialog():
    userid=request.args.get('userid')
    if "error" != personList.pop(userid, "error"):
        logInfo(("info", "close" + userid))
    else:
        logInfo(("error", "failed close" + userid))
            
if __name__ == '__main__':
#     mainLoop()
    app.run(host="0.0.0.0",port=9001)
#     return