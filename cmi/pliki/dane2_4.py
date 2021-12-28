# praca na plikach - zadanie maturalne
file = open('dane2_4.txt') # atrybut r - read jest domyślny
results_file = open('result2_4.txt', 'w') # w atrybut zapisu
for row in file:
    count = 0
    good = True
    for char in row:
        if char == '[':
            count += 1
        elif char == ']':
            count -= 1
            if count < 0: # sprawdzamy czy nawiasy są odpowiednio ustawione np. źle: []][
                good = False
                break

    answer = 'tak' if count == 0 and good else 'nie'

    results_file.write(str(answer)+'\n')

results_file.close() # zamykanie pliku
file.close()