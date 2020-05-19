import numpy as np
import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt


import tensorflow.keras.layers as layers
# from tensorflow.keras.layers import Dense, Activation,Dropout, Flatten,MaxPooling1D
from tensorflow.keras.layers import Dense, Embedding, Dropout, Activation,Flatten, Conv1D, GlobalMaxPooling1D,Dropout
import datasets

from tensorflow.keras.preprocessing.sequence import pad_sequences
import setting
import pickle

# # test
# num_features = 3000
# sequence_length = 300
# embedding_dimension = 100
# (x_train, y_train), (x_test, y_test) = keras.datasets.imdb.load_data(num_words=num_features)
# print(x_train)
# print(x_train.shape)
# print(len(x_train[0]))
# x_train = pad_sequences(x_train, maxlen=sequence_length)
# x_test = pad_sequences(x_test, maxlen=sequence_length)
# print(x_train)
# print(x_train.shape)
# print(len(x_train[0]))
# exit()






#param







# # datasets
print(datasets.trainX.shape)
print(len(datasets.trainX[0]))
print(len(datasets.trainX[2]))
print(datasets.trainX[0])
print(datasets.trainX[2])
# exit()



####### tf model process  ########
def CNN():
    # model parameters:
    nb_words =len(datasets.tokenizer.word_index)+1
    embedding_dims = setting.embedding_dims
    cnn_filters = 100
    cnn_kernel_size = 5
    dense_hidden_dims = 200
    maxlen =setting.maxlen
    print('Build model...')
    model = tf.keras.Sequential()
    model.add(layers.Embedding(nb_words,embedding_dims,input_length=maxlen))
    model.add(layers.Dropout(0.5))
    model.add(layers.Conv1D(cnn_filters, cnn_kernel_size,padding='valid', activation='relu'))
    model.add(layers.GlobalMaxPooling1D())
    model.add(layers.Dense(dense_hidden_dims))
    model.add(layers.Dropout(0.5))
    model.add(layers.Dense(64,activation='relu'))
    model.add(layers.Dense(1))
    model.add(layers.Dense(setting.class_length,activation='sigmoid'))
    return model

def FastText():
    maxlen =setting.maxlen
    embedding_dims = setting.embedding_dims
    max_features = len(datasets.tokenizer.word_index)+1
    model = tf.keras.Sequential()
    model.add(layers.Embedding(max_features,embedding_dims,input_length=maxlen))
    model.add(layers.GlobalAveragePooling1D())
    model.add(layers.Dense(setting.class_length, activation='sigmoid'))
    return model

def RNN():
    max_features = len(datasets.tokenizer.word_index)+1
    embedding_dims = setting.embedding_dims
    # embedding_dims_2 = 30
    
    model = tf.keras.Sequential()
    model.add(layers.Embedding(max_features,embedding_dims))
    model.add(layers.Bidirectional(layers.LSTM(embedding_dims)))
    # model.add(layers.Bidirectional(layers.LSTM(embedding_dims,return_sequences=True)))
    # model.add(layers.Bidirectional(layers.LSTM(20)))
    model.add(layers.Dense(10, activation='relu'))
    model.add(layers.Dense(setting.class_length, activation='sigmoid'))
    return model






# tfModel = FastText() #0.9683
# tfModel = CNN()
tfModel = RNN() #0.9874 #0.9992 

tfModel.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])

# train
history1 = tfModel.fit(datasets.trainX,datasets.trainY,
    epochs=setting.train_epochs,
    # validation_data=[],
    # verbose=1
    batch_size=10,
    )


#evaluate
# print(len(datasets.testX))
# print(datasets.testY)
results = tfModel.evaluate(datasets.testX,datasets.testY,verbose=0)
print(results)

#
for name, value in zip(tfModel.metrics_names, results):
    print("%s: %.3f" % (name, value))


#plot 
def plot_graphs(history, name):
    plt.plot(history.history[name])
    # plt.plot(history.history['validation'+ name])
    # plt.xlabel("Epochs")
    # plt.ylabel(name)
    # plt.legend([name, 'validation - ' + name])
    plt.show()


def modelsave(configpath):
    # saving
    with open(configpath+'/tokenizer.pickle', 'wb') as handle:
        pickle.dump(datasets.tokenizer, handle, protocol=pickle.HIGHEST_PROTOCOL)

    tf.keras.models.save_model(tfModel, configpath+"/model.h5", save_format="h5")

    with open(configpath+"/config.file", "wb") as f:
        pickle.dump({'categories':setting.categories,'maxlen':setting.maxlen}, f)

# plot_graphs(history1, 'accuracy')
modelsave('./modelconfigsave')
