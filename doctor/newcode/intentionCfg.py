#coding=utf-8
def cfglist2dict(infolist):
    defaultTag = "--"
    infodict = {}
    for val in infolist:
        infodict[val] = [defaultTag, 0]
    return infodict
def personInfo():
    infolist = ("name","age","sex","addr","weixin")
    return infolist
def GetPersonInfo():
    return cfglist2dict(personInfo())