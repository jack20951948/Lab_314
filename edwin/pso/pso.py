# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 11:50:18 2020

@author: edwin
"""

import pandas as pd
import numpy as np
import csv
import random
from openpyxl import Workbook
import configparser

class Position:
    def __init__(self,m1,m2,m3,m4,m5,m6,m7,m8,V1_1,V1_2,V1_3,V1_4,V2_1,V2_2,V2_3,V2_4,V3_1,V3_2,V3_3,V3_4,V4_1,V4_2,V4_3,V4_4,V5_1,V5_2,V5_3,V5_4,V6_1,V6_2,V6_3,V6_4,V7_1,V7_2,V7_3,V7_4,V8_1,V8_2,V8_3,V8_4,V9_1,V9_2,V9_3,V9_4,futuretotal):
        # x y為自變量,可以多個
        
        self.m1=m1
        self.m2=m2
        self.m3=m3
        self.m4=m4
        self.m5=m5
        self.m6=m6
        self.m7=m7
        self.m8=m8
        self.V1_1=V1_1
        self.V1_2=V1_2
        self.V1_3=V1_3
        self.V1_4=V1_4
        self.V2_1=V2_1
        self.V2_2=V2_2
        self.V2_3=V2_3
        self.V2_4=V2_4
        self.V3_1=V3_1
        self.V3_2=V3_2
        self.V3_3=V3_3
        self.V3_4=V3_4
        self.V4_1=V4_1
        self.V4_2=V4_2
        self.V4_3=V4_3
        self.V4_4=V4_4
        self.V5_1=V5_1
        self.V5_2=V5_2
        self.V5_3=V5_3
        self.V5_4=V5_4
        self.V6_1=V6_1
        self.V6_2=V6_2
        self.V6_3=V6_3
        self.V6_4=V6_4
        self.V7_1=V7_1
        self.V7_2=V7_2
        self.V7_3=V7_3
        self.V7_4=V7_4
        self.V8_1=V8_1
        self.V8_2=V8_2
        self.V8_3=V8_3
        self.V8_4=V8_4
        self.V9_1=V9_1
        self.V9_2=V9_2
        self.V9_3=V9_3
        self.V9_4=V9_4
        
        # 該點的適應度 即要求的函数值
        
        self.futuretotal=futuretotal
        
    def __str__(self):
        return "m1:"+str(self.m1)+"m2:"+str(self.m2)+"m3:"+str(self.m3)+"m4:"+str(self.m4)+"m5:"+str(self.m5)+"m6:"+str(self.m6)+"m7:"+str(self.m7)+"m8:"+str(self.m8)+"V1_1:"+str(self.V1_1)+"V1_2:"+str(self.V1_2)+"V1_3:"+str(self.V1_3)+"V1_4:"+str(self.V1_4)+"V2_1:"+str(self.V2_1)+"V2_2:"+str(self.V2_2)+"V2_3:"+str(self.V2_3)+"V2_4:"+str(self.V2_4)+"V3_1:"+str(self.V3_1)+"V3_2:"+str(self.V3_2)+"V3_3:"+str(self.V3_3)+"V3_4:"+str(self.V3_4)+"V4_1:"+str(self.V4_1)+"V4_2:"+str(self.V4_2)+"V4_3:"+str(self.V4_3)+"V4_4:"+str(self.V4_4)+"V5_1:"+str(self.V5_1)+"V5_2:"+str(self.V5_2)+"V5_3:"+str(self.V5_3)+"V5_4:"+str(self.V5_4)+"V6_1:"+str(self.V6_1)+"V6_2:"+str(self.V6_2)+"V6_3:"+str(self.V6_3)+"V6_4:"+str(self.V6_4)+"V7_1:"+str(self.V7_1)+"V7_2:"+str(self.V7_2)+"V7_3:"+str(self.V7_3)+"V7_4:"+str(self.V7_4)+"V8_1:"+str(self.V8_1)+"V8_2:"+str(self.V8_2)+"V8_3:"+str(self.V8_3)+"V8_4:"+str(self.V8_4)+"V9_1:"+str(self.V9_1)+"V9_2:"+str(self.V9_2)+"V9_3:"+str(self.V9_3)+"V9_4:"+str(self.V9_4)+"futuretotal:"+str(self.futuretotal)
    def __strm1__(self):
        return str(self.m1)
    def __strm2__(self):
        return str(self.m2)
    def __strm3__(self):
        return str(self.m3)
    def __strm4__(self):
        return str(self.m4)
    def __strm5__(self):
        return str(self.m5)
    def __strm6__(self):
        return str(self.m6)
    def __strm7__(self):
        return str(self.m7)
    def __strm8__(self):
        return str(self.m8)
    def __str1_1__(self):
        return str(self.V1_1)
    def __str1_2__(self):
        return str(self.V1_2)
    def __str1_3__(self):
        return str(self.V1_3)
    def __str1_4__(self):
        return str(self.V1_4)
    def __str2_1__(self):
        return str(self.V2_1)
    def __str2_2__(self):
        return str(self.V2_2)
    def __str2_3__(self):
        return str(self.V2_3)
    def __str2_4__(self):
        return str(self.V2_4)
    def __str3_1__(self):
        return str(self.V3_1)
    def __str3_2__(self):
        return str(self.V3_2)
    def __str3_3__(self):
        return str(self.V3_3)
    def __str3_4__(self):
        return str(self.V3_4)
    def __str4_1__(self):
        return str(self.V4_1)
    def __str4_2__(self):
        return str(self.V4_2)
    def __str4_3__(self):
        return str(self.V4_3)
    def __str4_4__(self):
        return str(self.V4_4)
    def __str5_1__(self):
        return str(self.V5_1)
    def __str5_2__(self):
        return str(self.V5_2)
    def __str5_3__(self):
        return str(self.V5_3)
    def __str5_4__(self):
        return str(self.V5_4)
    def __str6_1__(self):
        return str(self.V6_1)
    def __str6_2__(self):
        return str(self.V6_2)
    def __str6_3__(self):
        return str(self.V6_3)
    def __str6_4__(self):
        return str(self.V6_4)
    def __str7_1__(self):
        return str(self.V7_1)
    def __str7_2__(self):
        return str(self.V7_2)
    def __str7_3__(self):
        return str(self.V7_3)
    def __str7_4__(self):
        return str(self.V7_4)
    def __str8_1__(self):
        return str(self.V8_1)
    def __str8_2__(self):
        return str(self.V8_2)
    def __str8_3__(self):
        return str(self.V8_3)
    def __str8_4__(self):
        return str(self.V8_4)
    def __str9_1__(self):
        return str(self.V9_1)
    def __str9_2__(self):
        return str(self.V9_2)
    def __str9_3__(self):
        return str(self.V9_3)
    def __str9_4__(self):
        return str(self.V9_4)
    def __futuretotal__(self):
        return str(self.futuretotal)
    
# 粒子數
n=200
# 粒子集合
p=[]
v=[]
pBest=[]
#gBest=Position(0,0,0,0,0,0,0,0,Vx_x[0][0],Vx_x[0][1],Vx_x[0][2],Vx_x[0][3],0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
gBest=Position(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
# 學習因子
c1=2.1
c2=2.4
# 慣性權重
w=0.5
# 更新邊界
vmax=100
v1max=100
v2max=100
v3max=100
v4max=100
# 迭代次數
_max=2000

# 適應函數
def fitnessFunction(m1,m2,m3,m4,m5,m6,m7,m8,V1_1,V1_2,V1_3,V1_4,V2_1,V2_2,V2_3,V2_4,V3_1,V3_2,V3_3,V3_4,V4_1,V4_2,V4_3,V4_4,V5_1,V5_2,V5_3,V5_4,V6_1,V6_2,V6_3,V6_4,V7_1,V7_2,V7_3,V7_4,V8_1,V8_2,V8_3,V8_4,V9_1,V9_2,V9_3,V9_4):
    capbilitySetUp = []
    capbilitySetUp2 = []
    capbilitySetUp3 = []
    capbilitySetUp4 = []
    sameVprice1=0
    sameVprice2=0
    sameVprice3=0
    sameVprice4=0
    sameVprice5=0
    sameVprice6=0
    sameVprice7=0
    sameVprice8=0
    sameVprice9=0
    
    for k in range (0,int(m1)-1):
        if ((totalflow[k]['A'] is not 0) and (maxtotalflow[k]['A'] is not 0)) :
            #基本電費
            basic1 = ( 217.3 * V1_1 + 160.6 * V1_2 + 43.4 * V1_3 * max(( V1_3 + V1_4 - 0.5 * ( V1_1 + V1_2 )),0) ) * 0.98 * 1.15 #夏月
            #流動電費
            #flowsummer1 = 4.61 * totalflow[k]['A'] + 2.87 * totalflow[k]['B']  + 1.73 * totalflow[k]['D'] + 1.29 * totalflow[k]['C']
            #功率折扣費
            #discount1 = ( basic1 + flowsummer1 ) * (80-95) / 1000 
            #超約附加費
            Eov1_1 = max((maxtotalflow[k]['A']-V1_1),0)
            Eov1_2 = max((maxtotalflow[k]['B']-V1_1-V1_2),0)
            Eov1_4 = max((maxtotalflow[k]['D']-V1_1-V1_2-V1_4),0)
            Eov1_3 = max((maxtotalflow[k]['C']-V1_1-V1_2-V1_4-V1_3),0)

            Eovc1_1 = Eov1_1
            Eovc1_2 = max((Eov1_2-Eovc1_1),0)
            Eovc1_4 = max((Eov1_4-max(Eovc1_1,Eovc1_2)),0)
            Eovc1_3 = max((Eov1_3-max(Eovc1_1,Eovc1_2,Eovc1_4)),0)
        
            overAprice1 = 2 * 217.3 * max(min(Eovc1_1,(0.1*V1_1)),0) + 3*217.3*max((Eovc1_1-(0.1*V1_1)),0)  #夏月
            overBprice1 = 2*160.6*max(min(Eovc1_2,(0.1*V1_2)),0) + 3*160.6*max((Eovc1_2-(0.1*V1_2)),0)
            overDprice1 = 2*43.3*max(min(Eovc1_4,(0.1*V1_4)),0) + 3*43.3*max((Eovc1_4-(0.1*V1_4)),0)
            overCprice1 = 2*43.3*max(min(Eovc1_3,(0.1*V1_3)),0) + 3*43.3*max((Eovc1_3-(0.1*V1_3)),0)
            overprice1 = overAprice1 + overBprice1 + overDprice1 + overCprice1
            #price1 = basic1 + flowsummer1 + discount1 + overprice1
            price1 = basic1 +  overprice1
            sameVprice1 += price1
            totalprice.append(price1) 
            capbilitySetUp.append(V1_1)
            capbilitySetUp2.append(V1_2)
            capbilitySetUp3.append(V1_3)
            capbilitySetUp4.append(V1_4)
        else:
            #基本電費
            basic1 = ( 160.6 * V1_1 + 160.6 * V1_2 + 32.1 * V1_3 * max(( V1_3 + V1_4 - 0.5 * ( V1_1 + V1_2 )),0) ) * 0.98 * 1.15 #非夏月
            #流動電費
            #flowwinter1 = 2.78 * totalflow[k]['B'] + 1.65 * totalflow[k]['D'] + 1.22 * totalflow[k]['C']
            #功率折扣費
            #discount1 = ( basic1 + flowwinter1 ) * (80-95) / 1000 
            #超約附加費
            Eov1_1 = max((maxtotalflow[k]['B']-V1_1),0)
            Eov1_2 = max((maxtotalflow[k]['B']-V1_1-V1_2),0)
            Eov1_4 = max((maxtotalflow[k]['D']-V1_1-V1_2-V1_4),0)
            Eov1_3 = max((maxtotalflow[k]['C']-V1_1-V1_2-V1_4-V1_3),0)

            Eovc1_1 = Eov1_1
            Eovc1_2 = max((Eov1_2-Eovc1_1),0)
            Eovc1_4 = max((Eov1_4-max(Eovc1_1,Eovc1_2)),0)
            Eovc1_3 = max((Eov1_3-max(Eovc1_1,Eovc1_2,Eovc1_4)),0)
        
            overAprice1 = 2*160.6*max(min(Eovc1_1,(0.1*V1_1)),0) + 3*160.6*max((Eovc1_1-(0.1*V1_1)),0)
            overBprice1 = 2*160.6*max(min(Eovc1_2,(0.1*V1_2)),0) + 3*160.6*max((Eovc1_2-(0.1*V1_2)),0) #非夏月
            overDprice1 = 2*43.3*max(min(Eovc1_4,(0.1*V1_4)),0) + 3*43.3*max((Eovc1_4-(0.1*V1_4)),0)
            overCprice1 = 2*43.3*max(min(Eovc1_3,(0.1*V1_3)),0) + 3*43.3*max((Eovc1_3-(0.1*V1_3)),0)
            overprice1 = overAprice1 + overBprice1 + overDprice1 + overCprice1
            #price1 = basic1 + flowsummer1 + discount1 + overprice1
            price1 = basic1 + overprice1
            sameVprice1 += price1
            totalprice.append(price1) 
            capbilitySetUp.append(V1_1)
            capbilitySetUp2.append(V1_2)
            capbilitySetUp3.append(V1_3)
            capbilitySetUp4.append(V1_4)
    #return price1
    for k in range (int(m1)-1,int(m2)-1):
        if ((totalflow[k]['A'] is not 0) and (maxtotalflow[k]['A'] is not 0)) :
            #基本電費
            basic2 = ( 217.3 * V2_1 + 160.6 * V2_2 + 43.4 * V2_3 * max(( V2_3 + V2_4 - 0.5 * ( V2_1 + V2_2 )),0) ) * 0.98 * 1.15 #夏月
            #流動電費
            #flowsummer2 = 4.61 * totalflow[k]['A'] + 2.87 * totalflow[k]['B']  + 1.73 * totalflow[k]['D'] + 1.29 * totalflow[k]['C']
            #功率折扣費
            #discount2 = ( basic2 + flowsummer2 ) * (80-95) / 1000 
            #超約附加費
            Eov2_1 = max((maxtotalflow[k]['A']-V2_1),0)
            Eov2_2 = max((maxtotalflow[k]['B']-V2_1-V2_2),0)
            Eov2_4 = max((maxtotalflow[k]['D']-V2_1-V2_2-V2_4),0)
            Eov2_3 = max((maxtotalflow[k]['C']-V2_1-V2_2-V2_4-V2_3),0)

            Eovc2_1 = Eov2_1
            Eovc2_2 = max((Eov2_2-Eovc2_1),0)
            Eovc2_4 = max((Eov2_4-max(Eovc2_1,Eovc2_2)),0)
            Eovc2_3 = max((Eov2_3-max(Eovc2_1,Eovc2_2,Eovc2_4)),0)
        
            overAprice2 = 2 * 217.3 * max(min(Eovc2_1,(0.1*V2_1)),0) + 3*217.3*max((Eovc2_1-(0.1*V2_1)),0)  #夏月
            overBprice2 = 2*160.6*max(min(Eovc2_2,(0.1*V2_2)),0) + 3*160.6*max((Eovc2_2-(0.1*V2_2)),0)
            overDprice2 = 2*43.3*max(min(Eovc2_4,(0.1*V2_4)),0) + 3*43.3*max((Eovc2_4-(0.1*V2_4)),0)
            overCprice2 = 2*43.3*max(min(Eovc2_3,(0.1*V2_3)),0) + 3*43.3*max((Eovc2_3-(0.1*V2_3)),0)
            overprice2 = overAprice2 + overBprice2 + overDprice2 + overCprice2
            #price2 = basic2 + flowsummer2 + discount2 + overprice2
            price2 = basic2 + overprice2
            sameVprice2 += price2
            totalprice2.append(price2) 
            capbilitySetUp.append(V2_1)
            capbilitySetUp2.append(V2_2)
            capbilitySetUp3.append(V2_3)
            capbilitySetUp4.append(V2_4)
        else:
            #基本電費
            basic2 = ( 160.6 * V2_1 + 160.6 * V2_2 + 32.1 * V2_3 * max(( V2_3 + V2_4 - 0.5 * ( V2_1 + V2_2 )),0) ) * 0.98 * 1.15 #非夏月
            #流動電費
            #flowwinter2 = 2.78 * totalflow[k]['B'] + 1.65 * totalflow[k]['D'] + 1.22 * totalflow[k]['C']
            #功率折扣費
            #discount2 = ( basic2 + flowwinter2 ) * (80-95) / 1000 
            #超約附加費
            Eov2_1 = max((maxtotalflow[k]['B']-V2_1),0)
            Eov2_2 = max((maxtotalflow[k]['B']-V2_1-V2_2),0)
            Eov2_4 = max((maxtotalflow[k]['D']-V2_1-V2_2-V2_4),0)
            Eov2_3 = max((maxtotalflow[k]['C']-V2_1-V2_2-V2_4-V2_3),0)

            Eovc2_1 = Eov2_1
            Eovc2_2 = max((Eov2_2-Eovc2_1),0)
            Eovc2_4 = max((Eov2_4-max(Eovc2_1,Eovc2_2)),0)
            Eovc2_3 = max((Eov2_3-max(Eovc2_1,Eovc2_2,Eovc2_4)),0)
        
            overAprice2 = 2*160.6*max(min(Eovc2_1,(0.1*V2_1)),0) + 3*160.6*max((Eovc2_1-(0.1*V2_1)),0)
            overBprice2 = 2*160.6*max(min(Eovc2_2,(0.1*V2_2)),0) + 3*160.6*max((Eovc2_2-(0.1*V2_2)),0) #非夏月
            overDprice2 = 2*43.3*max(min(Eovc2_4,(0.1*V2_4)),0) + 3*43.3*max((Eovc2_4-(0.1*V2_4)),0)
            overCprice2 = 2*43.3*max(min(Eovc2_3,(0.1*V2_3)),0) + 3*43.3*max((Eovc2_3-(0.1*V2_3)),0)
            overprice2 = overAprice2 + overBprice2 + overDprice2 + overCprice2
            #price2 = basic2 + flowsummer2 + discount2 + overprice2
            price2 = basic2 + overprice2
            sameVprice2 += price2
            totalprice2.append(price2) 
            capbilitySetUp.append(V2_1)
            capbilitySetUp2.append(V2_2)
            capbilitySetUp3.append(V2_3)
            capbilitySetUp4.append(V2_4)
    #return price2
    for k in range (int(m2)-1,int(m3)-1):
        if ((totalflow[k]['A'] is not 0) and (maxtotalflow[k]['A'] is not 0)) :
            #基本電費
            basic3 = ( 217.3 * V3_1 + 160.6 * V3_2 + 43.4 * V3_3 * max(( V3_3 + V3_4 - 0.5 * ( V3_1 + V3_2 )),0) ) * 0.98 * 1.15 #夏月
            #流動電費
            #flowsummer3 = 4.61 * totalflow[k]['A'] + 2.87 * totalflow[k]['B']  + 1.73 * totalflow[k]['D'] + 1.29 * totalflow[k]['C']
            #功率折扣費
            #discount3 = ( basic3 + flowsummer3 ) * (80-95) / 1000 
            #超約附加費
            Eov3_1 = max((maxtotalflow[k]['A']-V3_1),0)
            Eov3_2 = max((maxtotalflow[k]['B']-V3_1-V3_2),0)
            Eov3_4 = max((maxtotalflow[k]['D']-V3_1-V3_2-V3_4),0)
            Eov3_3 = max((maxtotalflow[k]['C']-V3_1-V3_2-V3_4-V3_3),0)

            Eovc3_1 = Eov3_1
            Eovc3_2 = max((Eov3_2-Eovc3_1),0)
            Eovc3_4 = max((Eov3_4-max(Eovc3_1,Eovc3_2)),0)
            Eovc3_3 = max((Eov3_3-max(Eovc3_1,Eovc3_2,Eovc3_4)),0)
        
            overAprice3 = 2 * 217.3 * max(min(Eovc3_1,(0.1*V3_1)),0) + 3*217.3*max((Eovc3_1-(0.1*V3_1)),0)  #夏月
            overBprice3 = 2*160.6*max(min(Eovc3_2,(0.1*V3_2)),0) + 3*160.6*max((Eovc3_2-(0.1*V3_2)),0)
            overDprice3 = 2*43.3*max(min(Eovc3_4,(0.1*V3_4)),0) + 3*43.3*max((Eovc3_4-(0.1*V3_4)),0)
            overCprice3 = 2*43.3*max(min(Eovc3_3,(0.1*V3_3)),0) + 3*43.3*max((Eovc3_3-(0.1*V3_3)),0)
            overprice3 = overAprice3 + overBprice3 + overDprice3 + overCprice3
            #price3 = basic3 + flowsummer3 + discount3 + overprice3
            price3 = basic3 + overprice3
            sameVprice3 += price3
            totalprice3.append(price3) 
            capbilitySetUp.append(V3_1)
            capbilitySetUp2.append(V3_2)
            capbilitySetUp3.append(V3_3)
            capbilitySetUp4.append(V3_4)
        else:
            #基本電費
            basic3 = ( 160.6 * V3_1 + 160.6 * V3_2 + 32.1 * V3_3 * max(( V3_3 + V3_4 - 0.5 * ( V3_1 + V3_2 )),0) ) * 0.98 * 1.15 #非夏月
            #流動電費
            #flowwinter3 = 2.78 * totalflow[k]['B'] + 1.65 * totalflow[k]['D'] + 1.22 * totalflow[k]['C']
            #功率折扣費
            #discount3 = ( basic3 + flowwinter3 ) * (80-95) / 1000 
            #超約附加費
            Eov3_1 = max((maxtotalflow[k]['B']-V3_1),0)
            Eov3_2 = max((maxtotalflow[k]['B']-V3_1-V3_2),0)
            Eov3_4 = max((maxtotalflow[k]['D']-V3_1-V3_2-V3_4),0)
            Eov3_3 = max((maxtotalflow[k]['C']-V3_1-V3_2-V3_4-V3_3),0)

            Eovc3_1 = Eov3_1
            Eovc3_2 = max((Eov3_2-Eovc3_1),0)
            Eovc3_4 = max((Eov3_4-max(Eovc3_1,Eovc3_2)),0)
            Eovc3_3 = max((Eov3_3-max(Eovc3_1,Eovc3_2,Eovc3_4)),0)
        
            overAprice3 = 2*160.6*max(min(Eovc3_1,(0.1*V3_1)),0) + 3*160.6*max((Eovc3_1-(0.1*V3_1)),0)
            overBprice3 = 2*160.6*max(min(Eovc3_2,(0.1*V3_2)),0) + 3*160.6*max((Eovc3_2-(0.1*V3_2)),0) #非夏月
            overDprice3 = 2*43.3*max(min(Eovc3_4,(0.1*V3_4)),0) + 3*43.3*max((Eovc3_4-(0.1*V3_4)),0)
            overCprice3 = 2*43.3*max(min(Eovc3_3,(0.1*V3_3)),0) + 3*43.3*max((Eovc3_3-(0.1*V3_3)),0)
            overprice3 = overAprice3 + overBprice3 + overDprice3 + overCprice3
            #price3 = basic3 + flowsummer3 + discount3 + overprice3
            price3 = basic3 + overprice3
            sameVprice3 += price3
            totalprice3.append(price3) 
            capbilitySetUp.append(V3_1)
            capbilitySetUp2.append(V3_2)
            capbilitySetUp3.append(V3_3)
            capbilitySetUp4.append(V3_4)
    for k in range (int(m3)-1,int(m4)-1):
        if ((totalflow[k]['A'] is not 0) and (maxtotalflow[k]['A'] is not 0)) :
            #基本電費
            basic4 = ( 217.3 * V4_1 + 160.6 * V4_2 + 43.4 * V4_3 * max(( V4_3 + V4_4 - 0.5 * ( V4_1 + V4_2 )),0) ) * 0.98 * 1.15 #夏月
            #流動電費
            #flowsummer4 = 4.61 * totalflow[k]['A'] + 2.87 * totalflow[k]['B']  + 1.73 * totalflow[k]['D'] + 1.29 * totalflow[k]['C']
            #功率折扣費
            #discount4 = ( basic4 + flowsummer4 ) * (80-95) / 1000 
            #超約附加費
            Eov4_1 = max((maxtotalflow[k]['A']-V4_1),0)
            Eov4_2 = max((maxtotalflow[k]['B']-V4_1-V4_2),0)
            Eov4_4 = max((maxtotalflow[k]['D']-V4_1-V4_2-V4_4),0)
            Eov4_3 = max((maxtotalflow[k]['C']-V4_1-V4_2-V4_4-V4_3),0)

            Eovc4_1 = Eov4_1
            Eovc4_2 = max((Eov4_2-Eovc4_1),0)
            Eovc4_4 = max((Eov4_4-max(Eovc4_1,Eovc4_2)),0)
            Eovc4_3 = max((Eov4_3-max(Eovc4_1,Eovc4_2,Eovc4_4)),0)
        
            overAprice4 = 2 * 217.3 * max(min(Eovc4_1,(0.1*V4_1)),0) + 3*217.3*max((Eovc4_1-(0.1*V4_1)),0)  #夏月
            overBprice4 = 2*160.6*max(min(Eovc4_2,(0.1*V4_2)),0) + 3*160.6*max((Eovc4_2-(0.1*V4_2)),0)
            overDprice4 = 2*43.3*max(min(Eovc4_4,(0.1*V4_4)),0) + 3*43.3*max((Eovc4_4-(0.1*V4_4)),0)
            overCprice4 = 2*43.3*max(min(Eovc4_3,(0.1*V4_3)),0) + 3*43.3*max((Eovc4_3-(0.1*V4_3)),0)
            overprice4 = overAprice4 + overBprice4 + overDprice4 + overCprice4
            #price4 = basic4 + flowsummer4 + discount4 + overprice4
            price4 = basic4 + overprice4
            sameVprice4 += price4
            totalprice4.append(price4) 
            capbilitySetUp.append(V4_1)
            capbilitySetUp2.append(V4_2)
            capbilitySetUp3.append(V4_3)
            capbilitySetUp4.append(V4_4)
        else:
            #基本電費
            basic4 = ( 160.6 * V4_1 + 160.6 * V4_2 + 32.1 * V4_3 * max(( V4_3 + V4_4 - 0.5 * ( V4_1 + V4_2 )),0) ) * 0.98 * 1.15 #非夏月
            #流動電費
            #flowwinter4 = 2.78 * totalflow[k]['B'] + 1.65 * totalflow[k]['D'] + 1.22 * totalflow[k]['C']
            #功率折扣費
            #discount4 = ( basic4 + flowwinter4 ) * (80-95) / 1000 
            #超約附加費
            Eov4_1 = max((maxtotalflow[k]['B']-V4_1),0)
            Eov4_2 = max((maxtotalflow[k]['B']-V4_1-V4_2),0)
            Eov4_4 = max((maxtotalflow[k]['D']-V4_1-V4_2-V4_4),0)
            Eov4_3 = max((maxtotalflow[k]['C']-V4_1-V4_2-V4_4-V4_3),0)

            Eovc4_1 = Eov4_1
            Eovc4_2 = max((Eov4_2-Eovc4_1),0)
            Eovc4_4 = max((Eov4_4-max(Eovc4_1,Eovc4_2)),0)
            Eovc4_3 = max((Eov4_3-max(Eovc4_1,Eovc4_2,Eovc4_4)),0)
        
            overAprice4 = 2*160.6*max(min(Eovc4_1,(0.1*V4_1)),0) + 3*160.6*max((Eovc4_1-(0.1*V4_1)),0)
            overBprice4 = 2*160.6*max(min(Eovc4_2,(0.1*V4_2)),0) + 3*160.6*max((Eovc4_2-(0.1*V4_2)),0) #非夏月
            overDprice4 = 2*43.3*max(min(Eovc4_4,(0.1*V4_4)),0) + 3*43.3*max((Eovc4_4-(0.1*V4_4)),0)
            overCprice4 = 2*43.3*max(min(Eovc4_3,(0.1*V4_3)),0) + 3*43.3*max((Eovc4_3-(0.1*V4_3)),0)
            overprice4 = overAprice4 + overBprice4 + overDprice4 + overCprice4
            #price4 = basic4 + flowsummer4 + discount4 + overprice4
            price4 = basic4 + overprice4
            sameVprice4 += price4
            totalprice4.append(price4) 
            capbilitySetUp.append(V4_1)
            capbilitySetUp2.append(V4_2)
            capbilitySetUp3.append(V4_3)
            capbilitySetUp4.append(V4_4)
    for k in range (int(m4)-1,int(m5)-1):
        if ((totalflow[k]['A'] is not 0) and (maxtotalflow[k]['A'] is not 0)) :
            #基本電費
            basic5 = ( 217.3 * V5_1 + 160.6 * V5_2 + 43.4 * V5_3 * max(( V5_3 + V5_4 - 0.5 * ( V5_1 + V5_2 )),0) ) * 0.98 * 1.15 #夏月
            #流動電費
            #flowsummer5 = 4.61 * totalflow[k]['A'] + 2.87 * totalflow[k]['B']  + 1.73 * totalflow[k]['D'] + 1.29 * totalflow[k]['C']
            #功率折扣費
            #discount5 = ( basic5 + flowsummer5 ) * (80-95) / 1000 
            #超約附加費
            Eov5_1 = max((maxtotalflow[k]['A']-V5_1),0)
            Eov5_2 = max((maxtotalflow[k]['B']-V5_1-V5_2),0)
            Eov5_4 = max((maxtotalflow[k]['D']-V5_1-V5_2-V5_4),0)
            Eov5_3 = max((maxtotalflow[k]['C']-V5_1-V5_2-V5_4-V5_3),0)

            Eovc5_1 = Eov5_1
            Eovc5_2 = max((Eov5_2-Eovc5_1),0)
            Eovc5_4 = max((Eov5_4-max(Eovc5_1,Eovc5_2)),0)
            Eovc5_3 = max((Eov5_3-max(Eovc5_1,Eovc5_2,Eovc5_4)),0)
        
            overAprice5 = 2 * 217.3 * max(min(Eovc5_1,(0.1*V5_1)),0) + 3*217.3*max((Eovc5_1-(0.1*V5_1)),0)  #夏月
            overBprice5 = 2*160.6*max(min(Eovc5_2,(0.1*V5_2)),0) + 3*160.6*max((Eovc5_2-(0.1*V5_2)),0)
            overDprice5 = 2*43.3*max(min(Eovc5_4,(0.1*V5_4)),0) + 3*43.3*max((Eovc5_4-(0.1*V5_4)),0)
            overCprice5 = 2*43.3*max(min(Eovc5_3,(0.1*V5_3)),0) + 3*43.3*max((Eovc5_3-(0.1*V5_3)),0)
            overprice5 = overAprice5 + overBprice5 + overDprice5 + overCprice5
            #price5 = basic5 + flowsummer5 + discount5 + overprice5
            price5 = basic5 + overprice5
            sameVprice5 += price5
            totalprice5.append(price5) 
            capbilitySetUp.append(V5_1)
            capbilitySetUp2.append(V5_2)
            capbilitySetUp3.append(V5_3)
            capbilitySetUp4.append(V5_4)
        else:
            #基本電費
            basic5 = ( 160.6 * V5_1 + 160.6 * V5_2 + 32.1 * V5_3 * max(( V5_3 + V5_4 - 0.5 * ( V5_1 + V5_2 )),0) ) * 0.98 * 1.15 #非夏月
            #流動電費
            #flowwinter5 = 2.78 * totalflow[k]['B'] + 1.65 * totalflow[k]['D'] + 1.22 * totalflow[k]['C']
            #功率折扣費
            #discount5 = ( basic5 + flowwinter5 ) * (80-95) / 1000 
            #超約附加費
            Eov5_1 = max((maxtotalflow[k]['B']-V5_1),0)
            Eov5_2 = max((maxtotalflow[k]['B']-V5_1-V5_2),0)
            Eov5_4 = max((maxtotalflow[k]['D']-V5_1-V5_2-V5_4),0)
            Eov5_3 = max((maxtotalflow[k]['C']-V5_1-V5_2-V5_4-V5_3),0)

            Eovc5_1 = Eov5_1
            Eovc5_2 = max((Eov5_2-Eovc5_1),0)
            Eovc5_4 = max((Eov5_4-max(Eovc5_1,Eovc5_2)),0)
            Eovc5_3 = max((Eov5_3-max(Eovc5_1,Eovc5_2,Eovc5_4)),0)
        
            overAprice5 = 2*160.6*max(min(Eovc5_1,(0.1*V5_1)),0) + 3*160.6*max((Eovc5_1-(0.1*V5_1)),0)
            overBprice5 = 2*160.6*max(min(Eovc5_2,(0.1*V5_2)),0) + 3*160.6*max((Eovc5_2-(0.1*V5_2)),0) #非夏月
            overDprice5 = 2*43.3*max(min(Eovc5_4,(0.1*V5_4)),0) + 3*43.3*max((Eovc5_4-(0.1*V5_4)),0)
            overCprice5 = 2*43.3*max(min(Eovc5_3,(0.1*V5_3)),0) + 3*43.3*max((Eovc5_3-(0.1*V5_3)),0)
            overprice5 = overAprice5 + overBprice5 + overDprice5 + overCprice5
            #price5 = basic5 + flowwinter5 + discount5 + overprice5
            price5 = basic5 + overprice5
            sameVprice5 += price5
            totalprice5.append(price5) 
            capbilitySetUp.append(V5_1)
            capbilitySetUp2.append(V5_2)
            capbilitySetUp3.append(V5_3)
            capbilitySetUp4.append(V5_4)
    for k in range (int(m5)-1,int(m6)-1):
        if ((totalflow[k]['A'] is not 0) and (maxtotalflow[k]['A'] is not 0)) :
            #基本電費
            basic6 = ( 217.3 * V6_1 + 160.6 * V6_2 + 43.4 * V6_3 * max(( V6_3 + V6_4 - 0.5 * ( V6_1 + V6_2 )),0) ) * 0.98 * 1.15 #夏月
            #流動電費
            #flowsummer6 = 4.61 * totalflow[k]['A'] + 2.87 * totalflow[k]['B']  + 1.73 * totalflow[k]['D'] + 1.29 * totalflow[k]['C']
            #功率折扣費
            #discount6 = ( basic6 + flowsummer6 ) * (80-95) / 1000 
            #超約附加費
            Eov6_1 = max((maxtotalflow[k]['A']-V6_1),0)
            Eov6_2 = max((maxtotalflow[k]['B']-V6_1-V6_2),0)
            Eov6_4 = max((maxtotalflow[k]['D']-V6_1-V6_2-V6_4),0)
            Eov6_3 = max((maxtotalflow[k]['C']-V6_1-V6_2-V6_4-V6_3),0)

            Eovc6_1 = Eov6_1
            Eovc6_2 = max((Eov6_2-Eovc6_1),0)
            Eovc6_4 = max((Eov6_4-max(Eovc6_1,Eovc6_2)),0)
            Eovc6_3 = max((Eov6_3-max(Eovc6_1,Eovc6_2,Eovc6_4)),0)
        
            overAprice6 = 2 * 217.3 * max(min(Eovc6_1,(0.1*V6_1)),0) + 3*217.3*max((Eovc6_1-(0.1*V6_1)),0)  #夏月
            overBprice6 = 2*160.6*max(min(Eovc6_2,(0.1*V6_2)),0) + 3*160.6*max((Eovc6_2-(0.1*V6_2)),0)
            overDprice6 = 2*43.3*max(min(Eovc6_4,(0.1*V6_4)),0) + 3*43.3*max((Eovc6_4-(0.1*V6_4)),0)
            overCprice6 = 2*43.3*max(min(Eovc6_3,(0.1*V6_3)),0) + 3*43.3*max((Eovc6_3-(0.1*V6_3)),0)
            overprice6 = overAprice6 + overBprice6 + overDprice6 + overCprice6
            #price6 = basic6 + flowsummer6 + discount6 + overprice6
            price6 = basic6 + overprice6
            sameVprice6 += price6
            totalprice6.append(price6) 
            capbilitySetUp.append(V6_1)
            capbilitySetUp2.append(V6_2)
            capbilitySetUp3.append(V6_3)
            capbilitySetUp4.append(V6_4)
        else:
            #基本電費
            basic6 = ( 160.6 * V6_1 + 160.6 * V6_2 + 32.1 * V6_3 * max(( V6_3 + V6_4 - 0.5 * ( V6_1 + V6_2 )),0) ) * 0.98 * 1.15 #非夏月
            #流動電費
            #flowwinter6 = 2.78 * totalflow[k]['B'] + 1.65 * totalflow[k]['D'] + 1.22 * totalflow[k]['C']
            #功率折扣費
            #discount6 = ( basic6 + flowwinter6 ) * (80-95) / 1000 
            #超約附加費
            Eov6_1 = max((maxtotalflow[k]['B']-V6_1),0)
            Eov6_2 = max((maxtotalflow[k]['B']-V6_1-V6_2),0)
            Eov6_4 = max((maxtotalflow[k]['D']-V6_1-V6_2-V6_4),0)
            Eov6_3 = max((maxtotalflow[k]['C']-V6_1-V6_2-V6_4-V6_3),0)

            Eovc6_1 = Eov6_1
            Eovc6_2 = max((Eov6_2-Eovc6_1),0)
            Eovc6_4 = max((Eov6_4-max(Eovc6_1,Eovc6_2)),0)
            Eovc6_3 = max((Eov6_3-max(Eovc6_1,Eovc6_2,Eovc6_4)),0)
        
            overAprice6 = 2*160.6*max(min(Eovc6_1,(0.1*V6_1)),0) + 3*160.6*max((Eovc6_1-(0.1*V6_1)),0)
            overBprice6 = 2*160.6*max(min(Eovc6_2,(0.1*V6_2)),0) + 3*160.6*max((Eovc6_2-(0.1*V6_2)),0) #非夏月
            overDprice6 = 2*43.3*max(min(Eovc6_4,(0.1*V6_4)),0) + 3*43.3*max((Eovc6_4-(0.1*V6_4)),0)
            overCprice6 = 2*43.3*max(min(Eovc6_3,(0.1*V6_3)),0) + 3*43.3*max((Eovc6_3-(0.1*V6_3)),0)
            overprice6 = overAprice6 + overBprice6 + overDprice6 + overCprice6
            #price6 = basic6 + flowwinter6 + discount6 + overprice6
            price6 = basic6 + overprice6
            sameVprice6 += price6
            totalprice6.append(price6) 
            capbilitySetUp.append(V6_1)
            capbilitySetUp2.append(V6_2)
            capbilitySetUp3.append(V6_3)
            capbilitySetUp4.append(V6_4)
    for k in range (int(m6)-1,int(m7)-1):
        if ((totalflow[k]['A'] is not 0) and (maxtotalflow[k]['A'] is not 0)) :
            #基本電費
            basic7 = ( 217.3 * V7_1 + 160.6 * V7_2 + 43.4 * V7_3 * max(( V7_3 + V7_4 - 0.5 * ( V7_1 + V7_2 )),0) ) * 0.98 * 1.15 #夏月
            #流動電費
            #flowsummer7 = 4.61 * totalflow[k]['A'] + 2.87 * totalflow[k]['B']  + 1.73 * totalflow[k]['D'] + 1.29 * totalflow[k]['C']
            #功率折扣費
            #discount7 = ( basic7 + flowsummer7 ) * (80-95) / 1000 
            #超約附加費
            Eov7_1 = max((maxtotalflow[k]['A']-V7_1),0)
            Eov7_2 = max((maxtotalflow[k]['B']-V7_1-V7_2),0)
            Eov7_4 = max((maxtotalflow[k]['D']-V7_1-V7_2-V7_4),0)
            Eov7_3 = max((maxtotalflow[k]['C']-V7_1-V7_2-V7_4-V7_3),0)

            Eovc7_1 = Eov7_1
            Eovc7_2 = max((Eov7_2-Eovc7_1),0)
            Eovc7_4 = max((Eov7_4-max(Eovc7_1,Eovc7_2)),0)
            Eovc7_3 = max((Eov7_3-max(Eovc7_1,Eovc7_2,Eovc7_4)),0)
        
            overAprice7 = 2 * 217.3 * max(min(Eovc7_1,(0.1*V7_1)),0) + 3*217.3*max((Eovc7_1-(0.1*V7_1)),0)  #夏月
            overBprice7 = 2*160.6*max(min(Eovc7_2,(0.1*V7_2)),0) + 3*160.6*max((Eovc7_2-(0.1*V7_2)),0)
            overDprice7 = 2*43.3*max(min(Eovc7_4,(0.1*V7_4)),0) + 3*43.3*max((Eovc7_4-(0.1*V7_4)),0)
            overCprice7 = 2*43.3*max(min(Eovc7_3,(0.1*V7_3)),0) + 3*43.3*max((Eovc7_3-(0.1*V7_3)),0)
            overprice7 = overAprice7 + overBprice7 + overDprice7 + overCprice7
            #price7 = basic7 + flowsummer7 + discount7 + overprice7
            price7 = basic7 + overprice7
            sameVprice7 += price7
            totalprice7.append(price7) 
            capbilitySetUp.append(V7_1)
            capbilitySetUp2.append(V7_2)
            capbilitySetUp3.append(V7_3)
            capbilitySetUp4.append(V7_4)
        else:
            #基本電費
            basic7 = ( 160.6 * V7_1 + 160.6 * V7_2 + 32.1 * V7_3 * max(( V7_3 + V7_4 - 0.5 * ( V7_1 + V7_2 )),0) ) * 0.98 * 1.15 #非夏月
            #流動電費
            #flowwinter7 = 2.78 * totalflow[k]['B'] + 1.65 * totalflow[k]['D'] + 1.22 * totalflow[k]['C']
            #功率折扣費
            #discount7 = ( basic7 + flowwinter7 ) * (80-95) / 1000 
            #超約附加費
            Eov7_1 = max((maxtotalflow[k]['B']-V7_1),0)
            Eov7_2 = max((maxtotalflow[k]['B']-V7_1-V7_2),0)
            Eov7_4 = max((maxtotalflow[k]['D']-V7_1-V7_2-V7_4),0)
            Eov7_3 = max((maxtotalflow[k]['C']-V7_1-V7_2-V7_4-V7_3),0)

            Eovc7_1 = Eov7_1
            Eovc7_2 = max((Eov7_2-Eovc7_1),0)
            Eovc7_4 = max((Eov7_4-max(Eovc7_1,Eovc7_2)),0)
            Eovc7_3 = max((Eov7_3-max(Eovc7_1,Eovc7_2,Eovc7_4)),0)
        
            overAprice7 = 2*160.6*max(min(Eovc7_1,(0.1*V7_1)),0) + 3*160.6*max((Eovc7_1-(0.1*V7_1)),0)
            overBprice7 = 2*160.6*max(min(Eovc7_2,(0.1*V7_2)),0) + 3*160.6*max((Eovc7_2-(0.1*V7_2)),0) #非夏月
            overDprice7 = 2*43.3*max(min(Eovc7_4,(0.1*V7_4)),0) + 3*43.3*max((Eovc7_4-(0.1*V7_4)),0)
            overCprice7 = 2*43.3*max(min(Eovc7_3,(0.1*V7_3)),0) + 3*43.3*max((Eovc7_3-(0.1*V7_3)),0)
            overprice7 = overAprice7 + overBprice7 + overDprice7 + overCprice7
            #price7 = basic7 + flowwinter7 + discount7 + overprice7
            price7 = basic7 + overprice7
            sameVprice7 += price7
            totalprice7.append(price7) 
            capbilitySetUp.append(V7_1)
            capbilitySetUp2.append(V7_2)
            capbilitySetUp3.append(V7_3)
            capbilitySetUp4.append(V7_4)
    for k in range (int(m7)-1,int(m8)-1):
        if ((totalflow[k]['A'] is not 0) and (maxtotalflow[k]['A'] is not 0)) :
            #基本電費
            basic8 = ( 217.3 * V8_1 + 160.6 * V8_2 + 43.4 * V8_3 * max(( V8_3 + V8_4 - 0.5 * ( V8_1 + V8_2 )),0) ) * 0.98 * 1.15 #夏月
            #流動電費
            #flowsummer8 = 4.61 * totalflow[k]['A'] + 2.87 * totalflow[k]['B']  + 1.73 * totalflow[k]['D'] + 1.29 * totalflow[k]['C']
            #功率折扣費
            #discount8 = ( basic8 + flowsummer8 ) * (80-95) / 1000 
            #超約附加費
            Eov8_1 = max((maxtotalflow[k]['A']-V8_1),0)
            Eov8_2 = max((maxtotalflow[k]['B']-V8_1-V8_2),0)
            Eov8_4 = max((maxtotalflow[k]['D']-V8_1-V8_2-V8_4),0)
            Eov8_3 = max((maxtotalflow[k]['C']-V8_1-V8_2-V8_4-V8_3),0)

            Eovc8_1 = Eov8_1
            Eovc8_2 = max((Eov8_2-Eovc8_1),0)
            Eovc8_4 = max((Eov8_4-max(Eovc8_1,Eovc8_2)),0)
            Eovc8_3 = max((Eov8_3-max(Eovc8_1,Eovc8_2,Eovc8_4)),0)
    
            overAprice8 = 2 * 217.3 * max(min(Eovc8_1,(0.1*V8_1)),0) + 3*217.3*max((Eovc8_1-(0.1*V8_1)),0)  #夏月
            overBprice8 = 2*160.6*max(min(Eovc8_2,(0.1*V8_2)),0) + 3*160.6*max((Eovc8_2-(0.1*V8_2)),0)
            overDprice8 = 2*43.3*max(min(Eovc8_4,(0.1*V8_4)),0) + 3*43.3*max((Eovc8_4-(0.1*V8_4)),0)
            overCprice8 = 2*43.3*max(min(Eovc8_3,(0.1*V8_3)),0) + 3*43.3*max((Eovc8_3-(0.1*V8_3)),0)
            overprice8 = overAprice8 + overBprice8 + overDprice8 + overCprice8
            #price8 = basic8 + flowsummer8 + discount8 + overprice8
            price8 = basic8 + overprice8
            sameVprice8 += price8
            totalprice8.append(price8) 
            capbilitySetUp.append(V8_1)
            capbilitySetUp2.append(V8_2)
            capbilitySetUp3.append(V8_3)
            capbilitySetUp4.append(V8_4)
        else:
            #基本電費
            basic8 = ( 160.6 * V8_1 + 160.6 * V8_2 + 32.1 * V8_3 * max(( V8_3 + V8_4 - 0.5 * ( V8_1 + V8_2 )),0) ) * 0.98 * 1.15 #非夏月
            #流動電費
            #flowwinter8 = 2.78 * totalflow[k]['B'] + 1.65 * totalflow[k]['D'] + 1.22 * totalflow[k]['C']
            #功率折扣費
            #discount8 = ( basic8 + flowwinter8 ) * (80-95) / 1000 
            #超約附加費
            Eov8_1 = max((maxtotalflow[k]['B']-V8_1),0)
            Eov8_2 = max((maxtotalflow[k]['B']-V8_1-V8_2),0)
            Eov8_4 = max((maxtotalflow[k]['D']-V8_1-V8_2-V8_4),0)
            Eov8_3 = max((maxtotalflow[k]['C']-V8_1-V8_2-V8_4-V8_3),0)

            Eovc8_1 = Eov8_1
            Eovc8_2 = max((Eov8_2-Eovc8_1),0)
            Eovc8_4 = max((Eov8_4-max(Eovc8_1,Eovc8_2)),0)
            Eovc8_3 = max((Eov8_3-max(Eovc8_1,Eovc8_2,Eovc8_4)),0)
        
            overAprice8 = 2*160.6*max(min(Eovc8_1,(0.1*V8_1)),0) + 3*160.6*max((Eovc8_1-(0.1*V8_1)),0)
            overBprice8 = 2*160.6*max(min(Eovc8_2,(0.1*V8_2)),0) + 3*160.6*max((Eovc8_2-(0.1*V8_2)),0) #非夏月
            overDprice8 = 2*43.3*max(min(Eovc8_4,(0.1*V8_4)),0) + 3*43.3*max((Eovc8_4-(0.1*V8_4)),0)
            overCprice8 = 2*43.3*max(min(Eovc8_3,(0.1*V8_3)),0) + 3*43.3*max((Eovc8_3-(0.1*V8_3)),0)
            overprice8 = overAprice8 + overBprice8 + overDprice8 + overCprice8
            #price8 = basic8 + flowwinter8 + discount8 + overprice8
            price8 = basic8 + overprice8
            sameVprice8 += price8
            totalprice8.append(price8) 
            capbilitySetUp.append(V8_1)
            capbilitySetUp2.append(V8_2)
            capbilitySetUp3.append(V8_3)
            capbilitySetUp4.append(V8_4)
    for k in range (int(m8)-1,24):
        if ((totalflow[k]['A'] is not 0) and (maxtotalflow[k]['A'] is not 0)) :
            #基本電費
            basic9 = ( 217.3 * V9_1 + 160.6 * V9_2 + 43.4 * V9_3 * max(( V9_3 + V9_4 - 0.5 * ( V9_1 + V9_2 )),0) ) * 0.98 * 1.15 #夏月
            #流動電費
            #flowsummer9 = 4.61 * totalflow[k]['A'] + 2.87 * totalflow[k]['B']  + 1.73 * totalflow[k]['D'] + 1.29 * totalflow[k]['C']
            #功率折扣費
            #discount9 = ( basic9 + flowsummer9 ) * (80-95) / 1000 
            #超約附加費
            Eov9_1 = max((maxtotalflow[k]['A']-V9_1),0)
            Eov9_2 = max((maxtotalflow[k]['B']-V9_1-V9_2),0)
            Eov9_4 = max((maxtotalflow[k]['D']-V9_1-V9_2-V9_4),0)
            Eov9_3 = max((maxtotalflow[k]['C']-V9_1-V9_2-V9_4-V9_3),0)

            Eovc9_1 = Eov9_1
            Eovc9_2 = max((Eov9_2-Eovc9_1),0)
            Eovc9_4 = max((Eov9_4-max(Eovc9_1,Eovc9_2)),0)
            Eovc9_3 = max((Eov9_3-max(Eovc9_1,Eovc9_2,Eovc9_4)),0)
    
            overAprice9 = 2 * 217.3 * max(min(Eovc9_1,(0.1*V9_1)),0) + 3*217.3*max((Eovc9_1-(0.1*V9_1)),0)  #夏月
            overBprice9 = 2*160.6*max(min(Eovc9_2,(0.1*V9_2)),0) + 3*160.6*max((Eovc9_2-(0.1*V9_2)),0)
            overDprice9 = 2*43.3*max(min(Eovc9_4,(0.1*V9_4)),0) + 3*43.3*max((Eovc9_4-(0.1*V9_4)),0)
            overCprice9 = 2*43.3*max(min(Eovc9_3,(0.1*V9_3)),0) + 3*43.3*max((Eovc9_3-(0.1*V9_3)),0)
            overprice9 = overAprice9 + overBprice9 + overDprice9 + overCprice9
            #price9 = basic9 + flowsummer9 + discount9 + overprice9
            price9 = basic9 + overprice9
            sameVprice9 += price9
            totalprice9.append(price9) 
            capbilitySetUp.append(V9_1)
            capbilitySetUp2.append(V9_2)
            capbilitySetUp3.append(V9_3)
            capbilitySetUp4.append(V9_4)
        else:
            #基本電費
            basic9 = ( 160.6 * V9_1 + 160.6 * V9_2 + 32.1 * V9_3 * max(( V9_3 + V9_4 - 0.5 * ( V9_1 + V9_2 )),0) ) * 0.98 * 1.15 #非夏月
            #流動電費
            #flowwinter9 = 2.78 * totalflow[k]['B'] + 1.65 * totalflow[k]['D'] + 1.22 * totalflow[k]['C']
            #功率折扣費
            #discount9 = ( basic9 + flowwinter9 ) * (80-95) / 1000 
            #超約附加費
            Eov9_1 = max((maxtotalflow[k]['B']-V9_1),0)
            Eov9_2 = max((maxtotalflow[k]['B']-V9_1-V9_2),0)
            Eov9_4 = max((maxtotalflow[k]['D']-V9_1-V9_2-V9_4),0)
            Eov9_3 = max((maxtotalflow[k]['C']-V9_1-V9_2-V9_4-V9_3),0)

            Eovc9_1 = Eov9_1
            Eovc9_2 = max((Eov9_2-Eovc9_1),0)
            Eovc9_4 = max((Eov9_4-max(Eovc9_1,Eovc9_2)),0)
            Eovc9_3 = max((Eov9_3-max(Eovc9_1,Eovc9_2,Eovc9_4)),0)
        
            overAprice9 = 2*160.6*max(min(Eovc9_1,(0.1*V9_1)),0) + 3*160.6*max((Eovc9_1-(0.1*V9_1)),0)
            overBprice9 = 2*160.6*max(min(Eovc9_2,(0.1*V9_2)),0) + 3*160.6*max((Eovc9_2-(0.1*V9_2)),0) #非夏月
            overDprice9 = 2*43.3*max(min(Eovc9_4,(0.1*V9_4)),0) + 3*43.3*max((Eovc9_4-(0.1*V9_4)),0)
            overCprice9 = 2*43.3*max(min(Eovc9_3,(0.1*V9_3)),0) + 3*43.3*max((Eovc9_3-(0.1*V9_3)),0)
            overprice9 = overAprice9 + overBprice9 + overDprice9 + overCprice9
            #price9 = basic9 + flowwinter9 + discount9 + overprice9
            price9 = basic9 + overprice9
            sameVprice9 += price9
            totalprice9.append(price9) 
            capbilitySetUp.append(V9_1)
            capbilitySetUp2.append(V9_2)
            capbilitySetUp3.append(V9_3)
            capbilitySetUp4.append(V9_4)
    # #standard = V1_1 - 5000
    # standard = V1_1        
    # #容量設置費_1
    # spareSetUp = []
    # setupEachMonth = []
    # for i in range(0, 23):
    #     lessThanStandard = 0
    #     overThanStandard = 0
    #     if capbilitySetUp[i+1] > capbilitySetUp[i]:
    #         if capbilitySetUp[i+1] <= standard:
    #             lessThanStandard += (capbilitySetUp[i+1] - capbilitySetUp[i])
    #         else:
    #             lessThanStandard += (standard - capbilitySetUp[i])
    #             overThanStandard += (capbilitySetUp[i+1] - standard)
    #             standard = capbilitySetUp[i+1]
    #     spareSetUp.append(1050*lessThanStandard*0.25)
    #     setupEachMonth.append(1050*lessThanStandard*0.5 + 1050*overThanStandard)
    # delet=[]
    # setupEachMonth=np.array(setupEachMonth)
    # spareSetUp=np.array(spareSetUp)
    # for r in range(len(setupEachMonth)):
    #     if ((setupEachMonth[r]==0) and (spareSetUp[r]==0)) :
    #         delet.append(r)
    # spareSetUp=np.delete(spareSetUp,delet,axis=0)
    # setupEachMonth=np.delete(setupEachMonth,delet,axis=0)
    # spareSetUp=spareSetUp.tolist()
    # setupEachMonth=setupEachMonth.tolist()
    #容量設置費_1
    spareSetUp = []
    setupEachMonth = []
    cou_da = 3000
    for i in range(0, len(capbilitySetUp)-1):
        if capbilitySetUp[i+1] > capbilitySetUp[i]:
            if (capbilitySetUp[i+1] - capbilitySetUp[i]) >= cou_da:
                cou_da = 0
                spareSetUp.append(0.15*1050*(capbilitySetUp[i+1] - capbilitySetUp[i]))
                setupEachMonth.append(1050*(capbilitySetUp[i+1] - capbilitySetUp[i]))
            else:
                cou_da -= (capbilitySetUp[i+1] - capbilitySetUp[i])
                spareSetUp.append(0.25*1050*(capbilitySetUp[i+1] - capbilitySetUp[i]))
                setupEachMonth.append(0.5*1050*(capbilitySetUp[i+1] - capbilitySetUp[i]))
        else: 
            cou_da += (capbilitySetUp[i+1] - capbilitySetUp[i])
            spareSetUp.append(0)
            setupEachMonth.append(0)
    delet=[]
    setupEachMonth=np.array(setupEachMonth)
    spareSetUp=np.array(spareSetUp)
    for r in range(len(setupEachMonth)):
        if ((setupEachMonth[r]==0) and (spareSetUp[r]==0)) :
            delet.append(r)
    spareSetUp=np.delete(spareSetUp,delet,axis=0)
    setupEachMonth=np.delete(setupEachMonth,delet,axis=0)
    spareSetUp=spareSetUp.tolist()
    setupEachMonth=setupEachMonth.tolist()
    #設備維持費_1
    #做表格
    remainTotalPrice = 0
    remainPrice = []
    remainPosition = []
    upperTotalPrice = 0 
    upperPrice = []
    upperPosition = []   
    nonChangeMonthPosition = []
    for i in range(0, len(capbilitySetUp)-1):
        if capbilitySetUp[i+1] > capbilitySetUp[i]:
            upperPosition.append(i+1)
            upperPrice.append(capbilitySetUp[i+1] - capbilitySetUp[i])
            upperTotalPrice += (capbilitySetUp[i+1] - capbilitySetUp[i]) # > 0
        elif capbilitySetUp[i+1] < capbilitySetUp[i] :
            remainPosition.append(i+1)
            remainPrice.append(capbilitySetUp[i+1] - capbilitySetUp[i])
            remainTotalPrice += (capbilitySetUp[i+1] - capbilitySetUp[i]) # < 0
        else :
            nonChangeMonthPosition.append(i+1)  # = 0   
    #算價錢
    bonusPrice = 0
    overPrice = 0
    spareMaintain = []
    maintainEachMonth = []
    temporary = []
    temporary_spare = []
    x = 0
    y = 0
    while len(upperPosition) > x and len(remainPosition) > y :
    #while remainTotalPrice != 0 and upperTotalPrice != 0:
        #eachBonusPrice = 0
        eachOverPrice = 0
        month_can_remain = 0
        month_cant_remain = 0
        spare = 0
        if upperPosition[x] > remainPosition[y] :
            if upperPrice[x] > (-remainPrice[y]):
                month_can_remain = 176*(-remainPrice[y])*(upperPosition[x] - remainPosition[y])
                spare = month_can_remain*0.15
                temporary.append(month_can_remain)
                temporary_spare.append(spare)
                #bonusPrice += (-remainPrice[y])*(upperPosition[x] - remainPosition[y])
                remainTotalPrice = remainTotalPrice - remainPrice[y]
                upperTotalPrice = upperTotalPrice + remainPrice[y]
                upperPrice[x] = upperPrice[x] + remainPrice[y]
                y+=1
            else:
                month_can_remain = 176*upperPrice[x]*(upperPosition[x] - remainPosition[y])
                spare = month_can_remain*0.15
                if temporary :
                    month_can_remain = sum(temporary) + month_can_remain
                    maintainEachMonth.append(month_can_remain)
                    spare = sum(temporary_spare) + spare
                    spareMaintain.append(spare)
                    temporary.clear()
                    temporary_spare.clear()
                else :
                    maintainEachMonth.append(month_can_remain)
                    spareMaintain.append(spare)
                #bonusPrice += upperPrice[x]*(upperPosition[x] - remainPosition[y])
                remainTotalPrice = remainTotalPrice + upperPrice[x]
                upperTotalPrice = upperTotalPrice - upperPrice[x]
                remainPrice[y] = upperPrice[x] + remainPrice[y]
                x+=1
        else:
            overPrice += upperPrice[x]
            upperTotalPrice = upperTotalPrice - upperPrice[x]
            eachOverPrice = upperPrice[x]
            month_cant_remain = eachOverPrice*1050
            spare = month_cant_remain*0.15
            if temporary :
                month_cant_remain = sum(temporary) + month_cant_remain
                maintainEachMonth.append(month_cant_remain)
                spare = sum(temporary_spare) + spare
                spareMaintain.append(spare)
                temporary.clear()
                temporary_spare.clear()
            else :
                maintainEachMonth.append(month_cant_remain)
                spareMaintain.append(spare)
            x+=1
    while len(upperPosition) > x :
        monthcantremain = upperPrice[x] * 1050
        sparemonthcantremain = monthcantremain *0.15
        if temporary :
                monthcantremain = sum(temporary) + monthcantremain
                maintainEachMonth.append(monthcantremain)
                sparemonthcantremain = sum(temporary_spare) + sparemonthcantremain
                spareMaintain.append(sparemonthcantremain)
                temporary.clear()
                temporary_spare.clear()
        else :
            maintainEachMonth.append(monthcantremain)
            spareMaintain.append(sparemonthcantremain)
        x+=1
    
    if upperTotalPrice != 0:
        overPrice += upperTotalPrice
    recover = []
    #if len(setupEachMonth)==len(maintainEachMonth):
    for w1 in range(len(setupEachMonth)) :
        if setupEachMonth[w1] <= maintainEachMonth[w1] :
            recover.append(setupEachMonth[w1])
        else :
            recover.append(maintainEachMonth[w1])
    totalrecover = sum(recover)
    sparerecover = []
    #if len(spareSetUp)==len(spareMaintain):
    for v1 in range(len(spareSetUp)) :
        if spareSetUp[v1] <= spareMaintain[v1] :
            sparerecover.append(spareSetUp[v1])
        else :
            sparerecover.append(spareMaintain[v1])
    totalsparerecover = sum(sparerecover)
    cover = totalrecover + totalsparerecover
    
    standard2 = V1_2
    #容量設置費_2
    spareSetUp2 = []
    setupEachMonth2 = []
    for i in range(0, 23):
        lessThanStandard2 = 0
        overThanStandard2 = 0
        if capbilitySetUp2[i+1] > capbilitySetUp2[i]:
            if capbilitySetUp2[i+1] <= standard2:
                lessThanStandard2 += (capbilitySetUp2[i+1] - capbilitySetUp2[i])
            else:
                lessThanStandard2 += (standard2 - capbilitySetUp2[i])
                overThanStandard2 += (capbilitySetUp2[i+1] - standard2)
                standard2 = capbilitySetUp2[i+1]
        spareSetUp2.append(787.5*lessThanStandard2*0.25)
        setupEachMonth2.append(787.5*lessThanStandard2*0.5 + 787.5*overThanStandard2)
    delet2=[]
    setupEachMonth2=np.array(setupEachMonth2)
    spareSetUp2=np.array(spareSetUp2)
    for r in range(len(setupEachMonth2)):
        if setupEachMonth2[r]==0 and spareSetUp2[r]==0 :
            delet2.append(r)
    spareSetUp2=np.delete(spareSetUp2,delet2,axis=0)
    setupEachMonth2=np.delete(setupEachMonth2,delet2,axis=0)
    spareSetUp2=spareSetUp2.tolist()
    setupEachMonth2=setupEachMonth2.tolist()
    #設備維持費_2
    #做表格
    remainTotalPrice2 = 0
    remainPrice2 = []
    remainPosition2 = []
    upperTotalPrice2 = 0 
    upperPrice2 = []
    upperPosition2 = []   
    nonChangeMonthPosition2 = []
    for i in range(0, 23):
        if capbilitySetUp2[i+1] > capbilitySetUp2[i]:
            upperPosition2.append(i+1)
            upperPrice2.append(capbilitySetUp2[i+1] - capbilitySetUp2[i])
            upperTotalPrice2 += (capbilitySetUp2[i+1] - capbilitySetUp2[i]) # > 0
        elif capbilitySetUp2[i+1] < capbilitySetUp2[i] :
            remainPosition2.append(i+1)
            remainPrice2.append(capbilitySetUp2[i+1] - capbilitySetUp2[i])
            remainTotalPrice2 += (capbilitySetUp2[i+1] - capbilitySetUp2[i]) # < 0
        else :
            nonChangeMonthPosition2.append(i+1)  # = 0  
    #算價錢
    bonusPrice2 = 0
    overPrice2 = 0
    spareMaintain2 = []
    maintainEachMonth2 = []
    temporary2 = []
    temporary2_spare2 = []
    x2 = 0
    y2 = 0
    while len(upperPosition2) > x2 and len(remainPosition2) > y2 :
    #while remainTotalPrice2 != 0 and upperTotalPrice2 != 0:
        #eachBonusPrice2 = 0
        eachOverPrice2 = 0
        month_can_remain2 = 0
        month_cant_remain2 = 0
        spare2 = 0
        if upperPosition2[x2] > remainPosition2[y2] :
            if upperPrice2[x2] > (-remainPrice2[y2]):
                month_can_remain2 = 132*(-remainPrice2[y2])*(upperPosition2[x2] - remainPosition2[y2])
                spare2 = month_can_remain2*0.15
                temporary2.append(month_can_remain2)
                temporary2_spare2.append(spare2)
                bonusPrice2 += (-remainPrice2[y2])*(upperPosition2[x2] - remainPosition2[y2])
                remainTotalPrice2 = remainTotalPrice2 - remainPrice2[y2]
                upperTotalPrice2 = upperTotalPrice2 + remainPrice2[y2]
                upperPrice2[x2] = upperPrice2[x2] + remainPrice2[y2]
                y2+=1
            else:
                month_can_remain2 = 132*upperPrice2[x2]*(upperPosition2[x2] - remainPosition2[y2])
                spare2 = month_can_remain2*0.15
                if temporary2 :
                    month_can_remain2 = sum(temporary2) + month_can_remain2
                    maintainEachMonth2.append(month_can_remain2)
                    spare2 = sum(temporary2_spare2) + spare2
                    spareMaintain2.append(spare2)
                    temporary2.clear()
                    temporary2_spare2.clear()
                else :
                    maintainEachMonth2.append(month_can_remain2)
                    spareMaintain2.append(spare2)
                bonusPrice2 += upperPrice2[x2]*(upperPosition2[x2] - remainPosition2[y2])
                remainTotalPrice2 = remainTotalPrice2 + upperPrice2[x2]
                upperTotalPrice2 = upperTotalPrice2 - upperPrice2[x2]
                remainPrice2[y2] = upperPrice2[x2] + remainPrice2[y2]
                x2+=1
        else:
            overPrice2 += upperPrice2[x2]
            upperTotalPrice2 = upperTotalPrice2 - upperPrice2[x2]
            eachOverPrice2 = upperPrice2[x2]
            month_cant_remain2 = eachOverPrice2*787.5
            spare2 = month_cant_remain2*0.15
            if temporary2 :
                month_cant_remain2 = sum(temporary2) + month_cant_remain2
                maintainEachMonth2.append(month_cant_remain2)
                spare2 = sum(temporary2_spare2) + spare2
                spareMaintain2.append(spare2)
                temporary2.clear()
                temporary2_spare2.clear()
            else :
                maintainEachMonth2.append(month_cant_remain2)
                spareMaintain2.append(spare2)
            x2+=1
    while len(upperPosition2) > x2 :
        monthcantremain2 = upperPrice2[x2] * 787.5
        sparemonthcantremain2 = monthcantremain2 *0.15
        if temporary2 :
                monthcantremain2 = sum(temporary2) + monthcantremain2
                maintainEachMonth2.append(monthcantremain2)
                sparemonthcantremain2 = sum(temporary2_spare2) + sparemonthcantremain2
                spareMaintain2.append(sparemonthcantremain2)
                temporary2.clear()
                temporary2_spare2.clear()
        else :
            maintainEachMonth2.append(monthcantremain2)
            spareMaintain2.append(sparemonthcantremain2)
        x2+=1
    if upperTotalPrice2 != 0:
        overPrice2 += upperTotalPrice2
    recover2 = []
    # if len(setupEachMonth2)==len(maintainEachMonth2):
    for w2 in range(len(setupEachMonth2)) :
        if setupEachMonth2[w2] <= maintainEachMonth2[w2] :
            recover2.append(setupEachMonth2[w2])
        else :
            recover2.append(maintainEachMonth2[w2])
    recover2 = sum(recover2)
    sparerecover2 = []
    #if len(spareSetUp2)==len(spareMaintain2):
    for v2 in range(len(spareSetUp2)) :
        if spareSetUp2[v2] <= spareMaintain2[v2] :
            sparerecover2.append(spareSetUp2[v2])
        else :
            sparerecover2.append(spareMaintain2[v2])
    sparerecover2 = sum(sparerecover2)
    cover2 = recover2 + sparerecover2

    standard3 = V1_3
    #容量設置費_3
    spareSetUp3 = []
    setupEachMonth3 = []
    for i in range(0, 23):
        lessThanStandard3 = 0
        overThanStandard3 = 0
        if capbilitySetUp3[i+1] > capbilitySetUp3[i]:
            if capbilitySetUp3[i+1] <= standard3:
                lessThanStandard3 += (capbilitySetUp3[i+1] - capbilitySetUp3[i])
            else:
                lessThanStandard3 += (standard3 - capbilitySetUp3[i])
                overThanStandard3 += (capbilitySetUp3[i+1] - standard3)
                standard3 = capbilitySetUp3[i+1]
        spareSetUp3.append(210*lessThanStandard3*0.25)
        setupEachMonth3.append(210*lessThanStandard3*0.5 + 210*overThanStandard3)
    delet3=[]
    setupEachMonth3=np.array(setupEachMonth3)
    spareSetUp3=np.array(spareSetUp3)
    for r in range(len(setupEachMonth3)):
        if setupEachMonth3[r]==0 and spareSetUp3[r]==0 :
            delet3.append(r)
    spareSetUp3=np.delete(spareSetUp3,delet3,axis=0)
    setupEachMonth3=np.delete(setupEachMonth3,delet3,axis=0)
    spareSetUp3=spareSetUp3.tolist()
    setupEachMonth3=setupEachMonth3.tolist()
    #設備維持費_3
    #做表格
    remainTotalPrice3 = 0
    remainPrice3 = []
    remainPosition3 = []
    upperTotalPrice3 = 0 
    upperPrice3 = []
    upperPosition3 = []   
    nonChangeMonthPosition3 = []
    for i in range(0, 23):
        if capbilitySetUp3[i+1] > capbilitySetUp3[i]:
            upperPosition3.append(i+1)
            upperPrice3.append(capbilitySetUp3[i+1] - capbilitySetUp3[i])
            upperTotalPrice3 += (capbilitySetUp3[i+1] - capbilitySetUp3[i]) # > 0
        elif capbilitySetUp3[i+1] < capbilitySetUp3[i] :
            remainPosition3.append(i+1)
            remainPrice3.append(capbilitySetUp3[i+1] - capbilitySetUp3[i])
            remainTotalPrice3 += (capbilitySetUp3[i+1] - capbilitySetUp3[i]) # < 0
        else :
            nonChangeMonthPosition3.append(i+1)  # = 0
    #算價錢
    bonusPrice3 = 0
    overPrice3 = 0
    spareMaintain3 = []
    maintainEachMonth3 = []
    temporary3 = []
    temporary3_spare3 = []
    x3 = 0
    y3 = 0
    while len(upperPosition3) > x3 and len(remainPosition3) > y3 :
    #while remainTotalPrice3 != 0 and upperTotalPrice3 != 0:
        #eachBonusPrice = 0
        eachOverPrice3 = 0
        month_can_remain3 = 0
        month_cant_remain3 = 0
        spare3 = 0
        if upperPosition3[x3] > remainPosition3[y3] :
            if upperPrice3[x3] > (-remainPrice3[y3]):
                month_can_remain3 = 35.2*(-remainPrice3[y3])*(upperPosition3[x3] - remainPosition3[y3])
                spare3 = month_can_remain3*0.15
                temporary3.append(month_can_remain3)
                temporary3_spare3.append(spare3)
                bonusPrice3 += (-remainPrice3[y3])*(upperPosition3[x3] - remainPosition3[y3])
                remainTotalPrice3 = remainTotalPrice3 - remainPrice3[y3]
                upperTotalPrice3 = upperTotalPrice3 + remainPrice3[y3]
                upperPrice3[x3] = upperPrice3[x3] + remainPrice3[y3]
                y3+=1
            else:
                month_can_remain3 = 35.2*upperPrice3[x3]*(upperPosition3[x3] - remainPosition3[y3])
                spare3 = month_can_remain3*0.15
                if temporary3 :
                    month_can_remain3 = sum(temporary3) + month_can_remain3
                    maintainEachMonth3.append(month_can_remain3)
                    spare3 = sum(temporary3_spare3) + spare3
                    spareMaintain3.append(spare3)
                    temporary3.clear()
                    temporary3_spare3.clear()
                else :
                    maintainEachMonth3.append(month_can_remain3)
                    spareMaintain3.append(spare3)
                bonusPrice3 += upperPrice3[x3]*(upperPosition3[x3] - remainPosition3[y3])
                remainTotalPrice3 = remainTotalPrice3 + upperPrice3[x3]
                upperTotalPrice3 = upperTotalPrice3 - upperPrice3[x3]
                remainPrice3[y3] = upperPrice3[x3] + remainPrice3[y3]
                x3+=1
        else:
            overPrice3 += upperPrice3[x3]
            upperTotalPrice3 = upperTotalPrice3 - upperPrice3[x3]
            eachOverPrice3 = upperPrice3[x3]
            month_cant_remain3 = eachOverPrice3*210
            spare3 = month_cant_remain3*0.15
            if temporary3 :
                month_cant_remain3 = sum(temporary3) + month_cant_remain3
                maintainEachMonth3.append(month_cant_remain3)
                spare3 = sum(temporary3_spare3) + spare3
                spareMaintain3.append(spare3)
                temporary3.clear()
                temporary3_spare3.clear()
            else :
                maintainEachMonth3.append(month_cant_remain3)
                spareMaintain3.append(spare3)
            x3+=1
    while len(upperPosition3) > x3 :
        monthcantremain3 = upperPrice3[x3] * 1050
        sparemonthcantremain3 = monthcantremain3 *0.15
        if temporary3 :
                monthcantremain3 = sum(temporary3) + monthcantremain3
                maintainEachMonth3.append(monthcantremain3)
                sparemonthcantremain3 = sum(temporary3_spare3) + sparemonthcantremain3
                spareMaintain3.append(sparemonthcantremain3)
                temporary3.clear()
                temporary3_spare3.clear()
        else :
            maintainEachMonth3.append(monthcantremain3)
            spareMaintain3.append(sparemonthcantremain3)
        x3+=1
    if upperTotalPrice3 != 0:
        overPrice3 += upperTotalPrice3
    recover3 = []
    #if len(setupEachMonth3)==len(maintainEachMonth3):       
    for w3 in range(len(setupEachMonth3)) :
        if setupEachMonth3[w3] <= maintainEachMonth3[w3] :
            recover3.append(setupEachMonth3[w3])
        else :
            recover3.append(maintainEachMonth3[w3])
    recover3 = sum(recover3)
    sparerecover3 = []
    #if len(spareSetUp3)==len(spareMaintain3):
    for v3 in range(len(spareSetUp3)) :
        if spareSetUp3[v3] <= spareMaintain3[v3] :
            sparerecover3.append(spareSetUp3[v3])
        else :
            sparerecover3.append(spareMaintain3[v3])
    sparerecover3 = sum(sparerecover3)
    cover3 = recover3 + sparerecover3

    standard4 = V1_4
    #容量設置費_4
    spareSetUp4 = []
    setupEachMonth4 = []
    for i in range(0, 23):
        lessThanStandard4 = 0
        overThanStandard4 = 0
        if capbilitySetUp4[i+1] > capbilitySetUp4[i]:
            if capbilitySetUp4[i+1] <= standard4:
                lessThanStandard4 += (capbilitySetUp4[i+1] - capbilitySetUp4[i])
            else:
                lessThanStandard4 += (standard4 - capbilitySetUp4[i])
                overThanStandard4 += (capbilitySetUp4[i+1] - standard4)
                standard4 = capbilitySetUp4[i+1]
        spareSetUp4.append(210*lessThanStandard4*0.25)
        setupEachMonth4.append(210*lessThanStandard4*0.5 + 210*overThanStandard4)
    delet4=[]
    setupEachMonth4=np.array(setupEachMonth4)
    spareSetUp4=np.array(spareSetUp4)
    for r in range(len(setupEachMonth4)):
        if setupEachMonth4[r]==0 and spareSetUp4[r]==0 :
            delet4.append(r)
    spareSetUp4=np.delete(spareSetUp4,delet4,axis=0)
    setupEachMonth4=np.delete(setupEachMonth4,delet4,axis=0)
    spareSetUp4=spareSetUp4.tolist()
    setupEachMonth4=setupEachMonth4.tolist()
    #設備維持費_4
    #做表格
    remainTotalPrice4 = 0
    remainPrice4 = []
    remainPosition4 = []
    upperTotalPrice4 = 0 
    upperPrice4 = []
    upperPosition4 = []   
    nonChangeMonthPosition4 = []
    for i in range(0, 23):
        if capbilitySetUp4[i+1] > capbilitySetUp4[i]:
            upperPosition4.append(i+1)
            upperPrice4.append(capbilitySetUp4[i+1] - capbilitySetUp4[i])
            upperTotalPrice4 += (capbilitySetUp4[i+1] - capbilitySetUp4[i]) # > 0
        elif capbilitySetUp4[i+1] < capbilitySetUp4[i] :
            remainPosition4.append(i+1)
            remainPrice4.append(capbilitySetUp4[i+1] - capbilitySetUp4[i])
            remainTotalPrice4 += (capbilitySetUp4[i+1] - capbilitySetUp4[i]) # < 0
        else :
            nonChangeMonthPosition4.append(i+1)  # = 0
          
    #算價錢
    bonusPrice4 = 0
    overPrice4 = 0
    spareMaintain4 = []
    maintainEachMonth4 = []
    temporary4 = []
    temporary4_spare4 = []
    x4 = 0
    y4 = 0
    while len(upperPosition4) > x4 and len(remainPosition4) > y4 :
    #while remainTotalPrice4 != 0 and upperTotalPrice4 != 0:
        #eachBonusPrice = 0
        eachOverPrice4 = 0
        month_can_remain4 = 0
        month_cant_remain4 = 0
        spare4 = 0
        if upperPosition4[x4] > remainPosition4[y4] :
            if upperPrice4[x4] > (-remainPrice4[y4]):
                month_can_remain4 = 35.2*(-remainPrice4[y4])*(upperPosition4[x4] - remainPosition4[y4])
                spare4 = month_can_remain4*0.15
                temporary4.append(month_can_remain4)
                temporary4_spare4.append(spare4)
                bonusPrice4 += (-remainPrice4[y4])*(upperPosition4[x4] - remainPosition4[y4])
                remainTotalPrice4 = remainTotalPrice4 - remainPrice4[y4]
                upperTotalPrice4 = upperTotalPrice4 + remainPrice4[y4]
                upperPrice4[x4] = upperPrice4[x4] + remainPrice4[y4]
                y4+=1
            else:
                month_can_remain4 = 35.2*upperPrice4[x4]*(upperPosition4[x4] - remainPosition4[y4])
                spare4 = month_can_remain4*0.15
                if temporary4 :
                    month_can_remain4 = sum(temporary4) + month_can_remain4
                    maintainEachMonth4.append(month_can_remain4)
                    spare4 = sum(temporary4_spare4) + spare4
                    spareMaintain4.append(spare4)
                    temporary4.clear()
                    temporary4_spare4.clear()
                else :
                    maintainEachMonth4.append(month_can_remain4)
                    spareMaintain4.append(spare4)
                bonusPrice4 += upperPrice4[x4]*(upperPosition4[x4] - remainPosition4[y4])
                remainTotalPrice4 = remainTotalPrice4 + upperPrice4[x4]
                upperTotalPrice4 = upperTotalPrice4 - upperPrice4[x4]
                remainPrice4[y4] = upperPrice4[x4] + remainPrice4[y4]
                x4+=1
        else:
            overPrice4 += upperPrice4[x4]
            upperTotalPrice4 = upperTotalPrice4 - upperPrice4[x4]
            eachOverPrice4 = upperPrice4[x4]
            month_cant_remain4 = eachOverPrice4*210
            spare4 = month_cant_remain4*0.15
            if temporary4 :
                month_cant_remain4 = sum(temporary4) + month_cant_remain4
                maintainEachMonth4.append(month_cant_remain4)
                spare4 = sum(temporary4_spare4) + spare4
                spareMaintain4.append(spare4)
                temporary4.clear()
                temporary4_spare4.clear()
            else :
                maintainEachMonth4.append(month_cant_remain4)
                spareMaintain4.append(spare4)
            x4+=1
    while len(upperPosition4) > x4 :
        monthcantremain4 = upperPrice4[x4] * 1050
        sparemonthcantremain4 = monthcantremain4 *0.15
        if temporary4 :
                monthcantremain4 = sum(temporary4) + monthcantremain4
                maintainEachMonth4.append(monthcantremain4)
                sparemonthcantremain4 = sum(temporary4_spare4) + sparemonthcantremain4
                spareMaintain4.append(sparemonthcantremain4)
                temporary4.clear()
                temporary4_spare4.clear()
        else :
            maintainEachMonth4.append(monthcantremain4)
            spareMaintain4.append(sparemonthcantremain4)
        x4+=1
    if upperTotalPrice4 != 0:
        overPrice4 += upperTotalPrice4
    recover4 = []
    #if len(setupEachMonth4)==len(maintainEachMonth4):
    for w4 in range(len(setupEachMonth4)) :
        if setupEachMonth4[w4] <= maintainEachMonth4[w4] :
            recover4.append(setupEachMonth4[w4])
        else :
            recover4.append(maintainEachMonth4[w4])
    recover4 = sum(recover4)
    sparerecover4 = []
    #if len(spareSetUp4)==len(spareMaintain4):
    for v4 in range(len(spareSetUp4)) :
        if spareSetUp4[v4] <= spareMaintain4[v4] :
            sparerecover4.append(spareSetUp4[v4])
        else :
            sparerecover4.append(spareMaintain4[v4])
    sparerecover4 = sum(sparerecover4)
    cover4 = recover4 + sparerecover4
    
    futuretotal = sameVprice1 + sameVprice2 + sameVprice3 + sameVprice4 + sameVprice5 + sameVprice6 + sameVprice7 + sameVprice8 + sameVprice9 + cover + cover2 + cover3 + cover4
    return futuretotal
#return price3
    
# def get_random_8month():
#     data = list(range(2,25))
#     random.shuffle(data)
#     for index, i in enumerate(data):
#         if index == 0:
#             re_data = [i]
#         elif index >= 8:
#             break
#         else:
#             re_data.append(i)
#     return sorted(re_data)
# def n_times():
#     #l_data = []
#     for j in range(n):
#         if j == 0:
#             ntime_data = [get_random_8month()]
#         else:
#             ntime_data.append(get_random_8month())
#     return ntime_data

def pso():
    global table1
    global change_month
    # 創建點集合
    p = [Position(m1i,m2i,m3i,m4i,m5i,m6i,m7i,m8i,round(V1_1i),round(V1_2i*10000),round(V1_3i*10000),round(V1_4i*10000),round(V2_1i),round(V2_2i*10000),round(V2_3i*10000),round(V2_4i*10000),round(V3_1i),round(V3_2i*10000),round(V3_3i*10000),round(V3_4i*10000),round(V4_1i),round(V4_2i*10000),round(V4_3i*10000),round(V4_4i*10000),round(V5_1i),round(V5_2i*10000),round(V5_3i*10000),round(V5_4i*10000),round(V6_1i),round(V6_2i*10000),round(V6_3i*10000),round(V6_4i*10000),round(V7_1i),round(V7_2i*10000),round(V7_3i*10000),round(V7_4i*10000),round(V8_1i),round(V8_2i*10000),round(V8_3i*10000),round(V8_4i*10000),round(V9_1i),round(V9_2i*10000),round(V9_3i*10000),round(V9_4i*10000), fitnessFunction(m1i,m2i,m3i,m4i,m5i,m6i,m7i,m8i,V1_1i,V1_2i,V1_3i,V1_4i,V2_1i,V2_2i,V2_3i,V2_4i,V3_1i,V3_2i,V3_3i,V3_4i,V4_1i,V4_2i,V4_3i,V4_4i,V5_1i,V5_2i,V5_3i,V5_4i,V6_1i,V6_2i,V6_3i,V6_4i,V7_1i,V7_2i,V7_3i,V7_4i,V8_1i,V8_2i,V8_3i,V8_4i,V9_1i,V9_2i,V9_3i,V9_4i)) for m1i,m2i,m3i,m4i,m5i,m6i,m7i,m8i,V1_1i,V1_2i,V1_3i,V1_4i,V2_1i,V2_2i,V2_3i,V2_4i,V3_1i,V3_2i,V3_3i,V3_4i,V4_1i,V4_2i,V4_3i,V4_4i,V5_1i,V5_2i,V5_3i,V5_4i,V6_1i,V6_2i,V6_3i,V6_4i,V7_1i,V7_2i,V7_3i,V7_4i,V8_1i,V8_2i,V8_3i,V8_4i,V9_1i,V9_2i,V9_3i,V9_4i in zip(np.full(n,change_month[0][0]),np.full(n,change_month[1][0]),np.full(n,change_month[2][0]),np.full(n,change_month[3][0]),np.full(n,change_month[4][0]),np.full(n,change_month[5][0]),np.full(n,change_month[6][0]),np.full(n,change_month[7][0]),np.full(n,table1[0]),np.random.rand(n),np.random.rand(n),np.random.rand(n),np.full(n,table1[change_month[0][0]-1]),np.random.rand(n),np.random.rand(n),np.random.rand(n),np.full(n,table1[change_month[1][0]-1]),np.random.rand(n),np.random.rand(n),np.random.rand(n),np.full(n,table1[change_month[2][0]-1]),np.random.rand(n),np.random.rand(n),np.random.rand(n),np.full(n,table1[change_month[3][0]-1]),np.random.rand(n),np.random.rand(n),np.random.rand(n),np.full(n,table1[change_month[4][0]-1]),np.random.rand(n),np.random.rand(n),np.random.rand(n),np.full(n,table1[change_month[5][0]-1]),np.random.rand(n),np.random.rand(n),np.random.rand(n),np.full(n,table1[change_month[6][0]-1]),np.random.rand(n),np.random.rand(n),np.random.rand(n),np.full(n,table1[change_month[7][0]-1]),np.random.rand(n),np.random.rand(n),np.random.rand(n))]
    #print(m1i)
    v = [Position(m1i,m2i,m3i,m4i,m5i,m6i,m7i,m8i,V1_1i * vmax, V1_2i * vmax, V1_3i * vmax, V1_4i * vmax, V2_1i * vmax, V2_2i * vmax, V2_3i * vmax, V2_4i * vmax, V3_1i * vmax, V3_2i * vmax, V3_3i * vmax, V3_4i * vmax, V4_1i * vmax,V4_2i * vmax, V4_3i * vmax,V4_4i * vmax, V5_1i * vmax, V5_2i * vmax,V5_3i * vmax,V5_4i * vmax,V6_1i * vmax,V6_2i * vmax,V6_3i * vmax,V6_4i * vmax,V7_1i * vmax,V7_2i * vmax,V7_3i * vmax,V7_4i * vmax,V8_1i * vmax,V8_2i * vmax,V8_3i * vmax,V8_4i * vmax,V9_1i * vmax,V9_2i * vmax,V9_3i * vmax,V9_4i * vmax, fitnessFunction( m1i,m2i,m3i,m4i,m5i,m6i,m7i,m8i,V1_1i,V1_2i,V1_3i,V1_4i,V2_1i,V2_2i,V2_3i,V2_4i,V3_1i,V3_2i,V3_3i,V3_4i,V4_1i,V4_2i,V4_3i,V4_4i,V5_1i,V5_2i,V5_3i,V5_4i,V6_1i,V6_2i,V6_3i,V6_4i,V7_1i,V7_2i,V7_3i,V7_4i,V8_1i,V8_2i,V8_3i,V8_4i,V9_1i,V9_2i,V9_3i,V9_4i)) for m1i,m2i,m3i,m4i,m5i,m6i,m7i,m8i,V1_1i,V1_2i,V1_3i,V1_4i,V2_1i,V2_2i,V2_3i,V2_4i,V3_1i,V3_2i,V3_3i,V3_4i,V4_1i,V4_2i,V4_3i,V4_4i,V5_1i,V5_2i,V5_3i,V5_4i,V6_1i,V6_2i,V6_3i,V6_4i,V7_1i,V7_2i,V7_3i,V7_4i,V8_1i,V8_2i,V8_3i,V8_4i,V9_1i,V9_2i,V9_3i,V9_4i in zip(np.random.randn(n),np.random.randn(n),np.random.randn(n),np.random.randn(n),np.random.randn(n),np.random.randn(n),np.random.randn(n),np.random.randn(n),np.random.rand(n), np.random.rand(n), np.random.rand(n), np.random.rand(n), np.random.rand(n), np.random.rand(n), np.random.rand(n), np.random.rand(n), np.random.rand(n), np.random.rand(n), np.random.rand(n), np.random.rand(n), np.random.rand(n), np.random.rand(n), np.random.rand(n), np.random.rand(n), np.random.rand(n), np.random.rand(n), np.random.rand(n), np.random.rand(n), np.random.rand(n), np.random.rand(n), np.random.rand(n), np.random.rand(n), np.random.rand(n), np.random.rand(n), np.random.rand(n), np.random.rand(n), np.random.rand(n), np.random.rand(n), np.random.rand(n), np.random.rand(n), np.random.rand(n), np.random.rand(n), np.random.rand(n), np.random.rand(n))]

    pBest = p.copy()
    # 當前個體極值
    gBest = min(p, key=lambda pi: pi.futuretotal)
    wb = Workbook()    #將預測值存入excel    
    ws2= wb.active
    ws2['A1'] = 'month' 
    ws2['B1'] = '1'
    ws2['C1'] = '2'
    ws2['D1'] = '3'
    ws2['E1'] = '4'
    ws2['F1'] = '5'
    ws2['G1'] = '6'
    ws2['H1'] = '7'
    ws2['I1'] = '8'
    ws2['J1'] = '9'
    ws2['K1'] = '10'
    ws2['L1'] = '11'
    ws2['M1'] = '12'
    ws2['A2'] = 'w1'
    ws2['A3'] = 'w2'
    ws2['A4'] = 'w3'
    ws2['A5'] = 'w4'
    for i in range(_max):
        for j in range(n):
            
            if p[j].m1>p[j].m2:
                p[j].m1,p[j].m2 = p[j].m2,p[j].m1
            if p[j].m3>p[j].m4:
                p[j].m3,p[j].m4 = p[j].m4,p[j].m3
            if p[j].m5>p[j].m6:
                p[j].m5,p[j].m6 = p[j].m6,p[j].m5
            if p[j].m7>p[j].m8:
                p[j].m7,p[j].m8 = p[j].m8,p[j].m7
            else:
                pass
            # 更新速度和位置
            vm1=w*v[j].m1+c1*np.random.random()*(pBest[j].m1-p[j].m1)+c2*np.random.random()*(gBest.m1-p[j].m1)
            vm2=w*v[j].m2+c1*np.random.random()*(pBest[j].m2-p[j].m2)+c2*np.random.random()*(gBest.m2-p[j].m2)
            vm3=w*v[j].m3+c1*np.random.random()*(pBest[j].m3-p[j].m3)+c2*np.random.random()*(gBest.m3-p[j].m3)
            vm4=w*v[j].m4+c1*np.random.random()*(pBest[j].m4-p[j].m4)+c2*np.random.random()*(gBest.m4-p[j].m4)
            vm5=w*v[j].m5+c1*np.random.random()*(pBest[j].m5-p[j].m5)+c2*np.random.random()*(gBest.m5-p[j].m5)
            vm6=w*v[j].m6+c1*np.random.random()*(pBest[j].m6-p[j].m6)+c2*np.random.random()*(gBest.m6-p[j].m6)
            vm7=w*v[j].m7+c1*np.random.random()*(pBest[j].m7-p[j].m7)+c2*np.random.random()*(gBest.m7-p[j].m7)
            vm8=w*v[j].m8+c1*np.random.random()*(pBest[j].m8-p[j].m8)+c2*np.random.random()*(gBest.m8-p[j].m8)
            vV1_1=w*v[j].V1_1+c1*np.random.random()*(pBest[j].V1_1-p[j].V1_1)+c2*np.random.random()*(gBest.V1_1-p[j].V1_1)
            vV1_2=w*v[j].V1_2+c1*np.random.random()*(pBest[j].V1_2-p[j].V1_2)+c2*np.random.random()*(gBest.V1_2-p[j].V1_2)
            vV1_3=w*v[j].V1_3+c1*np.random.random()*(pBest[j].V1_3-p[j].V1_3)+c2*np.random.random()*(gBest.V1_3-p[j].V1_3)
            vV1_4=w*v[j].V1_4+c1*np.random.random()*(pBest[j].V1_4-p[j].V1_4)+c2*np.random.random()*(gBest.V1_4-p[j].V1_4)
            vV2_1=w*v[j].V2_1+c1*np.random.random()*(pBest[j].V2_1-p[j].V2_1)+c2*np.random.random()*(gBest.V2_1-p[j].V2_1)
            vV2_2=w*v[j].V2_2+c1*np.random.random()*(pBest[j].V2_2-p[j].V2_2)+c2*np.random.random()*(gBest.V2_2-p[j].V2_2)
            vV2_3=w*v[j].V2_3+c1*np.random.random()*(pBest[j].V2_3-p[j].V2_3)+c2*np.random.random()*(gBest.V2_3-p[j].V2_3)
            vV2_4=w*v[j].V2_4+c1*np.random.random()*(pBest[j].V2_4-p[j].V2_4)+c2*np.random.random()*(gBest.V2_4-p[j].V2_4)
            vV3_1=w*v[j].V3_1+c1*np.random.random()*(pBest[j].V3_1-p[j].V3_1)+c2*np.random.random()*(gBest.V3_1-p[j].V3_1)
            vV3_2=w*v[j].V3_2+c1*np.random.random()*(pBest[j].V3_2-p[j].V3_2)+c2*np.random.random()*(gBest.V3_2-p[j].V3_2)
            vV3_3=w*v[j].V3_3+c1*np.random.random()*(pBest[j].V3_3-p[j].V3_3)+c2*np.random.random()*(gBest.V3_3-p[j].V3_3)
            vV3_4=w*v[j].V3_4+c1*np.random.random()*(pBest[j].V3_4-p[j].V3_4)+c2*np.random.random()*(gBest.V3_4-p[j].V3_4)
            vV4_1=w*v[j].V4_1+c1*np.random.random()*(pBest[j].V4_1-p[j].V4_1)+c2*np.random.random()*(gBest.V4_1-p[j].V4_1)
            vV4_2=w*v[j].V4_2+c1*np.random.random()*(pBest[j].V4_2-p[j].V4_2)+c2*np.random.random()*(gBest.V4_2-p[j].V4_2)
            vV4_3=w*v[j].V4_3+c1*np.random.random()*(pBest[j].V4_3-p[j].V4_3)+c2*np.random.random()*(gBest.V4_3-p[j].V4_3)
            vV4_4=w*v[j].V4_4+c1*np.random.random()*(pBest[j].V4_4-p[j].V4_4)+c2*np.random.random()*(gBest.V4_4-p[j].V4_4)
            vV5_1=w*v[j].V5_1+c1*np.random.random()*(pBest[j].V5_1-p[j].V5_1)+c2*np.random.random()*(gBest.V5_1-p[j].V5_1)
            vV5_2=w*v[j].V5_2+c1*np.random.random()*(pBest[j].V5_2-p[j].V5_2)+c2*np.random.random()*(gBest.V5_2-p[j].V5_2)
            vV5_3=w*v[j].V5_3+c1*np.random.random()*(pBest[j].V5_3-p[j].V5_3)+c2*np.random.random()*(gBest.V5_3-p[j].V5_3)
            vV5_4=w*v[j].V5_4+c1*np.random.random()*(pBest[j].V5_4-p[j].V5_4)+c2*np.random.random()*(gBest.V5_4-p[j].V5_4)
            vV6_1=w*v[j].V6_1+c1*np.random.random()*(pBest[j].V6_1-p[j].V6_1)+c2*np.random.random()*(gBest.V6_1-p[j].V6_1)
            vV6_2=w*v[j].V6_2+c1*np.random.random()*(pBest[j].V6_2-p[j].V6_2)+c2*np.random.random()*(gBest.V6_2-p[j].V6_2)
            vV6_3=w*v[j].V6_3+c1*np.random.random()*(pBest[j].V6_3-p[j].V6_3)+c2*np.random.random()*(gBest.V6_3-p[j].V6_3)
            vV6_4=w*v[j].V6_4+c1*np.random.random()*(pBest[j].V6_4-p[j].V6_4)+c2*np.random.random()*(gBest.V6_4-p[j].V6_4)
            vV7_1=w*v[j].V7_1+c1*np.random.random()*(pBest[j].V7_1-p[j].V7_1)+c2*np.random.random()*(gBest.V7_1-p[j].V7_1)
            vV7_2=w*v[j].V7_2+c1*np.random.random()*(pBest[j].V7_2-p[j].V7_2)+c2*np.random.random()*(gBest.V7_2-p[j].V7_2)
            vV7_3=w*v[j].V7_3+c1*np.random.random()*(pBest[j].V7_3-p[j].V7_3)+c2*np.random.random()*(gBest.V7_3-p[j].V7_3)
            vV7_4=w*v[j].V7_4+c1*np.random.random()*(pBest[j].V7_4-p[j].V7_4)+c2*np.random.random()*(gBest.V7_4-p[j].V7_4)
            vV8_1=w*v[j].V8_1+c1*np.random.random()*(pBest[j].V8_1-p[j].V8_1)+c2*np.random.random()*(gBest.V8_1-p[j].V8_1)
            vV8_2=w*v[j].V8_2+c1*np.random.random()*(pBest[j].V8_2-p[j].V8_2)+c2*np.random.random()*(gBest.V8_2-p[j].V8_2)
            vV8_3=w*v[j].V8_3+c1*np.random.random()*(pBest[j].V8_3-p[j].V8_3)+c2*np.random.random()*(gBest.V8_3-p[j].V8_3)
            vV8_4=w*v[j].V8_4+c1*np.random.random()*(pBest[j].V8_4-p[j].V8_4)+c2*np.random.random()*(gBest.V8_4-p[j].V8_4)
            vV9_1=w*v[j].V9_1+c1*np.random.random()*(pBest[j].V9_1-p[j].V9_1)+c2*np.random.random()*(gBest.V9_1-p[j].V9_1)
            vV9_2=w*v[j].V9_2+c1*np.random.random()*(pBest[j].V9_2-p[j].V9_2)+c2*np.random.random()*(gBest.V9_2-p[j].V9_2)
            vV9_3=w*v[j].V9_3+c1*np.random.random()*(pBest[j].V9_3-p[j].V9_3)+c2*np.random.random()*(gBest.V9_3-p[j].V9_3)
            vV9_4=w*v[j].V9_4+c1*np.random.random()*(pBest[j].V9_4-p[j].V9_4)+c2*np.random.random()*(gBest.V9_4-p[j].V9_4)
            #w = w-((ws-we)*(i/_max))
            
          
                
            if vV1_1>v1max:
                vV1_1=v1max
            if vV1_2>v2max:
                vV1_2=v2max
            if vV1_3>v3max:
                vV1_3=v3max
            if vV1_4>v4max:
                vV1_4=v4max
            if vV2_1>v1max:
                vV2_1=v1max
            if vV2_2>v2max:
                vV2_2=v2max
            if vV2_3>v3max:
                vV2_3=v3max
            if vV2_4>v4max:
                vV2_4=v4max
            if vV3_1>v1max:
                vV3_1=v1max
            if vV3_2>v2max:
                vV3_2=v2max
            if vV3_3>v3max:
                vV3_3=v3max
            if vV3_4>v4max:
                vV3_4=v4max
            if vV4_1>v1max:
                vV4_1=v1max
            if vV4_2>v2max:
                vV4_2=v2max
            if vV4_3>v3max:
                vV4_3=v3max
            if vV4_4>v4max:
                vV4_4=v4max
            if vV5_1>v1max:
                vV5_1=v1max
            if vV5_2>v2max:
                vV5_2=v2max
            if vV5_3>v3max:
                vV5_3=v3max
            if vV5_4>v4max:
                vV5_4=v4max
            if vV6_1>v1max:
                vV6_1=v1max
            if vV6_2>v2max:
                vV6_2=v2max
            if vV6_3>v3max:
                vV6_3=v3max
            if vV6_4>v4max:
                vV6_4=v4max
            if vV7_1>v1max:
                vV7_1=v1max
            if vV7_2>v2max:
                vV7_2=v2max
            if vV7_3>v3max:
                vV7_3=v3max
            if vV7_4>v4max:
                vV7_4=v4max
            if vV8_1>v1max:
                vV8_1=v1max
            if vV8_2>v2max:
                vV8_2=v2max
            if vV8_3>v3max:
                vV8_3=v3max
            if vV8_4>v4max:
                vV8_4=v4max
            if vV9_1>v1max:
                vV9_1=v1max
            if vV9_2>v2max:
                vV9_2=v2max
            if vV9_3>v3max:
                vV9_3=v3max
            if vV9_4>v4max:
                vV9_4=v4max
            
            v[j]=Position(vm1,vm2,vm3,vm4,vm5,vm6,vm7,vm8,vV1_1,vV1_2,vV1_3,vV1_4,vV2_1,vV2_2,vV2_3,vV2_4,vV3_1,vV3_2,vV3_3,vV3_4,vV4_1,vV4_2,vV4_3,vV4_4,vV5_1,vV5_2,vV5_3,vV5_4,vV6_1,vV6_2,vV6_3,vV6_4,vV7_1,vV7_2,vV7_3,vV7_4,vV8_1,vV8_2,vV8_3,vV8_4,vV9_1,vV9_2,vV9_3,vV9_4,fitnessFunction(vm1,vm2,vm3,vm4,vm5,vm6,vm7,vm8,vV1_1,vV1_2,vV1_3,vV1_4,vV2_1,vV2_2,vV2_3,vV2_4,vV3_1,vV3_2,vV3_3,vV3_4,vV4_1,vV4_2,vV4_3,vV4_4,vV5_1,vV5_2,vV5_3,vV5_4,vV6_1,vV6_2,vV6_3,vV6_4,vV7_1,vV7_2,vV7_3,vV7_4,vV8_1,vV8_2,vV8_3,vV8_4,vV9_1,vV9_2,vV9_3,vV9_4))
            
            p[j].V1_1+=v[j].V1_1
            p[j].V1_2+=v[j].V1_2
            p[j].V1_3+=v[j].V1_3
            p[j].V1_4+=v[j].V1_4
            p[j].V2_1+=v[j].V2_1
            p[j].V2_2+=v[j].V2_2
            p[j].V2_3+=v[j].V2_3
            p[j].V2_4+=v[j].V2_4
            p[j].V3_1+=v[j].V3_1
            p[j].V3_2+=v[j].V3_2
            p[j].V3_3+=v[j].V3_3
            p[j].V3_4+=v[j].V3_4
            p[j].V4_1+=v[j].V4_1
            p[j].V4_2+=v[j].V4_2
            p[j].V4_3+=v[j].V4_3
            p[j].V4_4+=v[j].V4_4
            p[j].V5_1+=v[j].V5_1
            p[j].V5_2+=v[j].V5_2
            p[j].V5_3+=v[j].V5_3
            p[j].V5_4+=v[j].V5_4
            p[j].V6_1+=v[j].V6_1
            p[j].V6_2+=v[j].V6_2
            p[j].V6_3+=v[j].V6_3
            p[j].V6_4+=v[j].V6_4
            p[j].V7_1+=v[j].V7_1
            p[j].V7_2+=v[j].V7_2
            p[j].V7_3+=v[j].V7_3
            p[j].V7_4+=v[j].V7_4
            p[j].V8_1+=v[j].V8_1
            p[j].V8_2+=v[j].V8_2
            p[j].V8_3+=v[j].V8_3
            p[j].V8_4+=v[j].V8_4
            p[j].V9_1+=v[j].V9_1
            p[j].V9_2+=v[j].V9_2
            p[j].V9_3+=v[j].V9_3
            p[j].V9_4+=v[j].V9_4
            
            p[j].futuretotal=fitnessFunction(p[j].m1,p[j].m2,p[j].m3,p[j].m4,p[j].m5,p[j].m6,p[j].m7,p[j].m8,p[j].V1_1,p[j].V1_2,p[j].V1_3,p[j].V1_4,p[j].V2_1,p[j].V2_2,p[j].V2_3,p[j].V2_4,p[j].V3_1,p[j].V3_2,p[j].V3_3,p[j].V3_4,p[j].V4_1,p[j].V4_2,p[j].V4_3,p[j].V4_4,p[j].V5_1,p[j].V5_2,p[j].V5_3,p[j].V5_4,p[j].V6_1,p[j].V6_2,p[j].V6_3,p[j].V6_4,p[j].V7_1,p[j].V7_2,p[j].V7_3,p[j].V7_4,p[j].V8_1,p[j].V8_2,p[j].V8_3,p[j].V8_4,p[j].V9_1,p[j].V9_2,p[j].V9_3,p[j].V9_4)

            # 越界判断

            if p[j].V1_1>=85000:
                p[j].V1_1=85000
            if p[j].V1_1<=70000:
                p[j].V1_1=70000
            if p[j].V1_2>=5000:
                p[j].V1_2=5000
            if p[j].V1_2<=0:
                p[j].V1_2=0
            if p[j].V1_3>=5000:
                p[j].V1_3=5000
            if p[j].V1_3<=0:
                p[j].V1_3=0
            if p[j].V1_4>=5000:
                p[j].V1_4=5000
            if p[j].V1_4<=0:
                p[j].V1_4=0
            if p[j].V2_1>=85000:
                p[j].V2_1=85000
            if p[j].V2_1<=70000:
                p[j].V2_1=70000
            if p[j].V2_2>=5000:
                p[j].V2_2=5000
            if p[j].V2_2<=0:
                p[j].V2_2=0
            if p[j].V2_3>=5000:
                p[j].V2_3=5000
            if p[j].V2_3<=0:
                p[j].V2_3=0
            if p[j].V2_4>=5000:
                p[j].V2_4=5000
            if p[j].V2_4<=0:
                p[j].V2_4=0
            if p[j].V3_1>=85000:
                p[j].V3_1=85000
            if p[j].V3_1<=70000:
                p[j].V3_1=70000
            if p[j].V3_2>=5000:
                p[j].V3_2=5000
            if p[j].V3_2<=0:
                p[j].V3_2=0
            if p[j].V3_3>=5000:
                p[j].V3_3=5000
            if p[j].V3_3<=0:
                p[j].V3_3=0
            if p[j].V3_4>=5000:
                p[j].V3_4=5000
            if p[j].V3_4<=0:
                p[j].V3_4=0
            if p[j].V4_1>=85000:
                p[j].V4_1=85000
            if p[j].V4_1<=70000:
                p[j].V4_1=70000
            if p[j].V4_2>=5000:
                p[j].V4_2=5000
            if p[j].V4_2<=0:
                p[j].V4_2=0
            if p[j].V4_3>=5000:
                p[j].V4_3=5000
            if p[j].V4_3<=0:
                p[j].V4_3=0
            if p[j].V4_4>=5000:
                p[j].V4_4=5000
            if p[j].V4_4<=0:
                p[j].V4_4=0
            if p[j].V5_1>=85000:
                p[j].V5_1=85000
            if p[j].V5_1<=70000:
                p[j].V5_1=70000
            if p[j].V5_2>=5000:
                p[j].V5_2=5000
            if p[j].V5_2<=0:
                p[j].V5_2=0
            if p[j].V5_3>=5000:
                p[j].V5_3=5000
            if p[j].V5_3<=0:
                p[j].V5_3=0
            if p[j].V5_4>=5000:
                p[j].V5_4=5000
            if p[j].V5_4<=0:
                p[j].V5_4=0
            if p[j].V6_1>=85000:
                p[j].V6_1=85000
            if p[j].V6_1<=70000:
                p[j].V6_1=70000
            if p[j].V6_2>=5000:
                p[j].V6_2=5000
            if p[j].V6_2<=0:
                p[j].V6_2=0
            if p[j].V6_3>=5000:
                p[j].V6_3=5000
            if p[j].V6_3<=0:
                p[j].V6_3=0
            if p[j].V6_4>=5000:
                p[j].V6_4=5000
            if p[j].V6_4<=0:
                p[j].V6_4=0
            if p[j].V7_1>=85000:
                p[j].V7_1=85000
            if p[j].V7_1<=70000:
                p[j].V7_1=70000
            if p[j].V7_2>=5000:
                p[j].V7_2=5000
            if p[j].V7_2<=0:
                p[j].V7_2=0
            if p[j].V7_3>=5000:
                p[j].V7_3=5000
            if p[j].V7_3<=0:
                p[j].V7_3=0
            if p[j].V7_4>=5000:
                p[j].V7_4=5000
            if p[j].V7_4<=0:
                p[j].V7_4=0
            if p[j].V8_1>=85000:
                p[j].V8_1=85000
            if p[j].V8_1<=70000:
                p[j].V8_1=70000
            if p[j].V8_2>=5000:
                p[j].V8_2=5000
            if p[j].V8_2<=0:
                p[j].V8_2=0
            if p[j].V8_3>=5000:
                p[j].V8_3=5000
            if p[j].V8_3<=0:
                p[j].V8_3=0
            if p[j].V8_4>=5000:
                p[j].V8_4=5000
            if p[j].V8_4<=0:
                p[j].V8_4=0
            if p[j].V9_1>=85000:
                p[j].V9_1=85000
            if p[j].V9_1<=70000:
                p[j].V9_1=70000
            if p[j].V9_2>=5000:
                p[j].V9_2=5000
            if p[j].V9_2<=0:
                p[j].V9_2=0
            if p[j].V9_3>=5000:
                p[j].V9_3=5000
            if p[j].V9_3<=0:
                p[j].V9_3=0
            if p[j].V9_4>=5000:
                p[j].V9_4=5000
            if p[j].V9_4<=0:
                p[j].V9_4=0
                
        # 更新個體極值和群體極值
        for j in range(n):
            if pBest[j].futuretotal > p[j].futuretotal:
                pBest[j]=p[j]
            if gBest.futuretotal > p[j].futuretotal  :
                gBest=p[j]

        print("====="+str(i+1)+"=====gBest:"+gBest.__str__())
    
    print(int(float(gBest.__strm1__())))
    print(int(float(gBest.__strm2__())))
    print(int(float(gBest.__strm3__())))
    print(int(float(gBest.__strm4__())))
    print(int(float(gBest.__strm5__())))
    print(int(float(gBest.__strm6__())))
    print(int(float(gBest.__strm7__())))
    print(int(float(gBest.__strm8__())))
    table = [['1'],['2'],['3'],['4'],['5'],['6'],['7'],['8'],['9'],['10'],['11'],['12'],['13'],['14'],['15'],['16'],['17'],['18'],['19'],['20'],['21'],['22'],['23'],['24']]
    for d in range(int(float(gBest.__strm1__()))-1):
        table[d].append(gBest.__str1_1__())
        table[d].append(gBest.__str1_2__())
        table[d].append(gBest.__str1_3__())
        table[d].append(gBest.__str1_4__())
    for d in range(int(float(gBest.__strm1__()))-1,int(float(gBest.__strm2__()))-1):
        table[d].append(gBest.__str2_1__())
        table[d].append(gBest.__str2_2__())
        table[d].append(gBest.__str2_3__())
        table[d].append(gBest.__str2_4__())  
    for d in range(int(float(gBest.__strm2__()))-1,int(float(gBest.__strm3__()))-1):  
        table[d].append(gBest.__str3_1__())
        table[d].append(gBest.__str3_2__())
        table[d].append(gBest.__str3_3__())
        table[d].append(gBest.__str3_4__())
    for d in range(int(float(gBest.__strm3__()))-1,int(float(gBest.__strm4__()))-1):  
        table[d].append(gBest.__str4_1__())
        table[d].append(gBest.__str4_2__())
        table[d].append(gBest.__str4_3__())
        table[d].append(gBest.__str4_4__())
    for d in range(int(float(gBest.__strm4__()))-1,int(float(gBest.__strm5__()))-1):  
        table[d].append(gBest.__str5_1__())
        table[d].append(gBest.__str5_2__())
        table[d].append(gBest.__str5_3__())
        table[d].append(gBest.__str5_4__())
    for d in range(int(float(gBest.__strm5__()))-1,int(float(gBest.__strm6__()))-1):  
        table[d].append(gBest.__str6_1__())
        table[d].append(gBest.__str6_2__())
        table[d].append(gBest.__str6_3__())
        table[d].append(gBest.__str6_4__())
    for d in range(int(float(gBest.__strm6__()))-1,int(float(gBest.__strm7__()))-1):  
        table[d].append(gBest.__str7_1__())
        table[d].append(gBest.__str7_2__())
        table[d].append(gBest.__str7_3__())
        table[d].append(gBest.__str7_4__())
    for d in range(int(float(gBest.__strm7__()))-1,int(float(gBest.__strm8__()))-1):  
        table[d].append(gBest.__str8_1__())
        table[d].append(gBest.__str8_2__())
        table[d].append(gBest.__str8_3__())
        table[d].append(gBest.__str8_4__())
    for d in range(int(float(gBest.__strm8__()))-1,24):  
        table[d].append(gBest.__str9_1__())
        table[d].append(gBest.__str9_2__())
        table[d].append(gBest.__str9_3__())
        table[d].append(gBest.__str9_4__())
    for h in range(24):
        maxeachmonth = max(maxtotalflow[h], key=maxtotalflow[h].get)
        eachmonthmaxvalue = maxtotalflow[h][maxeachmonth]
        table[h].append(eachmonthmaxvalue)
    table[23].append(gBest.__futuretotal__())
    lst=[gBest.__strm1__(),gBest.__strm2__(),gBest.__strm3__(),gBest.__strm4__(),gBest.__strm5__(),gBest.__strm6__(),gBest.__strm7__(),gBest.__strm8__()]
    dic={}.fromkeys(lst)
    if len(dic)==len(lst):
        with open('PredictOneYearOutputtest.csv','a',newline ='',encoding ='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['month','w1','w2','w3','w4','max','total'])
            writer.writerows(table)
        return False
    else:
        return True
    #return int(float(gBest.__strm1__())) == 1 or int(float(gBest.__strm1__())) == int(float(gBest.__strm2__())) or int(float(gBest.__strm3__())) == int(float(gBest.__strm4__())) or int(float(gBest.__strm5__())) == int(float(gBest.__strm6__())) or int(float(gBest.__strm7__())) == int(float(gBest.__strm8__()))
def TakeCoefficient():
    for datapi in Pi.values:
        Coefficient = datapi[3]
        month = datapi[0]
        pi.append([month,Coefficient])
        #pi.append(Coefficient)

def MultiplyCoefficient():
    for data in makenewdf.values:
        
        DateTime = data[0]
        date = DateTime.split("/", 2)
        date = list(map(int, date))
        for i in range (12) :
            if date[1] == pi[i][0]:
                new = data[2]*pi[i][1]
        new_kw_del.append(new)
def flowcost(year, mmm):
    eachflow = {'A':0, 'B':0, 'C':0, 'D':0} 
    maxflow = {'A':0, 'B':0, 'C':0, 'D':0} 
    for index, data in enumerate(df.values):
        DateTime = data[0]
        date = DateTime.split("/", 2)
        date = list(map(int, date))
        if date[0] == int(year) and date[1] == int(mmm):
            eachflow[data[1]] += data[3]
            if maxflow[data[1]] < data[2]:
                maxflow[data[1]] = data[2]
    totalflow.append(eachflow)   
    maxtotalflow.append(maxflow)

def catch_year_month():
    df.columns = ['DateTime','Type','kW_del','kWh']
    df.head()
    DateTime = df['DateTime']
    DateTime = DateTime[0]
    date = DateTime.split("/", 2)
    date = list(map(int, date))
    datayear = date[0]
    datamonth = date[1]
    return datayear, datamonth

if __name__ == "__main__":
    #建造乘上pi的新資料
    makenewdf = pd.read_csv('PredictOneYear.csv')
    Pi = pd.read_csv('PredictAvgMonthOutput.csv')
    pi = []
    new_kw_del = []
    TakeCoefficient()
    MultiplyCoefficient()
    final_data = []
    for index, i in enumerate(makenewdf.values):
        DateTime = i[0]
        date = DateTime.split("/", 2)
        date = list(map(int, date))
        final_data.append(["{}/{}/{}".format(date[0]+1, date[1], date[2]), i[1], new_kw_del[index], new_kw_del[index]/4])
    for index, i in enumerate(makenewdf.values):
        DateTime = i[0]
        date = DateTime.split("/", 2)
        date = list(map(int, date))
        final_data.append(["{}/{}/{}".format(date[0]+2, date[1], date[2]), i[1], i[2], i[3]])
    df_final_data = pd.DataFrame(final_data, columns = ['DateTime', 'Type', 'kW_del', 'kWh']) 
    df_final_data.to_csv('df_final_2020_2022.csv', index=False, header=True)
    #開始做pso
    df = pd.read_csv('df_final_2020_2022.csv')
    totalflow = [] #流動電費各時段總度數
    maxtotalflow = [] #各個月的各時段最大需量
    totalprice=[]
    totalprice2=[]
    totalprice3=[]
    totalprice4=[]
    totalprice5=[]
    totalprice6=[]
    totalprice7=[]
    totalprice8=[]
    totalprice9=[]
    
    config = configparser.ConfigParser() 
    #Load ini 檔
    config.read('Setting.ini')
    capbility = config.get('Set', 'capbility')
    capbility1 = capbility.split(';') 
    capbilitySetUp = list(map(int, capbility1))
    #capbilitySetUp = []
    
    capbilitySetUp2 = []
    capbilitySetUp3 = []
    capbilitySetUp4 = []
    table1 = []
    Vx_x = []
    data_year, data_month = catch_year_month()
    startyear = data_year 
    startmonth = data_month  
    for year in range(startyear,startyear+3):
        if year == startyear:
            start_month = startmonth
        else:
            start_month = 1
        for mmm in range(start_month,13):
            flowcost(str(year),str(mmm))
    for h in range(0,24):
        maxeachmonth = max(maxtotalflow[h], key=maxtotalflow[h].get)
        eachmonthmaxvalue = maxtotalflow[h][maxeachmonth]
        table1.append(eachmonthmaxvalue)
    change_month = []
    for index, i in enumerate(table1):
        if index == 23:
            break
        change_month.append([index+2, abs(table1[index]-table1[index+1])])
    change_month.sort(key=lambda x: x[1])
    change_month = change_month[-8:]
    change_month.sort(key=lambda x: x[0])    
    keyValue = 1000
    biggerThanKeyValueMonth = []
    for i in range(len(change_month)):
        if change_month[i][1] >= keyValue:
            biggerThanKeyValueMonth.append(change_month[i])
    for i in range(0, len(biggerThanKeyValueMonth)):
        Vx_x.append([0, 0, 0, 0])
    for step in range(5):
        pso()
    # complete = pso()
    # while complete:
    #     complete = pso()
    outputdata = pd.read_csv("PredictOneYearOutputtest.csv")
    total = outputdata.total # data內，head為"total"的column
    total = total.dropna(axis = 0, how = 'all') # 去掉Nan
    total = total[total!= 'total'] # 留下不是'total'的值
    print(total)
    money = []
    for i in total:
        money.append(i)
    minimum = min(money)
    print(minimum)
    minimum_index = total[total == minimum].index[0] + 1
    #minimum_index = total[total == minimum].index[0] + 2
    #print("minimum_index", minimum_index)
    bestdata = outputdata[(minimum_index-24):minimum_index]
    bestdata.to_csv("best.csv", encoding = 'utf-8',index = False)