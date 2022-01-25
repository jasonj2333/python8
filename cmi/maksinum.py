#zadanie 9 - parzyste
for i in range(8):
    a = int(input("Podaj liczbę: "))
    if (i==0):
        max = a
    else:
        if(a>max):
            max = a

print("Max wynosi", max)

