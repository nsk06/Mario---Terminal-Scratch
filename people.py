import time,os
import random
class Person:
    '''The person class'''
    x_pos = 0
    y_pos = 0
    life = 1
    speed = 1
    lifetime = 300
    def attack(self):
        pass
class Mario(Person):
    ''' o-o
        -|-
        / /   Mario class'''
    def __init__(self):
        super(Person,self)
        self.speed = 1
        self.life = 1
    x_pos = 10
    y_pos = 25  
    coins_col=0
    points = 0
    def lif(self):
        self.lifetime = 50
        return self.lifetime
    def moveright(self):
        self.x_pos += self.speed
    def moveleft(self):
        self.x_pos -= self.speed
class Enemy(Person):
    ''' @_@
        | |  enemy class '''
    def __init__(self):
        super(Person,self).__init__()
        self.speed = 1
        self.life = 1
    y_pos = 26
    a = 55
    b = 100
    def genxpos(self):
        self.x_pos = random.randint(self.a,self.b)
    toremove = 0
    def move(self):
        self.x_pos -= self.speed

class Boss(Enemy):
    '''@@@
       |X| '''
    def __init__(self):
        super().__init__()
        self.speed = 2
        self.life = 3
    y_pos = 26
    x_pos = 167
    def move(self):
        if Mario.x_pos < self.x_pos:
            self.x_pos -= self.speed
        else:
            self.x_pos += self.speed