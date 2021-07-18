# -*- coding: utf-8 -*-
"""
Created on Fri May 22 23:25:18 2020

@author: -
"""

import pandas as pd
import numpy as np
import csv
def outputdatamoneydetail(): 
    global table
    for k in range (0,24):
        if totalflow[k]['A'] is not 0 and maxtotalflow[k]['A'] is not 0 :
            #基本電費
            basic1 = ( 217.3 * tryy[k][0] + 160.6 * tryy[k][1] + 43.4 * tryy[k][2] * max(( tryy[k][2] + tryy[k][3] - 0.5 * ( tryy[k][0] + tryy[k][1] )),0) ) * 0.98 * 1.15 #夏月
            basic.append(basic1)
            #流動電費
            flowsummer1 = 4.61 * totalflow[k]['A'] + 2.87 * totalflow[k]['B']  + 1.73 * totalflow[k]['D'] + 1.29 * totalflow[k]['C']
            #功率折扣費
            discount1 = ( basic1 + flowsummer1 ) * (80-95) / 1000 
            #超約附加費
            Eov1_1 = max((maxtotalflow[k]['A']-tryy[k][0]),0)
            Eov1_2 = max((maxtotalflow[k]['B']-tryy[k][0]-tryy[k][1]),0)
            Eov1_4 = max((maxtotalflow[k]['D']-tryy[k][0]-tryy[k][1]-tryy[k][3]),0)
            Eov1_3 = max((maxtotalflow[k]['C']-tryy[k][0]-tryy[k][1]-tryy[k][3]-tryy[k][2]),0)
    
            Eovc1_1 = Eov1_1
            Eovc1_2 = max((Eov1_2-Eovc1_1),0)
            Eovc1_4 = max((Eov1_4-max(Eovc1_1,Eovc1_2)),0)
            Eovc1_3 = max((Eov1_3-max(Eovc1_1,Eovc1_2,Eovc1_4)),0)
        
            overAprice1 = 2 * 217.3 * max(min(Eovc1_1,(0.1*tryy[k][0])),0) + 3*217.3*max((Eovc1_1-(0.1*tryy[k][0])),0)  #夏月
            overBprice1 = 2*160.6*max(min(Eovc1_2,(0.1*tryy[k][1])),0) + 3*160.6*max((Eovc1_2-(0.1*tryy[k][1])),0)
            overDprice1 = 2*43.3*max(min(Eovc1_4,(0.1*tryy[k][3])),0) + 3*43.3*max((Eovc1_4-(0.1*tryy[k][3])),0)
            overCprice1 = 2*43.3*max(min(Eovc1_3,(0.1*tryy[k][2])),0) + 3*43.3*max((Eovc1_3-(0.1*tryy[k][2])),0)
            overprice1 = overAprice1 + overBprice1 + overDprice1 + overCprice1
            overprice.append(overprice1)
            #price1 = basic1 + overprice1
            price1 = basic1 + flowsummer1 + discount1 + overprice1
            totalprice.append(price1) 
            table[k].append(basic1)
            table[k].append(overprice1)
        else:
            #基本電費
            basic1 = ( 160.6 * tryy[k][0] + 160.6 * tryy[k][1] + 32.1 * tryy[k][2] * max(( tryy[k][2] + tryy[k][3] - 0.5 * ( tryy[k][0] + tryy[k][1] )),0) ) * 0.98 * 1.15 #非夏月
            basic.append(basic1)
            #流動電費
            flowwinter1 = 2.78 * totalflow[k]['B'] + 1.65 * totalflow[k]['D'] + 1.22 * totalflow[k]['C']
            #功率折扣費
            discount1 = ( basic1 + flowwinter1 ) * (80-95) / 1000 
            #超約附加費
            Eov1_1 = max((maxtotalflow[k]['B']-tryy[k][0]),0)
            Eov1_2 = max((maxtotalflow[k]['B']-tryy[k][0]-tryy[k][1]),0)
            Eov1_4 = max((maxtotalflow[k]['D']-tryy[k][0]-tryy[k][1]-tryy[k][3]),0)
            Eov1_3 = max((maxtotalflow[k]['C']-tryy[k][0]-tryy[k][1]-tryy[k][3]-tryy[k][2]),0)
    
            Eovc1_1 = Eov1_1
            Eovc1_2 = max((Eov1_2-Eovc1_1),0)
            Eovc1_4 = max((Eov1_4-max(Eovc1_1,Eovc1_2)),0)
            Eovc1_3 = max((Eov1_3-max(Eovc1_1,Eovc1_2,Eovc1_4)),0)
            # Eovc1_2 = Eov1_2
            # Eovc1_4 = max((Eov1_4-Eovc1_2),0)
            # Eovc1_3 = max((Eov1_3-max(Eovc1_2,Eovc1_4)),0)
            
            overAprice1 = 2*160.6*max(min(Eovc1_1,(0.1*tryy[k][0])),0) + 3*160.6*max((Eovc1_1-(0.1*tryy[k][0])),0) #非夏月
            overBprice1 = 2*160.6*max(min(Eovc1_2,(0.1*tryy[k][1])),0) + 3*160.6*max((Eovc1_2-(0.1*tryy[k][1])),0) 
            overDprice1 = 2*43.3*max(min(Eovc1_4,(0.1*tryy[k][3])),0) + 3*43.3*max((Eovc1_4-(0.1*tryy[k][3])),0)
            overCprice1 = 2*43.3*max(min(Eovc1_3,(0.1*tryy[k][2])),0) + 3*43.3*max((Eovc1_3-(0.1*tryy[k][2])),0)
            overprice1 = overAprice1 + overBprice1 + overDprice1 + overCprice1
            #overprice1 = overBprice1 + overDprice1 + overCprice1
            overprice.append(overprice1)
            #price1 = basic1 + overprice1
            price1 = basic1 + flowwinter1 + discount1 + overprice1
            totalprice.append(price1) 
            table[k].append(basic1)
            table[k].append(overprice1)
    
    #print(w1valueee)
    
    
    capbilitySetUp2=[0,0,0,0,0,0,0,0,0,0,0,0]
    capbilitySetUp3=[0,0,0,0,0,0,0,0,0,0,0,0]
    capbilitySetUp4=[0,0,0,0,0,0,0,0,0,0,0,0]
    standard = capbilitySetUp[0]
    standard2 = capbilitySetUp2[0]
    standard3 = capbilitySetUp3[0]
    standard4 = capbilitySetUp4[0]

    #容量設置費_1
    spareSetUp = []
    setupEachMonth = []
    #lessThanStandard = 0
    #overThanStandard = 0
    cou_da = 0
    table[0].append(0)
    table[0].append(0)
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
        table[i+1].append(setupEachMonth[i])
        table[i+1].append(spareSetUp[i])
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
                bonusPrice += (-remainPrice[y])*(upperPosition[x] - remainPosition[y])
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
                bonusPrice += upperPrice[x]*(upperPosition[x] - remainPosition[y])
                remainTotalPrice = remainTotalPrice + upperPrice[x]
                upperTotalPrice = upperTotalPrice - upperPrice[x]
                remainPrice[y] = upperPrice[x] + remainPrice[y]
                x+=1
        else:
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
    i = 0
    for d in range(24):
        if table[d][4] != 0:
            table[d].append(maintainEachMonth[i])
            table[d].append(spareMaintain[i])
            i += 1
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
    table[-1].extend([None,None,cover])

    
    
    #容量設置費_2
    spareSetUp2 = []
    setupEachMonth2 = []
    for i in range(0, 11):
        lessThanStandard2 = 0
        overThanStandard2 = 0
        if capbilitySetUp2[i+1] > capbilitySetUp2[i]:
            if capbilitySetUp2[i+1] <= standard2:
                lessThanStandard2 += (capbilitySetUp2[i+1] - capbilitySetUp2[i])
            else:
                lessThanStandard2 += (standard2 - capbilitySetUp2[i])
                overThanStandard2 += (capbilitySetUp2[i+1] - standard2)
                standard2 = capbilitySetUp2[i+1]
        spareSetUp2.append(787.5*lessThanStandard2*0.25 + 0.15*787.5*overThanStandard2)
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
    for i in range(0, 11):
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
    if upperTotalPrice2 != 0:
        overPrice2 += upperTotalPrice2
    recover2 = []
    if len(setupEachMonth2)==len(maintainEachMonth2):
        for w2 in range(len(setupEachMonth2)) :
            if setupEachMonth2[w2] <= maintainEachMonth2[w2] :
                recover2.append(setupEachMonth2[w2])
            else :
                recover2.append(maintainEachMonth2[w2])
    totalrecover2 = sum(recover2)
    sparerecover2 = []
    if len(spareSetUp2)==len(spareMaintain2):
        for v2 in range(len(spareSetUp2)) :
            if spareSetUp2[v2] <= spareMaintain2[v2] :
                sparerecover2.append(spareSetUp2[v2])
            else :
                sparerecover2.append(spareMaintain2[v2])
    totalsparerecover2 = sum(sparerecover2)
    cover2 = totalrecover2 + totalsparerecover2
    
    
    #容量設置費_3
    spareSetUp3 = []
    setupEachMonth3 = []
    for i in range(0, 11):
        lessThanStandard3 = 0
        overThanStandard3 = 0
        if capbilitySetUp3[i+1] > capbilitySetUp3[i]:
            if capbilitySetUp3[i+1] <= standard3:
                lessThanStandard3 += (capbilitySetUp3[i+1] - capbilitySetUp3[i])
            else:
                lessThanStandard3 += (standard3 - capbilitySetUp3[i])
                overThanStandard3 += (capbilitySetUp3[i+1] - standard3)
                standard3 = capbilitySetUp3[i+1]
        spareSetUp3.append(210*lessThanStandard3*0.25 + 0.15*210*overThanStandard3)
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
    for i in range(0, 11):
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
    if upperTotalPrice3 != 0:
        overPrice3 += upperTotalPrice3
    recover3 = []
    if len(setupEachMonth3)==len(maintainEachMonth3):       
        for w3 in range(len(setupEachMonth3)) :
            if setupEachMonth3[w3] <= maintainEachMonth3[w3] :
                recover3.append(setupEachMonth3[w3])
            else :
                recover3.append(maintainEachMonth3[w3])
    totalrecover3 = sum(recover3)
    sparerecover3 = []
    if len(spareSetUp3)==len(spareMaintain3):
        for v3 in range(len(spareSetUp3)) :
            if spareSetUp3[v3] <= spareMaintain3[v3] :
                sparerecover3.append(spareSetUp3[v3])
            else :
                sparerecover3.append(spareMaintain3[v3])
    totalsparerecover3 = sum(sparerecover3)
    cover3 = totalrecover3 + totalsparerecover3
    
    
    #容量設置費_4
    spareSetUp4 = []
    setupEachMonth4 = []
    for i in range(0, 11):
        lessThanStandard4 = 0
        overThanStandard4 = 0
        if capbilitySetUp4[i+1] > capbilitySetUp4[i]:
            if capbilitySetUp4[i+1] <= standard4:
                lessThanStandard4 += (capbilitySetUp4[i+1] - capbilitySetUp4[i])
            else:
                lessThanStandard4 += (standard4 - capbilitySetUp4[i])
                overThanStandard4 += (capbilitySetUp4[i+1] - standard4)
                standard4 = capbilitySetUp4[i+1]
        spareSetUp4.append(210*lessThanStandard4*0.25 + 0.15*210*overThanStandard4)
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
    for i in range(0, 11):
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
    if upperTotalPrice4 != 0:
        overPrice4 += upperTotalPrice4
    recover4 = []
    if len(setupEachMonth4)==len(maintainEachMonth4):
        for w4 in range(len(setupEachMonth4)) :
            if setupEachMonth4[w4] <= maintainEachMonth4[w4] :
                recover4.append(setupEachMonth4[w4])
            else :
                recover4.append(maintainEachMonth4[w4])
    totalrecover4 = sum(recover4)
    sparerecover4 = []
    if len(spareSetUp4)==len(spareMaintain4):
        for v4 in range(len(spareSetUp4)) :
            if spareSetUp4[v4] <= spareMaintain4[v4] :
                sparerecover4.append(spareSetUp4[v4])
            else :
                sparerecover4.append(spareMaintain4[v4])
    totalsparerecover4 = sum(sparerecover4)
    cover4 = totalrecover4 + totalsparerecover4
    with open('moneyresultPredictOneYearOutputtest.csv','a',newline ='',encoding ='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['month','basic','over','setup','sparesetup','maintain','sparemaintain','subsidy'])
            writer.writerows(table)  
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
    

if __name__ == "__main__":
    df = pd.read_csv('df_final_2020_2022.csv')
    totalflow = [] #流動電費各時段總度數
    maxtotalflow = [] #各個月的各時段最大需量
    totalprice=[]
    basic = []
    overprice = []
    start = df['DateTime'][0]
    start = start.split("/", 2)
    st_month = int(start[1])
    start_year = int(start[0])
    end = df['DateTime'][df.shape[0]-1]
    end = end.split("/", 2)
    end_year = int(end[0])+1
    for year in range(start_year,end_year):
        if year == start_year :
            start_month = st_month
        else:
            start_month = 1
        for mmm in range(start_month,13):
            flowcost(str(year),str(mmm))
    outputdata = pd.read_csv('PredictOneYearOutputtest.csv')
    valueee = []
    w1valueee = [] 
    w1value=outputdata[['w1']].values
    wvalue=outputdata[['w1','w2','w3','w4']].values
    print(int((wvalue.shape[0]+1)/25))
    
    for d in range(int((wvalue.shape[0]+1)/25)):
        table = [['1'],['2'],['3'],['4'],['5'],['6'],['7'],['8'],['9'],['10'],['11'],['12'],['13'],['14'],['15'],['16'],['17'],['18'],['19'],['20'],['21'],['22'],['23'],['24']]
        valuee = wvalue[25*d:25*d+24]
        w1_value = w1value[25*d:25*d+24]
        for g in range(24):
            valuee[g] = list(map(float,valuee[g]))
            w1_value[g] = list(map(float,w1_value[g]))
            valueee.append(valuee[g])
            w1valueee.extend(w1_value[g])
        tryy = valueee[24*d:24*d+24]  
        capbilitySetUp=w1valueee[24*d:24*d+24] 
        outputdatamoneydetail()
        
        

    