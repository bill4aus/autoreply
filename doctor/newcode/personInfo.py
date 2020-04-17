#coding=utf-8
from src.msgDeal import infoBase, msgdeal
from src.util import getContactInfo, getContactQQ, getSecs
from src.intentionCfg import GetPersonInfo
import random
class personInfo(infoBase):
    def __init__(self, intentionList = GetPersonInfo()):
#         self.infoList = intentionList
        infoBase.__init__(self, intentionList)
class personInfoWeixin(msgdeal):
    def __init__(self, pInfo, msg):
        self.msg = msg
        self.pInfo =pInfo
        self.req = msg.getRequest()
    def ismsgType(self, msg):
        return -1 < self.req.find("微信") or \
           -1 < self.req.find("qq") or -1 < self.req.find("QQ") or\
           -1 < self.req.find("联系方式") or \
          (-1 < self.req.find("威信") and -1 < self.req.find("加") and msg.length < 14)
    def thridDeal(self):
        self.msg.setRespose("有毛病了,一直问个傻子")
        self.pInfo.setInfo("weixin")
    def secondDeal(self):
            self.msg.setRespose("??")
            self.msg.setRespose("我刚刚不是发给你了么,没发过去?" + self.pInfo.getInfo("weixin"))
            self.pInfo.setInfo("weixin")
    def fristDeal(self):
        weixin,info = getContactInfo()
        if self.req.find("加我") and -1 < self.req.find(""):
            if -1 < self.req.find("qq") or -1 < self.req.find("QQ"):
                res = "好,可以的哈"
                weixin,info = getContactQQ()
            else:
                res = "医生你加我我的吧"
            self.msg.setRespose(res, getSecs(len(res) + self.msg.length))
            self.msg.setRespose(info + "..这我的")
            self.pInfo.setInfo("weixin", weixin + str(info))
            return 1
        if weixin == "qq":
            res1 = ("医生,那个不怎么用,你加我的qq吧", "医生你加我qq吧,这个")
            res = random.choice(res1)
            self.msg.setRespose(res, getSecs(len(res) + self.msg.length))
            self.msg.setRespose(info + "..我qq,你加的时候你备注一下吧")
            self.pInfo.setInfo("weixin", "qq :" + info)
            return 1
        if weixin == "weixin":
            res1 = ("可以,你稍等,我看一下","可以,我看一下发给你")
            res = random.choice(res1)
            self.msg.setRespose(res, getSecs(len(res) + self.msg.length))
            self.msg.setRespose(info + "...你家的时候备注下", 10)
            self.pInfo.setInfo("weixin","weixin" + info)
            return 1
            