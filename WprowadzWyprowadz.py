N = 5
a = [0] * N

def WprowadzDane():
    for i in range(N):
        a[i] = int(input("Podaj liczbę: "))

def WyprowadzDane():
    for i in range(N):
        print(a[i])

WprowadzDane()
WyprowadzDane()

