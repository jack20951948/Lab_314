import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from pandas import read_csv
from pandas import DataFrame
from calendar import monthrange


START_MONTH_2018 = 5
START_MONTH_2019 = 1
DATA_NUM_2018 = 8
DATA_NUM_2019 = 4
SOLAR_TBLOCK = 48


process_data1 = np.array([])
process_data2 = np.array([])
raw_data1 = np.array([])
process_data3 = np.array([])
process_data4 = np.array([])
raw_data2 = np.array([])


for i in range(DATA_NUM_2018):
	
	month = START_MONTH_2018 + i

	if month < 10:
		str_month = str(month)
		str_month = str_month.zfill(2)
	else:
		str_month = str(month)

	dataset = read_csv("./raw/HEMS_sqldata_2018_"+str_month+"_new.csv")
	#dataset = read_csv("./raw/HEMS_sqldata_2018_"+str_month+".csv")

	#print(dataset)
	df_1 = DataFrame(dataset)
	df_2 = DataFrame(dataset)
	#print(df_1)
	dataset_1 = df_1.set_index('datetime')
	dataset_2 = df_2.set_index('datetime')
	#print(dataset_1)
	dataset_1.drop(['Unnamed: 0','Vsys','Psys','Pload','Pbat','Psolar','Prect','P_1','P_2','P_3','Vfc','Pfc','Psell','SOC','lx_power','PV_temp','id'] ,axis=1, inplace=True)
	#print(dataset_1)
	dataset_2.drop(['Unnamed: 0','Vsys','Psys','Pload','Pbat','Psolar','Prect','P_1','P_2','P_3','Vfc','Pfc','Psell','SOC','period','lx_power','PV_temp','id','day'] ,axis=1, inplace=True)

	dataset_2 = dataset_2.values
	raw_data1 = np.append(raw_data1,dataset_2)


	num_day_in_month = monthrange(2018,month)
	num_day_in_month = num_day_in_month[1]
	


	for j in range(num_day_in_month):

		data_buffer1 = np.array([])
		data_buffer2 = np.array([])

		mask1 = (dataset_1["day"] == j+1)
		mask2 = (dataset_1["period"] >= 19)
		mask3 = (dataset_1["period"] <= 75)	
		data_filter = dataset_1[(mask1&mask2&mask3)]
		data_filter.drop(['day','period'] ,axis=1, inplace=True)
		data_filter = data_filter.values
		print(len(data_filter),j+1)
		size_filter = len(data_filter) - SOLAR_TBLOCK

		for index in range(len(data_filter)-size_filter):
			data_buffer1 = np.append(data_buffer1 , data_filter[index: index + size_filter])
		data_buffer1 = data_buffer1.reshape(SOLAR_TBLOCK,size_filter)
		#print(data_buffer1,data_buffer1.shape)

		for run_time in range(data_buffer1.shape[0]):
			alpha = np.average(data_buffer1[run_time])
			data_buffer2 = np.append(data_buffer2,alpha)	
		#print(data_buffer2,data_buffer2.shape)

		process_data1 = np.append(process_data1,data_buffer2)
		process_data2 = np.append(process_data2,data_filter)




for i in range(DATA_NUM_2019):
	
	month = START_MONTH_2019 + i

	if month < 10:
		str_month = str(month)
		str_month = str_month.zfill(2)
	else:
		str_month = str(month)

	dataset = read_csv("./raw/HEMS_sqldata_2019_"+str_month+"_new.csv",encoding='big5')
	#dataset = read_csv("./raw/HEMS_sqldata_2019_"+str_month+".csv")

	#print(dataset)
	df_1 = DataFrame(dataset)
	df_2 = DataFrame(dataset)
	#print(df_1)
	dataset_1 = df_1.set_index('datetime')
	dataset_2 = df_2.set_index('datetime')
	#print(dataset_1)
	dataset_1.drop(['Unnamed: 0','Vsys','Psys','Pload','Pbat','Psolar','Prect','P_1','P_2','P_3','Vfc','Pfc','Psell','SOC','lx_power','PV_temp','id'] ,axis=1, inplace=True)
	#print(dataset_1)
	dataset_2.drop(['Unnamed: 0','Vsys','Psys','Pload','Pbat','Psolar','Prect','P_1','P_2','P_3','Vfc','Pfc','Psell','SOC','period','lx_power','PV_temp','id','day'] ,axis=1, inplace=True)

	dataset_2 = dataset_2.values
	raw_data2 = np.append(raw_data2,dataset_2)

	num_day_in_month = monthrange(2019,month)
	num_day_in_month = num_day_in_month[1]
	

	for j in range(num_day_in_month):

		data_buffer1 = np.array([])
		data_buffer2 = np.array([])

		mask1 = (dataset_1["day"] == j+1)
		mask2 = (dataset_1["period"] >= 19)
		mask3 = (dataset_1["period"] <= 75)	
		data_filter = dataset_1[(mask1&mask2&mask3)]
		data_filter.drop(['day','period'] ,axis=1, inplace=True)
		data_filter = data_filter.values
		print(len(data_filter),j+1)
		size_filter = len(data_filter) - SOLAR_TBLOCK

		for index in range(len(data_filter)-size_filter):
			data_buffer1 = np.append(data_buffer1 , data_filter[index: index + size_filter])
		data_buffer1 = data_buffer1.reshape(SOLAR_TBLOCK,size_filter)
		#print(data_buffer1,data_buffer1.shape)

		for run_time in range(data_buffer1.shape[0]):
			alpha = np.average(data_buffer1[run_time])
			data_buffer2 = np.append(data_buffer2,alpha)	
		#print(data_buffer2,data_buffer2.shape)

		process_data3 = np.append(process_data3,data_buffer2)
		process_data4 = np.append(process_data4,data_filter)

raw_data_final = np.append(raw_data1,raw_data2)
process_data_final1 = np.append(process_data1,process_data3)
process_data_final2 = np.append(process_data2,process_data4)

plt.subplot(2, 1, 1)
plt.plot(raw_data_final, label='Raw Data')
plt.subplot(2, 1, 2)
plt.plot(process_data_final2,label='Without Night Time')
plt.show()
print(process_data_final2,process_data_final2.shape,size_filter)


run_time_final = len(process_data_final1) / 4
data_for_model1 = np.array([])


for k in range(int(run_time_final)):
	data_buffer = process_data_final1[:4]
	alpha = np.average(data_buffer)
	process_data_final1 = process_data_final1[4:]
	data_for_model1 = np.append(data_for_model1,alpha)



fig = plt.figure(facecolor='white')
ax = fig.add_subplot(111)
ax.plot(data_for_model1, label='preprocess data')
plt.legend()
plt.show()
#print(data_for_model1,data_for_model1.shape)

'''
data_for_model1 = DataFrame(data_for_model1)
data_for_model1.to_csv("./process_data/data_for_day_ahead_prediction.csv")
'''
data_for_model2 = DataFrame(process_data_final2)
data_for_model2.to_csv("./process_data/data_for_real_time_prediction_new.csv")




