def dwukrotnosc(x):
    s=0
    t=[]
    while x>0:
        r=x%10
        x=x//10
        t.append(r)
    t.sort()
    t=t[::-1]
    w=''
    for i in t:
        w+=str(i)
    return 2*int(w)

def dwukrotnosc_2(a):
    a = str(a)
    a = sorted(a)
    a = a[::-1]
    b = ''
    for s in a:
        b = b +s
    return 2*int(b)

x = int(input())
print(dwukrotnosc_2(x))