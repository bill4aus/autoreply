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


tfModel,tokenizer,config = build_ishot_model('./modelconfigsave')
classesname = config['categories']

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

testfile_f = open('t.txt','w+') 


# testtext = [
# '你这种情况多属于风湿性性的',
# '采取理疗康复应该可以的',
# '您好，这里是 皮肤病专科 请讲',
# '你是看诊什么病？  什么症状',
# '有没有出现脱皮情况',
# '我问你多久了',
# '你有看到我的问题吗',
# '您好',
# ]

# for tt in testtext:
#     tt_res = predictClass(tt)
#     testfile_f.writelines(tt_res+'\n')


testtext=[]
# for n in range(24):
for n in range(5,10,1):
    with open('t/'+str(n+1)+'.txt',encoding='utf-8') as f:
        for tt in f.readlines():
            testtext.append(tt)

for tt in testtext:
    tt_=tt.split('||')
    role = tt_[0]
    stext = tt_[1].replace('\n','')

    if '医生' in role:
        # print('医生：{}'.format(predictClass(stext)))
        # d_int = predictClass(stext)
        testfile_f.writelines(stext+'\n')
    else:
        # print('病人：{}'.format(stext))
        d_int = predictClass(stext)
        testfile_f.writelines(d_int+'\n')


testfile_f.close()