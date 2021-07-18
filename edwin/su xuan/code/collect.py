import numpy as np
import pandas as pd

import pymysql

print("connect to the database...")
print("--------------------------")


conn = pymysql.connect(host='140.124.42.70',port = 6666, user='root',password='fuzzy314', db='monitor_data',charset='utf8', use_unicode=True)


sql = "SELECT * FROM monitor_history_2018_04"
dt_1= pd.read_sql(sql, con=conn)
dt_1.to_csv("./raw/HEMS_sqldata_2018_04.csv")


sql = "SELECT * FROM monitor_history_2018_05"
dt_2= pd.read_sql(sql, con=conn)
dt_2.to_csv("./raw/HEMS_sqldata_2018_05.csv")


sql = "SELECT * FROM monitor_history_2018_06"
dt_3= pd.read_sql(sql, con=conn)
dt_3.to_csv("./raw/HEMS_sqldata_2018_06.csv")


sql = "SELECT * FROM monitor_history_2018_07"
dt_4= pd.read_sql(sql, con=conn)
dt_4.to_csv("./raw/HEMS_sqldata_2018_07.csv")


sql = "SELECT * FROM monitor_history_2018_08"
dt_5= pd.read_sql(sql, con=conn)
dt_5.to_csv("./raw/HEMS_sqldata_2018_08.csv")


sql = "SELECT * FROM monitor_history_2018_09"
dt_6= pd.read_sql(sql, con=conn)
dt_6.to_csv("./raw/HEMS_sqldata_2018_09.csv")


sql = "SELECT * FROM monitor_history_2018_10"
dt_7= pd.read_sql(sql, con=conn)
dt_7.to_csv("./raw/HEMS_sqldata_2018_10.csv")


sql = "SELECT * FROM monitor_history_2018_11"
dt_8= pd.read_sql(sql, con=conn)
dt_8.to_csv("./raw/HEMS_sqldata_2018_11.csv")


sql = "SELECT * FROM monitor_history_2018_12"
dt_9= pd.read_sql(sql, con=conn)
dt_9.to_csv("./raw/HEMS_sqldata_2018_12.csv")

sql = "SELECT * FROM monitor_history_2019_01"
dt_9= pd.read_sql(sql, con=conn)
dt_9.to_csv("./raw/HEMS_sqldata_2019_01.csv")

sql = "SELECT * FROM monitor_history_2019_02"
dt_9= pd.read_sql(sql, con=conn)
dt_9.to_csv("./raw/HEMS_sqldata_2019_02.csv")

sql = "SELECT * FROM monitor_history_2019_03"
dt_9= pd.read_sql(sql, con=conn)
dt_9.to_csv("./raw/HEMS_sqldata_2019_03.csv")

sql = "SELECT * FROM monitor_history_2019_04"
dt_9= pd.read_sql(sql, con=conn)
dt_9.to_csv("./raw/HEMS_sqldata_2019_04.csv")


print("collect complete ")
conn.close()
print("--------------------------")
print("disconnect")