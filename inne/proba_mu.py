from turtle import *
def osmiokat():
    for i in range(8):
        forward(50)
        left(45)

def osmiokaty():
    for i in range(12):
        osmiokat()
        forward(50)
        left(30)

osmiokaty()
