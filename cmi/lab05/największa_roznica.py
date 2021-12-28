def list_to_int(numbers):
    strings = [str(element) for element in numbers]
    a_string = "".join(strings)
    an_integer = int(a_string)
    return an_integer

number = input("Podaj liczbę: ")
min = list_to_int(sorted(number))
max = list_to_int(sorted(number, reverse=True))
print(f"Największa możliwa różnica dla liczby {number} wynosi {max} - {min} = {max-min}")