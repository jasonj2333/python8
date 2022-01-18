from turtle import *
def kwadrat(x, y, a, kat=0, pen="black", fill="white"):
 penup()
 goto(x, y)
 backward(a // 2)
 left(90)
 backward(a // 2)
 right(90)
 setheading(kat)
 pendown()
 color(pen, fill)
 begin_fill()
 for i in range(4):
    forward(a)
    left(90)
 end_fill()
WYMIARY=8
X=-160
Y=-160
BOK=40
KOLOR=["white","black"]
for i in range(WYMIARY):
 for j in range(WYMIARY):
    kwadrat(X,Y,BOK,0,"black",KOLOR[j%2])
    X+=BOK
 X=-160
 Y+=BOK
 if i%2==1:
    KOLOR=["white","black"]
 else:
    KOLOR=["black","white"]