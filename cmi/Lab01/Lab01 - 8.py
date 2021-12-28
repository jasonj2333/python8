#zadanie 8 - parzyste
a = int(input("Podaj 1 liczbę: "))
b = int(input("Podaj 2 liczbę: "))
c=a
d=b

while(b != 0):
    dzielnik = b
    b = a%b
    a = dzielnik
print("NWD dla liczb %d i %d wynosi %d"%(c, d, a))
