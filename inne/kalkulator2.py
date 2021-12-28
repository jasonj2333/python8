def menu():
    print('Kalkulator')
    print('1. Dodawanie')
    print('2. Odejmowanie')
    print('3. Mnożenie')
    print('4. Dzielenie')

def licz(a, b, dzialanie):
    if dzialanie == '1':
        wynik = a+b
    elif dzialanie == '2':
        wynik = a-b
    elif dzialanie == '3':
        wynik = a*b
    elif dzialanie == '4':
        wynik = a/b
    else:
        wynik = 'Nie ma takiego działania'

    return wynik

menu()
a = int(input('Podaj pierwszą liczbę: '))
b = int(input('Podaj drugą liczbę: '))
wynik = 0
dzialanie = input('Wybierz działanie: ')
wynik = licz(a, b, dzialanie)
print(wynik)