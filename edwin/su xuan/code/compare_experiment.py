import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import os
import warnings
import time
import random


from math import sqrt
from pandas import read_csv,DataFrame
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
from keras import backend
from keras.models import load_model

seq_len = 10
demo_day = 3

solar_data_for_valicsv =  read_csv("./process_data/data_for_real_time_prediction_new.csv")
solar_data_for_valicsv.drop(['Unnamed: 0'],axis=1, inplace=True)
df = DataFrame(solar_data_for_valicsv)
series = df.values
series = series.reshape(series.shape[0],)
result_realdata = np.array([])

for index in range(len(series) - (seq_len+1)):
	result_realdata = np.append(result_realdata , series[index: index + (seq_len+1)])
result_realdata = result_realdata.reshape(len(series)-(seq_len+1),(seq_len+1))
cut = round(0.9 * result_realdata.shape[0])
vali_data = result_realdata[int(cut):, -1]

data_num = np.loadtxt("./EMD_sequence/sub_num_real_time_new1.txt")

predicted_save = np.array([])
predicted_save_ELM = np.array([])


for run_time in range(int(data_num)):

    solar_data_for_modelcsv = read_csv("./process_data/smooth_data/smooth_data_real_time"+(str(run_time+1))+"_new1.csv")
    solar_data_for_y_test = read_csv("./EMD_sequence/series_sub_real_time"+str((run_time)+1)+"_new1.csv")
    solar_data_for_modelcsv.drop(['Unnamed: 0'],axis=1, inplace=True)
    solar_data_for_y_test.drop(['Unnamed: 0'],axis=1, inplace=True)
    solar_data_for_modelDF = DataFrame(solar_data_for_modelcsv)
    solar_data_for_y_testDF = DataFrame(solar_data_for_y_test)
    solar_data_for_modelval = solar_data_for_modelDF.values
    solar_data_for_y_testval = solar_data_for_y_testDF.values
    scaler = MinMaxScaler(feature_range=(-1, 1)) 
    solar_data_for_modelval = scaler.fit_transform(solar_data_for_modelval)
    solar_data_for_modelval = solar_data_for_modelval.reshape(solar_data_for_modelval.shape[0],)



    sequence_length = seq_len + 1
    result = np.array([])
    result_y_test = np.array([])
    
    for index in range(len(solar_data_for_modelval) - sequence_length):
    	result = np.append(result , solar_data_for_modelval[index: index + sequence_length])
    result = result.reshape(len(solar_data_for_modelval)-sequence_length,sequence_length)

    for index in range(len(solar_data_for_y_testval) - sequence_length):
    	result_y_test = np.append(result_y_test , solar_data_for_y_testval[index: index + sequence_length])
    result_y_test = result_y_test.reshape(len(solar_data_for_y_testval)-sequence_length,sequence_length)


    row = round(0.9 * result.shape[0])
    train = result[:int(row), :]
    np.random.shuffle(train)
    x_train = train[:, :-1]
    y_train = train[:, -1]
    x_test = result[int(row):, :-1]
    y_test = result_y_test[int(row):, -1]
    x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
    x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1)) 

    model = load_model("./model/model_smooth"+str((run_time+1))+"_new1.h5")
    predicted = model.predict(x_test)


    predicted = np.reshape(predicted,(predicted.shape[0],1))
    predicted = scaler.inverse_transform(predicted)
    predicted = np.reshape(predicted,(predicted.shape[0],))


    if run_time < 1 :
    	predicted_save = np.append(predicted_save,predicted)

    else :
    	predicted_save = predicted_save + predicted

    rmselm = sqrt(mean_squared_error(y_test , predicted))
    print('RMSE FOR EMD-SSA-LSTM %ds sub-series: %f' % ((int(run_time)+1),rmselm))
    fig = plt.figure(facecolor='white')
    ax = fig.add_subplot(111)
    ax.plot(y_test[-(57*demo_day):], label='True Data')
    plt.plot(predicted[-(57*demo_day):], label='Prediction')
    plt.legend()
    plt.savefig('./plot/EMD-SSA-LSTM-sub'+(str(run_time+1))+'.png')



rms = sqrt(mean_squared_error(vali_data, predicted_save))
print('RMSE FOR EMD-SSA-LSTM: %f' % (rms))

fig = plt.figure(facecolor='white')
ax = fig.add_subplot(111)
ax.plot(vali_data[-(57*demo_day):], label='True Data')
plt.plot(predicted_save[-(57*demo_day):], label='Prediction')
plt.legend()
plt.savefig('./plot/EMD-SSA-LSTM total.png')


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

    model = load_model("./model/model_ELM"+str((run_time)+1)+".h5")
    predicted = model.predict(x_test)

    predicted = np.reshape(predicted,(predicted.shape[0],1))
    predicted = scaler.inverse_transform(predicted)
    predicted = np.reshape(predicted,(predicted.shape[0],))

    y_test = np.reshape(y_test,(y_test.shape[0],1))
    y_test = scaler.inverse_transform(y_test)
    y_test = np.reshape(y_test,(y_test.shape[0],))

    if run_time < 1 :
        predicted_save_ELM = np.append(predicted_save_ELM,predicted)

    else :
    	predicted_save_ELM = predicted_save_ELM + predicted

    rmselm = sqrt(mean_squared_error(y_test , predicted))
    print('RMSE FOR EMD-ELM %ds sub-series: %f' % ((int(run_time)+1),rmselm))
    fig = plt.figure(facecolor='white')
    ax = fig.add_subplot(111)
    ax.plot(y_test[-(57*demo_day):], label='True Data')
    plt.plot(predicted[-(57*demo_day):], label='Prediction')
    plt.legend()
    plt.savefig('./plot/EMD-ELM-sub'+(str(run_time+1))+'.png')


rms = sqrt(mean_squared_error(vali_data , predicted_save_ELM))
print('RMSE FOR EMD-ELM: %f' % (rms))

fig = plt.figure(facecolor='white')
ax = fig.add_subplot(111)
ax.plot(vali_data[-(57*demo_day):], label='True Data')
plt.plot(predicted_save_ELM[-(57*demo_day):], label='Prediction')
plt.legend()
plt.savefig('./plot/EMD-ELM total.png')
