N = 5
a = [0] * N
MAX_DANA = 99

def WprowadzDane():
    print("Wprowadź liczby z przedziału < 0,", MAX_DANA.">")
    for i in range(N):
        a[i] = int(input("Podaj liczbę: "))
        if a[i] < 0:
            a[i] = 0
        if a[i] > MAX_DANA:
            a[i] = MAX_DANA

def WyprowadzDane():
    for i in range(N):
        print(a[i])

def SortZlicz():
    liczniki = [0] * (MAX_DANA+1)
    for i in range(N):
        liczniki[a[i]] = liczniki[a[i]]+1
    for i in range(MAX_DANA+1):
        for j in range(liczniki[i])
            a[poz] = i
            poz = poz + 1

WprowadzDane()
WyprowadzDane()
print("Dane posortowane metodą przez zliczanie")
SortZlicz()
WyprowadzDane()