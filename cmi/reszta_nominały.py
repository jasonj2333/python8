print('Podaj nominały')
nom = [int(x) for x in (input().split())]
r = int(input('Podaj resztę: h'))

nom.sort(reverse=True)
print(nom)

w=0
i=0

while r>0:
    w=w+r//nom[i]
    r = r % nom[i]
    i+=1

print(w)