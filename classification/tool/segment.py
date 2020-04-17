#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""

import jieba
import jieba.analyse
import os
import sys
sys.path.append("..")
import functions


stopwordfile = '../stopwords'

# stop_words
stop_words = []
stwd_Path_list = functions.getFilePathList(stopwordfile)
for fpath in stwd_Path_list:
  for line in open(fpath, encoding='utf-8'):
      # line.replace(' ', '').replace('\n', '')
      stop_words.append(line.replace(' ', '').replace('\n', ''))
stop_words.append('\n')
stop_words.append(' ')


def mkdir(path):
    # 去除首位空格
    path=path.strip()
    # 去除尾部 \ 符号
    path=path.rstrip("\\")

    isExists=os.path.exists(path)
    if not isExists:
        os.makedirs(path)
    else:
        pass

# classlist=['财经','房产','国际', '家居','教育','科技', '旅游','美食','民生','汽车','社会','时尚','时政','体育','玩乐', '医疗','游戏', '娱乐']
classlist=['打招呼','询问病情','介绍治疗方法','套取个人信息','病情介绍','套取联系方式','介绍医院地址','推荐医院检查','网上不能看病','介绍本院特色','强调医院正规','安排诊号面诊','介绍医保的情况','还在么','医生不爽','其他情况','发现异常',]

# for catename in  classlist:
#     mkdir('../segment/'+catename)

# 语料库分词处理
filepath = functions.getFilePathList('../corpus')
for fpath in filepath:
    with open(fpath,'rb') as f:
        document = f.read()
        #document_decode = document.decode('GBK')
        document_cut = list(jieba.cut(document))

        # corpus = []
        # for ww in document_cut:
        #     if ww not in stop_words:
        #         corpus.append(ww)
        # result = ' '.join(corpus)
        
        result = ' '.join(document_cut)
        result = result.encode('utf-8')
        # print('here....')
        with open(fpath.replace('corpus','segment')+'_segment.txt', 'wb+') as f2:
            f2.write(result)

    f.close()
    f2.close()