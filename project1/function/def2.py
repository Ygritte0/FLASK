#-*-coding:utf-8-*-
import math

nx = 1

def move(x,y,step, angle = 0):
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    return nx,ny



print(move(1,2,3,60))