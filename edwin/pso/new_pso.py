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
import copy

class Position:
    def __init__(self,ls_months, ls_Vn_n, futuretotal):
        self.ls_months=ls_months
        self.ls_Vn_n=ls_Vn_n
        
        # 該點的適應度 即要求的函数值
        
        self.futuretotal=futuretotal
        
    def __str__(self):
        re_str = "Months:" + str(self.ls_months) + "\n"
        for index, price in enumerate(self.ls_Vn_n):
            re_str += "Price_%s: %.3f, %.3f, %.3f, %.3f \n" %(index+1, price[0], price[1], price[2],price[3])
        re_str += "FutureTotal: "+ str(self.futuretotal)
        return re_str
    
# 粒子數
n=200
# 粒子集合
p=[]
v=[]
pBest=[]
gBest=Position([0], [[0, 0, 0, 0]], 0)
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
def fitnessFunction(ls_months,ls_Vn_n):
    capbilitySetUp = []
    capbilitySetUp2 = []
    capbilitySetUp3 = []
    capbilitySetUp4 = []
    sameVprice = 0
    months_append_25 = ls_months.copy()
    months_append_25.append(25)
    for k in range(24):
        for m in range(len(months_append_25)):
            if k >= (months_append_25[m] - 1):
                continue
            else:
                if ((totalflow[k]['A'] is not 0) and (maxtotalflow[k]['A'] is not 0)) :
                    #基本電費
                    basic = ( 217.3 * ls_Vn_n[m][0] + 160.6 * ls_Vn_n[m][1] + 43.4 * ls_Vn_n[m][2] * max(( ls_Vn_n[m][2] + ls_Vn_n[m][3] - 0.5 * ( ls_Vn_n[m][0] + ls_Vn_n[m][1] )),0) ) * 0.98 * 1.15 #夏月
                    #流動電費
                    #flowsummer1 = 4.61 * totalflow[k]['A'] + 2.87 * totalflow[k]['B']  + 1.73 * totalflow[k]['D'] + 1.29 * totalflow[k]['C']
                    #功率折扣費
                    #discount1 = ( basic + flowsummer1 ) * (80-95) / 1000 
                    #超約附加費
                    Eov1_1 = max((maxtotalflow[k]['A'] - ls_Vn_n[m][0]), 0)
                    Eov1_2 = max((maxtotalflow[k]['B'] - ls_Vn_n[m][0] - ls_Vn_n[m][1]), 0)
                    Eov1_4 = max((maxtotalflow[k]['D'] - ls_Vn_n[m][0] - ls_Vn_n[m][1] - ls_Vn_n[m][3]), 0)
                    Eov1_3 = max((maxtotalflow[k]['C'] - ls_Vn_n[m][0] - ls_Vn_n[m][1] - ls_Vn_n[m][3] - ls_Vn_n[m][2]), 0)

                    Eovc1_1 = Eov1_1
                    Eovc1_2 = max((Eov1_2 - Eovc1_1), 0)
                    Eovc1_4 = max((Eov1_4 - max(Eovc1_1, Eovc1_2)), 0)
                    Eovc1_3 = max((Eov1_3 - max(Eovc1_1, Eovc1_2, Eovc1_4)), 0)
                
                    overAprice = 2 * 217.3 * max(min(Eovc1_1, (0.1*ls_Vn_n[m][0])), 0) + 3*217.3*max((Eovc1_1-(0.1*ls_Vn_n[m][0])), 0)  #夏月
                    overBprice = 2*160.6*max(min(Eovc1_2,(0.1*ls_Vn_n[m][1])),0) + 3*160.6*max((Eovc1_2-(0.1*ls_Vn_n[m][1])),0)
                    overDprice = 2*43.3*max(min(Eovc1_4,(0.1*ls_Vn_n[m][3])),0) + 3*43.3*max((Eovc1_4-(0.1*ls_Vn_n[m][3])),0)
                    overCprice = 2*43.3*max(min(Eovc1_3,(0.1*ls_Vn_n[m][2])),0) + 3*43.3*max((Eovc1_3-(0.1*ls_Vn_n[m][2])),0)
                    overprice = overAprice + overBprice + overDprice + overCprice
                    #price1 = basic + flowsummer1 + discount1 + overprice1
                    price = basic +  overprice
                    sameVprice += price
                    totalprice.append(price) 
                    capbilitySetUp.append(ls_Vn_n[m][0])
                    capbilitySetUp2.append(ls_Vn_n[m][1])
                    capbilitySetUp3.append(ls_Vn_n[m][2])
                    capbilitySetUp4.append(ls_Vn_n[m][3])
                else:
                    #基本電費
                    basic = ( 160.6 * ls_Vn_n[m][0] + 160.6 * ls_Vn_n[m][1] + 32.1 * ls_Vn_n[m][2] * max(( ls_Vn_n[m][2] + ls_Vn_n[m][3] - 0.5 * ( ls_Vn_n[m][0] + ls_Vn_n[m][1] )),0) ) * 0.98 * 1.15 #非夏月
                    #流動電費
                    #flowwinter1 = 2.78 * totalflow[k]['B'] + 1.65 * totalflow[k]['D'] + 1.22 * totalflow[k]['C']
                    #功率折扣費
                    #discount1 = ( basic + flowwinter1 ) * (80-95) / 1000 
                    #超約附加費
                    Eov1_1 = max((maxtotalflow[k]['B']-ls_Vn_n[m][0]),0)
                    Eov1_2 = max((maxtotalflow[k]['B']-ls_Vn_n[m][0]-ls_Vn_n[m][1]),0)
                    Eov1_4 = max((maxtotalflow[k]['D']-ls_Vn_n[m][0]-ls_Vn_n[m][1]-ls_Vn_n[m][3]),0)
                    Eov1_3 = max((maxtotalflow[k]['C']-ls_Vn_n[m][0]-ls_Vn_n[m][1]-ls_Vn_n[m][3]-ls_Vn_n[m][2]),0)

                    Eovc1_1 = Eov1_1
                    Eovc1_2 = max((Eov1_2-Eovc1_1),0)
                    Eovc1_4 = max((Eov1_4-max(Eovc1_1,Eovc1_2)),0)
                    Eovc1_3 = max((Eov1_3-max(Eovc1_1,Eovc1_2,Eovc1_4)),0)
                
                    overAprice = 2*160.6*max(min(Eovc1_1,(0.1*ls_Vn_n[m][0])),0) + 3*160.6*max((Eovc1_1-(0.1*ls_Vn_n[m][0])),0)
                    overBprice = 2*160.6*max(min(Eovc1_2,(0.1*ls_Vn_n[m][1])),0) + 3*160.6*max((Eovc1_2-(0.1*ls_Vn_n[m][1])),0) #非夏月
                    overDprice = 2*43.3*max(min(Eovc1_4,(0.1*ls_Vn_n[m][3])),0) + 3*43.3*max((Eovc1_4-(0.1*ls_Vn_n[m][3])),0)
                    overCprice = 2*43.3*max(min(Eovc1_3,(0.1*ls_Vn_n[m][2])),0) + 3*43.3*max((Eovc1_3-(0.1*ls_Vn_n[m][2])),0)
                    overprice = overAprice + overBprice + overDprice + overCprice
                    #price1 = basic + flowsummer1 + discount1 + overprice1
                    price = basic + overprice
                    sameVprice += price
                    totalprice.append(price) 
                    capbilitySetUp.append(ls_Vn_n[m][0])
                    capbilitySetUp2.append(ls_Vn_n[m][1])
                    capbilitySetUp3.append(ls_Vn_n[m][2])
                    capbilitySetUp4.append(ls_Vn_n[m][3])
                break
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
    
    standard2 = ls_Vn_n[0][1]
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

    standard3 = ls_Vn_n[0][2]
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

    standard4 = ls_Vn_n[0][3]
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
    
    futuretotal = sameVprice + cover + cover2 + cover3 + cover4
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
    global biggerThanKeyValueMonth
    change_month_index_only = [months[0] for months in biggerThanKeyValueMonth]

    # 創建點集合
    def rand_VN(Scale=False):
        vn_n = None
        if not Scale:
            for v in range(len(change_month_index_only) + 1):
                if vn_n == None:
                    vn_n = [[table1[0], np.random.rand(), np.random.rand(), np.random.rand()]]
                else:
                    vn_n.append([table1[change_month_index_only[v-1] - 1], np.random.rand(), np.random.rand(), np.random.rand()])
        else:
            for v in range(len(change_month_index_only) + 1):
                if vn_n == None:
                    vn_n = [[round(table1[0]), round(np.random.rand() * 10000), round(np.random.rand() * 10000), round(np.random.rand() * 10000)]]
                else:
                    vn_n.append([round(table1[change_month_index_only[v-1] - 1]), round(np.random.rand() * 10000), round(np.random.rand() * 10000), round(np.random.rand() * 10000)])
        return vn_n
    # 創造P
    p = None
    for i in range(n):
        if i == 0:
            p = [Position(ls_months=change_month_index_only, ls_Vn_n=rand_VN(Scale=True), futuretotal=fitnessFunction(ls_months=change_month_index_only, ls_Vn_n=rand_VN()))]
        else:
            p.append(Position(ls_months=change_month_index_only, ls_Vn_n=rand_VN(Scale=True), futuretotal=fitnessFunction(ls_months=change_month_index_only, ls_Vn_n=rand_VN())))

    # 創造V
    v = None
    def randomMonth():
        return [np.random.randn() for i in range(len(change_month_index_only))]
    def randomSpeed(Scale=False, Value=0):
        if not Scale:
            return [[np.random.rand(), np.random.rand(), np.random.rand(), np.random.rand()] for i in range(len(change_month_index_only)+1)]
        else:
            return [[np.random.rand()*Value, np.random.rand()*Value, np.random.rand()*Value, np.random.rand()*Value] for i in range(len(change_month_index_only)+1)]

    for i in range(n):
        if i == 0:
            v = [Position(ls_months=randomMonth(), ls_Vn_n=randomSpeed(Scale=True, Value=vmax), futuretotal=fitnessFunction(ls_months=randomMonth(), ls_Vn_n=randomSpeed()))]
        else:
            v.append(Position(ls_months=randomMonth(), ls_Vn_n=randomSpeed(Scale=True, Value=vmax), futuretotal=fitnessFunction(ls_months=randomMonth(), ls_Vn_n=randomSpeed())))

    pBest = copy.deepcopy(p)
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
            # 更新速度和位置
            vm = None
            vVn_n = None
            for k in range(len(change_month_index_only)):
                if k == 0:
                    vm = [w*v[j].ls_months[0]+c1*np.random.random()*(pBest[j].ls_months[0]-p[j].ls_months[0])+c2*np.random.random()*(gBest.ls_months[0]-p[j].ls_months[0])]
                    vVn_n = [[min(w*v[j].ls_Vn_n[k][0]+c1*np.random.random()*(pBest[j].ls_Vn_n[k][0]-p[j].ls_Vn_n[k][0])+c2*np.random.random()*(gBest.ls_Vn_n[k][0]-p[j].ls_Vn_n[k][0]), v1max)]]
                    vVn_n[0].append(min(w*v[j].ls_Vn_n[k][1]+c1*np.random.random()*(pBest[j].ls_Vn_n[k][1]-p[j].ls_Vn_n[k][1])+c2*np.random.random()*(gBest.ls_Vn_n[k][1]-p[j].ls_Vn_n[k][1]), v2max))
                    vVn_n[0].append(min(w*v[j].ls_Vn_n[k][2]+c1*np.random.random()*(pBest[j].ls_Vn_n[k][2]-p[j].ls_Vn_n[k][2])+c2*np.random.random()*(gBest.ls_Vn_n[k][2]-p[j].ls_Vn_n[k][2]), v3max))
                    vVn_n[0].append(min(w*v[j].ls_Vn_n[k][3]+c1*np.random.random()*(pBest[j].ls_Vn_n[k][3]-p[j].ls_Vn_n[k][3])+c2*np.random.random()*(gBest.ls_Vn_n[k][3]-p[j].ls_Vn_n[k][3]), v4max))
                else:
                    vm.append(w*v[j].ls_months[k]+c1*np.random.random()*(pBest[j].ls_months[k]-p[j].ls_months[k])+c2*np.random.random()*(gBest.ls_months[k]-p[j].ls_months[k]))
                    vVn_n.append([min(w*v[j].ls_Vn_n[k][0]+c1*np.random.random()*(pBest[j].ls_Vn_n[k][0]-p[j].ls_Vn_n[k][0])+c2*np.random.random()*(gBest.ls_Vn_n[k][0]-p[j].ls_Vn_n[k][0]), v1max)])
                    vVn_n[k].append(min(w*v[j].ls_Vn_n[k][1]+c1*np.random.random()*(pBest[j].ls_Vn_n[k][1]-p[j].ls_Vn_n[k][1])+c2*np.random.random()*(gBest.ls_Vn_n[k][1]-p[j].ls_Vn_n[k][1]), v2max))
                    vVn_n[k].append(min(w*v[j].ls_Vn_n[k][2]+c1*np.random.random()*(pBest[j].ls_Vn_n[k][2]-p[j].ls_Vn_n[k][2])+c2*np.random.random()*(gBest.ls_Vn_n[k][2]-p[j].ls_Vn_n[k][2]), v3max))
                    vVn_n[k].append(min(w*v[j].ls_Vn_n[k][3]+c1*np.random.random()*(pBest[j].ls_Vn_n[k][3]-p[j].ls_Vn_n[k][3])+c2*np.random.random()*(gBest.ls_Vn_n[k][3]-p[j].ls_Vn_n[k][3]), v4max))
                        
            vVn_n.append([min(w*v[j].ls_Vn_n[k][0]+c1*np.random.random()*(pBest[j].ls_Vn_n[k][0]-p[j].ls_Vn_n[k][0])+c2*np.random.random()*(gBest.ls_Vn_n[k][0]-p[j].ls_Vn_n[k][0]), v1max)])
            vVn_n[len(change_month_index_only)].append(min(w*v[j].ls_Vn_n[len(change_month_index_only)][1]+c1*np.random.random()*(pBest[j].ls_Vn_n[len(change_month_index_only)][1]-p[j].ls_Vn_n[len(change_month_index_only)][1])+c2*np.random.random()*(gBest.ls_Vn_n[len(change_month_index_only)][1]-p[j].ls_Vn_n[len(change_month_index_only)][1]), v2max))
            vVn_n[len(change_month_index_only)].append(min(w*v[j].ls_Vn_n[len(change_month_index_only)][2]+c1*np.random.random()*(pBest[j].ls_Vn_n[len(change_month_index_only)][2]-p[j].ls_Vn_n[len(change_month_index_only)][2])+c2*np.random.random()*(gBest.ls_Vn_n[len(change_month_index_only)][2]-p[j].ls_Vn_n[len(change_month_index_only)][2]), v3max))
            vVn_n[len(change_month_index_only)].append(min(w*v[j].ls_Vn_n[len(change_month_index_only)][3]+c1*np.random.random()*(pBest[j].ls_Vn_n[len(change_month_index_only)][3]-p[j].ls_Vn_n[len(change_month_index_only)][3])+c2*np.random.random()*(gBest.ls_Vn_n[len(change_month_index_only)][3]-p[j].ls_Vn_n[len(change_month_index_only)][3]), v4max))
              
            v[j] = Position(ls_months=vm, ls_Vn_n=vVn_n, futuretotal=fitnessFunction(ls_months=vm, ls_Vn_n=vVn_n)) 
            for k in range(len(v[j].ls_Vn_n)):
                for q in range(len(v[j].ls_Vn_n[0])):
                    p[j].ls_Vn_n[k][q] += v[j].ls_Vn_n[k][q] 
            p[j].futuretotal=fitnessFunction(p[j].ls_months,p[j].ls_Vn_n)

            # 越界判断
            for k in range(len(p[j].ls_Vn_n)):
                if p[j].ls_Vn_n[k][0] >= 85000:
                    p[j].ls_Vn_n[k][0] = 85000
                if p[j].ls_Vn_n[k][0] <= 70000:
                    p[j].ls_Vn_n[k][0] = 70000
                if p[j].ls_Vn_n[k][1] >= 5000:
                    p[j].ls_Vn_n[k][1] = 5000
                if p[j].ls_Vn_n[k][1] <= 0:
                    p[j].ls_Vn_n[k][1] = 0
                if p[j].ls_Vn_n[k][2] >= 5000:
                    p[j].ls_Vn_n[k][2] = 5000
                if p[j].ls_Vn_n[k][2] <= 0:
                    p[j].ls_Vn_n[k][2] = 0
                if p[j].ls_Vn_n[k][3] >= 5000:
                    p[j].ls_Vn_n[k][3] = 5000
                if p[j].ls_Vn_n[k][3] <= 0:
                    p[j].ls_Vn_n[k][3] = 0  
                
        # 更新個體極值和群體極值
        for j in range(n):
            if pBest[j].futuretotal > p[j].futuretotal:
                pBest[j]=copy.deepcopy(p[j])
            if gBest.futuretotal > p[j].futuretotal  :
                gBest=copy.deepcopy(p[j])

        print("====="+str(i+1)+"=====\ngBest:"+gBest.__str__())
    
    
    for k in gBest.ls_months:
        print(k)

    table = [['1'],['2'],['3'],['4'],['5'],['6'],['7'],['8'],['9'],['10'],['11'],['12'],['13'],['14'],['15'],['16'],['17'],['18'],['19'],['20'],['21'],['22'],['23'],['24']]
    
    mons_append_25 = gBest.ls_months.copy()
    mons_append_25.append(25)
    for k in range(24):
        for m in range(len(mons_append_25)):
            if k >= (mons_append_25[m] - 1):
                continue
            else:
                table[k].append(str(gBest.ls_Vn_n[m][0]))
                table[k].append(str(gBest.ls_Vn_n[m][1]))
                table[k].append(str(gBest.ls_Vn_n[m][2]))
                table[k].append(str(gBest.ls_Vn_n[m][3]))
                break
    
    for h in range(24):
        maxeachmonth = max(maxtotalflow[h], key=maxtotalflow[h].get)
        eachmonthmaxvalue = maxtotalflow[h][maxeachmonth]
        table[h].append(eachmonthmaxvalue)
    table[23].append(str(gBest.futuretotal))

    lst = None
    for t in gBest.ls_months:
        if lst == None:
            lst=[str(t)]
        else:
            lst.append(str(t))
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
    # change_month = change_month[-8:]
    change_month.sort(key=lambda x: x[0])    
    # print(change_month)
    keyValue = 1000
    biggerThanKeyValueMonth = []
    for i in range(len(change_month)):
        if change_month[i][1] >= keyValue:
            biggerThanKeyValueMonth.append(change_month[i])
    # print(biggerThanKeyValueMonth)
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