#servant
import socket              
import pygame
import time

pygame.init()

sock = socket.socket()
host = str(input("Enter host IP Address: "))
print("Host IP Address: ",host,"\n")
port = 80 #ESP32 Server Port     
sock.connect((host, port))
delay= 0.3

def main(): 
 
    joysticks = []
    Action="STOP"
    clock = pygame.time.Clock()
    keepPlaying = True
 
    for i in range(0, pygame.joystick.get_count()):
        joysticks.append(pygame.joystick.Joystick(i))
        joysticks[-1].init()
        print("Detected joystick '",joysticks[-1].get_name(),"'")

    while keepPlaying:
        clock.tick(60)
        #print(Action)
        if Action=="GO":
            sock.send(b'S\n')
            time.sleep(delay)

        elif Action=="go":
            sock.send(b's\n')
            time.sleep(delay)

        elif Action=="LEFT":
            sock.send(b'L\n')
            time.sleep(delay)

        elif Action=="left":
            sock.send(b'l\n')
            time.sleep(delay)

        elif Action=="RIGHT":
            sock.send(b'R\n')
            time.sleep(delay)

        elif Action=="right":
            sock.send(b'r\n')
            time.sleep(delay)

        elif Action=="STOP":
            sock.send(b'X\n')
            time.sleep(delay)

        elif Action=="stop":
            sock.send(b'x\n')
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

        elif Action=="Auto":
            sock.send(b'A\n')
            time.sleep(delay)

        elif Action=="Manual":
            sock.send(b'O\n')
            time.sleep(delay)

        elif Action=="Crazy":
            sock.send(b'C\n')
            time.sleep(delay)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Received event 'Quit', exiting.")
                keepPlaying = False

            elif event.type == pygame.JOYBUTTONDOWN:
                if event.type == pygame.JOYBUTTONDOWN:
                    if event.button ==1:
                        print("Auto")
                        #Action = "Auto"

                    elif event.button ==2:
                        print("Manual")
                        #Action = "Manual"

                    elif event.button ==7:
                            print("Received event 'Quit', exiting.")
                            keepPlaying = False

                    if Action != "Auto":
                        if event.button ==0:
                            print("STOP")
                            Action = "STOP"
                        elif event.button ==3:
                            print("Crazy")
                            Action = "Crazy"     
                        elif event.button ==4:
                            print("UP")
                            Action = "UP"
                        elif event.button ==5:
                            print("DOWN")
                            Action = "DOWN"
                        

            elif event.type == pygame.JOYBUTTONUP:
                if Action != "Auto":
                    if event.button ==4:
                        print("Middle")
                        Action = "Middle"
                    elif event.button ==5:
                        print("Middle")
                        Action = "Middle"  

            elif event.type == pygame.JOYAXISMOTION:
                if Action != "Auto":
                    if event.axis== 3:
                        if event.value<= -0.9:
                            print("GO")
                            Action="GO"
                    elif event.axis== 4:
                        if event.value>= 0.8:
                            print("RIGHT")
                            Action="RIGHT"
                        elif event.value<= -0.8:
                            print("LEFT")
                            Action="LEFT"

                    elif event.axis== 1:
                        if event.value<= -0.9:
                            print("go")
                            Action="go"
                    elif event.axis== 0:
                        if event.value>= 0.8:
                            print("right")
                            Action="right"
                        elif event.value<= -0.8:
                            print("left")
                            Action="left"

            elif event.type ==pygame.JOYHATMOTION:
                if Action != "Auto":
                    if event.value==(-1,0):
                        print("back")
                        Action = "back"
                        sock.send(b'B\n')
                    elif event.value==(1,0):
                        print("front")
                        Action = "front"
                        sock.send(b'Fn')

            

main()
sock.close()
pygame.quit()
