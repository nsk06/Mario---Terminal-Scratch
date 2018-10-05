import os,sys,termios,time,random,tty
from colorama import *
from takeinput import *
from board import Board
class Start:
    '''start screen for game'''
    start = [[] for i in range(0,20)]
    boundary = ["x" for i in range(0,50)]
    innerwall = []
    usecase = []
    for i in range(0,50):
        if i<4 or i>46:
            innerwall.append("x")
            usecase.append("x")
        else:
            innerwall.append(" ")
            usecase.append(" ")
    u1 = usecase[:]
    u2 = usecase[:]
    u3 = usecase[:]
    usecase[20:25] = "S","U","P","E","R"                        
    u1[20:25] = "M","A","R","I","O"
    u2[20:28] = "1"," ","P","L","A","Y","E","R"
    #u3[20:28] = "2"," ","P","L","A","Y","E","R"
    for i in range(0,20):
        if i <2 or i>17:
            start[i] = boundary[:]
        else:
            start[i] = innerwall[:]
    start[7] = usecase[:]
    start[9] = u1[:]
    start[11] = u2
    start[13] = u3
    start[11][18] = ">"
    os.system("aplay ./sounds/smb_world_clear.wav &")               #opening sound play
    time.sleep(.02)
    def pri(self):
        temp = ['' for i in range(0, 50)]
        for j in range(0, 20):
            for i in range(0, 50):
                temp[j] = temp[j] + self.start[j][i]
        for i in range(0,20):
            if temp[i] == ''.join(self.boundary):
                print(Back.RED,temp[i],end="")
                print(Style.RESET_ALL)
            else:
                print(Back.BLUE,temp[i])
        print("Press q to quit\nPress p to play")
s = Start()
i=0
os.system('clear')
s.pri()
if __name__ == "__main__":
    while True:
        char = user_input()
        if char == "w":
            s.start[13][18] = " "
            os.system('clear')
            s.start[11][18] = ">"
            s.pri()
        elif char == "s":
            s.start[11][18] = " "
            os.system('clear')
            s.start[13][18] = ">"
            s.pri()
        elif char == "p":
            os.system('clear')
            exec(open('play.py').read())
        elif char == "q":
            quit()