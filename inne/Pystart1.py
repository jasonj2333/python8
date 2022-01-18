#podzielność
number = int(input('Podaj liczbę: '))
if(number%5 == 0):
    print(f"{number} jest podzielne przez 5")
if(number%11 == 0):
    print(f"{number} jest podzielne przez 11")

# stopnie
tempC = int(input('Podaj temperaturę w stopniach Celsjusza: '))
tempF = tempC * (9 / 5) + 32
print(f"{tempC} stopni Celsjusza to {tempF} stopni Fahrenheita")

### Trójkąt
xa = -1
ya = 3

xb = -3
yb = -3

xc = 2
yc = 1

p = 1/2*abs((xb-xa)*(yc-ya)-(yb-ya)*(xc-xa))
print(f'Pole trójkąta wynosi: {p}')