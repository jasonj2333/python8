monety = [5, 2, 1]
reszta = int(input('Jaką resztę trzeba wydać: '))

dowydania = reszta
i = 0
liczba_monet = 0

while dowydania>0:
    if(dowydania - monety[i] > -1):
        dowydania -= monety[i]
        liczba_monet +=1
        print(monety[i], end='')
    else:
        i+=1

print()
print(liczba_monet)
