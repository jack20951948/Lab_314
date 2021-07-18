import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import os
import warnings
import time

from matplotlib import pyplot
from datetime import date
from pandas import DataFrame
from pandas import read_csv
from datetime import datetime
from keras.layers.core import Dense, Activation, Dropout
from keras.models import Sequential,load_model
from sklearn.preprocessing import MinMaxScaler

seq_len = 10
epochs = 200
batchsize = 20 
hiden_neuron = 20


data_num = np.loadtxt("./EMD_sequence/sub_num_real_time_new1.txt")

for run_time in range(int(data_num)):
    solar_datacsv = read_csv("./EMD_sequence/series_sub_real_time"+str((run_time)+1)+"_new1.csv")
    solar_datacsv.drop(['Unnamed: 0'],axis=1, inplace=True)
    solar_dataDF = DataFrame(solar_datacsv)
    solar_dataval = solar_dataDF.values
    scaler = MinMaxScaler(feature_range=(-1, 1))
    solar_dataval = scaler.fit_transform(solar_dataval)
    solar_dataval = solar_dataval.reshape(solar_dataval.shape[0],)
    sequence_length = seq_len + 1
    result = np.array([])
	
    for index in range(len(solar_dataval) - sequence_length):
    	result = np.append(result , solar_dataval[index: index + sequence_length])
    result = result.reshape(len(solar_dataval)-sequence_length,sequence_length)

    row = round(0.9 * result.shape[0])
    train = result[:int(row), :]
    np.random.shuffle(train)
    x_train = train[:, :-1]
    y_train = train[:, -1]
    x_test = result[int(row):, :-1]
    y_test = result[int(row):, -1]

    model = Sequential()
    model.add(Dense(hiden_neuron,input_shape = (x_train.shape[1],) ,activation = 'tanh'))
    model.add(Dense(1,activation='linear'))


    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' #Hide messy TensorFlow warnings
    warnings.filterwarnings("ignore") #Hide messy Numpy warning
    start = time.time()
    model.compile(optimizer="adam", loss="mae")
    print("> Compilation Time : ", time.time() - start)
    model.fit(x_train,y_train,batch_size=batchsize,nb_epoch=epochs,validation_split=0.05)
    model.save("./model/model_ELM"+str((run_time)+1)+".h5")
    
    '''
    predicted = model.predict(x_test)
    fig = plt.figure(facecolor='white')
    ax = fig.add_subplot(111)
    ax.plot(y_test, label='True Data')
    plt.plot(predicted, label='Prediction')
    plt.legend()
    plt.show()
    '''