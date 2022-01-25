n = int(input())
w = [] #lista banknotów
w = [int(m) for m in input().split()]
q = int(input()) #lista zapytań
x = [0]*q #tworzenie pustej tablicy możliwości
for i in range(q):
    x[i] = int(input())

inf=1e5 #nasza nieskończoność
g=max(x) #największa wartość zapytania

wynik =[inf]*(g+1) #lista z wynikami - inicjalizacja
wynik[0]=0
nominal=[0]*(g+1) #lista ostatnio dodanych nominałów

for i in range(n):
    for j in range(w[i], g+1):
        if wynik[j-w[i]]+1<wynik[j]:
            wynik[j]=wynik[j-w[i]]+1
            nominal[j]=w[i]

#print(wynik)
#print(nominal)
#wypisywanie wyników
for k in x:
    if wynik[k]<inf:
        print(wynik[k], end=' ')
        while(k>0):
            print(nominal[k], end=' ')
            k=k-nominal[k]
    else:
        print(-1, end=' ')
    print()