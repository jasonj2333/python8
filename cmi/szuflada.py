n = int(input())
c = [int(x) for x in input().split()]
wys = c[n-1]
b = wys
licz = 0
for i in range(n-2, -1, -1):
    if c[i]>=b:
        c[i] = b-1
        licz+=1
    b = c[i]
if b <= 0:
    licz=-1
print(licz)