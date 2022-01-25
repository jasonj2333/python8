def silnia(n):
    if n==0:
        return 1
    else:
        return silnia(n-1)*n

x = int(input('podaj liczbę: '))
print(silnia(x))