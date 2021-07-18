import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
from pandas import read_csv,DataFrame

WINDOWSIZE = 3
n = 100


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



dataset = read_csv('./process_data/data_for_real_time_prediction')
dataset.drop(['Unnamed: 0'],axis=1, inplace=True)
df = DataFrame(dataset)
org_data = df.values
org_data = org_data.reshape(org_data.shape[0],)
smooth_data = getWindowMatrix(org_data,len(org_data),WINDOWSIZE)
smooth_data = SVDreduce (smooth_data)
smooth_data = recreateArray(smooth_data,len(org_data),WINDOWSIZE)



fig = plt.figure(facecolor='white')
ax = fig.add_subplot(111)
ax.plot(org_data[-n*(57):], label='Original')
plt.plot(smooth_data[-n*(57):], label='Smooth')
plt.legend()
plt.show()

erro_data = org_data - smooth_data

plt.figure(figsize=(16,4))
plt.plot(erro_data[-n*(57):], label = 'error_data')
plt.legend()
plt.show()