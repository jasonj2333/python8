#100pk - https://szkopul.edu.pl/problemset/problem/AtGV96kvpMvjO8KntOC6v-MJ/site/?key=statement

alfabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
litery = list(alfabet)
dl = len(litery)

def szyfruj_znak_pl(znak, klucz):
    if znak not in litery: return znak
    if znak.isupper(): a = 0
    else: a=26
        
    i =  litery.index(znak)
    return litery[(i-a+klucz)%int(dl-a) +a]

def szyfruj_pl(tekst, klucz):
    pom = ""
    for znak in tekst:
        pom = pom + szyfruj_znak_pl(znak, klucz)
    return pom

def deszyfruj_pl(tekst, klucz):
    return szyfruj_pl(tekst, dl-klucz)


typ = input()
klucz = int(input())
tekst = input()

if typ == 'szyfruj':
    cezar = szyfruj_pl(tekst, klucz)
if typ == 'odszyfruj':
    cezar = deszyfruj_pl(tekst, klucz)

print(cezar)
