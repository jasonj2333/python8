from turtle import *

speed(10)

color('red', 'green')

def wielokat(boki=4):
    if(boki < 3):
        boki = 3
    begin_fill()
    for i in range(boki):
        fd(100)
        rt(360/boki)
    end_fill()

def rozeta(figury=10, boki=4):
    for i in range(figury):
        wielokat(boki)
        rt(360/figury)

rozeta(36, 7)