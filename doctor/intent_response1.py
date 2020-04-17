#!/usr/bin/env python
#coding:utf-8
# -*- coding: utf-8 -*-


from flask import Flask, jsonify,request



# 导入工具
# things we need for NLP
import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()

# things we need for Tensorflow
import numpy as np
import tflearn
import tensorflow as tf
import random
import jieba
import json
import os
import codecs
import logging




fpath='/usr/application/autoreplay/doctors_intent/'



# restore all of our data structures
import pickle
data = pickle.load( open(fpath+ "training_data", "rb" ) )
words = data['words']
classes = data['classes']
train_x = data['train_x']
train_y = data['train_y']

# import our chat-bot intents file
import json
with open(fpath+'intents.json',encoding='utf-8') as json_data:
    intents = json.load(json_data)



### 加载病例数据到内存  将来需要改成  每一个病种  一个单独的obj,参数从url里面传过来
# binglilist

# 科室列表
keshi_list=['xinggongnengzhangai','qianliexianjibing','niaodaoxialie','miniaowaike','baopibaojing','chuanranbingke','pifuke','guke','jingshenxinlike','neike','qitakeshi','waike','wuguanke','zhongyike','erke','erkezonghe','fuchanke','pifuxingbingke','yanke','yijike','yixueyingxiangxue','zhongliuke']
# keshi_list=['xinggongnengzhangai','qianliexianjibing','niaodaoxialie','miniaowaike','baopibaojing','fuchanke','pifuxingbingke']

# 获取相应的疾病目录数据
bingli_id_obj={}

# bingli_list=[]
bingli={}


for kname in keshi_list:
    bingliflodername=kname#'xinggongnengzhangai'
    bingliforthisill={}
    datapath='/usr/application/autoreplay/conversation/'
    for root, dirs, files in os.walk(datapath+bingliflodername):
        for nfile in files:
            if os.path.splitext(nfile)[1] == '.json':
                # bingli_id_list.append(os.path.splitext(nfile)[0])

                patient_id=os.path.splitext(nfile)[0]

                myjsonfile=open(datapath+bingliflodername+'/'+patient_id+'.json')
                jstr=myjsonfile.read()
                # print('jstr')
                newjstr=''.join(jstr.split('\n'))
                # print(newjstr)
                new_bingli_dict = json.loads(newjstr)
                bingliforthisill[patient_id]=new_bingli_dict

    bingli_id_obj[bingliflodername]=bingliforthisill

                

                # bingli_list.append()


### 加载病例数据到内存


### 加载回复套路数据
# taolu
with codecs.open('taolu.json',encoding='utf-8') as json_data:
    taolu = json.load(json_data)
#通用病例
with codecs.open('bingli.json',encoding='utf-8') as json_data:
    bingli_foreveryone = json.load(json_data)

### 加载回复套路数据







# Build neural network
net = tflearn.input_data(shape=[None, len(train_x[0])])
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, len(train_y[0]), activation='softmax')
net = tflearn.regression(net)

# Define model and setup tensorboard
model = tflearn.DNN(net, tensorboard_dir=fpath+'tflearn_logs')



def clean_up_sentence(sentence):
    # tokenize the pattern
    sentence_words = nltk.word_tokenize(sentence)
    # stem each word
    sentence_words = [stemmer.stem(word.lower()) for word in sentence_words]
    return sentence_words

# return bag of words array: 0 or 1 for each word in the bag that exists in the sentence
def bow(sentence, words, show_details=False):
    # tokenize the pattern
    sentence_words = clean_up_sentence(sentence)
    # bag of words
    bag = [0]*len(words)  
    for s in sentence_words:
        for i,w in enumerate(words):
            if w == s: 
                bag[i] = 1
                if show_details:
                    print ("found in bag: %s" % w)

    return(np.array(bag))




# load our saved model
model.load(fpath+'model.tflearn')


# create a data structure to hold user context
context = {}

ERROR_THRESHOLD = 0.25
def classify(sentence):
    # generate probabilities from the model
    results = model.predict([bow(sentence, words)])[0]
    # filter out predictions below a threshold
    results = [[i,r] for i,r in enumerate(results) if r>ERROR_THRESHOLD]
    # sort by strength of probability
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append((classes[r[0]], r[1]))
    # return tuple of intent and probability
    return return_list


###回复套路，选择套路的回复语
def taolurespone(dintent,keshiname=''):
    pass
    global taolu
    global bingli_foreveryone
    global bingli_id_obj

    bingli=bingli_id_obj[keshiname]
    


    replyintent=taolu[dintent].split(',')
    random.shuffle(replyintent)
    myintent=replyintent[0]

    # 随机选一个默认回复
    #random words
    random.shuffle(bingli_foreveryone[myintent])    
    random_uwords=bingli_foreveryone[myintent][0]
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
    this_bingli_list=list(bingli.keys())
    print(this_bingli_list)

    random.shuffle(this_bingli_list)
    new_bingli_dict=bingli.get(this_bingli_list[0])
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

    #如果该病人没有此意图，则随机找个该意图的对话
    if uwordslist==None:
        # 默认是皮肤科的对话，不妥
        # 默认改为中性对话了
        uwords=random_uwords
        print('默认病例的回复uwords')
        # uwords=''
    elif len(uwordslist)==0:
        # 默认是皮肤科的对话，不妥
        # 默认改为中性对话了
        uwords=random_uwords
        # uwords=''
        print('默认病例的回复uwords')
    else:
        random.shuffle(uwordslist)
        print('新病例的回复uwords')
        
        if len(uwordslist)>0:
            uwords=uwordslist[0]
        else:
            uwords=random_uwords
        print(uwords)

    # return random.choice(i['responses'])+"||"+i['tag']
    return uwords+"||"+dintent+"||"+myintent


def response(sentence, userID='123', keshiname='',show_details=False):
    results = classify(sentence)
    # if we have a classification then find the matching intent tag
    if results:
        # loop as long as there are matches to process
        while results:
            for i in intents['intents']:
                # find a tag matching the first result
                if i['tag'] == results[0][0]:
                    # set context for this intent if necessary
                    if 'context_set' in i:
                        if show_details: print ('context:', i['context_set'])
                        context[userID] = i['context_set']

                    # check if this intent is contextual and applies to this user's conversation
                    if not 'context_filter' in i or \
                        (userID in context and 'context_filter' in i and i['context_filter'] == context[userID]):
                        if show_details: print ('tag:', i['tag'])
                        # a random response from the intent
                        # return print('>>BOT:'+random.choice(i['responses']))


                        
                        # return random.choice(i['responses'])+"||"+i['tag']
                        #new logic
                        dintent=i['tag']
                        return taolurespone(dintent,keshiname=keshiname)

            results.pop(0)




app = Flask(__name__)

wcount=0

@app.route('/', methods=['GET'])
def home():
    global wcount
    w=request.args['word']
    keshiname=request.args['keshi']

    question=w
    newdoc=question
    nwd=jieba.cut(newdoc,cut_all=False)
    wcount=+1
    try:
        answer=response(' '.join(nwd),keshiname=keshiname,show_details=True)
    except Exception as e:
        # raise e
        print(str(e))
        answer=None

    
    if answer==None:
        answer='stop to say||stop to say'
    print('wcount')
    print(wcount)
    return answer


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=False,port=9003)

    pass

