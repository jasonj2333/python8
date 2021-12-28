def tuziny(n):
    return n/12

def tuziny2(n):
    j = n//12
    r = n%12
    odp = str(j)+' tuziny '+str(r)+' sztuk'
    return odp

def izby(n):
    return n/40

def kopy(n):
    return n/60

def grosy(n):
    return n/144

def menu():
    print('Wybierz jednostkę na która chcesz przeliczyć: ')
    print('1. Tuziny')
    print('2. Izby')
    print('3. Kopy')
    print('4. Grosy')

koniec = 0

while not koniec:
    n = int(input('Podaj liczbę cukierków: '))
    menu()
    m = int(input())

    if m==1:
        print('Twoje cukierki w tuzinach: ', tuziny2(n))
    elif m==2:
        print('Twoje cukierki w izbach: ', izby(n))
    elif m==3:
        print('Twoje cukierki w kopach: ', kopy(n))
    elif m==4:
        print('Twoje cukierki w grosach: ', grosy(n))
    else:
        print('Nie ma takiej jednostki')

    koniec = int(input('Kończymy ? 1-tak/0-nie: '))
