n=int(input())
t=[]
for i in range(n):
    a=input().split()
    t.append(int(a[1]))

s=[]
k=0

for b in t:
    while len(s)>0 and s[-1]>b:
        del(s[-1])
        k+=1
    if len(s)==0 or b>s[-1]:
        s.append(b)

print(k+len(s))