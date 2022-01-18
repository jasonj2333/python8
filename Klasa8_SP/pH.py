def ph(roztwor):
    if roztwor > 7:
        print("Odczyn zasadowy")
    else:
        if roztwor < 7:
            print("Odczyn kwaśny")
        else:
            print("Odczyn neutralny")
            
for i in range(5):
    roztwor = float(input("Podaj pH roztworu: "))
    ph(roztwor)



