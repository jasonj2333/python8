def newton(n, k):
    if k == 0 or k == n:
        return 1
    else:
        return float(n) / k * newton(n - 1, k - 1)
#zadanie 6 - pierwsza
n = 7
k = 2

print(newton(n, k))