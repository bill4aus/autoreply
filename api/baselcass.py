#!/usr/bin/env python
#coding:utf-8
# -*- coding: utf-8 -*-

# 导入工具
import time
import datetime
import sys
import io
import logging
#from apscheduler.schedulers.background import BackgroundScheduler
import urllib

import threading
import json
import random
import math
import codecs
import os

import jieba




#coding:utf-8
import numpy as np
import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt


import tensorflow.keras.layers as layers
# from tensorflow.keras.layers import Dense, Activation,Dropout, Flatten,MaxPooling1D
from tensorflow.keras.layers import Dense, Embedding, Dropout, Activation,Flatten, Conv1D, GlobalMaxPooling1D,Dropout

from tensorflow.keras.preprocessing.sequence import pad_sequences
import jieba

import pickle

# load model


def build_keras_model(configpath):
    # load model
    tfModel = tf.keras.models.load_model(configpath+"/model.h5")

    with open(configpath+'/tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)

    with open(configpath+"/config.file", "rb") as handle:
        config = pickle.load(handle)

    return tfModel,tokenizer,config



def predictClass(text_test):
    # tfModel,tokenizer,config = build_keras_model('/modelfile')
    # print(text_test)
    x_test_word_ids = tokenizer.texts_to_sequences([' '.join(jieba.cut(text_test))])
    x_test_padded_seqs = pad_sequences(x_test_word_ids, maxlen=config['maxlen'])

    x_test_padded_seqs = np.array(x_test_padded_seqs)
    #perdict
    y_predict = tfModel.predict_classes(x_test_padded_seqs)  # 预测的是类别，结果就是类别号
    # print(y_predict)
    y_predict = list(map(str, y_predict))
    idofclass=int(y_predict[0])
    # categories
    # print(classesname.inverse[idofclass])

    # print('{}-【{}-{}】'.format(text_test,classesname.inverse[idofclass],idofclass))
    # return idofclass #number
    return '{}-【{}-{}】'.format(text_test,classesname.inverse[idofclass],idofclass)








# # import our chat-bot intents file
# import json
# with open(fpath+'intents.json',encoding='utf-8') as json_data:
#     intents = json.load(json_data)



### 加载病例数据到内存  将来需要改成  每一个病种  一个单独的obj,参数从url里面传过来
# binglilist

# 科室列表
keshi_list=['xinggongnengzhangai','qianliexianjibing','niaodaoxialie','miniaowaike','baopibaojing','chuanranbingke','pifuke','guke','jingshenxinlike','neike','qitakeshi','waike','wuguanke','zhongyike','erke','erkezonghe','fuchanke','pifuxingbingke','yanke','yijike','yixueyingxiangxue','zhongliuke']
# keshi_list=['xinggongnengzhangai','qianliexianjibing','niaodaoxialie','miniaowaike','baopibaojing','fuchanke','pifuxingbingke']

# 获取相应的疾病目录数据
# bingli_id_obj={}

# bingli_list=[]
# bingli={}


# for kname in keshi_list:
#     bingliflodername=kname#'xinggongnengzhangai'
#     bingliforthisill={}
#     datapath='/usr/application/autoreplay/conversation/'
#     for root, dirs, files in os.walk(datapath+bingliflodername):
#         for nfile in files:
#             if os.path.splitext(nfile)[1] == '.json':
#                 # bingli_id_list.append(os.path.splitext(nfile)[0])

#                 patient_id=os.path.splitext(nfile)[0]

#                 myjsonfile=open(datapath+bingliflodername+'/'+patient_id+'.json')
#                 jstr=myjsonfile.read()
#                 # print('jstr')
#                 newjstr=''.join(jstr.split('\n'))
#                 # print(newjstr)
#                 singleone_bingli_dict = json.loads(newjstr)
#                 bingliforthisill[patient_id]=singleone_bingli_dict

#     bingli_id_obj[bingliflodername]=bingliforthisill

                

                # bingli_list.append()

# 获取某个人任意的对话
def getrandomrespone(singleone_bingli_dict):
    saylist=[]
    for intent in singleone_bingli_dict:
        for x in singleone_bingli_dict.get(intent):
            saylist.append(x)
    return random.choice(saylist)
def get_random_intent_respone(bingli,replyintent):
    random.shuffle(replyintent)
    chosenintent = replyintent[0]
    saylist=[]

    for userid in bingli:
        ubingli = bingli.get(userid)
        if chosenintent in ubingli:
            saylist.extend(ubingli.get(chosenintent))
    robotsay = random.choice(saylist)

    return robotsay,chosenintent




class robot(object):
    """docstring for robot"""
    def __init__(self,name,intentonly=False):
        super(robot, self).__init__()
        # self.arg = arg
        # 构建url
        # 科室
        # %E4%BD%A0%E5%A5%BD&keshi=xinggongnengzhangai
        # self.keshi=keshi
        self.name = name
        self.intentonly = intentonly
    
    def load(self,configfile):
        pass
        modelfile = configfile+'/modelconfigsave/'
        modelfile.replace('//','/')
        self.tfModel,self.tokenizer,self.config = build_keras_model(modelfile)
        self.classesname = self.config['categories']



        # #intent list
        # # 医生意图索引
        # path='/usr/application/autoreplay/doctors_intent/classify/train/'
        # with open(path+'doc_intent.json',encoding='utf-8') as json_data:
        #     # print(json_data)
        #     self.doc_intents = json.load(json_data)
        #
                
        ### 加载病例数据到内存


        ### 加载回复套路数据
        # taolu
        with codecs.open(configfile+'/taolu.json',encoding='utf-8') as json_data:
            self.taolu = json.load(json_data)
        #通用病例
        with codecs.open(configfile+'/bingli.json',encoding='utf-8') as json_data:
            self.bingli_foreveryone = json.load(json_data)


        # self.bingli=bingli_id_obj[keshiname]
        # 获取相应的疾病目录数据
        self.bingli_id_obj={}
        # 
        #### 加载病例数据到内存  将来需要改成  每一个病种  一个单独的obj,参数从url里面传过来
        # 科室列表
        keshi_list=['xinggongnengzhangai','qianliexianjibing','niaodaoxialie','miniaowaike','baopibaojing','chuanranbingke','pifuke','guke','jingshenxinlike','neike','qitakeshi','waike','wuguanke','zhongyike','erke','erkezonghe','fuchanke','pifuxingbingke','yanke','yijike','yixueyingxiangxue','zhongliuke']
        
        datapath=configfile+'/conversation/'
        datapath.replace('//','/')
        # print(datapath)
        for kname in keshi_list:
            bingliflodername=kname#'xinggongnengzhangai'
            bingliforthisill={}
            # print(datapath+bingliflodername)
            for root, dirs, files in os.walk(datapath+bingliflodername):
                # print(files)
                for nfile in files:
                    # print(nfile)
                    # print(os.path.splitext(nfile)[1])
                    if os.path.splitext(nfile)[1] == '.json':
                        # bingli_id_list.append(os.path.splitext(nfile)[0])

                        patient_id=os.path.splitext(nfile)[0]

                        try:
                            pass
                            myjsonfile=open(datapath+bingliflodername+'/'+patient_id+'.json',encoding='utf-8')
                            jstr=myjsonfile.read()
                            # print('jstr')
                            newjstr=''.join(jstr.split('\n'))
                            # print(newjstr)
                            singleone_bingli_dict = json.loads(newjstr)
                            bingliforthisill[patient_id]=singleone_bingli_dict

                        except Exception as e:
                            # raise e
                            pass

                       

            self.bingli_id_obj[bingliflodername]=bingliforthisill
        print(self.bingli_id_obj.keys())



    def perdict(self,text_test):

        # tfModel,tokenizer,config = build_keras_model('/modelfile')
        # print(text_test)
        x_test_word_ids = self.tokenizer.texts_to_sequences([' '.join(jieba.cut(text_test))])
        x_test_padded_seqs = pad_sequences(x_test_word_ids, maxlen=self.config['maxlen'])

        x_test_padded_seqs = np.array(x_test_padded_seqs)
        #perdict
        y_predict = self.tfModel.predict_classes(x_test_padded_seqs)  # 预测的是类别，结果就是类别号
        # print(y_predict)
        y_predict = list(map(str, y_predict))
        idofclass=int(y_predict[0])
        # categories
        # print(classesname.inverse[idofclass])

        # return idofclass #number
        # return '{}-【{}-{}】'.format(text_test,classesname.inverse[idofclass],idofclass)
        return self.classesname.inverse[idofclass]


        pass
    # def bingli(self):
    #     pass

    def random_users_bingli(self,keshiname,robotintent):

        self.bingli=self.bingli_id_obj[keshiname]
        binglilist = []
        for userid in self.bingli:
            ubingli = self.bingli.get(userid)
            if ubingli.get(robotintent)!=None:
                if len(ubingli.get(robotintent))>0:
                    binglilist.append(ubingli)

        # #现在，换一个方法。随机找一个用户，取出该用户的，该意图的回复用于返回
        # this_bingli_list=list(self.bingli.keys())
        # # print(this_bingli_list)
        # random.shuffle(this_bingli_list)
        # singleone_bingli_dict=self.bingli.get(this_bingli_list[0])
        # # print(singleone_bingli_dict)

        try:
            random.shuffle(binglilist)
            singleone_bingli_dict = binglilist[0]
            return singleone_bingli_dict

        except Exception as e:
            # raise e
            return None


    def random_user_intent(self,replyintent):
        # avilabe_intent=[]
        # for intentstr in singleone_bingli_dict:
        #     if singleone_bingli_dict.get(intentstr) :
        #         if len(singleone_bingli_dict.get(intentstr))!=0:
        #             avilabe_intent.append(intentstr)
        # # logging.info(u'----------------可用的意图avilabe_intent---------')   
        # # print(avilabe_intent)

        # thisintent=None

        # for mintent in replyintent:
        #     if mintent in avilabe_intent:
        #         # if robotintent=='打招呼':
        #         #     break
        #         # else:
        #         #     robotintent=mintent
        #         #     logging.info(u'----------------找到一个可用的意图---------') 
        #         #     # print(robotintent)
        #         #     break
        #         thisintent = mintent



        # # print('最终的意图选择 robotintent')
        # # print(robotintent)

        # # print('新病例中的该意图文本uwordslist')
        # # uwordslist=singleone_bingli_dict.get(robotintent)

        # return thisintent
        
        random.shuffle(replyintent)
        return replyintent[0]

    #    ###回复套路，选择套路的回复语
    def taolurespone(self,otherintent,keshiname=''):
        pass
        # global taolu
        # global bingli_foreveryone
        # global bingli_id_obj

        
        # print('self.bingli')
        # print(self.bingli)
        

        # print(self.taolu.keys())
        # print('otherintent:')
        # print(otherintent)


        replyintent=self.taolu[otherintent].split(',')

        # random.shuffle(replyintent)
        # robotintent=replyintent[0]

        robotintent=self.random_user_intent(replyintent)
        singleone_bingli_dict=self.random_users_bingli(keshiname,robotintent)
        if singleone_bingli_dict !=None:
            print('病例中可以回复的意图:{}'.format(robotintent))
            # print('新病例中的该意图文本uwordslist')
            uwordslist=singleone_bingli_dict.get(robotintent)
        else:
     
            '''
            # 该病例没有相关的意图
            # 随机选一个默认回复

            #如果该病人没有此意图，则随机找个该默认设置中，该意图的对话
            # 也不太好
            # 换成： 该病例中其他意图的对话 如果再没有，则为默认对话
        
            # 随机选一个默认回复
            # 默认是皮肤科的对话，不妥
            # 默认改为中性对话了

            print(self.bingli_foreveryone.keys())
            # random_uwords=self.bingli_foreveryone[otherintent]
            '''
        

            uwordslist =None

            random.shuffle(replyintent)
            robotintent=replyintent[0]
            #random words
            print(self.bingli_foreveryone.keys())
            random.shuffle(self.bingli_foreveryone[robotintent])    
            random_uwords=self.bingli_foreveryone[robotintent][0]
            print('病例没找到，随机选意图：{}，文本：{}'.format(robotintent,random_uwords))
        
      

        
        # if uwordslist==None:
        #     try:
        #         robotwords,robotintent = get_random_intent_respone(self.bingli,replyintent)
        #         print('机器人的意图：{}，文本：{}'.format(robotintent,robotwords))
        #     except Exception as e:
        #         print('默认病例的回复uwords')
        #         robotwords=random_uwords
        # elif len(uwordslist)==0:
        #     try:
        #         robotwords,robotintent = get_random_intent_respone(self.bingli,replyintent)
        #         print('机器人的意图：{}，文本：{}'.format(robotintent,robotwords))
        #     except Exception as e:
        #         print('默认病例的回复uwords')
        #         robotwords=random_uwords
        

        if uwordslist==None:
            robotwords=random_uwords
        else:
            random.shuffle(uwordslist)
            if len(uwordslist)>0:
                robotwords=uwordslist[0]
            else:
                robotwords=random_uwords
        print('最终敲定意图：{}，文本：{}'.format(robotintent,robotwords))
        # 病人说的||医生意图||病人意图
        # return random.choice(i['responses'])+"||"+i['tag']
        return robotwords+"||"+otherintent+"||"+robotintent



    def response(self,newdoc, userID='123', keshiname='',show_details=False):
        # pass
        # nwd=jieba.cut(newdoc,cut_all=False)
        # sentence=' '.join(nwd)
        # results = classify.classify(sentence)
        # 
        
        otherintent = self.perdict(newdoc)


        # 
        # if we have a classification then find the matching intent tag
        # if results:
        # doctorintent=results[0][0]
        # 
        if show_details: print ('otherintent:', otherintent)

        

        if self.intentonly==True:
            return otherintent
        else:
            pass
            # 病人说的||医生意图||病人意图
            # return taolurespone(doctorintent,keshiname=keshiname)
            return self.taolurespone(otherintent,keshiname=keshiname)
        

        # # loop as long as there are matches to process
        # while results:
        #     for i in intents['intents']:
        #         # find a tag matching the first result
        #         if i['tag'] == results[0][0]:
        #             # set context for this intent if necessary
        #             if 'context_set' in i:
        #                 if show_details: print ('context:', i['context_set'])
        #                 context[userID] = i['context_set']

        #             # check if this intent is contextual and applies to this user's conversation
        #             if not 'context_filter' in i or \
        #                 (userID in context and 'context_filter' in i and i['context_filter'] == context[userID]):
        #                 if show_details: print ('tag:', i['tag'])
        #                 # a random response from the intent
        #                 # return print('>>BOT:'+random.choice(i['responses']))


                        
        #                 # return random.choice(i['responses'])+"||"+i['tag']
        #                 #new logic
        #                 dintent=i['tag']
        #                 return taolurespone(dintent,keshiname=keshiname)

            # results.pop(0)
    

        