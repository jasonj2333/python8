pesel = input("Podaj nr pesel: ")
pesel_list = [int(element) for element in pesel]
if len(pesel_list) != 11:
    print("Niepoprawny numer pesel")
else:
    a,b,c,d,e,f,g,h,i,j,k = pesel_list
    check_pesel = a + 3*b + 7*c + 9*d + 1*e + 3*f + 7*g + 9*h + 1*i + 3*j + 1*k
    if check_pesel%10 == 0:
        print("Poprawny pesel")
        if j%2 == 0:
            print("kobieta")
        else:
            print("mężczyzna")
    else:
        print("Niepoprawny numer pesel")

