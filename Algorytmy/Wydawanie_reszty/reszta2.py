monety = [5, 2, 1]
reszta = int(input('Jaką resztę trzeba wydać: '))

dowydania = reszta
i = 0
liczba_monet = 0

while dowydania>0:
    liczba_monet += dowydania//monety[i]
    dowydania = dowydania%monety[i]
    i+=1

print(liczba_monet)
