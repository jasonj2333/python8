from turtle import *
speed(0)
kolory=[]
#generujemy wszystkie możliwe warianty kolorów
#jako listę zawierającą krotki
for i in range(256):
 tmp=(0,i,0)
 kolory.append(tmp)
colormode(255)#zmiana trybu zapisu kolorów
#domyślnie turtle rozpoznaje kolory według skali 0.0 - 1.0
#od tego momentu możemy definiować kolory
#jako krotkę zawierającą 3 wartości,
#każda od 0 do 255
pensize(1)
left(90)
X=0
for i in kolory:
 penup()
 goto(X,0)
 pendown()
 pencolor(i)
 forward(256)
 X+=1