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


def build_ishot_model(configpath):
    # load model
    tfModel = tf.keras.models.load_model(configpath+"/model.h5")

    with open(configpath+'/tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)

    with open(configpath+"/config.file", "rb") as handle:
        config = pickle.load(handle)

    return tfModel,tokenizer,config



def predictClass(text_test):
    # tfModel,tokenizer,config = build_ishot_model('/modelfile')
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
#                 new_bingli_dict = json.loads(newjstr)
#                 bingliforthisill[patient_id]=new_bingli_dict

#     bingli_id_obj[bingliflodername]=bingliforthisill

                

                # bingli_list.append()

# 获取某个人任意的对话
def getrandomrespone(new_bingli_dict):
    saylist=[]
    for intent in new_bingli_dict:
        for x in new_bingli_dict.get(intent):
            saylist.append(x)
    return random.choice(saylist)


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
        self.tfModel,self.tokenizer,self.config = build_ishot_model(modelfile)
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

                        myjsonfile=open(datapath+bingliflodername+'/'+patient_id+'.json',encoding='utf-8')
                        jstr=myjsonfile.read()
                        # print('jstr')
                        newjstr=''.join(jstr.split('\n'))
                        # print(newjstr)
                        new_bingli_dict = json.loads(newjstr)
                        bingliforthisill[patient_id]=new_bingli_dict

            self.bingli_id_obj[bingliflodername]=bingliforthisill
        # print(self.bingli_id_obj)



    def perdict(self,text_test):

        # tfModel,tokenizer,config = build_ishot_model('/modelfile')
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
    #    ###回复套路，选择套路的回复语
    def taolurespone(self,dintent,keshiname=''):
        pass
        # global taolu
        # global bingli_foreveryone
        # global bingli_id_obj

        self.bingli=self.bingli_id_obj[keshiname]
        print('self.bingli')
        print(self.bingli)
        


        replyintent=self.taolu[dintent].split(',')
        random.shuffle(replyintent)
        myintent=replyintent[0]

        # 随机选一个默认回复
        #random words
        random.shuffle(self.bingli_foreveryone[myintent])    
        random_uwords=self.bingli_foreveryone[myintent][0]
        print('随机选的默认回复文本 random_uwords')
        print(random_uwords)

        # random.shuffle(bingli_id_list)
        # myjsonfile=open('bingli/'+bingli_id_list[0]+'.json')
        # jstr=myjsonfile.read()
        # print('jstr')
        # newjstr=''.join(jstr.split('\n'))
        # print(newjstr)
        # new_bingli_dict = json.loads(newjstr)


        #现在，换一个方法。随机找一个用户，取出该用户的，该意图的回复用于返回
        this_bingli_list=list(self.bingli.keys())
        print(this_bingli_list)

        random.shuffle(this_bingli_list)
        new_bingli_dict=self.bingli.get(this_bingli_list[0])
        print(new_bingli_dict)

        avilabe_intent=[]
        for intentstr in new_bingli_dict:
            if new_bingli_dict.get(intentstr) :
                if len(new_bingli_dict.get(intentstr))!=0:
                    avilabe_intent.append(intentstr)
        logging.info(u'----------------可用的意图avilabe_intent---------')   
        print(avilabe_intent)

        for mintent in replyintent:
            if mintent in avilabe_intent:
                if myintent=='打招呼':
                    break
                else:
                    myintent=mintent
                    logging.info(u'----------------找到一个可用的意图---------') 
                    # print(myintent)
                    break

        print('最终的意图选择 myintent')
        print(myintent)

        print('新病例中的该意图文本uwordslist')
        uwordslist=new_bingli_dict.get(myintent)

        #如果该病人没有此意图，则随机找个该默认设置中，该意图的对话
        # 也不太好
        # 换成： 该病例中其他意图的对话 如果再没有，则为默认对话
        if uwordslist==None:
            # 默认是皮肤科的对话，不妥
            # 默认改为中性对话了
            
            print('病例任意回复')
            try:
                uwords=getrandomrespone(new_bingli_dict)
            except Exception as e:
                # raise e
                print('默认病例的回复uwords')
                uwords=random_uwords

            
            # uwords=''
        elif len(uwordslist)==0:
            # 默认是皮肤科的对话，不妥
            # 默认改为中性对话了
            print('病例任意回复')
            try:
                uwords=getrandomrespone(new_bingli_dict)
            except Exception as e:
                # raise e
                print('默认病例的回复uwords')
                uwords=random_uwords
        else:
            random.shuffle(uwordslist)
            print('新病例的回复uwords')
            
            if len(uwordslist)>0:
                uwords=uwordslist[0]
            else:
                uwords=random_uwords
            print(uwords)
        # 病人说的||医生意图||病人意图
        # return random.choice(i['responses'])+"||"+i['tag']
        return uwords+"||"+dintent+"||"+myintent



    def response(self,newdoc, userID='123', keshiname='',show_details=False):
        # pass
        # nwd=jieba.cut(newdoc,cut_all=False)
        # sentence=' '.join(nwd)
        # results = classify.classify(sentence)
        # 
        
        doctorintent = self.perdict(newdoc)


        # 
        # if we have a classification then find the matching intent tag
        # if results:
        # doctorintent=results[0][0]
        # 
        if show_details: print ('results:', doctorintent)

        

        if self.intentonly==True:
            return doctorintent
        else:
            pass
            # 病人说的||医生意图||病人意图
            # return taolurespone(doctorintent,keshiname=keshiname)
            return self.taolurespone(doctorintent,keshiname=keshiname)
        

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
    

        