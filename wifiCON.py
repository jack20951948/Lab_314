#servant
import socket              
import pygame
import time
pygame.init()

sock = socket.socket()
host = "10.1.1.10"#ESP32 IP in local network
#host = "192.168.137.82"#ESP32 IP in local network
port = 80             #ESP32 Server Port     
sock.connect((host, port))
delay= 0.3

def main(): 
 
    joysticks = []
    Action="STOP"
    clock = pygame.time.Clock()
    keepPlaying = True

    HoldButton=False
    WaitButton=0
 
    for i in range(0, pygame.joystick.get_count()):
        joysticks.append(pygame.joystick.Joystick(i))
        joysticks[-1].init()
        print("Detected joystick '",joysticks[-1].get_name(),"'")

    while keepPlaying:
        clock.tick(60)
        #print(Action)
        if Action=="GO":
            sock.send(b'O,1,1.6,0.6,-10,\n')
            time.sleep(delay)

        elif Action=="go":
            sock.send(b'O,1,1.6,0.3,-10,\n')
            time.sleep(delay)

        elif Action=="LEFT":
            sock.send(b'L,3,1.6,0.5,-2,\n')
            time.sleep(delay)

        elif Action=="left":
            sock.send(b'L,3,1.6,0.5,-2,\n')
            time.sleep(delay)

        elif Action=="RIGHT":
            sock.send(b'R,3,1.6,0.5,-2,\n')
            time.sleep(delay)

        elif Action=="right":
            sock.send(b'R,3,1.6,0.5,-2,\n')
            time.sleep(delay)

        elif Action=="STOP":
            sock.send(b'S\n')
            time.sleep(delay)

        elif Action=="stop":
            sock.send(b'S\n')
            time.sleep(delay)

        elif Action=="UP":
            sock.send(b'U\n')
            time.sleep(delay)

        elif Action=="Middle":
            sock.send(b'M\n')
            time.sleep(delay)

        elif Action=="DOWN":
            sock.send(b'D\n')
            time.sleep(delay)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Received event 'Quit', exiting.")
                keepPlaying = False

            elif event.type == pygame.JOYBUTTONDOWN:
                HoldButton=True

            elif event.type == pygame.JOYBUTTONUP:
                HoldButton=False
                WaitButton=0
                '''
                if event.button ==4:
                    print("Middle")
                    Action = "Middle"
                elif event.button ==5:
                    print("Middle")
                    Action = "Middle"
                '''

            elif event.type ==pygame.JOYHATMOTION:
                if event.value==(0,0) or event.value==(1,1) or event.value==(1,-1) or event.value==(-1,1):
                    HoldButton=False
                    WaitButton=0
                else:
                    HoldButton=True


        #ADD HOLD TIME
        if HoldButton is True:
            WaitButton+=1

        #READ HOLD
        if WaitButton==1:
            if event.type == pygame.JOYBUTTONDOWN:
                if event.button ==0:
                    print("STOP")
                    Action = "STOP"
                    HoldButton=False
                    WaitButton=0
                elif event.button ==3:
                    print("GO")
                    Action = "GO"
                    HoldButton=False
                    WaitButton=0
                elif event.button ==2:
                    print("LEFT")
                    Action = "LEFT"
                    HoldButton=False
                    WaitButton=0
                elif event.button ==1:
                    print("RIGHT")
                    Action = "RIGHT"
                    HoldButton=False
                    WaitButton=0
                elif event.button ==4:
                    print("UP")
                    Action = "UP"
                    HoldButton=False
                    WaitButton=0
                elif event.button ==5:
                    print("DOWN")
                    Action = "DOWN"
                    HoldButton=False
                    WaitButton=0
                elif event.button ==8:
                    print("back")
                    Action = "back"
                    sock.send(b'B\n')
                    HoldButton=False
                    WaitButton=0
                elif event.button ==9:
                    print("front")
                    Action = "front"
                    sock.send(b'F\n')
                    HoldButton=False
                    WaitButton=0
                elif event.button ==7:
                    print("Received event 'Quit', exiting.")
                    keepPlaying = False

            elif event.type == pygame.JOYHATMOTION:
                if event.value==(0,1):
                    print("go")
                    Action = "go"
                    HoldButton=False
                    WaitButton=0
                elif event.value==(-1,0):
                    print("left")
                    Action = "left"
                    HoldButton=False
                    WaitButton=0
                elif event.value==(1,0):
                    print("right")
                    Action = "right"
                    HoldButton=False
                    WaitButton=0
                elif event.value==(0,-1):
                    print("stop")
                    Action = "stop"
                    HoldButton=False
                    WaitButton=0
                else:
                    print("stop")
                    Action = "stop"
                    HoldButton=False
                    WaitButton=0
                
            else:
                WaitButton=0

main()
sock.close()
pygame.quit()
