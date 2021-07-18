import scipy

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from pandas import read_csv
from pandas import DataFrame
from sklearn.preprocessing import MinMaxScaler
from scipy.stats import kurtosis , skew
from math import sqrt



def euclid_dist(t1,t2):
    return (sum((t1-t2)**2))

sample_day = 90

dataset = read_csv('./process_data/data_for_real_time_prediction')
dataset.drop(['Unnamed: 0'],axis=1, inplace=True)
df = DataFrame(dataset)
series = df.values[:(sample_day*57)]
print(series.shape)

fig = plt.figure(facecolor='white')
ax = fig.add_subplot(111)
ax.plot(series, label='preprocess data')
plt.legend()
plt.show()

scaler = MinMaxScaler(feature_range=(-1, 1)) 

runtime = len(series)/57
average_value = np.array([])
total_value = np.array([])
deviation_value = np.array([])
variance_value = np.array([])
coef_variance_value = np.array([])
kurtosis_value = np.array([])
skew_value = np.array([])

for i in range(int(runtime)):
	value_buffer = series[:57]
	series = series[57:]
	tolal = np.sum(value_buffer)
	average = tolal/57
	deviation = np.std(value_buffer)
	variance = np.var(value_buffer)
	coef_variance = deviation/average
	kurtos = kurtosis(value_buffer)
	skewness = skew(value_buffer)


	total_value = np.append(total_value,tolal)
	average_value = np.append(average_value,average)
	deviation_value = np.append(deviation_value,deviation)
	variance_value = np.append(variance_value,variance)
	coef_variance_value = np.append(coef_variance_value,coef_variance)
	kurtosis_value = np.append(kurtosis_value,kurtos)
	skew_value = np.append(skew_value,skewness)



total_value = np.reshape(total_value,(total_value.shape[0],1))
average_value = np.reshape(average_value,(average_value.shape[0],1))
deviation_value = np.reshape(deviation_value,(deviation_value.shape[0],1))
variance_value = np.reshape(variance_value,(variance_value.shape[0],1))
coef_variance_value = np.reshape(coef_variance_value,(coef_variance_value.shape[0],1))
kurtosis_value = np.reshape(kurtosis_value,(kurtosis_value.shape[0],1))
skew_value = np.reshape(skew_value,(skew_value.shape[0],1))

total_value_nor = scaler.fit_transform(total_value)
average_value_nor = scaler.fit_transform(average_value)
deviation_value_nor = scaler.fit_transform(deviation_value)
variance_value_nor = scaler.fit_transform(variance_value)
coef_variance_value_nor = scaler.fit_transform(coef_variance_value)
kurtosis_value_nor = scaler.fit_transform(kurtosis_value)
skew_value_nor = scaler.fit_transform(skew_value)

total_value_nor = np.reshape(total_value_nor,(total_value.shape[0],))
average_value_nor = np.reshape(average_value_nor,(average_value.shape[0],))
deviation_value_nor = np.reshape(deviation_value_nor,(deviation_value.shape[0],))
variance_value_nor = np.reshape(variance_value_nor,(variance_value.shape[0],))
coef_variance_value_nor = np.reshape(coef_variance_value_nor,(coef_variance_value.shape[0],))
kurtosis_value_nor = np.reshape(kurtosis_value_nor,(kurtosis_value.shape[0],))
skew_value_nor = np.reshape(skew_value_nor,(skew_value.shape[0],))


plt.subplot(6,1,1)
plt.plot(average_value_nor,label = 'average_value')
plt.subplot(6,1,2)
plt.plot(total_value_nor,label = 'total_value')
plt.subplot(6,1,3)
plt.plot(deviation_value_nor,label = 'deviation_value')
plt.subplot(6,1,4)
plt.plot(skew_value_nor,label = 'skewness_value')
plt.subplot(6,1,5)
plt.plot(coef_variance_value_nor,label = 'coef_variance_value')
plt.subplot(6,1,6)
plt.plot(kurtosis_value_nor,label = 'kurtosis_value')

plt.show()

feature_space = np.array([])
feature_space = np.append(feature_space,average_value_nor)
feature_space = np.append(feature_space,total_value_nor)
feature_space = np.append(feature_space,deviation_value_nor)
feature_space = np.append(feature_space,skew_value_nor)
feature_space = np.append(feature_space,coef_variance_value_nor)
feature_space = np.append(feature_space,kurtosis_value_nor)

feature_space = np.reshape(feature_space,(6,sample_day))
feature_space = feature_space.T
feature_space_copy = feature_space
print(feature_space.shape)
print(feature_space)


d_final = np.array([])
for runtime_i in range(sample_day):
	mid_buffer = np.array([])
	for runtime_j in range(sample_day):
		d = euclid_dist(feature_space[runtime_i],feature_space_copy[runtime_j])
		mid_buffer = np.append(mid_buffer,d)
	mid_buffer = np.sum(mid_buffer)
	mid_buffer = sqrt(mid_buffer)
	d_final = np.append(d_final,mid_buffer)

print(d_final)
print(d_final.shape)

scaler1= MinMaxScaler(feature_range=(0, 1)) 
d_final = np.reshape(d_final,(d_final.shape[0],1))
d_final = scaler1.fit_transform(d_final)
d_final = np.reshape(d_final,(d_final.shape[0],))

print(d_final)

for i in range(len(d_final)):
	if d_final[i] <= 0.2:
		d_final[i] = 1
	elif d_final[i] > 0.2 and d_final[i] <= 0.4 :
		d_final[i] = 2
	elif d_final[i] > 0.4 and d_final[i] <= 0.6 :
		d_final[i] = 3
	elif d_final[i] > 0.6 and d_final[i] <= 0.8 :
		d_final[i] = 4
	else:
		d_final[i] = 5


print(d_final)



