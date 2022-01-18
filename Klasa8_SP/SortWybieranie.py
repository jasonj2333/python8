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
    mini = starti
    min = a[mini]
    for i in range(starti + 1, N):
        if a[i] < min:
            mini = i
            min = a[mini]
    return mini


def SortMaksWybor():
    for i in range(N-1):
        maksi = MaksWybor(i)
        t = a[i]
        a[i] = a[maksi]
        a[maksi] = t


def SortMinWybor():
    for i in range(N-1):
        mini = MinWybor(i)
        t = a[i]
        a[i] = a[mini]
        a[mini] = t


WprowadzDane()
SortMinWybor()
WyprowadzDane()
