import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

from pandas import read_csv,DataFrame


WINDOWSIZE = 3
n = 7
 

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




#data_num = np.loadtxt("./EMD_sequence/sub_num_real_time.txt")
data_num = np.loadtxt("./EMD_sequence/sub_num_real_time_new1.txt")

for run_time in range(int(data_num)+1) :

	#org_datacsv = read_csv("./EMD_sequence/series_sub_real_time"+(str(run_time+1))+".csv")
	org_datacsv = read_csv("./EMD_sequence/series_sub_real_time"+str((run_time)+1)+"_new1.csv")
	org_datacsv.drop(['Unnamed: 0'],axis=1, inplace=True)
	org_dataDF = DataFrame(org_datacsv)
	org_data = org_dataDF.values
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
	
	#erro_data = DataFrame(erro_data)
	#erro_data.to_csv("./process_data/error_data/error_data_real_time"+(str(run_time+1))+".csv")
	#smooth_data = DataFrame(smooth_data)
	#smooth_data.to_csv("./process_data/smooth_data/smooth_data_real_time"+(str(run_time+1))+".csv")
	

	erro_data = DataFrame(erro_data)
	erro_data.to_csv("./process_data/error_data/error_data_real_time"+(str(run_time+1))+"_new1.csv")
	smooth_data = DataFrame(smooth_data)
	smooth_data.to_csv("./process_data/smooth_data/smooth_data_real_time"+(str(run_time+1))+"_new1.csv")

