def encryption(string, operation):
    map_char = {'a' : '1', 'e' : '2', 'i' : '3', 'o' : '4', 'u' : '5', 'u' : '6'}
    if operation == '1':
        for char, number in map_char.items():
            string = string.replace(char, number)
    elif operation == '2':
        for char, number in map_char.items():
            string = string.replace(number, char)
    else:
        string = 'Nie ma takiej opreacji'

    return string

string = input("Podaj tekst: ")
operation = input("Zaszyfrować - 1, czy odszyfrować - 2: ")

print(encryption(string, operation))


