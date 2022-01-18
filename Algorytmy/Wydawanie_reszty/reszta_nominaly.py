monety = [5, 2, 1]
reszta = int(input('Jaką resztę trzeba wydać: '))

dowydania = reszta
i = 0
liczba_monet = 0
reszta = {}

while dowydania>0:
    l_nominal = dowydania//monety[i]
    liczba_monet += l_nominal
    if l_nominal:
        reszta[monety[i]] = l_nominal
    dowydania = dowydania%monety[i]
    i+=1

print(liczba_monet)
print(reszta)
