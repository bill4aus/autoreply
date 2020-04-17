#coding=utf-8
from src.person import person
from src.util import getContactInfo
def taolu1(msg):
    taolist = {"one":"具体什么时候不知道"}
    return taolist.values()
def taolu2(msg):
    taolist = {"one":"大概了解了,我想问几个问题哈",\
               "two":"费用大概会花多少",\
               "three":"有没有其他费用",\
               "three":"还有这个医保能报销么",\
               "four":"然后,大概能报销多少",\
               "five":"嗯....",\
               "six": "我大概了解了,谢谢医生",\
               "seven":"对了,你们那礼拜 六,礼拜天上班么",\
               "eight":"好的,了解了,谢谢了"}
    return taolist.values()
def taolu3(msg):
    typeIn = "weixin"
    taolu3 = {"one":"嗯,差不多了解了,医生",\
              "two":"我还有点事,下次再问你了",\
              "three":typeIn,\
              "four":"886"}
    '''
    if person.weixin == "--":
        weixin, info = getContactInfo()
        wx = weixin + info
        person.weixin = wx
        taolu3["three"] = "你可以加我 " + wx 
    else :
        wx = person.weixin
        taolu3["three"] = "刚刚给你发了联系方式, 你可以加我" + wx
    return taolu3.values()
    '''
def handleTaolu(msg, taolu):
    if taolu == 3:
        taolist = taolu3(msg)
    if taolu == 2:
        taolist = taolu2(msg)
    if taolu == 1:
        taolist =taolu1(msg)
    for val in taolist:
        msg.setRespose(val,len(msg.length + val)/5)
        
    