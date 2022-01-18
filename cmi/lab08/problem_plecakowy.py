#problem plecakowy dyskretny
x=6 #liczba przedmiotów
w=11 #wielkość plecaka
cena=[6,4,5,7,10,2]
waga=[6,2,3,2,3,1]
plecak = [0]*(w+1)


for i in range(x):
    for j in range(waga[i], w+1):
        plecak[j]=max(plecak[j], plecak[j-waga[i]]+cena[i])

print(plecak)
print(plecak[w])