def pierwsza(liczba):
    if (liczba < 2):
        return False
    else:
        i = 2
        while(i*i<=liczba):
            if(liczba%i==0):
                return False
            i += 1
            #print(i)
    return True
#zadanie 6 - pierwsza
liczba = int(input('Podaj liczbę: '))

print("Liczba pierwsza", pierwsza(liczba))