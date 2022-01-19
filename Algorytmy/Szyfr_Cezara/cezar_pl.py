alfabet = 'AĄBCĆDEĘFGHIJKLŁMNŃOÓPRSŚTUWYZŹŻaąbcćdeęfghijklłmnńoóprsśtuwyzźż0123456789:;,. '
litery = list(alfabet)
#litery = [litera for litera in alfabet]


#wersja małe i duże litery z polskimi znakami i spacją
def szyfruj_znak_pl(znak, klucz):
    if znak not in litery: return znak
    for i, litera in enumerate(litery):
        if znak == litera: 
            return litery[(i+klucz)%len(litery)]

def szyfruj_pl(tekst, klucz):
    pom = ""
    for znak in tekst:
        pom = pom + szyfruj_znak_pl(znak, klucz)
    return pom

def deszyfruj_pl(tekst, klucz):
    return szyfruj_pl(tekst, len(litery)-klucz)



zaszyfrowany = szyfruj_pl("Zajęcia w środę o 10:00", 58)
odszyfrowany = deszyfruj_pl(zaszyfrowany, 58)

print(zaszyfrowany)
print(odszyfrowany)
