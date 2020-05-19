from bidict import bidict
from tensorflow.keras.preprocessing.text import Tokenizer

'''
病情初步判断
发送图片
图片接收失败
询问医院检查过没
询问治疗效果
询问检查方式
突出其他医院的劣势
强调疾病的复杂性可能性
吃药解答
询问是否有时间过来看病
强调治疗方便时间快
以病情而定
强调历史悠久技术牛逼能治好
强调治疗效果不要在乎费用
介绍其他医院怎么治疗的
病情严重
该疾病详细介绍
询问病人地址
揭露行业的套路
介绍病因


打招呼
询问病情
介绍治疗方法
套取个人信息
病情介绍
套取联系方式
介绍医院地址
推荐医院检查
网上不能看病
介绍本院特色
强调医院正规
安排诊号面诊
介绍医保的情况
还在么
医生不爽
其他情况
发现异常


'''
# 病人
classlist=['打招呼','描述病情','个人信息','询问病情','怎么治疗','询问医院地址','怎么收费','尝试过哪些治疗方法','不方便接电话','我的顾虑','介绍其他医院费用低廉','询问治疗效果','不方便过来','询问医保','准备过来','我考虑下关闭','愤怒关闭']
# 医生/
# classlist=['打招呼','询问病情','介绍治疗方法','套取个人信息','病情介绍','套取联系方式','介绍医院地址','推荐医院检查','网上不能看病','介绍本院特色','强调医院正规','安排诊号面诊','介绍医保的情况','还在么','医生不爽','其他情况','发现异常',]
classdict={}
for cate in classlist:
    classdict[cate] = classlist.index(cate)

categories = bidict(classdict)


maxlen = 500 #400
embedding_dims = 60 #60
maxFeature = 5000 #10000
test_size = 0.05
train_epochs = 300
class_length = len(categories)


tokenizer = Tokenizer(filters='!"#$%&()*+,-./:;<=>?@[\]^_`{|}~\t\n！，。（）；’‘的我你他好很',split=" ",num_words=maxFeature)  #创建一个Tokenizer对象
modelfile = 'D:\dev\Command\datamining\embedding\\word2vec\\word2vec.model'
corpusfile='segment'
