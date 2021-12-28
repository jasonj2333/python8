n = int(input())
x1 = 0
y1 = 0
x2 = 0
y2 = 0

for i in range(n-1):
    x,y = input().split()
    if int(x) > x1:
        x1 = int(x)
    elif int(x) < x2:
        x2 = int(x)

    if int(y) > y1:
        y1 = int(y)
    elif int(y) < y2:
        y2 = int(y)

d = 2*(x1+2 + abs(x2)+2 + y1+2 + abs(y2)+2)
print(d)
