liczby =  input().split()
liczby = [int(liczba) for liczba in liczby]
a, b, c = liczby
if a+b>c and a+c>b and b+c>a:
    print('TAK')
else:
    print('NIE')