#coding=utf-8

class msgInstance: 
    def __init__(self, request):
        self.request = request
        self.length = len(request)
        self.respose = {"list":[]}
        self.intention = {"intention": []} #personinfo,illness,hospital,unknown
    def getIntention(self):
        return self.intention["intention"]           
    def setIntention(self, intention):
        self.intention["intention"].append(intention)
    def setRespose(self, res, time=1):
        self.respose["list"].append({"word": res, "wait": time})
    def getRespose(self):
        return self.respose
    def getRequest(self):
        return self.request   