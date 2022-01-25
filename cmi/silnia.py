def silnia(liczba):
    silnia = 1
    for i in range(1, liczba+1):
        silnia *= i
    return silnia
#zadanie 6 - pierwsza
liczba = int(input('Podaj liczbę: '))

print("Silnia liczby", liczba, "wynosi", silnia(liczba))