from turtle import *
def kwadrat(x, y, a, kat=0, pen="black", fill="white"):
 penup()#podnosimy żółwia
 goto(x, y)#przemieszczamy się na wskazaną pozycję
 backward(a // 2)#cofamy się połowę długości boku
 left(90)#skręcamy w lewo o 90
 backward(a // 2)#cofamy się o połowę długości boku
 right(90)#wracamy do pozycji początkowej
 setheading(kat)#ustawimy żółwia o zadany kąt
 pendown()#opuszczamy żółwia
 color(pen, fill)#ustawiam kolor linii na
 #wskazany w zm. pen, zaś
 #wypełnienia w zm. fill
 begin_fill()
 for i in range(4):#pętla wykonuje się 4 razy
    forward(a)#ruch na przód o wartość zm.
    left(90)#a obrót o 90 stopni
 end_fill()
kwadrat(0, 0, 100, 0, "#000000", "#ff0000")
kwadrat(120, 0, 100, 0, "black", "black")