N = 25
a = [0] * N
MAX_DANA = 99


def WprowadzDane():
    print("Wprowadź liczby z przedziału < 0,", MAX_DANA, ">")
    for i in range(N):
        a[i] = int(input("Podaj liczbę: "))
        if a[i] < 0:
            a[i] = 0
        if a[i] > MAX_DANA:
            a[i] = MAX_DANA


def LosujDane():
    import random
    random.seed()
    for i in range(N):
        a[i] = random.randint(0, MAX_DANA)


def SortZlicz():
    liczniki = [0] * (MAX_DANA+1)
    for i in range(N):
        liczniki[a[i]] = liczniki[a[i]]+1
    poz = 0
    for i in range(MAX_DANA+1):
        for j in range(liczniki[i]):
            a[poz] = i
            poz = poz + 1


def SzukajLiniowo(wartosc):
    for i in range(N):
        if a[i] == wartosc:
            return i
    return -1


def ZnajdzDana(wartosc):
    poczatek = 0
    koniec = N - 1
    while poczatek <= koniec:
        srodek = (poczatek + koniec) // 2
        if a[srodek] == wartosc:
            return srodek
        else:
            if wartosc < a[srodek]:
                koniec = srodek - 1
            else:
                poczatek = srodek + 1
    return -1


print("-------------------------------------------------------------")
# WprowadzDane()
LosujDane()
SortZlicz()
print(a)
wartosc = int(input("Podaj szukaną wartość: "))
pozycja = ZnajdzDana(wartosc)
if pozycja >= 0:
    print("Znaleziono wartość:", wartosc, "na pozycji:", pozycja+1)
else:
    print("Nie znaleziono wartości:", wartosc)