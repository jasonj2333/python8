rok = int(input("Podaj rok: "))

if rok % 400 == 0 or rok % 4 == 0 and rok % 100 != 0:
    print(f"{rok} jest przestępny")
else:
    print(f"{rok} nie jest przestępny")