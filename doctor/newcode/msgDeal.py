#coding=utf-8
class infoBase:
    defaultTag = "--"
    def __init__(self,infolist):
        self.infoList=infolist
    def getitem(self, typeIn, typeFun):
        print(len(self.infoList))
        print(self.infoList)
        print(typeIn)
        print(self.infoList.get(typeIn))
        item = self.infoList.get(typeIn)
        if item[1] == 1000:
            print("type error", typeIn)
        if typeFun == 1:
            return item[1]
        if typeFun == 2:
            return item[0]    
    def setInfo(self, typeIn, info=defaultTag):
        item = self.infoList.get(typeIn)
        num = item[1]
        if num == 1000:
            print("set type error", typeIn)
            return
        # item[1]=1,��һ������,Ҳ����˵������Ϣ,ֻ����һ��
        item[1] = item[1] + 1
        if info != self.defaultTag and item[1] == 1:
            item[0] = info
        self.infoList.setdefault(typeIn, item)
    
    def checkInfo(self, typeIn):
        return self.getitem(typeIn, 1)    
    def getInfo(self,typeIn):
        return self.getitem(typeIn, 2) 
            
class msgdeal():        
    def mainMsgDeal(self, pInfo, msg, intention):
        if self.ismsgType(msg):
            num = pInfo.checkInfo(intention)
            if num == 1:
                self.secondDeal() 
            if num == 2:
                self.thridDeal()
            if num > 2:
                self.fourDeal()
            if num == 0:
                self.fristDeal()    
            return 1
        return 0