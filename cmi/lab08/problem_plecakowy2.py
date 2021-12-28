#problem plecakowy dyskretny
x=6 #liczba przedmiotów
w=23 #wielkość plecaka
cena=[6,4,5,7,10,2]
waga=[6,2,3,2,3,1]
plecak = [0]*(w+1)
przedmiot = [0]*(w+1) #ostatnio dodany przedmiot - jego numer

for i in range(x):
    for j in range(waga[i], w+1):
        if plecak[j-waga[i]]+cena[i]>plecak[j]:
            plecak[j]=plecak[j-waga[i]]+cena[i]
            przedmiot[j]=i+1


k=w
wynik=plecak[k]
print("Najlepsze upakowanie plecaka dla rozmiaru",k,"wynosi", wynik)
print("Plecak zapakowany przedmiotami:")
while k>0:
    print(przedmiot[k], end=",")
    k-=waga[przedmiot[k]-1]