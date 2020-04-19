#!/usr/bin/env python
#coding:utf-8
# -*- coding: utf-8 -*-

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


# # import our chat-bot intents file
# import json
# with open('intents.json',encoding='utf-8') as json_data:
#     # print(json_data)
#     intents = json.load(json_data)


# 病人意图索引
path='/usr/application/autoreplay/patients_intent/classify/train/'
with open(path+'patient_intent.json',encoding='utf-8') as json_data:
    # print(json_data)
    doc_intents = json.load(json_data)



words = []
classes = []
documents = []
ignore_words = ['?']

classes=doc_intents.keys()

for tag in doc_intents:
    # 意图索引tag tag.txt为该意图的文本库

    # 病人意图
    dintent=doc_intents[tag]

    f = open(path+'corpus/'+tag+".txt","r+")# 返回一个文件对象
    for text in f.readlines():
        new_pattern=jieba.cut(text)
        w = nltk.tokenize.word_tokenize(' '.join(new_pattern))
        words.extend(w)
        documents.append((w,tag))
        

    f.close()  



# words = []
# classes = []
# documents = []
# ignore_words = ['?']
# # loop through each sentence in our intents patterns
# for intent in intents['intents']:
#     for pattern in intent['patterns']:
#         # tokenize each word in the sentence
#         # print(pattern)
#         new_pattern=jieba.cut(pattern)
#         # print(new_pattern)
#         w = nltk.tokenize.word_tokenize(' '.join(new_pattern))
#         # add to our words list
#         words.extend(w)
#         # add to documents in our corpus
#         documents.append((w, intent['tag']))
#         # add to our classes list
#         if intent['tag'] not in classes:
#             classes.append(intent['tag'])

# stem and lower each word and remove duplicates
words = [stemmer.stem(w.lower()) for w in words if w not in ignore_words]
words = sorted(list(set(words)))

# remove duplicates
classes = sorted(list(set(classes)))

print (len(documents), "documents")
print (len(classes), "classes", classes)
print (len(words), "unique stemmed words", words)













# create our training data
training = []
output = []
# create an empty array for our output
output_empty = [0] * len(classes)

# training set, bag of words for each sentence
for doc in documents:
    # initialize our bag of words
    bag = []
    # list of tokenized words for the pattern
    pattern_words = doc[0]
    # stem each word
    pattern_words = [stemmer.stem(word.lower()) for word in pattern_words]
    # create our bag of words array
    for w in words:
        bag.append(1) if w in pattern_words else bag.append(0)

    # output is a '0' for each tag and '1' for current tag
    output_row = list(output_empty)
    output_row[classes.index(doc[1])] = 1

    training.append([bag, output_row])

# shuffle our features and turn into np.array
random.shuffle(training)
training = np.array(training)

# create train and test lists
train_x = list(training[:,0])
train_y = list(training[:,1])






# reset underlying graph data
tf.reset_default_graph()
# Build neural network
net = tflearn.input_data(shape=[None, len(train_x[0])])
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, len(train_y[0]), activation='softmax')
net = tflearn.regression(net)

# Define model and setup tensorboard
model = tflearn.DNN(net, tensorboard_dir='tflearn_logs')
# Start training (apply gradient descent algorithm)
model.fit(train_x, train_y, n_epoch=1000, batch_size=8, show_metric=True)
model.save('model.tflearn')









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








p = bow("is your shop open today?", words)
print (p)
print (classes)



print(model.predict([p]))



# save all of our data structures
import pickle
pickle.dump( {'words':words, 'classes':classes, 'train_x':train_x, 'train_y':train_y}, open( "training_data", "wb" ) )

