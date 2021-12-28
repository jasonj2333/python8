#problem plecakowy tradycjny
n,k=input().split()
n,k=int(n),int(k)
w=[]
u=[]
for i in range(n):
    x,y=input().split()
    x,y=int(x),int(y)
    w.append(x)
    u.append(y)

#print(w)
#print(u)
plecak=[0]*(k+1)
poprzedni=plecak.copy() #kopia listy plecak

for i in range(n):
    for j in range(w[i], k+1):
        plecak[j]=max(poprzedni[j], poprzedni[j-w[i]]+u[i])
    poprzedni=plecak.copy()

#print(plecak)
print(plecak[k])