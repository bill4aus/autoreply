# coding=utf-8
import random
from src.util import getSecs
from src.personInfo import personInfoWeixin
def isHello(p, msg):
    if p.seq == 1 or (msg.request.startswith(("你好","您好")) and (p.seq < 3)):
        helloList = ["nihao ,医生", "你好,医生", "医生,你好"]
        res = random.choice(helloList)
        msg.setRespose(res)
        return 1      
    return 0
def isPersonInfo(p, msg):
    req = msg.request
    pInfo = p.getPersonInfo()
    
    weixin = personInfoWeixin(pInfo, msg)
    if weixin.ismsgType(msg):
        return 1
        
    if (-1 < req.find("今年") and -1 < req.find("多大")) or \
       (-1 < req.find("岁") and msg.length < 7) or \
       (-1 < req.find("多大") and msg.length < 7):
        num = pInfo.checkInfo("age")
        if num == 1:
            msg.setRespose("....嗯?")
            msg.setRespose("我刚刚说了啊? 我今年" + pInfo.getInfo("age"))
            pInfo.setInfo("age")
            return 1
        if num == 2:
            print(".........")
            pInfo.setInfo("age")
            return 1
        if num > 2:
            return 1
        rand = random.choice([1,2])
        res1 = ("26了,今年我", "我今年26了")
        res2 = ("怎么了?","年龄有什么影响么,,医生")
        res3 = ("你问我年龄么,我今年刚25..", "我今年刚25")
        if rand == 1:
            res = random.choice(res1)
            msg.setRespose(res, getSecs(len(res) + msg.length))
            res = random.choice(res2)
            msg.setRespose(res, getSecs(len(res)))
            pInfo.setInfo("age", "26")
        if rand == 2:
            res = random.choice(res3)
            msg.setRespose(res, getSecs(len(res) + msg.length))
            pInfo.setInfo("age", "25")   
        return 1    
    if msg.length < 12:
        addrkey = ["住哪","住那","你家是", "你家哪", "你家那", "你家在"]
        res1 = ("我就是市里的","我家离得比较远,在郊县","在下面的一个县,比较远")
        keyInAddr = 0
        for key in addrkey:
            if -1 < req.find(key):
                keyInAddr = 1
                pass
        if  keyInAddr == 1 or \
            (-1 < req.find("家") and -1 < req.find("市")) or \
            (-1 < req.find("家") and -1 < req.find("住")) or \
            (-1 < req.find("哪里") and -1 < req.find("住")) or \
            (-1 < req.find("住") and req.endswith("么")) and msg.length < 8  :
            num = pInfo.checkInfo("addr")
            if num == 1:
                msg.setRespose("什么.....")
                msg.setRespose("我刚刚不是讲了么? " + pInfo.getInfo("addr"))
                pInfo.setInfo("addr")
                return 1
            if num == 2:
                print(".........不重要")
                pInfo.setInfo("addr")
                return 1
            if num > 2:
                return 1
            res = random.choice(res1)
            msg.setRespose(res, getSecs(len(res) + msg.length))
            pInfo.setInfo("addr", res)
            return 1
    if (-1 < req.find("男的") and -1 < req.find("女的")) or\
       (-1 < req.find("男的") and -1 < req.find("是")):
        num = pInfo.checkInfo("sex")
        if num == 1:
            msg.setRespose("什么.....")
            msg.setRespose("我刚刚不是讲了么? " + pInfo.getInfo("age"))
            pInfo.setInfo("sex")
            return 1
        if num == 2:
            print("再问自杀")
            pInfo.setInfo("sex")
            return 1
        if num > 2:
            return 1
        res1 = ("我男的","我就男的","是男的")
        res = random.choice(res1)
        msg.setRespose(res, getSecs(len(res) + msg.length))
        pInfo.setInfo("sex", res)           
        return 1       
    if msg.length < 7:
        if req.startswith("是") or req.endswith(("吗","么")):
            res1 = ("en...", "嗯...时的", "en, 是的")
            res = random.choice(res1)
            msg.setRespose(res, getSecs(len(res) + msg.length))
            return 1   
    return 0    

def isAskIllness(p, msg):
    req = msg.request
    if -1 < req.find("病") and \
       (-1 < req.find("多长") or -1 < req.find("多久")):
        p.setTaolu(1)
        return 1
    return 0
def isIntroHosptial(msg):
    if msg.length > 20:
        msg.setTaolu(2)
        return 1
def isUnknown(p, msg):
    if msg.length < 4:
        res1 = ("蒽..","..", "en","嗯","--")
        res = random.choice(res1)
        msg.setRespose(res, getSecs(len(res) + msg.length))
        if p.seq > 12: 
            p.setTaolu(3)
        return 1 
    return 0
def handleMsg(p, msg):
    #问候
    if isHello(p, msg):
        return 
    if isPersonInfo(p, msg):
        return
    if isAskIllness(p, msg):
        return
    if isIntroHosptial(p, msg):
        return
    if isUnknown(p, msg):
        return


    