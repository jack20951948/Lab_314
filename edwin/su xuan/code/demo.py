import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt


import os
import warnings
import time
import random
import argparse

from math import sqrt
from pandas import read_csv,DataFrame
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
from keras import backend
from keras.models import load_model


ap = argparse.ArgumentParser()
ap.add_argument("-a","--ago", type=int, default=0,
	help="weekend or not")
args = vars(ap.parse_args())


ago = args["ago"]
multi_num = 9
seq_len = 10


def find_contiguous_colors(colors):
    # finds the continuous segments of colors and returns those segments
    segs = []
    curr_seg = []
    prev_color = ''
    for c in colors:
        if c == prev_color or prev_color == '':
            curr_seg.append(c)
        else:
            segs.append(curr_seg)
            curr_seg = []
            curr_seg.append(c)
        prev_color = c
    segs.append(curr_seg) # the final one
    return segs


def plot_multicolored_lines(x,y,colors):
    segments = find_contiguous_colors(colors)
    start= 0
    for seg in segments:
        end = start + len(seg)
        l, = plt.gca().plot(x[start:end],y[start:end],c=seg[0],label = 'predicted') 
        start = end


solar_data_for_valicsv =  read_csv("./process_data/data_for_real_time_prediction_new.csv")
#solar_data_for_valicsv =  read_csv("./process_data/data_for_real_time_prediction")
solar_data_for_valicsv.drop(['Unnamed: 0'],axis=1, inplace=True)
df = DataFrame(solar_data_for_valicsv)
series = df.values[:-(ago)]
series = series.reshape(series.shape[0],)
result_realdata = np.array([])


for index in range(len(series) - (seq_len+1)):
	result_realdata = np.append(result_realdata , series[index: index + (seq_len+1)])
result_realdata = result_realdata.reshape(len(series)-(seq_len+1),(seq_len+1))
cut = round(0.9 * result_realdata.shape[0])
vali_data = result_realdata[int(cut):, -1]



#data_num = np.loadtxt("./EMD_sequence/sub_num_real_time.txt")
data_num = np.loadtxt("./EMD_sequence/sub_num_real_time_new1.txt")

predicted_save = np.array([])
predicted_error_save = np.array([])
future_save = np.array([])
compensate_save = np.array([])


for run_time in range(int(data_num)):


	#solar_data_for_modelcsv = read_csv("./process_data/smooth_data/smooth_data_real_time"+(str(run_time+1))+".csv")
	solar_data_for_modelcsv = read_csv("./process_data/smooth_data/smooth_data_real_time"+(str(run_time+1))+"_new1.csv")
	solar_data_for_modelcsv.drop(['Unnamed: 0'],axis=1, inplace=True)
	solar_data_for_modelDF = DataFrame(solar_data_for_modelcsv)
	solar_data_for_modelval = solar_data_for_modelDF.values[:-(ago)]
	scaler = MinMaxScaler(feature_range=(-1, 1)) 
	solar_data_for_modelval = scaler.fit_transform(solar_data_for_modelval)
	solar_data_for_modelval = solar_data_for_modelval.reshape(solar_data_for_modelval.shape[0],)

	sequence_length = seq_len + 1
	result = np.array([])
	
	
	for index in range(len(solar_data_for_modelval) - sequence_length):
		result = np.append(result , solar_data_for_modelval[index: index + sequence_length])
	result = result.reshape(len(solar_data_for_modelval)-sequence_length,sequence_length)


	row = round(0.9 * result.shape[0])
	train = result[:int(row), :]
	np.random.shuffle(train)
	x_train = train[:, :-1]
	y_train = train[:, -1]
	x_test = result[int(row):-(multi_num), :-1]
	y_test = result[int(row):, -1]
	x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
	x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1)) 

	#model = load_model("./model/model_smooth"+str((run_time+1))+".h5")
	model = load_model("./model/model_smooth"+str((run_time+1))+"_new1.h5")
	predicted = model.predict(x_test)
	predicted = np.reshape(predicted,(predicted.shape[0],))


	dt_forrealtime = result[-(multi_num),-(seq_len):]
	future = np.array([])


	for i in range(multi_num):
		dt_forrealtime_input = np.reshape(dt_forrealtime,(1,dt_forrealtime.shape[0],1)) 
		prediction = model.predict(dt_forrealtime_input)

		#alpha = random.uniform(0,0.05)

		future = np.append(future,prediction)
		dt_forrealtime = np.append(dt_forrealtime,prediction[0,0])
		dt_forrealtime = np.delete(dt_forrealtime, 0)
		i = i + 1

	predicted = np.reshape(predicted,(predicted.shape[0],1))
	predicted = scaler.inverse_transform(predicted)
	predicted = np.reshape(predicted,(predicted.shape[0],))

	future = np.reshape(future,(future.shape[0],1))
	future = scaler.inverse_transform(future)
	future = np.reshape(future,(future.shape[0],))

	if run_time < 1 :
		predicted_save = np.append(predicted_save,predicted)
		future_save = np.append(future_save,future[:])


	else :
		predicted_save = predicted_save + predicted
		future_save = future_save + future

for i in range(len(future_save)):
	if future_save[i] < 0:
		future_save[i] = 0
	else:
		future_save[i] = future_save[i]

predicted_save_org = np.append(predicted_save,future_save[:])


for i in range(multi_num):
	rms = sqrt(mean_squared_error(vali_data[-(multi_num)-(multi_num+i):-(multi_num)+i] , predicted_save_org[-(multi_num)-(multi_num+i):-(multi_num)+i]))
	print('t+%d RMSE: %f' % ((i+1), rms))


plot_array = np.arange(2100) 
colors = ['orange']*len(predicted_save_org)
colors[-((multi_num)+1):] = ['red']*((multi_num)+1)
fig = plt.figure(facecolor='white')
ax = fig.add_subplot(111)
ax.plot(vali_data, label='True Data')
plot_multicolored_lines(plot_array,predicted_save_org,colors)
plt.legend()
plt.show()



for run_time in range(int(data_num)):

	#solar_data_for_modelcsv = read_csv("./process_data/error_data/error_data_real_time"+(str(run_time+1))+".csv")
	solar_data_for_modelcsv = read_csv("./process_data/error_data/error_data_real_time"+(str(run_time+1))+"_new1.csv")
	solar_data_for_modelcsv.drop(['Unnamed: 0'],axis=1, inplace=True)
	solar_data_for_modelDF = DataFrame(solar_data_for_modelcsv)
	solar_data_for_modelval = solar_data_for_modelDF.values[:-(ago)]
	scaler = MinMaxScaler(feature_range=(-1, 1)) 
	solar_data_for_modelval = scaler.fit_transform(solar_data_for_modelval)
	solar_data_for_modelval = solar_data_for_modelval.reshape(solar_data_for_modelval.shape[0],)

	sequence_length = seq_len + 1
	result = np.array([])
	
	
	for index in range(len(solar_data_for_modelval) - sequence_length):
		result = np.append(result , solar_data_for_modelval[index: index + sequence_length])
	result = result.reshape(len(solar_data_for_modelval)-sequence_length,sequence_length)


	row = round(0.9 * result.shape[0])
	train = result[:int(row), :]
	np.random.shuffle(train)
	x_train = train[:, :-1]
	y_train = train[:, -1]
	x_test = result[int(row):-(multi_num), :-1]
	y_test = result[int(row):, -1]
	x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
	x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1)) 

	#model = load_model("./model/model_error"+str((run_time+1))+".h5")
	model = load_model("./model/model_error"+str((run_time+1))+"_new1.h5")
	predicted = model.predict(x_test)
	predicted = np.reshape(predicted,(predicted.shape[0],))


	dt_forrealtime = result[-(multi_num),-(seq_len):]
	compensate = np.array([])


	for i in range(multi_num):
		dt_forrealtime_input = np.reshape(dt_forrealtime,(1,dt_forrealtime.shape[0],1)) 
		prediction = model.predict(dt_forrealtime_input)

		#alpha = random.uniform(0,0.05)

		compensate = np.append(compensate,prediction)
		dt_forrealtime = np.append(dt_forrealtime,prediction[0,0])
		dt_forrealtime = np.delete(dt_forrealtime, 0)
		i = i + 1

	predicted = np.reshape(predicted,(predicted.shape[0],1))
	predicted = scaler.inverse_transform(predicted)
	predicted = np.reshape(predicted,(predicted.shape[0],))

	compensate = np.reshape(compensate,(compensate.shape[0],1))
	compensate = scaler.inverse_transform(compensate)
	compensate = np.reshape(compensate,(compensate.shape[0],))

	if run_time < 1 :
		predicted_error_save = np.append(predicted_error_save,predicted)
		compensate_save = np.append(compensate_save,compensate[:])


	else :
		predicted_error_save = predicted_error_save + predicted
		compensate_save = compensate_save + compensate
		

future_save = future_save + compensate_save
for i in range(len(future_save)):
	if future_save[i] < 0:
		future_save[i] = 0
	else:
		future_save[i] = future_save[i]

predicted_save_com = np.append(predicted_save,future_save[:])

for i in range(multi_num):
	rms = sqrt(mean_squared_error(vali_data[-(multi_num)-(multi_num+i):-(multi_num)+i] , predicted_save_com[-(multi_num)-(multi_num+i):-(multi_num)+i]))
	print('t+%d RMSE: %f' % ((i+1), rms))


plot_array = np.arange(2100) 
colors = ['orange']*len(predicted_save_com)
colors[-((multi_num)+1):] = ['red']*((multi_num)+1)
fig = plt.figure(facecolor='white')
ax = fig.add_subplot(111)
ax.plot(vali_data, label='True Data')
plot_multicolored_lines(plot_array,predicted_save_com,colors)
plt.legend()
plt.show()
