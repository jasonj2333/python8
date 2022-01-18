def Maksimum(n):
    for i in range(n):
        a = int(input("Podaj liczbę: "))
        if i == 0:
            maks = a
        else:
            if a > maks:
                maks = a
    return maks

def Minimum(n):
    for i in range(n):
        a = int(input("Podaj liczbę: "))
        if i == 0:
            minimum = a
        else:
            if a < minimum:
                minimum = a
    return minimum

minimum = Minimum(5)
print("Najmniejsza liczba w zbiorze to: ", minimum)
