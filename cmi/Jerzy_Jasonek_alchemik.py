import random
lewa = 0
prawa = 0
rownowaga = 0

for i in range(200):
    los = random.randrange(2) #1-orzel; 0-reszka
    if los:
        lewa+=1
    else:
        prawa+=1

    if lewa == prawa:
        rownowaga +=1

print(rownowaga)