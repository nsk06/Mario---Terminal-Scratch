import time,random
class Coin:
    '''0 Class for coins'''
    spawntime = time.time()
    pt = random.randint(75,250)
    x_pos = 400
    y_pos = 400
    count=0

class Bullet:
    ''' > class for bullets '''
    spawntime = time.time()
    x_pos = 400
    y_pos = 400
    start = 400
    speed  = 2
    def shot(self):
        self.x_pos += self.speed

class Lifeadd:
    '''+  Class for Lifeadder'''
    spawntime = time.time()
    x_pos = 400
    y_pos = 400
    add = 0