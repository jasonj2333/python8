dane = input().split()
dane = [int(row) for row in dane]
a, b, k = dane
if a<k or  b<k:
    stolki = 0
elif a<2*k or b<2*k:
    stolki=max(a,b)//k
else:
    stolki = ((a//k) + ((b//k)))*2-4
print(stolki)