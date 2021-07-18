import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import sympy
import math
from scipy import signal

Nowfile = 2 ###測試檔名為head_u_2_2和head_s_2_2

fileTotal = 1

def dataConbining():
    u_data = None
    s_data = None
    for i in range(fileTotal):
        tmpdata = np.loadtxt("Lab_314/Lab_random_motion/head_u_2_{}.txt".format(i+Nowfile), delimiter="\t", dtype=float, skiprows=2)
        if u_data is None:
            u_data = tmpdata
        else:
            u_data = np.vstack((u_data, tmpdata))
    for i in range(fileTotal):
        tmpdata = np.loadtxt("Lab_314/Lab_random_motion/head_s_2_{}.txt".format(i+Nowfile), delimiter="\t", dtype=float, skiprows=2)
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
    data_li_1 = []
    for i in range(len(data)):
        data_li_1.append(data[i][1])
    data_n1 = np.asarray(data_li_1)
    dataDiff = np.gradient(data_n1)

    data_li_2 = []
    for i in range(len(data)):
        data_li_2.append(data[i][2])
    data_n2 = np.asarray(data_li_2)
    dataDiff2 = np.gradient(data_n2)

    data_li_3 = []
    for i in range(len(data)):
        data_li_3.append(data[i][3])
    data_n3 = np.asarray(data_li_3)
    dataDiff3 = np.gradient(data_n3)
    difData = conbine3toOne(dataDiff, dataDiff2, dataDiff3)
    return difData

def filteTheData(data):
    filtedDataX = filter(data, 1, fc=70)
    filtedDataY = filter(data, 2, fc=70)
    filtedDataZ = filter(data, 3, fc=70)
    filtedData = conbine3toOne(filtedDataX, filtedDataY, filtedDataZ)
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

def findCritical(data, bios=0.001):
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

def data2Direction(step, data, bias=0.001):
    action = []
    for i in range(len(data)):
        for j in range(len(step)):
            if data[i,0] == step[j]:
                if data[i,3] > bias:
                    if -bias < abs(data[i,1]) < bias and data[i,2] > bias:
                        action.append([step[j], 1])
                    if data[i,1] > bias and data[i,2] > bias:
                        action.append([step[j], 2])
                    if data[i,1] > bias and -bias < abs(data[i,2]) <(bias):
                        action.append([step[j], 3])
                    if data[i,1] > bias and data[i,2] < -bias:
                        action.append([step[j], 4])
                    if -bias < abs(data[i,1]) < bias and data[i,2] < bias:
                        action.append([step[j], 5])
                    if data[i,1] < -bias and data[i,2] < bias:
                        action.append([step[j], 6])
                    if data[i,1] < -bias and -bias < abs(data[i,2]) < bias:
                        action.append([step[j], 7])
                    if data[i,1] < -bias and data[i,2] > bias:
                        action.append([step[j], 8])
                    if -bias < abs(data[i,1]) < bias and -bias < abs(data[i,2]) < bias:
                        action.append([step[j], 25])
                if -bias < abs(data[i,3]) < bias:
                    if -bias < abs(data[i,1]) < bias and data[i,2] > bias:
                        action.append([step[j], 9])
                    if data[i,1] > bias and data[i,2] > bias:
                        action.append([step[j], 10])
                    if data[i,1] > bias and -bias < abs(data[i,2]) <(bias):
                        action.append([step[j], 11])
                    if data[i,1] > bias and data[i,2] < -bias:
                        action.append([step[j], 12])
                    if -bias < abs(data[i,1]) < bias and data[i,2] < bias:
                        action.append([step[j], 13])
                    if data[i,1] < -bias and data[i,2] < bias:
                        action.append([step[j], 14])
                    if data[i,1] < -bias and -bias < abs(data[i,2]) < bias:
                        action.append([step[j], 15])
                    if data[i,1] < -bias and data[i,2] > bias:
                        action.append([step[j], 16])
                if data[i,3] < bias:
                    if -bias < abs(data[i,1]) < bias and data[i,2] > bias:
                        action.append([step[j], 17])
                    if data[i,1] > bias and data[i,2] > bias:
                        action.append([step[j], 18])
                    if data[i,1] > bias and -bias < abs(data[i,2]) <(bias):
                        action.append([step[j], 19])
                    if data[i,1] > bias and data[i,2] < -bias:
                        action.append([step[j], 20])
                    if -bias < abs(data[i,1]) < bias and data[i,2] < bias:
                        action.append([step[j], 21])
                    if data[i,1] < -bias and data[i,2] < bias:
                        action.append([step[j], 22])
                    if data[i,1] < -bias and -bias < abs(data[i,2]) < bias:
                        action.append([step[j], 23])
                    if data[i,1] < -bias and data[i,2] > bias:
                        action.append([step[j], 24])
                    if -bias < abs(data[i,1]) < bias and -bias < abs(data[i,2]) < bias:
                        action.append([step[j], 26])
                # continue
            # else:
            #     action.append([i, 0])
                # break
    print("action:\n", action)
    return action


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


if __name__ == "__main__":
    data = dataConbining()
    # plotRoute(data)
    # plotData(data)
    graData = Gradient(data)

    filtedData = filteTheData(data)
    graFilData = Gradient(filtedData)

    # plotData(filtedData)
    # plotData(graData)
    plotData(graFilData)

    gradata2 = Gradient(graData)
    graFilData2 = Gradient(graFilData)

    # plotData(gradata2)
    plotData(graFilData2)

############################################################
    peak1, troughs1 = findCritical(graFilData2[:,1])
    peak2, troughs2 = findCritical(graFilData2[:,2])
    peak3, troughs3 = findCritical(graFilData2[:,3])
    critical = peak1 + peak2 + peak3 + troughs1 + troughs2 + troughs3
    critical.sort()
    print("critical:", critical)

    action = data2Direction(critical, graFilData2)
    action_li = []
    for index, x in enumerate(action):
        action_li.append(x[1])
    print(action_li)
    l2 = []
    [l2.append(i) for i in action_li if not i in l2]
    l2.sort()
    print(l2)
############################################################







    # plot3dRoute(data)
    plotRoute(filtedData)
    plot3dRoute(filtedData)
    plt.show()


    t = [1,1,2,6,8,5,5,7,8,8,1,1,4,5,5,0,0,0,1,1,4,4,5,1,3,3,4,5,4,1,1]
    m = transition_matrix(t)
    for row in m: print(' '.join('{0:.2f}'.format(x) for x in row))


