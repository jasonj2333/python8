n, p = input().split()
n, p = int(n), int(p)
skladniki = [int(s) for s in input().split()]
magazyn = [int(m) for m in input().split()]
dziel = []

for i in range(n):
    dziel.append(magazyn[i]//skladniki[i])

dawki = min(dziel)

while True:
    dawki+=1
    pan = p
    for i in range(n):
        if skladniki[i] * dawki >  magazyn[i]:
            pan -= skladniki[i] * dawki - magazyn[i]
            if pan < 0: break
    if pan < 0: break

print(dawki-1)