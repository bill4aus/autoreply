#coding=utf-8
from src.util import getSymptom
from src.personInfo import personInfo
class person:   
    def __init__(self, userid):
        self.userid = userid
        self.seq = 0
        '''套路模块,屏幕医生的问题,主动发起几个问题
           #2 当医生介绍医院时,设置为10,发起问题
           #1  病情询问
           #3  想结束对话的,发起的问题
        '''
        self.taoluNum = 1
        self.taoluFlag = 0
        self.personInfo = personInfo()
        #基本信息只回答两次
        '''
        self.name = ["我姓徐", 0]
        self.age = ["--", 0]
        self.sex = ["--", 0]
        self.weixin = ["--", 0]
        self.addr = ["--", 0]
        '''
        self.illness, self.symptom = getSymptom()
    def setTaolu(self, typeIn):        
        if self.taoluNum == typeIn: #严格按照1,2,3套路
            self.taoluNum = self.taoluNum + 1
            self.taoluFlag = 1
    def getTaolu(self):        
        if self.taoluNum != 0 and self.taoluNum > 4 :  #大于4说明已经套路了3次了
            return 0
        if self.taoluFlag == 1:
            self.taoluFlag = 0 
            return self.taoluNum - 1 
        return 0 
    def getPersonInfo(self):
        return self.personInfo
    '''
    def getContact(self):
        return self.weixin[0]
    def getAge(self):
        return self.age[0]
    def getAddr(self):
        return self.addr[0]
    def getSex(self):
        return self.sex[0]
    def getSymptom(self):
        return self.getSymptom
    
    def checkInfo(self,typeIn):
        temp = self.getType(typeIn)  
        if temp[1] > 3:
            return 3
        return temp[1]
    
    def setInfo(self, typeIn, info = "--"):
        if info != "--":
            if typeIn == "weixin":
                self.weixin[0] = info
            elif typeIn == "age":
                self.age[0] = info
            elif typeIn == "sex":
                self.sex[0] = info
            elif typeIn == "addr":
                self.addr[0] = info
            else:
                print("error set type: ", typeIn)
        if typeIn == "weixin":
            self.weixin[1] = self.weixin[1] + 1
        elif typeIn == "age":
            self.age[1] = self.age[1] + 1
        elif typeIn == "sex":
            self.sex[1] = self.sex[1] + 1
        elif typeIn == "addr":
            self.addr[1] = self.addr[1] + 1
        else:
            print("error set type: ", typeIn)
        return
    
    def getType(self,typeIn):
        temp = ["", 0]
        if typeIn == "weixin":
            temp = self.weixin
        elif typeIn == "age":
            temp =self.age
        elif typeIn == "sex":
            temp = self.sex
        elif typeIn == "addr":
            temp = self.addr
        else:
            print("error set type: ", typeIn)
        return temp
    '''        
            
        