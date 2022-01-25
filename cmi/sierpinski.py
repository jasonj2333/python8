import turtle
import random

wn = turtle.Screen()
alex = turtle.Turtle()
alex.color(0,0,1)
alex.pensize(2)

def print_troj(a,b,c):
    alex.up()
    alex.setposition(a)
    alex.color(0.5,0,0)
    alex.down()
    alex.goto(b)
    alex.goto(c)
    alex.goto(a)
    alex.up()

def sierpinski(n,a,b,c):
    if n==0:
        return
    else:
        print_troj(a,b,c)
        x = ((a[0] + b[0])/2, (a[1] + b[1])/2)
        y = ((b[0] + c[0])/2, (b[1] + c[1])/2)
        z = ((c[0] + a[0])/2, (c[1] + a[1])/2)

        sierpinski(n - 1, a, x, z)
        sierpinski(n - 1, x, b, y)
        sierpinski(n - 1, c, z, y)

alex.up()

n=4
a=(-300,-300)
b=(300,-300)
c=(0,300)

sierpinski(n,a,b,c)


turtle.done()

