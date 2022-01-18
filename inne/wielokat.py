from turtle import *
shape("turtle")
speed(6)
pencolor('red')
color('red', 'green')
def wielokat(boki):
    if(boki<3):
            boki=3
    begin_fill()
    for i in range(boki):
        fd(50)
        rt(360/boki)
    end_fill()
def rozeta(figury=10, boki=4):
    for i in range(figury):
        wielokat(boki)
        rt(360/figury)
rozeta()