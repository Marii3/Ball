from turtle import *
from random import randint, random

class Ball:
    def __init__(self, W, H):
        self.r = randint(10,30)
        self.ver = H // 2
        self.hor = W // 2
        self.x = randint(-W//2 + self.r, W//2 - self.r)
        self.y = randint(-H//2, H//2 - (self.r *2))
        self.dx = randint(-5, 5)
        self.dy = randint(-5, 5)
        self.color = (random(),random(),random())
        
    
    def move(self):
        if self.hor < self.x + self.r + (self.r//2) or self.x - self.r < -self.hor:
            self.dx *= -1
        if self.ver < (self.r * 2)+ self.y or self.y-(self.r//2) < -self.ver:
            self.dy *= -1      
        self.x+=self.dx
        self.y+=self.dy     
        
    def isCollision(self, other):
        a = abs((self.y+self.r) - (other.y+other.r))
        b = abs(self.x - other.x)     
        c = ((a**2) + (b**2)) ** 0.5
        return not self.r + other.r <= c
       
    

W = 800
H = 600
setup(W, H)
speed(0)
delay(0)
ht()

balls = []

def onClick(x,y):
    balls.append(Ball(W,H))

def move():
    clear()
    for ball in balls:
        ball.move()
    for i in range(len(balls)-1):
        for j in range( i+1, len(balls)):
            if balls[i]== None or balls[j]==None:
                continue            
            elif balls[i].isCollision(balls[j]):
             
                balls[i] = None
                balls[j] = None
    
    while None in balls:
        balls.remove(None)  
    
    for ball in balls:    
        up()
        goto(ball.x,ball.y)
        down()
        begin_fill()
        color(*ball.color)
        circle(ball.r)
        end_fill()
    ontimer(move,30)
     
        

onscreenclick(onClick)
move()

done()
