import os,sys,time,signal
import numpy as np
from colorama import *
from people import *
from takeinput import *
import color
class Board:
    ''' contains the design of self.board'''
    #full self.board
    def __init__(self):
        self.board = np.ones((30,400),str)
        self.board[:] = "*"
        self.mov=0
        
        #first screen
        for j in  range(2,28):
            self.board[j][4:496]="-" #setting background
        for j in range(23,28):
            self.board[j][47:51]="#"  #setting tunnels

        self.board[23][80:96]="*"
        #clouds
        for j in range(4,8):
            for i in range(30,280):
                if i%20 < 5:
                    self.board[j][i] = "^"
                    if (j==4 or j==7) and (i%20==0 or i%20==4):
                        self.board[j][i]="-"
        #second screen
        for j in range(100,200):
            if j%20 < 4:
                if j%20 == 1 or j%20 ==2:
                    self.board[21][j]="$"
                    self.board[22][j]="$"                    #Setting bricks with coins
                    self.board[16][j+7]="$"
                    self.board[17][j+7]="$"
                else:
                    self.board[21][j]="B"
                    self.board[22][j]="B"                    #Setting solid bricks
                    self.board[16][j+7]="B"
                    self.board[17][j+7]="B"
        for j in range(23,28):
            self.board[j][190:194]="#"
        self.board[23][195:204]="*"
        self.board[23][152:160]="*"                          #Setting random paths 
        self.board[23][130:139]="*"
        for j in range(26,30):
            self.board[j][170:174]=" "
        
        #3rd screen
        for j in range(200,280):
            if j%15 < 4:
                if j%15 == 1 or j%15 == 2:
                    self.board[21][j]="$"
                    self.board[22][j]="$"
                    self.board[13][j+7]="$"
                    self.board[14][j+7]="$"
                else:
                    self.board[21][j]="B"
                    self.board[22][j]="B"
                    self.board[13][j+7]="B"
                    self.board[14][j+7]="B"
        self.board[21][226:228]="?"
        self.board[22][226:228]="?"
        for j in range(23,28):
            self.board[j][250:254]="#"
            self.board[j][279:282]="#"

        self.board[21][230:240] = "*"
        self.board[18][275:284] = "*"
        
        for j in range(26,30):
            self.board[j][217:221]=" "
            self.board[j][254:258]=" "

        for j in range(12,30):
            self.board[j][297:299] = "#"
        for j in range(13,17):
            self.board[j][296+13-j] = "#" 
        self.board[17][292:297] = "# "

        for j in range(6,14):
            self.board[j][310]="#"
            self.board[j][313]="#"
        self.board[13][313:319]="#" #L
        self.board[11][310:319]="#"
        self.board[12][313]="-"
        for j in range(6,14):
            self.board[j][320]="#"
            self.board[j][322]="#"
        self.board[6][320:326]="#"
        self.board[7][320:326]="#"
        self.board[9][322:326]="#" #E
        self.board[12][320:326]="#"
        self.board[13][320:326]="#"
        for j in range(6,14):
            self.board[j][324+j]="#" #V
            self.board[j][352-j]="#"
        for j in range(6,14):
            self.board[j][350]="#"
            self.board[j][352]="#"
        self.board[6][350:356]="#" #E
        self.board[7][350:356]="#"
        self.board[9][352:356]="#"
        self.board[12][350:356]="#"
        self.board[13][350:356]="#"
        for j in range(6,14):
            self.board[j][365]="#"
            self.board[j][368]="#"
        self.board[13][368:374]="#" #L
        self.board[11][365:374]="#"
        self.board[12][368]="-"
        for j in range(15,23):
            self.board[j][310]="#"   #U
            self.board[j][316]="#"
        self.board[22][310:316]="#"
        for j in range(15,23):
            self.board[j][324]="#"
        self.board[15][324:328]="#"
        self.board[18][324:328]="#"  #P
        self.board[16][327]="#"
        self.board[17][327]="#"
#function to print self.board
    def boardprint(self): 
        np.set_printoptions(linewidth=1000,threshold=np.nan)
        sys.stdout.flush()
        for row in range(30):
            for column in range(0+self.mov,self.mov+100):
                sys.stdout.write(color.colorchoice(self.board[row,column]))
                sys.stdout.write(" ")
            sys.stdout.write("\n")
        #print(str(self.self.board[:,0+self.mov:self.mov+100]).replace('.','').replace('b','').replace('\'','').replace('[','').replace(']',''))
        print("lives :",Mario.life)
        print("Coins:",Mario.coins_col,"Points:",Mario.points)
        print("d->right\na->left\nb->bullet\n\nsw->jump\ndw->rjump\naw->ljump\n\nq->quit")
    
    def over(self):
        print(color.Col.Green + "  _   _   _  _ _    _   _ _ \n",
            " / _| /_\ |  \/  | __|  / _ \ \ / / __| _ \\\n",
            "| ( |/ _ \| |\/| | |  | () \ V /| _||   /\n",
            " \___/_/ \_\_|  |_|___|  \___/ \_/ |___|_|_\\\n")

class Leveltwo(Board):
    def __init__(self):
        super().__init__()
        self.mov = 0
        for j in range(8,11):
            self.board[j][100:150]="#"
            self.board[j][210:245]="#"
        for j in range(3,27):
            self.board[j][303:400]="-"
        for j in range(7,14):
            self.board[j][310]="#"
        for j in range(14,10,-1):
            self.board[j][301+j]="#"
            self.board[j][330-j]="#"
        for j in range(7,14):
            self.board[j][321]="#"
        for j in range(8,14):
            self.board[j][326]="#"
            self.board[j][332]="#"
        self.board[8][326:332]="#"
        self.board[13][326:332]="#"
        for j in range(7,14):
            self.board[j][336]="#"
            self.board[j][345]="#"
            self.board[j][330+j]="#"
    def boardprint(self):
        np.set_printoptions(linewidth=1000,threshold=np.nan)
        sys.stdout.flush()
        for row in range(30):
            for column in range(0+self.mov,self.mov+100):
                sys.stdout.write(color.choicetwo(self.board[row,column]))
                sys.stdout.write(" ")
            sys.stdout.write("\n")
        #print(str(self.self.board[:,0+self.mov:self.mov+100]).replace('.','').replace('b','').replace('\'','').replace('[','').replace(']',''))
        print("lives :",Mario.life)
        print("Coins:",Mario.coins_col,"Points:",Mario.points)
        print("d->right\na->left\nb->bullet\n\nsw->jump\ndw->rjump\naw->ljump\n\nq->quit")
