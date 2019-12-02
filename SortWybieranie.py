N = 5
a = [0] * N

def WprowadzDane():
    for i in range(N):
        a[i] = int(input("Podaj liczbę: "))

def WyprowadzDane():
    for i in range(N):
        print(a[i])

def MaksWybor(starti):
    maksi = starti
    maks = a[maksi]
    for i in range(starti + 1, N):
        if a[i] > maks:
            maksi = i
            maks = a[maksi]
    return maksi

def MinWybor(starti):
    maksi = starti
    maks = a[maksi]
    for i in range(starti + 1, N):
        if a[i] < maks:
            maksi = i
            maks = a[maksi]
    return maksi

def SortWybor():
    for i in range(N-1):
        maksi = MaksWybor(i)
        t = a[i]
        a[i] = a[maksi]
        a[maksi] = t
    

