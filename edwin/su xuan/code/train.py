import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt


import os
import warnings
import time
import random


from pandas import read_csv,DataFrame
from sklearn.preprocessing import MinMaxScaler
from keras import backend
from keras.layers.core import Dense, Activation, Dropout
from keras.layers.recurrent import LSTM , SimpleRNN
from keras.models import Sequential,load_model
from keras import metrics


seq_len = 10
epochs = 200
batchsize = 20
in_put = 1 
hiden_neuron = 20
multi_num = 10
layers = [in_put, seq_len, 100, 1]


#data_num = np.loadtxt("./EMD_sequence/sub_num_real_time.txt")
data_num = np.loadtxt("./EMD_sequence/sub_num_real_time_new1.txt")
'''
for run_time in range(int(data_num)):

	#solar_datacsv = read_csv("./process_data/smooth_data/smooth_data_real_time"+(str(run_time+1))+".csv")
	solar_datacsv = read_csv("./process_data/smooth_data/smooth_data_real_time"+(str(run_time+1))+"_new1.csv")
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
	x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
	x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1)) 

	model = Sequential()
	model.add(LSTM(hiden_neuron,input_shape=(layers[1], layers[0])))
	model.add(Dense(1))
	model.add(Activation("linear"))

	os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' #Hide messy TensorFlow warnings
	warnings.filterwarnings("ignore") #Hide messy Numpy warning
	start = time.time()

	model.compile(loss="mse", optimizer="adam")
	print("> Compilation %s Time : "%(run_time+1), time.time() - start)
	history = model.fit(x_train,y_train,batch_size=batchsize,nb_epoch=epochs,validation_split=0.05)
	#model.save("./model/model_smooth"+str((run_time)+1)+".h5")
	model.save("./model/model_smooth"+str((run_time)+1)+"_new1.h5")

'''
for run_time in range(int(data_num)):

	#error_datacsv = read_csv("./process_data/error_data/error_data_real_time"+(str(run_time+1))+".csv")
	error_datacsv = read_csv("./process_data/error_data/error_data_real_time"+(str(run_time+1))+"_new1.csv")
	error_datacsv.drop(['Unnamed: 0'],axis=1, inplace=True)
	error_dataDF = DataFrame(error_datacsv)
	error_dataval = error_dataDF.values
	scaler = MinMaxScaler(feature_range=(-1, 1))
	error_dataval = scaler.fit_transform(error_dataval)

	sequence_length = seq_len + 1
	result = np.array([])
	
	for index in range(len(error_dataval) - sequence_length):
		result = np.append(result , error_dataval[index: index + sequence_length])
	result = result.reshape(len(error_dataval)-sequence_length,sequence_length)

	row = round(0.9 * result.shape[0])
	train = result[:int(row), :]
	np.random.shuffle(train)
	x_train = train[:, :-1]
	y_train = train[:, -1]
	x_test = result[int(row):-(multi_num), :-1]
	y_test = result[int(row):, -1]
	x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
	x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1)) 	

	model_error = Sequential()
	model_error.add(SimpleRNN(hiden_neuron,input_shape=(layers[1], layers[0])))
	model_error.add(Dense(1))
	model_error.add(Activation("linear"))

	os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' #Hide messy TensorFlow warnings
	warnings.filterwarnings("ignore") #Hide messy Numpy warning
	start = time.time()

	model_error.compile(loss="mse", optimizer="adam")
	print("> Compilation %s Time : "%(run_time+1), time.time() - start)
	history = model_error.fit(x_train,y_train,batch_size=batchsize,nb_epoch=epochs,validation_split=0.05)
	#model_error.save("./model/model_error"+str((run_time)+1)+".h5")
	model_error.save("./model/model_error"+str((run_time)+1)+"_new1.h5")









    
    