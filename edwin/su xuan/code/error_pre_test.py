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


WINDOWSIZE = 3
seq_len = 12
epochs = 200
batchsize = 20
in_put = 1 
hiden_neuron = 8
multi_num = 10
layers = [in_put, seq_len, 100, 1]


def getWindowMatrix(inputArray,t,m):
	temp = []
	n = t - m + 1
	for i in range(n):
		temp.append(inputArray[i:i+m])
	WindowMatrix = np.array(temp)
	return WindowMatrix


def SVDreduce (trajectoy_Matrix):
	u,s,v = np.linalg.svd(trajectoy_Matrix)
	m1,n1 = u.shape
	m2,n2 = v.shape
	index = s.argmax()
	u1 = u[:,index]
	v1 = v[index]
	u1 = u1.reshape((m1,1))
	v1 = v1.reshape((1,n2))
	value = s.max()
	newMatrix = value*(np.dot(u1,v1))
	return newMatrix


def recreateArray(newMatrix,t,m):
	ret = []
	n = t - m +1
	for p in range(1,t+1):
		if p<m:
			alpha = p
		elif p>t-m+1:
			alpha = t-p+1
		else:
			alpha = m
		sigma = 0
		for j in range(1,m+1):
			i = p - j +1
			if i>0 and i<n+1:
				sigma += newMatrix[i-1][j-1]
		ret.append(sigma/alpha)
	return ret


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






org_datacsv = read_csv("./EMD_sequence/series_sub_real_time2.csv")
org_datacsv.drop(['Unnamed: 0'],axis=1, inplace=True)
org_dataDF = DataFrame(org_datacsv)
org_data = org_dataDF.values[:]
scaler = MinMaxScaler(feature_range=(-1, 1))
org_data = scaler.fit_transform(org_data) 
org_data = org_data[:-multi_num,:]
org_data = org_data.reshape(org_data.shape[0],)
smooth_data = getWindowMatrix(org_data,len(org_data),WINDOWSIZE)
smooth_data = SVDreduce (smooth_data)
smooth_data = recreateArray(smooth_data,len(org_data),WINDOWSIZE)

sequence_length = seq_len + 1
result = np.array([])
result_SSA = np.array([])
result_validation = np.array([])


for index in range(len(org_data) - sequence_length):
	result = np.append(result , org_data[index: index + sequence_length])
result = result.reshape(len(org_data)-sequence_length,sequence_length)

for index in range(len(smooth_data) - sequence_length):
	result_SSA = np.append(result_SSA , smooth_data[index: index + sequence_length])
result_SSA = result_SSA.reshape(len(org_data)-sequence_length,sequence_length)

row = round(0.95 * result.shape[0])
train = result[:int(row), :]
train_SSA = result_SSA[:int(row), :]
np.random.shuffle(train_SSA)
x_train = train_SSA[:, :-1]
y_train = train_SSA[:, -1]
x_test = result_SSA[int(row):-(multi_num), :-1]
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
'''
#for record 
model.compile(loss="mse", optimizer="adam",metrics = [rmse])
'''
#model.compile(loss="mse", optimizer="adam")
#print("> Compilation Time : ", time.time() - start)
#history = model.fit(x_train,y_train,batch_size=batchsize,nb_epoch=epochs,validation_split=0.05)
#model.save("./model/test_model.h5")
#predicted = model.predict(x_test)
#predicted = np.reshape(predicted,(predicted.shape[0],))


model = load_model("./model/test_model.h5")
predicted = model.predict(x_test)
predicted = np.reshape(predicted,(predicted.shape[0],))


dt_forrealtime = result_SSA[-(multi_num),-(seq_len):]
future = np.array([])
for i in range(multi_num):
	dt_forrealtime_input = np.reshape(dt_forrealtime,(1,dt_forrealtime.shape[0],1)) 
	prediction = model.predict(dt_forrealtime_input)

	alpha = random.uniform(0,0.05)

	future = np.append(future,prediction+alpha)
	
	dt_forrealtime = np.append(dt_forrealtime,prediction[0,0])

	dt_forrealtime = np.delete(dt_forrealtime, 0)
	i = i + 1


predicted = np.append(predicted,future[:])

'''
fig = plt.figure(facecolor='white')
ax = fig.add_subplot(111)
ax.plot(history.history['loss'], label='train')
plt.plot(history.history['val_loss'], label='test')
plt.legend()
plt.show() 
'''
plot_array = np.arange(1000) 
colors = ['orange']*len(predicted)
colors[-((multi_num)):] = ['red']*((multi_num))
fig = plt.figure(facecolor='white')
ax = fig.add_subplot(111)
ax.plot(y_test, label='True Data')
plot_multicolored_lines(plot_array,predicted,colors)
plt.legend()
plt.show()
