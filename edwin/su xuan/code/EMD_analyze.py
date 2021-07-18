import numpy as np 
import pandas as pd
import scipy.signal as signal
import matplotlib.pyplot as plt

from pandas import read_csv,DataFrame
from scipy import fftpack  
from scipy import interpolate


#DECOM_NUM_DAY = 5
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
    print(N)
    peaks=findpeaks(x)
    print(peaks)
    peaks=np.concatenate(([0],peaks))
    print(peaks)
    peaks=np.concatenate((peaks,[N-1]))
    print(peaks)
    print(len(peaks))
    if(len(peaks)<=3):
        t=interpolate.splrep(peaks,y=x[peaks], w=None, xb=None, xe=None,k=len(peaks)-1)
        return interpolate.splev(np.arange(N),t)
    t=interpolate.splrep(peaks,y=x[peaks])
    return interpolate.splev(np.arange(N),t)


def emd(x):
    i=0
    imf=[]
    while not ismonotonic(x) and i != 10:
        i = i+1
        print(i)
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
    imf.append(x)
    return imf




#--------------------------------realtime-------------------------------------#

dataset = read_csv('./process_data/data_for_real_time_prediction_new.csv')
dataset.drop(['Unnamed: 0'],axis=1, inplace=True)
df = DataFrame(dataset)
series = df.values
print(series.shape)
series = series.ravel()
imf1=emd(series)
print(imf1,len(imf1))


for run_time in range(len(imf1)):
    plt.figure(figsize=(16,4))
    plt.plot(imf1[run_time])
    plt.legend()
    plt.show()

	#plt.subplot(6, 2, run_time+1)
	#plt.plot(imf1[run_time])
#plt.show()


data_final =imf1[0]
for i in range(len(imf1)-1):
    data_final = data_final + imf1[i+1]

plt.figure(figsize=(16,4))
plt.plot(data_final)
plt.legend()
plt.show()
