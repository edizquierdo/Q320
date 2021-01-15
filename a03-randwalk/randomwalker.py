import random
import math

class Person:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.x_hist = [self.x]
        self.y_hist = [self.y]
        self.d_hist = [self.distance()]

    def __str__(self):
        return "%d,%d" % (self.x,self.y)

    def record(self):
        self.x_hist.append(self.x)
        self.y_hist.append(self.y)
        self.d_hist.append(self.distance())

    def step(self):
        move = random.choice([[1,0],[-1,0],[0,-1],[0,1]])
        self.x += move[0]
        self.y += move[1]

    def distance(self):
        return math.sqrt(self.x**2 + self.y**2)


        
        
