n = int(input())
a = [int(x) for x in input().split()]
sum_a = sum(a)
if sum_a>n//2:
    print(n-sum_a)
else:
    print(n-(n-sum_a))