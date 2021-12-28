from math import sqrt
liczba = int(input())
b = int(sqrt(liczba))
dzielniki = []

for i in range(1, b+1):
    if(liczba%i == 0):
        print(i)
        if i * i != liczba:
            dzielniki.append(liczba//i)
dzielniki.reverse()
for i in dzielniki:
    print(i)

