alfabet = 'AĄBCĆDEĘFGHIJKLŁMNŃOÓPRSŚTUWYZŹŻaąbcćdeęfghijklłmnńoóprsśtuwyzźż '
alfabet2 = 'AĄBCĆDEĘFGHIJKLŁMNŃOÓPRSŚTUWYZŹŻ '
litery = [litera for litera in alfabet2]
dlugosc_litery = len(litery)
#print(litery)

#wersja klasyczna - tylko małe litery, bez polskich znaków
def szyfruj_znak(znak, klucz):
    return chr((ord(znak) - 97 + klucz) % 26 + 97)

def szyfruj(tekst, klucz):
    pom = ""
    for znak in tekst:
        pom = pom + szyfruj_znak(znak, klucz)

    return pom

def deszyfruj(tekst, klucz):
    return szyfruj(tekst, 26-klucz)

#wersja małe i duże litery z polskimi znakami i spacją
def szyfruj_znak_pl(znak, klucz):
    for i, litera in enumerate(litery):
        if znak == litera:
            return litery[(i+klucz)%dlugosc_litery]

def szyfruj_pl(tekst, klucz):
    pom = ""
    for znak in tekst:
        pom = pom + szyfruj_znak_pl(znak, klucz)
    return pom

def deszyfruj_pl(tekst, klucz):
    return szyfruj_pl(tekst, dlugosc_litery-klucz)

#print(szyfruj("tajne", 3))
#print(deszyfruj("wdmqh", 3))

#łamanie szyfru
#for i in range(1,27):
    #print(i, deszyfruj('xvrqlfcbgxnavr', i))

zaszyfrowany = szyfruj_pl("CZEŚĆ ZAPRASZAM NA KANAŁ SCRATCHSPWZ NA YOUTUBE", 3)
odszyfrowany = deszyfruj_pl(zaszyfrowany, 3)

print(zaszyfrowany)
print(odszyfrowany)