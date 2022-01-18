def odczyn(ph):
    if ph > 7:
        print("Zasadowy")
    elif ph < 7:
        print("Kwaśny")
    else:
        print("Neutralny")


for i in range(5):
    ph = int(input('Podaj ph '))
    odczyn(ph)
