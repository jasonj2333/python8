def sumujCyfry(a):
  suma = 0
  while (a > 0):
    suma += a % 10
    a = int(a / 10)
  return suma

#zadanie 6 - pierwsza
a = 567

print(sumujCyfry(a))