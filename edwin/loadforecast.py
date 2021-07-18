import math
import numpy as np 
from sklearn.metrics import accuracy_score
import pylab as pl
import pandas as pd
import matplotlib.pyplot as plt
from pandas import read_csv
import scipy.signal as signal
from scipy import fftpack  
import scipy.signal as signal
from scipy import interpolate
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
from keras.models import load_model

#判定當前的時間序列是否是單調序列
def ismonotonic(x):
    max_peaks=signal.argrelextrema(x,np.greater)[0]
    min_peaks=signal.argrelextrema(x,np.less)[0]
    all_num=len(max_peaks)+len(min_peaks)
    if all_num>0:
        return False
    else:
        return True       
#尋找當前時間序列的極值點
def findpeaks(x):    
#     df_index=np.nonzero(np.diff((np.diff(x)>=0)+0)<0)
    
#     u_data=np.nonzero((x[df_index[0]+1]>x[df_index[0]]))
#     df_index[0][u_data[0]]+=1
    
#     return df_index[0]
    return signal.argrelextrema(x,np.greater)[0]
#判斷當前的序列是否為 IMF 序列
def isImf(x):
    N=np.size(x)
    pass_zero=np.sum(x[0:N-2]*x[1:N-1]<0)#過零點的個數
    peaks_num=np.size(findpeaks(x))+np.size(findpeaks(-x))#極值點的個數
    if abs(pass_zero-peaks_num)>1:
        return False
    else:
        return True
#獲取當前樣條曲線
def getspline(x):
    N=np.size(x)
    peaks=findpeaks(x)
#     print '當前極值點個數：',len(peaks)
    peaks=np.concatenate(([0],peaks))
    peaks=np.concatenate((peaks,[N-1]))
    if(len(peaks)<=3):
#         if(len(peaks)<2):
#             peaks=np.concatenate(([0],peaks))
#             peaks=np.concatenate((peaks,[N-1]))
#             t=interpolate.splrep(peaks,y=x[peaks], w=None, xb=None, xe=None,k=len(peaks)-1)
#             return interpolate.splev(np.arange(N),t)
        t=interpolate.splrep(peaks,y=x[peaks], w=None, xb=None, xe=None,k=len(peaks)-1)
        return interpolate.splev(np.arange(N),t)
    t=interpolate.splrep(peaks,y=x[peaks])
    return interpolate.splev(np.arange(N),t)
#     f=interp1d(np.concatenate(([0,1],peaks,[N+1])),np.concatenate(([0,1],x[peaks],[0])),kind='cubic')
#     f=interp1d(peaks,x[peaks],kind='cubic')
#     return f(np.linspace(1,N,N))
#經驗模態分解方法
def emd(xr):
    imf=[]
    u=0
    while u<14 and (not ismonotonic(xr)):
        u+=1
        x1=xr
        sd=np.inf
        
        while sd>0.1 or  (not isImf(x1)):
#             print isImf(x1)
            
            s1=getspline(x1)
            s2=-getspline(-1*x1)
            x2=x1-(s1+s2)/2
            sd=np.sum((x1-x2)**2)/np.sum(x1**2)
            x1=x2
    
        imf.append(x1)
        xr=xr-x1
    imf.append(xr)
    return imf
 
def create_dataset(dataset, look_back=1):
        dataX, dataY = [], []
        for i in range(len(dataset)-look_back-1):#-1是python從0開始所以把0扣掉
                a = dataset[i:(i+look_back), 0]
                dataX.append(a)#1~96是dataX 以此類推
                dataY.append(dataset[i + look_back, 0]) #97是dataY 以此類推    
        return np.array(dataX), np.array(dataY)
def main():
        #載入時間序列數據
        data = read_csv('107test.txt',header=None,engine='python')
        x=data.values
        xr=np.reshape(x,(1,len(x)))
        xa=xr.flatten()
        #給時間長度
        t=np.linspace(1,35040,35040)
        #t1=np.reshape(t,(len(t)))

        #做imf
        imf = emd(xa)
        imfs = pd.DataFrame(imf)
        imfss = imfs.values
        total=np.zeros([35136,1])
        
        for k in range(0, len(imf)) :
                # fix random seed for reproducibility
                np.random.seed(7)
                # load the dataset
                #dataframe = read_csv('loaddata.txt', usecols=[3], engine='python', skipfooter=3)
                datasets = imfss[k]
                datasets= np.reshape(datasets,(len(datasets),1))
                dataset = datasets.astype('float32')
                avgVol= datasets.mean()
                # normalize the dataset
                scaler = MinMaxScaler(feature_range=(0, 1))
                dataset = scaler.fit_transform(dataset)
                dataForPre = dataset
                # split into train and test sets
                train_size = int(len(dataset) * 0.67)
                test_size = len(dataset) - train_size
                train, test = dataset[0:train_size,:], dataset[train_size:len(dataset),:]
                # reshape into X=t and Y=t+1
                look_back = 96
                trainX, trainY = create_dataset(train, look_back)
                testX, testY = create_dataset(test, look_back)
                # reshape input to be [samples, time steps, features]
                trainX = np.reshape(trainX, (trainX.shape[0], trainX.shape[1], 1))
                testX = np.reshape(testX, (testX.shape[0], testX.shape[1], 1))
                # create and fit the LSTM network
                model = Sequential()
                model.add(LSTM(96, input_shape=(look_back,1)))
                model.add(Dense(1))
          #     model.add(LSTM(96,return_sequences = True))
          #     model.add(LSTM(96,return_sequences = True))
          #     model.add(LSTM(96))
          #     model.add(Dense(1))
                model.compile(loss='mean_squared_error', optimizer='adam')
                model.fit(trainX, trainY,epochs=1, batch_size=48, validation_split=0.1, verbose=2)
                model.save('eletricmodel_{}.h5'.format(k))
                #make predictions
                trainPredict = model.predict(trainX)
                testPredict = model.predict(testX)
                # invert predictions
                trainPredict = scaler.inverse_transform(trainPredict)
                
                trainY = scaler.inverse_transform([trainY])
                testPredict = scaler.inverse_transform(testPredict)
                testY = scaler.inverse_transform([testY])
                # calculate root mean squared error
                trainScore = math.sqrt(mean_squared_error(trainY[0], trainPredict[:,0]))
                print('Train Score: %.2f RMSE' % (trainScore))
                testScore = math.sqrt(mean_squared_error(testY[0], testPredict[:,0]))
                print('Test Score: %.2f RMSE' % (testScore))
           

                # shift train predictions for plotting
                trainPredictPlot = np.empty_like(dataset)
                trainPredictPlot[:, :] = np.nan
                trainPredictPlot[look_back:len(trainPredict)+look_back, :] = trainPredict
                # shift test predictions for plotting
                testPredictPlot = np.empty_like(dataset)
                testPredictPlot[:, :] = np.nan
                testPredictPlot[len(trainPredict)+(look_back*2)+1:len(dataset)-1, :] = testPredict
                # model = load_model('eletricmodel_{}.h5'.format(k))
                for r in range(96):
                        scalered_data_np = dataForPre[-96:]
                        np.savetxt('scalered_data_np_{}.txt'.format(r),scalered_data_np)
                        #scalered_data_np = scaler.fit_transform(data_np)
                        preparedToPredict_np = np.reshape(scalered_data_np, ( 1,look_back,1))
                        sca_future = model.predict(preparedToPredict_np)
                        future = scaler.inverse_transform(sca_future)
                        future = future.astype(np.float64)
                        int_future = future[0].tolist()
                        dataForPre = dataForPre.tolist()
                        dataForPre.append(sca_future)
                        dataForPre = np.array(dataForPre)
                dataForPre = scaler.inverse_transform(dataForPre)
                total=np.add(total,dataForPre)
                print("total",total)
                np.savetxt('total1114.txt',total)
                
        # plt.plot(x)
        # plt.plot(trainPredictPlot)
        # plt.plot(testPredictPlot)
        # #print(np.shape(testPredictPlot))
        # plt.ylabel('Volume in kW')
        # plt.xlabel('Records')
        # plt.show()
        # # plt.plot(train_history.history['loss'])  
        # # plt.plot(train_history.history['val_loss'])  
        # #print("model_imf_%d.h5")%(k+1)
        # # model.save('model_imf.h5')
        # # print("model_save!")

        
main()
