#Czy liczba pierwsza
a = int(input("Podaj liczbę większą od 1: "))

import math
z=2
while z <=math.sqrt(a) and a%z !=0:
    z+=1
if a==2 or a%z:
    print("Liczba jest pierwsza")
else:
    print("Liczba nie jest pierwsza")