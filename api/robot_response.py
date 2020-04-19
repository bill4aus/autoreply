#!/usr/bin/env python
#coding:utf-8
# -*- coding: utf-8 -*-


from flask import Flask, jsonify,request

# things we need for Tensorflow

import json
import os
import codecs
import sys




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

from baselcass import *

#批量加载机器人

robotdict ={}
roleList = ['doctor','patient']
for role_ in roleList:
    rbt = robot(role_,intentonly=True)
    rbt.load(role_)
    robotdict[rbt.name] = rbt




# #医生
# doctor = robot('doctor',intentonly=True)
# doctor.load('d_config')

# #病人
# patient = robot('patient',intentonly=True)
# patient.load('p_config')

# robotdict={}
# robotdict['doctor'] =doctor
# robotdict['patient'] =patient
# robotdict['techer'] ={}
# robotdict['student'] ={}
# robotdict['sales'] ={}
# robotdict['custmer'] ={}



app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    role=request.args['role']
    question=request.args['word']
    keshiname=request.args['keshi']



    try:
        myrobot = robotdict[role]
        answer=myrobot.response(question,keshiname=keshiname,show_details=True)
    except Exception as e:
        # raise e
        print(str(e))
        answer=None

    
    if answer==None:
        answer='stop'
    return answer


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=False,port=9003)
    pass

