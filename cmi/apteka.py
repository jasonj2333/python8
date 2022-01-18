n = int(input())
c = [int(x) for x in input().split()]
w = c[n-1]
b = w
for i in range(n-2, -1, -1):
    if c[i]<b:
        b=c[i]
    w=w+b
print(w)