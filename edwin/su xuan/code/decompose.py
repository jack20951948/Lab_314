import numpy as np 
import pandas as pd
import scipy.signal as signal
import matplotlib.pyplot as plt

from pandas import read_csv,DataFrame
from scipy import fftpack  
from scipy import interpolate


DECOM_NUM_DAY = 5
DECOM_NUM_REAL_TIME = 11
#DECOM_NUM_REAL_TIME = 6


def ismonotonic(x):
    max_peaks=signal.argrelextrema(x,np.greater)[0]
    min_peaks=signal.argrelextrema(x,np.less)[0]
    all_num=len(max_peaks)+len(min_peaks)
    if all_num>0:
        return False
    else:
        return True

def findpeaks(x):
    return signal.argrelextrema(x,np.greater)[0]


def isImf(x):
    N=np.size(x)
    pass_zero=np.sum(x[0:N-2]*x[1:N-1]<0)#过零点的个数
    peaks_num=np.size(findpeaks(x))+np.size(findpeaks(-x))#极值点的个数
    if abs(pass_zero-peaks_num)>1:
        return False
    else:
        return True


def getspline(x):
    N=np.size(x)
    peaks=findpeaks(x)
    peaks=np.concatenate(([0],peaks))
    peaks=np.concatenate((peaks,[N-1]))
    if(len(peaks)<=3):
        t=interpolate.splrep(peaks,y=x[peaks], w=None, xb=None, xe=None,k=len(peaks)-1)
        return interpolate.splev(np.arange(N),t)
    t=interpolate.splrep(peaks,y=x[peaks])
    return interpolate.splev(np.arange(N),t)


def emd(x,num):
    imf=[]
    y = num
    while not ismonotonic(x) and y != 0:
        x1=x
        sd=np.inf
        while sd>0.1 or  (not isImf(x1)):
            s1=getspline(x1)
            s2=-getspline(-1*x1)
            x2=x1-(s1+s2)/2
            sd=np.sum((x1-x2)**2)/np.sum(x1**2)
            x1=x2

        imf.append(x1)
        x=x-x1
        y=y-1
    imf.append(x)
    return imf


def save_emd(data,mode):

	if mode == 0 :
		for i in range(len(data)):
			sub_data = DataFrame(data[i])
			sub_data.to_csv("./EMD_sequence/series_sub_day"+str(i+1)+".csv")
	elif mode == 1 :
		for i in range(len(data)):
			sub_data = DataFrame(data[i])
			sub_data.to_csv("./EMD_sequence/series_sub_real_time"+str(i+1)+"_new1.csv")
            #sub_data.to_csv("./EMD_sequence/series_sub_real_time"+str(i+1)+".csv")

#--------------------------------day-------------------------------------#
'''

dataset = read_csv('./process_data/data_for_day_ahead_prediction')
dataset.drop(['Unnamed: 0'],axis=1, inplace=True)
df = DataFrame(dataset)
series = df.values
print(series.shape)
series = series.ravel()

imf1=emd(series,DECOM_NUM_DAY-1)
print(imf1,len(imf1))
data_len = np.array([])
data_len = np.append(data_len,len(imf1))
np.savetxt("./EMD_sequence/sub_num_day.txt",data_len)
save_emd(imf1,0)


data_num = np.loadtxt("./EMD_sequence/sub_num_day.txt")


for run_time in range(int(data_num)):
	solar_datacsv = read_csv("./EMD_sequence/series_sub_day"+str((run_time)+1)+".csv")
	solar_datacsv.drop(['Unnamed: 0'],axis=1, inplace=True)
	solar_dataDF = DataFrame(solar_datacsv)
	solar_dataFIN = solar_dataDF.values
	solar_ssain = solar_dataFIN.reshape(solar_dataFIN.shape[0],)
	plt.subplot(5, 1, run_time+1)
	plt.plot(solar_ssain[-1000:])
plt.show()

data_final =imf1[0]
for i in range(len(imf1)-1):
    data_final = data_final + imf1[i+1]

plt.figure(figsize=(16,4))
plt.plot(data_final)
plt.legend()
plt.show()
'''
#--------------------------------realtime-------------------------------------#

dataset = read_csv('./process_data/data_for_real_time_prediction_new.csv')
#dataset = read_csv('./process_data/data_for_real_time_prediction')
dataset.drop(['Unnamed: 0'],axis=1, inplace=True)
df = DataFrame(dataset)
series = df.values
print(series.shape)
series = series.ravel()

imf1=emd(series,DECOM_NUM_REAL_TIME-1)
print(imf1,len(imf1))
data_len = np.array([])
data_len = np.append(data_len,len(imf1))
#np.savetxt("./EMD_sequence/sub_num_real_time_new.txt",data_len)
np.savetxt("./EMD_sequence/sub_num_real_time_new1.txt",data_len)
#np.savetxt("./EMD_sequence/sub_num_real_time.txt",data_len)
save_emd(imf1,1)


data_num = np.loadtxt("./EMD_sequence/sub_num_real_time_new1.txt")


for run_time in range(int(data_num)):
	solar_datacsv = read_csv("./EMD_sequence/series_sub_real_time"+str((run_time)+1)+"_new1.csv")
	solar_datacsv.drop(['Unnamed: 0'],axis=1, inplace=True)
	solar_dataDF = DataFrame(solar_datacsv)
	solar_dataFIN = solar_dataDF.values
	solar_ssain = solar_dataFIN.reshape(solar_dataFIN.shape[0],)
	plt.subplot(6, 3, run_time+1)
	plt.plot(solar_ssain[:])
plt.show()

data_final =imf1[0]
for i in range(len(imf1)-1):
    data_final = data_final + imf1[i+1]

plt.figure(figsize=(16,4))
plt.plot(data_final)
plt.legend()
plt.show()
