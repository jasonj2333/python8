def zamiana_10_to_n(l, n):
    C={0:'0', 1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9', 10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
    W=""
    while l>0:
        W=W+C[l%n]
        l=l//n
    W=W[::-1]
    return W

l = int(input('Podaj liczbę: '))
n = int(input('Podaj system na który chcesz przeliczyć 2-16 '))
print(zamiana_10_to_n(l,n))
