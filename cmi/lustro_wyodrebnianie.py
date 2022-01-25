liczba = int(input())

def lustro_str(liczba: int) -> int:
    cyfry = ''

    while liczba > 0:
        cyfra = liczba % 10
        cyfry += str(cyfra)
        liczba //= 10
        
    return int(cyfry)

def lustro_list(liczba: int) -> int:
    cyfry = []

    while liczba > 0:
        cyfra = liczba % 10
        cyfry.append(cyfra)
        liczba //= 10
        
    return int(''.join(str(x) for x in cyfry))

def lustro_py(liczba: str) -> int:
    return int(liczba[::-1])

print(lustro_py(str(liczba)))


      