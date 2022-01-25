#100pk - https://szkopul.edu.pl/problemset/problem/AtGV96kvpMvjO8KntOC6v-MJ/site/?key=statement

def szyfruj_znak(znak, klucz):
    if ord(znak) < 65 or (ord(znak) > 90 and ord(znak) < 97) or ord(znak) > 122: return znak
    if ord(znak) < 97: a = 65
    else: a = 97
    return chr((ord(znak) - a + klucz) % 26 + a)

def szyfruj(tekst, klucz):
    pom = ""
    for znak in tekst:
        pom = pom + szyfruj_znak(znak, klucz)

    return pom

def deszyfruj(tekst, klucz):
    return szyfruj(tekst, 26-klucz)

typ = input()
klucz = int(input())
tekst = input()

if typ == 'szyfruj':
    cezar = szyfruj(tekst, klucz)
if typ == 'odszyfruj':
    cezar = deszyfruj(tekst, klucz)

print(cezar)

