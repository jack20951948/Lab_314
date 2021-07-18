# from vpython import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from mpl_toolkits.mplot3d import Axes3D
import sympy
import math
from scipy import signal
import sys
import time
import statistics
import random
import array

random.seed(time.time())

Nowfile = 2 ###從幾號檔案開始import
fileTotal = 5 ###import幾組資料

######################simulation parameter##########
g = 9.8            #重力加速度 9.8 m/s^2
size = 0.5         #球半徑 0.5 m
m = np.array([1, 1, 1])            #球質量1kg
air_drag_coe = 0.2  #水中阻力(與速率成正比)

vel_x = 0.0
vel_y = 0.0
vel_z = 0.0
pos_x = 0.0
pos_y = 0.0
pos_z = 0.0

dt = 1.0     #時間間隔 1 秒
####################################################

def dataConbining():
    u_data = None
    s_data = None
    for i in range(fileTotal):
        tmpdata = np.loadtxt("Lab_314/Lab_random_motion/randomData/head_u_{}.txt".format(i+Nowfile), delimiter="\t", dtype=float, skiprows=2)
        if u_data is None:
            u_data = tmpdata
        else:
            u_data = np.vstack((u_data, tmpdata))
    for i in range(fileTotal):
        tmpdata = np.loadtxt("Lab_314/Lab_random_motion/randomData/head_s_{}.txt".format(i+Nowfile), delimiter="\t", dtype=float, skiprows=2)
        if s_data is None:
            s_data = tmpdata
        else:
            s_data = np.vstack((s_data, tmpdata))
    data = dataProcessing(u_data, s_data)
    print("data:\n", data)
    return data

def dataProcessing(uData, sData):
    ul = uData.tolist()
    sl = sData.tolist()
    for i in range(len(ul)):
        ul[i][0] = i
        ul[i].append(sl[i][2])
    Data = np.asarray(ul)
    return Data

def plotData(data):
    plt.figure()
    plt.subplot(311)
    plt.plot([x[0] for x in data], [x[1] for x in data], color='b', label="Time - x")
    plt.ylabel('x(m)')
    plt.title("data Step - xy plot")
    plt.subplot(312)
    plt.plot([x[0] for x in data], [x[2] for x in data], color='g', label="Time - y")
    plt.ylabel('y(m)')
    plt.subplot(313)
    plt.plot([x[0] for x in data], [x[3] for x in data], color='r', label="Time - z")
    plt.xlabel('Time(sec.)')
    plt.ylabel('z(m)')
    plt.legend()
    # plt.show()

def plotRoute(data):
    plt.figure()
    plt.plot([x[1] for x in data], [x[2] for x in data], label="Motion Route",color='b')
    plt.xlabel('x(m)')
    plt.ylabel('y(m)')
    plt.title("Motion Route")
    plt.legend()
    # plt.show()

def plot3dRoute(Data):
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.plot([x[1] for x in Data],[x[2] for x in Data], [x[3] for x in Data], color='r')
    ax.set_xlabel('x(m)')
    ax.set_xlim(-0.64, 0.58)
    ax.set_ylabel('y(m)')
    ax.set_ylim(-0.31, 0.27)
    ax.set_zlabel('z(m)')
    ax.set_zlim(-0.016, 0.82)
    plt.title("3D Route")
    # plt.show()

def filter(data, axix, fs=1000, fc=30, order=5 ,plotData=False ,returnValue=True): #fs=>Sampling frequency, fc=>Cut-off frequency of the filter
    w = fc / (fs / 2) # Normalize the frequency
    b, a = signal.butter(order, w, 'low')
    output = signal.filtfilt(b, a, [x[axix] for x in data])
    if plotData == True:
        plt.plot([x[0] for x in data], output, label='filtered')
        plt.legend()
    if returnValue == True:
        return output
    else:
        pass

def Gradient(data):
    difData = conbine3toOne(np.gradient(data[:,1]), np.gradient(data[:,2]), np.gradient(data[:,3]))
    return difData

def filteTheData(data):
    filtedData = conbine3toOne(filter(data, 1, fc=70), filter(data, 2, fc=70), filter(data, 3, fc=70))
    return filtedData

def conbine3toOne(data1, data2, data3):
    Data = [[] * 4] * len(data1)
    for i in range(len(data1)):
        Data[i] = [i]
        Data[i].append(data1[i])
        Data[i].append(data2[i])
        Data[i].append(data3[i])
        Data_np = np.asarray(Data)
    return Data_np

def findCritical(data, bios=0.0005):
    peaks = []
    troughs = []
    for idx in range(1, len(data)-1):
        if data[idx-1] < data[idx] > data[idx+1]:
            if abs(data[idx]) >= bios:
                peaks.append(idx)
        if data[idx-1] > data[idx] < data[idx+1]:
            if abs(data[idx]) >= bios:
                troughs.append(idx)
    return peaks, troughs

def getCritical(data):
    peak1, troughs1 = findCritical(data[:,1])
    peak2, troughs2 = findCritical(data[:,2])
    peak3, troughs3 = findCritical(data[:,3])
    critical = peak1 + peak2 + peak3 + troughs1 + troughs2 + troughs3
    critical = np.unique(critical).tolist()
    critical.sort()
    print("criticalByOrder(step):\n", critical)

    peakvalue1 = []
    for i in peak1:
        peakvalue1.append(data[i,1])
    print("meanofP1:\n",statistics.mean(peakvalue1))



    return critical

def data2Direction(step, data, bias=0.001):
    action = []
    for i in range(len(data)):
        checkstep = 0
        for j in range(len(step)):
            if data[i,0] == step[j]:
                checkstep = 1
                if data[i,3] > bias:
                    if -bias < abs(data[i,1]) < bias and data[i,2] > bias:
                        speed = data2Speed(data[i])
                        action.append([step[j], 1, speed])
                        continue
                    if data[i,1] > bias and data[i,2] > bias:
                        speed = data2Speed(data[i])
                        action.append([step[j], 2, speed])
                        continue
                    if data[i,1] > bias and -bias < abs(data[i,2]) <(bias):
                        speed = data2Speed(data[i])
                        action.append([step[j], 3, speed])
                        continue
                    if data[i,1] > bias and data[i,2] < -bias:
                        speed = data2Speed(data[i])
                        action.append([step[j], 4, speed])
                        continue
                    if -bias < abs(data[i,1]) < bias and data[i,2] < bias:
                        speed = data2Speed(data[i])
                        action.append([step[j], 5, speed])
                        continue
                    if data[i,1] < -bias and data[i,2] < bias:
                        speed = data2Speed(data[i])
                        action.append([step[j], 6, speed])
                        continue
                    if data[i,1] < -bias and -bias < abs(data[i,2]) < bias:
                        speed = data2Speed(data[i])
                        action.append([step[j], 7, speed])
                        continue
                    if data[i,1] < -bias and data[i,2] > bias:
                        speed = data2Speed(data[i])
                        action.append([step[j], 8, speed])
                        continue
                    if -bias < abs(data[i,1]) < bias and -bias < abs(data[i,2]) < bias:
                        speed = data2Speed(data[i])
                        action.append([step[j], 25, speed])
                        continue
                if -bias < abs(data[i,3]) < bias:
                    if -bias < abs(data[i,1]) < bias and data[i,2] > bias:
                        speed = data2Speed(data[i])
                        action.append([step[j], 9, speed])
                        continue
                    if data[i,1] > bias and data[i,2] > bias:
                        speed = data2Speed(data[i])
                        action.append([step[j], 10, speed])
                        continue
                    if data[i,1] > bias and -bias < abs(data[i,2]) <(bias):
                        speed = data2Speed(data[i])
                        action.append([step[j], 11, speed])
                        continue
                    if data[i,1] > bias and data[i,2] < -bias:
                        speed = data2Speed(data[i])
                        action.append([step[j], 12, speed])
                        continue
                    if -bias < abs(data[i,1]) < bias and data[i,2] < bias:
                        speed = data2Speed(data[i])
                        action.append([step[j], 13, speed])
                        continue
                    if data[i,1] < -bias and data[i,2] < bias:
                        speed = data2Speed(data[i])
                        action.append([step[j], 14, speed])
                        continue
                    if data[i,1] < -bias and -bias < abs(data[i,2]) < bias:
                        speed = data2Speed(data[i])
                        action.append([step[j], 15, speed])
                        continue
                    if data[i,1] < -bias and data[i,2] > bias:
                        speed = data2Speed(data[i])
                        action.append([step[j], 16, speed])
                        continue
                if data[i,3] < bias:
                    if -bias < abs(data[i,1]) < bias and data[i,2] > bias:
                        speed = data2Speed(data[i])
                        action.append([step[j], 17, speed])
                        continue
                    if data[i,1] > bias and data[i,2] > bias:
                        speed = data2Speed(data[i])
                        action.append([step[j], 18, speed])
                        continue
                    if data[i,1] > bias and -bias < abs(data[i,2]) <(bias):
                        speed = data2Speed(data[i])
                        action.append([step[j], 19, speed])
                        continue
                    if data[i,1] > bias and data[i,2] < -bias:
                        speed = data2Speed(data[i])
                        action.append([step[j], 20, speed])
                        continue
                    if -bias < abs(data[i,1]) < bias and data[i,2] < bias:
                        speed = data2Speed(data[i])
                        action.append([step[j], 21, speed])
                        continue
                    if data[i,1] < -bias and data[i,2] < bias:
                        speed = data2Speed(data[i])
                        action.append([step[j], 22, speed])
                        continue
                    if data[i,1] < -bias and -bias < abs(data[i,2]) < bias:
                        speed = data2Speed(data[i])
                        action.append([step[j], 23, speed])
                        continue
                    if data[i,1] < -bias and data[i,2] > bias:
                        speed = data2Speed(data[i])
                        action.append([step[j], 24, speed])
                        continue
                    if -bias < abs(data[i,1]) < bias and -bias < abs(data[i,2]) < bias:
                        speed = data2Speed(data[i])
                        action.append([step[j], 26, speed])
                        continue
            else:
                pass
        if checkstep == 0:
            action.append([i, 0, 0])
    actionWithoutStep = []
    for x in action:
        actionWithoutStep.append(x[1])
    return action, actionWithoutStep

def data2Speed(data, bias1=0.0015,bias2=0.003 ,bias3=0.0045):
    if (pow(data[1], 2) + pow(data[2], 2) + pow(data[3], 2)) > pow(bias3, 2):
        return 2
    elif (pow(data[1], 2) + pow(data[2], 2) + pow(data[3], 2)) >= pow(bias2, 2) and (pow(data[1], 2) + pow(data[2], 2) + pow(data[3], 2)) <= pow(bias3, 2):
        return 1
    else:
        return 0

def num_to_string(num):
    numbers = {
        0 : "pass",
        1 : "NU",
        2 : "ENU",
        3 : "EU",
        4 : "ESU",
        5 : "SU",
        6 : "WSU",
        7 : "WU",
        8 : "WNU",
        9 : "N",
        10 : "EN",
        11 : "E",
        12 : "ES",
        13 : "S",
        14 : "WS",
        15 : "W",
        16 : "WN",
        17 : "ND",
        18 : "END",
        19 : "ED",
        20 : "ESD",
        21 : "SD",
        22: "WSD",
        23 : "WD",
        24 : "WND",
        25 : "U",
        26 : "D"
    }
    return numbers.get(num, None)

def transition_matrix(transitions):
    n = 1+ max(transitions) #number of states

    M = [[0]*n for _ in range(n)]

    for (i,j) in zip(transitions,transitions[1:]):
        M[i][j] += 1

    #now convert to probabilities:
    for row in M:
        s = sum(row)
        if s > 0:
            row[:] = [f/s for f in row]
    return M

def speed_probabilities(data):
    M = [[0]*3 for _ in range(27)]
    N = [[0]*3 for _ in range(27)]
    for i in data:
        if i[2] == 0:
            M[i[1]][0] += 1
        if i[2] == 1:
            M[i[1]][1] += 1
        if i[2] == 2:
            M[i[1]][2] += 1
    for i in range(len(M)):
        if sum(M[i][:]) != 0:
            N[i][0] = M[i][0]/sum(M[i][:])
            N[i][1] = M[i][1]/sum(M[i][:])
            N[i][2] = M[i][2]/sum(M[i][:])
    return N

def MotionAnimation(a, b, c):
    # rate(1/dt)    #每一秒跑 1000 次
    # ti += dt    #計時器
    global air_drag_coe, dt, vel_x, vel_y, vel_z, pos_x, pos_y, pos_z

    vel_x += a*dt - air_drag_coe*vel_x*dt
    vel_y += b*dt - air_drag_coe*vel_y*dt
    vel_z += c*dt - air_drag_coe*vel_z*dt

    pos_x += vel_x*dt
    pos_y += vel_y*dt
    pos_z += vel_z*dt

    vel = np.array([vel_x, vel_y, vel_z])
    pos = np.array([pos_x, pos_y, pos_z])
    print("vel: ", vel)
    print("pos: ", pos)
    return pos

def update_line(hl, new_data):
	xdata, ydata, zdata = hl._verts3d
	hl.set_xdata(list(np.append(xdata, new_data[0])))
	hl.set_ydata(list(np.append(ydata, new_data[1])))
	hl.set_3d_properties(list(np.append(zdata, new_data[2])))
	plt.draw()

def Avoidance():
    global pos_x, pos_y, pos_z, vel_x, vel_y, vel_z
    if pos_x < -0.59:
        return 11, 2
    if pos_x > 0.53:
        return 15, 2
    if pos_y < -0.26:
        return 9, 2
    if pos_y > 0.22:
        return 13, 2
    if pos_z < -0.368:
        return 1, 2
    if pos_z > 0.368:
        return 17, 2
    

def motionForecast(transitionMatrixM, transitionMatrixS):   ####馬爾可夫鏈預測模型

    map = plt.figure()
    # 動作量化
    acceleration = [[0, 0, 0],
                    [0, 1, 1], 
                    [1, 1, 1],
                    [1, 0, 1],
                    [1, -1, 1],
                    [0, -1, 1],
                    [-1, -1, 1],
                    [-1, 0, 1],
                    [-1, 1, 1],
                    [0, 1, 0], 
                    [1, 1, 0],
                    [1, 0, 0],
                    [1, -1, 0],
                    [0, -1, 0],
                    [-1, -1, 0],
                    [-1, 0, 0],
                    [-1, 1, 0],
                    [0, 1, -1], 
                    [1, 1, -1],
                    [1, 0, -1],
                    [1, -1, -1],
                    [0, -1, -1],
                    [-1, -1, -1],
                    [-1, 0, -1],
                    [-1, 1, -1],
                    [0, 0, 1],
                    [0, 0, -1]]
    map_ax = Axes3D(map)
    map_ax.autoscale(enable=True, axis='both', tight=True)
    # # # Setting the axes properties
    map_ax.set_xlim3d([-0.64, 0.58])
    map_ax.set_ylim3d([-0.31, 0.27])
    map_ax.set_zlim3d([-0.418, 0.418])

    hl, = map_ax.plot3D([0], [0], [0])

    # 選擇初始狀態 
    current_action = random.randint(0,24)  #25,26動作沒有直
    speed = 0
    while current_action >= 0 and current_action != 23 and current_action != 7: # 7, 23動作沒有直
        if pos_x >= -0.59 and pos_x <= 0.53 and pos_y >= -0.26 and pos_y <= 0.22 and pos_z >= -0.368 and pos_z <= 0.368:
            Random = random.randint(0,99)
            Prob = 0
            for NA in range(len(transitionMatrixM)):
                if transitionMatrixM[current_action][NA] > 0:
                    Prob = Prob + transitionMatrixM[current_action][NA]*100
                    if Random < Prob:
                        current_action = NA
                        break
            
            Random = random.randint(0,99)
            Prob = 0
            for speed in range(3):
                if transitionMatrixS[current_action][speed]*100 > 0:
                    Prob = Prob + transitionMatrixS[current_action][speed]*100
                    if Random < Prob:
                        print("Action: ", current_action, "Speed: ", speed)
                        break
        else:
            current_action, speed = Avoidance()
            print("Action: ", current_action, "Speed: ", speed, "Avoidance............................................................................................")

        a = acceleration[current_action][0] * (speed+1) * 0.0015
        b = acceleration[current_action][1] * (speed+1) * 0.0015
        c = acceleration[current_action][2] * (speed+1) * 0.0015

        now_pos = MotionAnimation(a, b, c)
        now_pos = list(now_pos)

        update_line(hl, (now_pos[0],now_pos[1],now_pos[2]))
        plt.show(block=False)
        plt.pause(0.001)

    print("Action is nill")


if __name__ == "__main__":
    data = dataConbining()
    graData = Gradient(data)
    gradata2 = Gradient(graData)

    filtedData = filteTheData(data)
    graFilData = Gradient(filtedData)
    graFilData2 = Gradient(graFilData)

    plotRoute(data)
    plotData(data)
    plotData(filtedData)
    # plotData(graData)
    plotData(graFilData)
    # plotData(gradata2)
    plotData(graFilData2)

    critical = getCritical(graFilData2)
    action, actionWithoutStep = data2Direction(critical, graFilData2)

    print("action(step, action, speed):\n", action)
    print("actionWithoutStep:\n", actionWithoutStep)

    listAction = []
    [listAction.append(i) for i in actionWithoutStep if not i in listAction]
    listAction.sort()
    print("listAction:\n", listAction)

    # plot3dRoute(data)
    # plotRoute(filtedData)
    plot3dRoute(filtedData)
    plt.show()

    m = transition_matrix(actionWithoutStep)
    print("Posibitity:")
    for row in m: print(' '.join('{0:.2f}'.format(x) for x in row))
    # print(m)

    s = speed_probabilities(action)
    print("speed_Posibitity:")
    for row in s: print(' '.join('{0:.2f}'.format(x) for x in row))

    print("\nAction-predict begin......")
    motionForecast(m, s)


#############################################驗證馬爾可夫鏈#####################################

    # # 記錄每次的 activityList 
    # list_activity = [] 
    # count = 0 
    # # `range` 從第一個參數開始數起，一直到第二個參數（不包含） 
    # for iterations in range(1,10000): 
    #     list_activity.append(motionForecast(2, transitionName, transitionMatrix)) 
    # # 查看記錄到的所有 `activityList` 
    # #print(list_activity) 
    # # 遍歷列表，得到所有最終狀態是跑步的 activityList 
    # for smaller_list in list_activity: 
    #     if(smaller_list[2] == "Run"): 
    #         count += 1 
    # # 計算從睡覺狀態開始到跑步狀態結束的機率 
    # percentage = (count/10000) * 100 
    # print("The probability of starting at state:'Sleep' and ending at state:'Run'= " + str(percentage) + "%")


