kod = input()
n = int(input())

for i in range(n):
    c1, c2 = input().split()
    kod = kod.replace(c1,c2)
print(kod)