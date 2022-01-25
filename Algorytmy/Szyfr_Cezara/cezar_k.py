#wersja klasyczna - tylko małe litery, bez polskich znaków
def szyfruj_znak(znak, klucz):
    #(nr_znaku_w_asci - 97(to numer a) + klucz) reszta z dzielenia przez 26(ilosc znakow w alfabecie) + 97
    return chr((ord(znak) - 97 + klucz) % 26 + 97)

def szyfruj(tekst, klucz):
    pom = ""
    for znak in tekst:
        pom = pom + szyfruj_znak(znak, klucz)

    return pom

def deszyfruj(tekst, klucz):
    return szyfruj(tekst, 26-klucz)

szyfrogram = szyfruj("python", 3)

print(szyfrogram)

print(deszyfruj(szyfrogram, 3))

