import turtle
import random
n=70
wn = turtle.Screen()
alex = turtle.Turtle()
alex.color(0,0,1)
alex.pensize(2)
a=("red", "green", "blue")
alex.dot(15,"black")
alex.speed(16)
for j in range(3):
    alex.color(a[j])
    alex.up()
    alex.setposition(0,0)
    alex.down()
    for i in range(n):
        angle=random.random()*360
        alex.lt(angle)
        alex.fd(40)
    alex.dot(15)
turtle.done()

