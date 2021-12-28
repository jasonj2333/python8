#zadanie 5 - parzyste
parzyste = 0
for i in range(10):
  liczba = int(input('Podaj liczbę: '))
  if (liczba%2 == 0): 
    parzyste +=1

print("Podałeś", parzyste, " liczb parzystych")