#!/usr/bin/env python
#coding:utf-8
# -*- coding: utf-8 -*-


from flask import Flask, jsonify,request

# things we need for Tensorflow

import json
import os
import codecs
import sys

# 上级目录
sys.path.append('../')
import robot.robot as robot


myrobot=robot.robot()

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    question=request.args['word']
    # 暂时不做处理
    # keshiname=request.args['keshi']

    try:
        answer=myrobot.response(question,keshiname='keshiname',show_details=True)
    except Exception as e:
        # raise e
        print(str(e))
        answer=None

    
    if answer==None:
        answer='stop'
    return answer


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=False,port=9001)
    pass

