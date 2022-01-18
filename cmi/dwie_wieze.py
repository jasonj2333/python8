n, m = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
sum_a = sum(a)
sum_b = sum(b)
k=0
while sum_a != sum_b:
    k+=1
    if sum_a > sum_b:
        sum_a = sum_a-a[n-1]
        n-=1
    else:
        sum_b = sum_b-b[m-1]
        m-=1
print(k)