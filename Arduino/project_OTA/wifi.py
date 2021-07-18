#servant
import socket              
import pygame
pygame.init()

sock = socket.socket()
host = "10.1.1.10"#ESP32 IP in local network
#host = "192.168.137.82"#ESP32 IP in local network
port = 80             #ESP32 Server Port     
sock.connect((host, port))

def main(): 
 
    joysticks = []
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
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Received event 'Quit', exiting.")
                keepPlaying = False

            elif event.type == pygame.JOYBUTTONDOWN:
                HoldButton=True

            elif event.type == pygame.JOYBUTTONUP:
                HoldButton=False
                WaitButton=0
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
        if WaitButton==3:
            if event.type == pygame.JOYBUTTONDOWN:
                if event.button ==0:
                    print("STOP")
                    sock.send(b'S\n')
                    HoldButton=False
                    WaitButton=0
                elif event.button ==3:
                    print("GO")
                    sock.send(b'O,1,1.0,0.9,2,\n')
                    HoldButton=False
                    WaitButton=0
                elif event.button ==2:
                    print("LEFT")
                    sock.send(b'L,3,1.0,0.7,-2,\n')
                    HoldButton=False
                    WaitButton=0
                elif event.button ==1:
                    print("RIGHT")
                    sock.send(b'R,3,1.0,0.7,-2,\n')
                    HoldButton=False
                    WaitButton=0
                elif event.button ==4:
                    print("UP")
                    sock.send(b'U\n')
                    HoldButton=False
                    WaitButton=0
                elif event.button ==5:
                    print("DOWN")
                    sock.send(b'D\n')
                    HoldButton=False
                    WaitButton=0
                elif event.button ==8:
                    print("back")
                    sock.send(b'B\n')
                    HoldButton=False
                    WaitButton=0
                elif event.button ==9:
                    print("front")
                    sock.send(b'F\n')
                    HoldButton=False
                    WaitButton=0
                elif event.button ==7:
                    print("Received event 'Quit', exiting.")
                    keepPlaying = False

            elif event.type == pygame.JOYHATMOTION:
                if event.value==(0,1):
                    print("go")
                    sock.send(b'O,1,1.6,0.6,2,\n')
                    HoldButton=False
                    WaitButton=0
                elif event.value==(-1,0):
                    print("left")
                    sock.send(b'L,1,1.0,0.5,-2,\n')
                    HoldButton=False
                    WaitButton=0
                elif event.value==(1,0):
                    print("right")
                    sock.send(b'R,1,1.0,0.5,-2,\n')
                    HoldButton=False
                    WaitButton=0
                elif event.value==(0,-1):
                    print("stop")
                    sock.send(b'S\n')
                    HoldButton=False
                    WaitButton=0
                else:
                    print("stop")
                    sock.send(b'S\n')
                    HoldButton=False
                    WaitButton=0
                
            else:
                WaitButton=0

               
main()
sock.close()
pygame.quit()
