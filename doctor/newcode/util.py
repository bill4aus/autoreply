#coding=utf-8
import random
def getIllness():
    illness = ("皮肤病","男科病")
    return random.choice((illness))
def getSymptom():
    illness = getIllness()
    if illness == "皮肤病":
        symptom = ("瘙痒","不疼")
    if illness == "男科病":
        symptom = ("阴囊潮湿","瘙痒")
    return illness, symptom
def getContactInfo():
    zimu = 'abcdefjhijklmnopqrstuwvsyt'
    shuzi = '0123456789'
    typeIn = ("weixin","qq")
    info = ''
    if random.choice(typeIn) == "weixin":
        for i in range(random.choice((2,3,4,5))):
            info = info + random.choice(zimu)
        for i in range(random.choice((4,5,6,))):
            info = info + random.choice(shuzi)
        return "weixin",info
    else:
        num = random.choice((8,9,10,11))
        info = random.choice(shuzi)
        if info == '0':
            info = '1'
        for i in range(num-1):
            info = info + random.choice(shuzi)
            
        return "qq",info
def getContactQQ():
    shuzi = '0123456789'
    info = ''
    num = random.choice((8,9,10,11))
    info = random.choice(shuzi)
    if info == '0':
        info = '1'
    for i in range(num-1):
        info = info + random.choice(shuzi)
        
    return "qq",info
def getSecs(size):
    if size <= 5:
        time = 1
    if size > 5 and size < 25:
        time = size/5
    if size > 25:
        time = 4
    return random.choice((time,time,time,time, 8))
 
def logError(res):
    print(res) 
def logInfo(res):
    print(res)                  