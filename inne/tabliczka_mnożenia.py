#Tabliczka mnożenia
import random
print('Witaj w programie tabliczka mnożenia')
punkty = 0

for i in range(10):
    a = random.randint(1,10)
    b = random.randint(1,10)

    wynik = input('Podaj wynik mnożenia: '+str(a)+'*'+str(b)+'=')
    if int(wynik) == a*b:
        print('Dobrze')
        punkty = punkty+1
        #punkty+=1
    else:
        print('Źle')

#print('Wynik:', punkty)
print(f"Wynik: {punkty}")