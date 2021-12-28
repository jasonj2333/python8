a = 1
b =1
while a < 2000:
    if a+b < 2000: print(a+b)
    a = a+b
    b = a+b
#end
print(id(b))

print('ala ma \n"kota"')
print(2+7)
a=5
b=7
print(a+b) #dodawanie a + b

a=a+b
print(a)

e=int(input('Podaj liczbę: '))
print('kwadrat liczby', e, 'wynosi', e**2)

a = int(input('Podaj 1 liczbę: '))
b = int(input('Podaj 2 liczbę: '))
print(a+b)

a=int(input('a: '))
b=int(input('b: '))
c=int(input('c: '))
if a+b>c and b+c>a and c+a>b:
  print('Można zbudować trójkąt')
else:
  print('Nie można')

print('Program oblicza wartość bezwlędna z liczby całkowitej')
a = int(input('Podaj liczbę: '))
if a >=0:
  print(a)
else:
  print(-a)

#print(a)

if a > 0:
  print('dodatnia')
elif a==0:
  print('twoja liczba to zero')
else:
  print('ujemna')


a=20
b=12
x,y = a,b
while a!=b:
  if a>b:
    a = a-b
  else:
    b = b-a


print(f'NWD z licz {x}, {y} wynosi: {a}')

a = 1
suma = 0
while a !=0:
  a = int(input('Podaj liczbę: '))
  suma +=a

print(suma)

s=0
a=2
while a<=11:
  s+=a
  a+=1
print(s)

#zadanie 5 - parzyste
parzyste = 0
a = 1
while a <=10:
  liczba = int(input('Podaj liczbę: '))
  if (a%2 == 0): 
    parzyste +=1

print("Podałeś", parzyste, " liczb parzystych")