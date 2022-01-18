scene0 = """
---------
|       |
|
|
|
|
|
|
----------
"""
scene1 = """
---------
|       |
|       O
|
|
|
|
|
----------
"""
scene2 = """
---------
|       |
|       O
|    |--T--|
|
|
|
|
----------
"""
scene3 = """
---------
|       |
|       O
|    |--T--|
|       |
|
|
|
----------
"""
scene4 = """
---------
|       |
|       O
|    |--T--|
|       |
|       ^
|
|
----------
"""
scene5 = """
---------
|       |
|       O
|    |--T--|
|       |
|       M
|      | |
|
----------
"""

def wypisz_wynik_gry(haslo_odgadniete, scene):
    if haslo_odgadniete:
        print('Haslo odgadniete - Brawo')
    else: # przegrana
        print('Wisisz - gra przegrana')
        print(scene)

def wypisz_haslo(haslo, litery):
    czy_kompletne = True
    for litera in haslo:
        if litera == ' ':
            print(litera,sep='', end='')
        elif litera in litery:
            print(litera,sep='', end='')
        else:
            print('_',sep='', end='')
            czy_kompletne = False
    print()
    return czy_kompletne

def wypisz_menu(scena, litery_odkryte, haslo):
    print('Zagrajmy w grę\n Zgadnij moje tajne hasło')
    print(scena)
    print('Dotychczasowe litery to ', litery_odkryte)
    wypisz_haslo(haslo, litery_odkryte)
    litera = input('Podaj kolejna litere\n>')
    return litera

def gra_wisielec(tajne_haslo):

    scenes = [scene0, scene1, scene2, scene3, scene4, scene5]
    scenes_count = 5
    current_scene = 0
    czy_haslo_zgadniete = False
    litery_sprawdzone = []

    ## petla opisuje proces odgadywania
    while current_scene < scenes_count and not czy_haslo_zgadniete:
        litera = wypisz_menu(scenes[current_scene], litery_sprawdzone, tajne_haslo)
        litery_sprawdzone.append(litera)
        # czy trafiona litera
        if not litera in tajne_haslo:
                current_scene += 1
        czy_kompletne = wypisz_haslo(tajne_haslo, litery_sprawdzone)
        if czy_kompletne:
            czy_haslo_zgadniete = True
    wypisz_wynik_gry(czy_haslo_zgadniete, scenes[current_scene])

gra_wisielec('cmi')