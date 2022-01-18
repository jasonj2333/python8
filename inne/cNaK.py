def cNaK(c):
    k = c+273.15
    return k

c = 10
while c != 0:
    c = input('Podaj temperaturę w stopniach Celsjusza: ')
    c = int(c)
    k = cNaK(c)
    print('Temperatura w stopniach Kelwina wynosi: ', k)
print('Do widzenia')