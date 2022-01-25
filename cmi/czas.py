t = int(input())
g = t//3600
m = (t%3600)//60
s = t-g*3600-m*60

print(g,'g',m,'m',s,'s', sep='')


