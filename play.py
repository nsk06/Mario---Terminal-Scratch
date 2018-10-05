import os,sys,tty,termios,signal
from people import *
from board import *
from takeinput import *
from objects import *
Board = Leveltwo()
class Game:
    '''main Game class'''
    #These check for obstructions in the path of mario while moving linearly or while jumping
    level = 1
    mdetl,mdetr,edetl,edetr = "none" 
    mjumpcol = 0
    #This function draws mario on board after every change
    def mariomove(self,t):
        x = Mario.x_pos
        y = Mario.y_pos
        Board.board[y,x],Board.board[y,x+1],Board.board[y,x+2] = 'o','-','o'
        Board.board[y+1,x],Board.board[y+1,x+1],Board.board[y+1,x+2] = '-','|','-'
        Board.board[y+2,x],Board.board[y+2,x+1],Board.board[y+2,x+2] = '/'," ","/"
        if t==1:
            Board.mov += 1
        elif t==0:
            Board.mov -=1
    #This function draws enemies
    def enemymove(self):
        x = enemy.x_pos
        y = enemy.y_pos
        Board.board[y,x],Board.board[y,x+1],Board.board[y,x+2] = '@','_','@'
        Board.board[y+1,x],Board.board[y+1,x+1],Board.board[y+1,x+2] = '|',' ','|'
    def bossmove(self):
        x = Boss.x_pos
        y = Boss.y_pos
        Board.board[y,x],Board.board[y,x+1],Board.board[y,x+2] = '@','@','@'
        Board.board[y+1,x],Board.board[y+1,x+1],Board.board[y+1,x+2] = '|','X','|'
    #This function removes the previous instance of mario from screen
    def removeprev(self):
        x = Mario.x_pos
        y = Mario.y_pos
        Board.board[y,x],Board.board[y,x+1],Board.board[y,x+2] = "-"*3
        Board.board[y+1,x],Board.board[y+1,x+1],Board.board[y+1,x+2] = "-"*3
        Board.board[y+2,x],Board.board[y+2,x+1],Board.board[y+2,x+2] = "-"*3
    #This function removes the previous instance of enemies from screen
    def enemiesclear(self,enemy):
        x = enemy.x_pos
        y = enemy.y_pos
        Board.board[y,x],Board.board[y,x+1],Board.board[y,x+2] = "-"*3
        Board.board[y+1,x],Board.board[y+1,x+1],Board.board[y+1,x+2] = "-"*3
        if enemy.toremove == 1:
            enemies.remove(enemy)
    def removeboss(self):
        x = Boss.x_pos
        y = Boss.y_pos
        Board.board[y,x],Board.board[y,x+1],Board.board[y,x+2] = "-"*3
        Board.board[y+1,x],Board.board[y+1,x+1],Board.board[y+1,x+2] = "-"*3
    #This draws bullet on board
    def showbul(self,bul):
        x = bul.x_pos
        y = bul.y_pos
        Board.board[y][x] = ">"
    # Clear bullets previous position
    def bulclear(self,bul):
        x = bul.x_pos
        y = bul.y_pos
        Board.board[y][x] = "-"
    #This kills the enemy from bullet
    def bulkill(self,bul):
        x = bul.x_pos
        y = bul.y_pos
        if Board.board[y][x+1] == "@":
            for enemy in enemies:
                if Board.board[enemy.y_pos][enemy.x_pos-1] == ">":
                    Mario.points += 100
                    self.enemiesclear(enemy)
                    enemy.toremove = 1
                    enemies.remove(enemy)
                    os.system("aplay ./sounds/smb_stomp.wav &")
                    time.sleep(.005)
            if Board.board[y][x+2] == "@" and Board.board[y][x+3]== "@":
                Boss.life-=1
                Mario.points += 500
    #detect for obstructuons in way of mario
    def detect(self):
        x = Mario.x_pos
        y = Mario.y_pos
        if (Mario.x_pos < 10 or Board.board[y][x-1] != "-" or
             Board.board[y+1][x-1] != "-" or Board.board[y+2][x-1] != "-"):
            if (Board.board[y][x-1] == " " or Board.board[y+1][x-1] == " "
                 or Board.board[y+2][x-1] == " "):
                pass
            else:
                self.mdetl = "obsl"
        else:
            self.mdetl = "none"
        if (Board.board[y][x+3] != "-"  or Board.board[y+1][x+3] != "-"
             or Board.board[y+2][x+3] != "-") :
            if  (Board.board[y][x+3] == " " or Board.board[y+1][x+3] == " "
                 or Board.board[y+2][x+3] == " "):
                pass
            else:
                self.mdetr = "obsr"
        else:
            self.mdetr = "none"
    #detect for obstruction in way of enemies
    def edetect(self):
        x = enemy.x_pos
        y = enemy.y_pos
        if enemy.x_pos < 10 or Board.board[y][x-1] != "-" or Board.board[y+1][x-1] != "-":
            if Board.board[y][x-1] == " " or Board.board[y+1][x-1] == " ":
                enemy.toremove =1
            elif Board.board[y][x-1] == "-" and Board.board[y+1][x-1] == "/":
                Mario.life-=1
                os.system("aplay ./sounds/smb_mariodie.wav")
                os.system('clear')
            else:
                self.edetl = "obstl"
                enemy.speed = -1
        else:
            self.edetl = "none"
        if Board.board[y][x+3] != "-" or Board.board[y+1][x+3] != "-":
            if Board.board[y][x+3] == " " or Board.board[y+1][x+3] == " ":
                enemy.toremove=1
            elif Board.board[y][x+3] == "-" or Board.board[y+1][x+3] == "/":
                Mario.life-=1
                os.system("aplay ./sounds/smb_mariodie.wav") 
                os.system('clear')
            else:
                self.edetr = "obstl"
                enemy.speed = 1
        else:
            self.edetr = "none"
    #check for obstruction in path of boss
    def bossdetect(self):
        x = Boss.x_pos
        y = Boss.y_pos
        if Boss.x_pos < 10 or Board.board[y][x-1] != "-" or Board.board[y+1][x-1] != "-":
            if Board.board[y][x-1] == " " or Board.board[y+1][x-1] == " ":
                pass
            elif Board.board[y][x-1] == ">":
                pass
            elif Board.board[y][x-1] == "-" and Board.board[y+1][x-1] == "/":
                Mario.life-=1
                os.system("aplay ./sounds/smb_mariodie.wav")
                os.system('clear')
            else:
                self.edetl = "obstl"
                Boss.speed = -2
        else:
            self.edetl = "none"
        if Board.board[y][x+3] != "-" or Board.board[y+1][x+3] != "-":
            if Board.board[y][x+3] == " " or Board.board[y+1][x+3] == " ":
                pass
            elif Board.board[y][x+3] == ">":
                pass
            elif Board.board[y][x+3] == "-" or Board.board[y+1][x+3] == "/":
                Mario.life-=1
                os.system("aplay ./sounds/smb_mariodie.wav") 
                os.system('clear')
            else:
                self.edetr = "obstl"
                Boss.speed = 2
        else:
            self.edetr = "none"
    #free fall of mario 
    def mariofall(self):
        if Board.board[Mario.y_pos+3][Mario.x_pos] == " ":
            Mario.life -= 1
            os.system("aplay ./sounds/smb_mariodie.wav &")
            os.system('clear')
            game.removeprev()
    #fall down of mario
    def mariofalldown(self):
        if (Board.board[Mario.y_pos+3][Mario.x_pos] == "-" and Board.board[Mario.y_pos+3][Mario.x_pos+1] == "-" 
             and Board.board[Mario.y_pos+3][Mario.x_pos+2] == "-") :
            while (Board.board[Mario.y_pos+3][Mario.x_pos] == "-" and Board.board[Mario.y_pos+3][Mario.x_pos+1] == "-" 
                 and Board.board[Mario.y_pos+3][Mario.x_pos+2] == "-"):
                os.system('clear')
                game.removeprev()
                Mario.y_pos+=1
                game.mariomove(3)
                Board.boardprint()
                time.sleep(0.01)
    #killing enemies while jumping on them
    def jumpkill(self):
        if (Board.board[Mario.y_pos+3][Mario.x_pos] in l  or Board.board[Mario.y_pos+3][Mario.x_pos+1] in l
              or Board.board[Mario.y_pos+3][Mario.x_pos+2] in l):
            Mario.points+=100
            for enemy in enemies:
                if Board.board[enemy.y_pos-1][enemy.x_pos] == "/" or  Board.board[enemy.y_pos-1][enemy.x_pos+1] == "/" or Board.board[enemy.y_pos-1][enemy.x_pos+2] == "/":
                    self.enemiesclear(enemy)
                    enemy.toremove=1
                    enemies.remove(enemy)
                    os.system("aplay ./sounds/smb_stomp.wav &")
    #This generates coin on collision
    def coingen(self):
        c = Coin()
        c.x_pos = Mario.x_pos+1
        c.y_pos = Mario.y_pos-3
        for coin in coins:
            if c.x_pos == coin.x_pos and c.y_pos == coin.y_pos:
                                    c.count+=1
        if c.count < 3:
            Board.board[Mario.y_pos-3][Mario.x_pos+1]="0"
            Mario.points += c.pt
            Mario.coins_col +=1
            coins.append(c)
            os.system("aplay ./sounds/smb_coin.wav &")

enemies = []
e = Enemy()
e.genxpos()
enemies.append(e)
l = ["@","_"]
prevstroke = "d"
coins =[]
bullets = []
pos = []
gametime = time.time()
#leveltwo = Leveltwo()
if __name__ == "__main__":
    game = Game()
    game.level=2
    game.mariomove(1)
    Board.boardprint()
    prev=0
    st = time.time()
    while True:
        if Mario.life == 0 :
            Board.over()
            os.system("aplay ./sounds/smb_gameover.wav &")
            time.sleep(.01)
            quit()
        if Board.mov % 40 == 0 and Board.mov != prev:  #generate enemies after 40 steps
            x = Enemy()
            x.a = Mario.x_pos+15
            if x.a < 220:   
                x.b = x.a+80
            else:
                x.b=280
            for i in range(x.a,x.b):
                for j in range(-3,4):
                    if Board.board[x.y_pos][i+j]=="-":              #Choosing random x coordinate carefully
                        pos.append(i)
            x.x_pos = random.choice(pos)
            if game.level ==2:
                x.speed = 2
            enemies.append(x)
            prev = Board.mov
        game.mjumpcol =0 
        game.mariofall()
        if Mario.x_pos+3 == 294 and game.level <=2:                            #Checking end of level  
            game.level +=1
            if game.level > 2:
                print("YOU WON")
                time.sleep(.1)
                print("COINS:",Mario.coins_col)
                print("POINTS:",Mario.points)
                quit()
            Board = Leveltwo()
            Mario.x_pos = 10
            Mario.y_pos = 25                                     
        game.mariofalldown()                                    
        game.jumpkill()
        if time.time()- st > .15:                                     #Ensuring smooth movements of all enemies all time
            for enemy in enemies:
                game.edetect() 
                game.enemiesclear(enemy)
                if enemy.toremove !=1:
                    enemy.move()
                    game.enemymove()
                os.system('clear')
                Board.boardprint()
            if game.level > 1 and Boss.life > 0:
                game.bossdetect()
                game.removeboss()
                Boss.move(Boss)
                game.bossmove()
            st = time.time()
        if Boss.life == 0:
            game.removeboss()
        for coin in coins:                                             #Printing of coins for some time
            if time.time()-coin.spawntime > 2:
                Board.board[coin.y_pos][coin.x_pos] = "-"
                #coins.remove(coin)
        for bul in bullets:                                             #showing all bullets
            game.bulkill(bul)
            if bul.x_pos - bul.start < 10:
                game.bulclear(bul)
                bul.shot()
                game.showbul(bul)
                os.system('clear')
                Board.boardprint()
            else:
                game.bulclear(bul)
                bullets.remove(bul)
                os.system('clear')
                Board.boardprint()
        try:
            prevstroke = char
        except:
            prevstroke = "d"
        char = user_input()                                         #taking user input
        #move right
        if char == "d":
            game.detect() #checking objects in 1d
            if game.mdetr == "none": 
                os.system('clear')
                game.removeprev()
                Mario.moveright(Mario)
                game.mariomove(1)
                Board.boardprint()
        #quit game
        elif char == "q":
            Board.mov=0
            quit()
        #move left
        elif char == "a":
            game.detect()
            if game.mdetl == "none": 
                os.system('clear')
                game.removeprev()
                Mario.moveleft(Mario)
                game.mariomove(0)
                Board.boardprint()
        #shoot bullet
        elif char == "b":
            b = Bullet()
            b.x_pos = Mario.x_pos+3
            b.y_pos = Mario.y_pos+1
            b.start = Mario.x_pos+3
            bullets.append(b)
        #main jump functionality
        elif char == "w":
            os.system("aplay ./sounds/smb_jump-small.wav &")
            time.sleep(.005)
            if prevstroke == "d":
                for j in range(6):
                    os.system('clear')
                    game.removeprev()
                    if (Board.board[Mario.y_pos+2][Mario.x_pos+3] != "-" or Board.board[Mario.y_pos+1][Mario.x_pos+3] != "-"
                        or Board.board[Mario.y_pos][Mario.x_pos+3] != "-" or Board.board[Mario.y_pos-1][Mario.x_pos+3] != "-"
                        or Board.board[Mario.y_pos-1][Mario.x_pos+2] != "-" or Board.board[Mario.y_pos-1][Mario.x_pos+1] != "-") :  #checking collisions while jumping forward
                        if (Board.board[Mario.y_pos-1][Mario.x_pos+3] == "$" or Board.board[Mario.y_pos-1][Mario.x_pos+2] == "$"
                            or Board.board[Mario.y_pos-1][Mario.x_pos+1] == "$") :
                            game.coingen()
                        game.mariomove(3)
                        os.system('clear')
                        Board.boardprint()
                        game.mjumpcol = 1
                        break
                    else: # if no collisions then move 
                        Mario.y_pos-=1
                        Mario.x_pos+=1
                        Board.mov += 1                                                                                                      
                        game.mariomove(3)
                        Board.boardprint()
                        time.sleep(.03)
                if game.mjumpcol != 1: #if encounter collsion while forward jump
                    for j in range(6):
                        os.system('clear')
                        game.removeprev()
                        if (Board.board[Mario.y_pos+2][Mario.x_pos+3] != "-" or Board.board[Mario.y_pos+1][Mario.x_pos+3] != "-"
                             or Board.board[Mario.y_pos][Mario.x_pos+3] != "-" or Board.board[Mario.y_pos-1][Mario.x_pos+3] != "-") : #collision during downward jump
                            game.mariomove(3)
                            #os.system('clear')
                            Board.boardprint()
                            game.mjumpcol = 1
                            break
                        else:
                            if (Board.board[Mario.y_pos+3][Mario.x_pos] != "-" or Board.board[Mario.y_pos+3][Mario.x_pos+1] != "-"
                                 or Board.board[Mario.y_pos+3][Mario.x_pos+2] != "-" or Board.board[Mario.y_pos+3][Mario.x_pos+3] != "-"):
                                game.mariomove(3)
                                os.system('clear')
                                Board.boardprint()
                                break
                            else:
                                Mario.y_pos+=1
                                Mario.x_pos+=1                                                                                          #move downwards
                                Board.mov +=1
                                game.mariomove(3)
                                Board.boardprint()
                                time.sleep(.025)
            elif prevstroke == "a":
                #jump toward left
                for j in range(6):
                    os.system('clear')
                    game.removeprev()
                    if (Board.board[Mario.y_pos+2][Mario.x_pos-1] != "-" or Board.board[Mario.y_pos+1][Mario.x_pos-1] != "-"
                        or Board.board[Mario.y_pos][Mario.x_pos-1] != "-" or Board.board[Mario.y_pos-1][Mario.x_pos-1] != "-"
                        or Board.board[Mario.y_pos-1][Mario.x_pos] != "-" or Board.board[Mario.y_pos-1][Mario.x_pos+1] != "-") :
                        if (Board.board[Mario.y_pos-1][Mario.x_pos-1] == "$" or Board.board[Mario.y_pos-1][Mario.x_pos] == "$"
                             or Board.board[Mario.y_pos-1][Mario.x_pos+1] == "$") :
                            game.coingen()
                        game.mariomove(3)
                        os.system('clear')
                        Board.boardprint()
                        game.mjumpcol = 1
                        break
                    else:
                        Mario.y_pos-=1
                        Mario.x_pos-=1
                        Board.mov -= 1
                        game.mariomove(3)
                        Board.boardprint()
                        time.sleep(.03)
                if game.mjumpcol != 1:
                    for j in range(6):
                        os.system('clear')
                        game.removeprev()
                        if (Board.board[Mario.y_pos+2][Mario.x_pos-1] != "-" or Board.board[Mario.y_pos+1][Mario.x_pos-1] != "-"
                             or Board.board[Mario.y_pos][Mario.x_pos-1] != "-" or Board.board[Mario.y_pos-1][Mario.x_pos-1] != "-") :
                            game.mariomove(3)
                            #os.system('clear')
                            Board.boardprint()
                            game.mjumpcol = 1
                            break
                        else:
                            if (Board.board[Mario.y_pos+3][Mario.x_pos] != "-" or Board.board[Mario.y_pos+3][Mario.x_pos+1] != "-"
                                 or Board.board[Mario.y_pos+3][Mario.x_pos+2] != "-" or Board.board[Mario.y_pos+3][Mario.x_pos-1] != "-"):
                                game.mariomove(3)
                                os.system('clear')
                                Board.boardprint()
                            else:
                                Mario.y_pos+=1
                                Mario.x_pos-=1
                                Board.mov -=1
                                game.mariomove(3)
                                Board.boardprint()
                                time.sleep(.025)
            elif prevstroke == "s":
                #vertical jump
                for j in range(6):
                    os.system('clear')
                    game.removeprev()
                    if (Board.board[Mario.y_pos-1][Mario.x_pos] != "-" or Board.board[Mario.y_pos-1][Mario.x_pos+1] != "-" 
                        or Board.board[Mario.y_pos-1][Mario.x_pos+2] != "-"):
                        if (Board.board[Mario.y_pos-1][Mario.x_pos] == "$" or Board.board[Mario.y_pos-1][Mario.x_pos+2] == "$"
                             or Board.board[Mario.y_pos-1][Mario.x_pos+1] == "$") :
                            game.coingen()
                        elif (Board.board[Mario.y_pos-1][Mario.x_pos] == "?" or Board.board[Mario.y_pos-1][Mario.x_pos+2] == "?"
                             or Board.board[Mario.y_pos-1][Mario.x_pos+1] == "?") :
                            p = Lifeadd()
                            if p.add != 1:
                                p.x_pos = Mario.x_pos+1
                                p.y_pos = Mario.y_pos-3
                                Board.board[Mario.y_pos-3][Mario.x_pos+1]="+"
                                Mario.life+=1
                                p.add = 1
                                os.system("aplay ./sounds/smb_powerup_appears.wav &")
                        game.mariomove(3)
                        os.system('clear')
                        Board.boardprint()
                        game.mjumpcol = 1
                        break
                    else:
                        Mario.y_pos -=1
                        game.mariomove(3)
                        Board.boardprint()
                        time.sleep(.03)
                for j in range(6):
                    os.system('clear')
                    game.removeprev()
                    if (Board.board[Mario.y_pos+3][Mario.x_pos] != "-" or Board.board[Mario.y_pos+3][Mario.x_pos+1] != "-"
                         or Board.board[Mario.y_pos+3][Mario.x_pos+2] != "-"):
                        game.mariomove(3)
                        #os.system('clear')
                        Board.boardprint()
                        break
                    else:
                        Mario.y_pos +=1
                        game.mariomove(3)
                        Board.boardprint()
                        time.sleep(.025)
