from gensim.models import word2vec,Word2Vec
import jieba
import os
import random
from sklearn.model_selection import train_test_split
import keras
import numpy as np
from tensorflow.keras.preprocessing.sequence import pad_sequences
import setting
import functions

####### config  ########
modelfile = setting.modelfile
# categories=['财经','房产','国际', '家居','教育','科技', '旅游','美食','民生','汽车','社会','时尚','时政','体育','玩乐', '医疗','游戏', '娱乐']
tokenizer =setting.tokenizer
# num_words:None或整数,处理的最大单词数量。少于此数的单词丢掉
# 建立一个max_features个词的字典
# MODEL_CONFIG['INPUT_DIM']
# num_words = 1000


# def tokenize(lang):
#     lang_tokenizer = Tokenizer(filters='!"#$%&()*+,-./:;<=>?@[\]^_`{|}~\t\n！，。（）；’‘的我你他好很',split=" ",num_words=2000)  #创建一个Tokenizer对象
#     lang_tokenizer.fit_on_texts(lang)
#     # tensor = lang_tokenizer.texts_to_sequences(lang)
#     tensor = lang_tokenizer.texts_to_matrix(lang)

#     # print(tensor[0])
#     tensor = pad_sequences(tensor, padding='post')
#     return tensor, lang_tokenizer

# def extracttags(content,k):
#     # etlregex = re.compile(ur"[^\u4e00-\u9f5aa-zA-Z0-9]")
#     punctuation = re.compile(u"[~!@#$%^&*()_+`=\[\]\\\{\}\"|;':,./<>?·！@#￥%……&*（）——+【】,、；‘：“”，。、《》？「『」』＃\t\n\r\x0b\x0c]+")
#     printable=re.compile("[0-9a-zA-Z]")
#     content=punctuation.sub('',content)
#     content = printable.sub('',content)


#     w2=[]
#     w=[]
#     w1 = filter(lambda x: len(x)>0,jieba.analyse.extract_tags(content, topK=k,allowPOS=('ns','nn','n')))
    
#     wdall=list(w1)+w2+w
#     wdall=list(set(wdall))

#     # w=jieba.cut(doc)
#     wd=[]
#     for xx in wdall:
#         if len(xx) > 1 and len(xx) < 4:
#             wd.append(xx)
#     st=list(set(wd))
#     return st[:50]


#==============词向量求平均===================  
def sentenceByWordVectAvg(sentence,model,embeddingSize):  
    # 将所有词向量的woed2vec向量相加到句向量  
    sentenceVector = np.zeros(embeddingSize)  
    # 计算每个词向量的权重，并将词向量加到句向量  
    for word in sentence:
        try:
            sentenceVector = np.add(sentenceVector, model[word])
        except KeyError:
            pass
    sentenceVector = np.divide(sentenceVector,len(sentence))  
    return sentenceVector  

def getPretrainedEmbedding(model,VOCAB,EMBEDDING_DIM):

    # EMBEDDING_DIM = 100  # embedding dimension
    MAX_WORDS_NUM = len(VOCAB)
    embedding_matrix = np.zeros((MAX_WORDS_NUM + 1, EMBEDDING_DIM))  # row 0 for 0

    # model = Word2Vec.load('Embedding/myself/renmin.model')
    for word, i in VOCAB.items():
        if word in model:
            embedding_vector = model[word]
            if i < MAX_WORDS_NUM:
                if embedding_vector is not None:
                    # Words not found in embedding index will be all-zeros.
                    embedding_matrix[i] = embedding_vector

    nonzero_elements = np.count_nonzero(np.count_nonzero(embedding_matrix, axis=1))
    #有多少词在预训练向量中
    print('nonzero_elements / MAX_WORDS_NUM')
    print(nonzero_elements / MAX_WORDS_NUM)
    return embedding_matrix


####### text process  ########

#load word vector model
wordModel = Word2Vec.load(modelfile)

# model.wv.index2word
# model.wv.vocab
# model.wv['词语']


# load text data


# categories = getFolderPathList('./corpus')
# # print(categories)

categories=setting.categories


# import pickle
# data = pickle.load( open( "training_data", "rb" ) )
# words = data['words']
# classes = data['classes']
# train_x = data['train_x']
# train_y = data['train_y']
# print(len(train_x))
# print(train_x)
# # print(words)
# exit()





corpus = []


for cate in categories:
    # print(cate)
    with open('./segment/'+cate+'.txt_segment.txt','r',encoding='utf8') as f:
        for texts_ in f.readlines():
            texts = texts_.replace('\n','')
            # print(texts,cate)
            # wordslist.remove('')
            # DVector = sentenceByWordVectAvg(wordslist,wordModel,300)
            # DVector = np.array(DVector_)
            
            corpus.append((texts,categories[cate]))

#
random.shuffle(corpus)

print(corpus)
print(len(corpus))
# exit()


corpusX = []
corpusY = []

for x,y in corpus:
	corpusX.append(x)
	corpusY.append(y)




# random.shuffle(corpus)
corpusY = keras.utils.to_categorical(corpusY, num_classes=setting.class_length)  # 将标签转换为one-hot编码
# corpusY =np.array(corpusY)


tokenizer.fit_on_texts(corpusX)
vocab=tokenizer.word_index #得到每个词的编号
# print(vocab)
print(len(vocab))
print(len(corpus))



x_train_word_ids=tokenizer.texts_to_sequences(corpusX)
x_train_word_ids = np.array(x_train_word_ids)

# print(x_train_word_ids.shape)
# print(x_train_word_ids[0])

# exit()

#split

trainX_,testX_,trainY_,testY_ = train_test_split(x_train_word_ids,corpusY,test_size=setting.test_size)


# padding
trainX = pad_sequences(trainX_,maxlen=setting.maxlen, dtype='int')
testX = pad_sequences(testX_,maxlen=setting.maxlen, dtype='int')

# # without padding
# trainX=trainX_
# testX=testX_

# trainX = np.array(trainX)
# testX = np.array(testX)
trainY = trainY_
testY = testY_
# corpusY = np.array(corpusY)



# embedding_matrix = getPretrainedEmbedding(wordModel,tokenizer.word_index,300)