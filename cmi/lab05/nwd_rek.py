def NWD_rek(a,b):
    if b==0:
        return a
    else:
        return NWD_rek(b, a%b)

def NWD_iter(a,b):
    while(b!=0):
        r=a%b
        a=b
        b=r
    return a

a = int(input())
b = int(input())
print(NWD_iter(a,b))
