# praca na plikach - zadanie maturalne
file = open('dane2_3.txt') # atrybut r - read jest domyślny
results_file = open('result.txt', 'w') # w atrybut zapisu
for row in file:
    maximum = 0
    count = 0
    for char in row:
        if char == '[':
            count += 1
            if count > maximum:
                maximum = count
        else:
            count -= 1

    results_file.write(str(maximum)+'\n')

results_file.close() # zamykanie pliku
file.close()