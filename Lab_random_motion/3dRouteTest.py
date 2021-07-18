from vpython import *

data = [[0, 0, 0, 0], [1, 1, 0, 3], [2, 1, 1, 3], [3, 0, 0, 2], [4, 0, 0, 0], [5, 0, 1, 3], [6, 0, 0, 0], [7, 0, 2, 1], [8, 0, 0, 0], [9, 0, 0, 1], [10, 0, 0, 0]]

g = 9.8            #重力加速度 9.8 m/s^2
size = 0.5         #球半徑 0.5 m
height = 15.0      #球初始高度 15 m
m = 1.0            #球質量1kg
air_drag_coe = 0.2 #空氣阻力(與速率成正比)

scene = canvas(width=600, height=600,x=0, y=0, center = vector(0,height/2,0)) #設定畫面
floor = box(length=20, height=0.01, width=10, color=color.green)  	#畫地板
ball = sphere(radius = size, color=color.yellow, make_trail= True, trail_type="points", interval=100) 	#畫球

ball.pos = vector(0, height, 0)    #球初始位置
ball.v = vector(0, 0, 0)           #球初速 

dt = 1	#時間間隔 1 秒
t = 0.0		#模擬初始時間為0秒

for a in data:
    rate(1)    #每一秒跑 1000 次
    t = t + dt    #計時器
    print(type(vector(a[1],a[2],a[3])))
    ball.a = vector(a[1],a[2],a[3])/m            #球的加速度
    ball.v += ball.a*dt - air_drag_coe * ball.v * dt          #球的末速度 = 前一刻速度 + 加速度*時間間隔 - 空氣阻力
    ball.pos += ball.v * dt    #球的末位置 = 前一刻位置 + 速度*時間間隔

    print(a[1])
    # if ball.pos.y <= size and ball.v.y < 0:    #條件：球心高度小於球半徑且速度沿-y軸
    #     ball.v.y = - ball.v.y    #條件成立則球的速度加一負號表示反彈
    for i in range(10000000):
        pass
    
# print (t, ball.v)