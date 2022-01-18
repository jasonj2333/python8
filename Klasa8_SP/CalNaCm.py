loop = 1;
def CalNaCm(cal):
    cm = cal * 2.54
    return cm

while loop != 0:
    cal = float(input("Podaj odległość w calach: "))
    print("Odległość w cm wynosi:", CalNaCm(cal))
    loop = int(input("Kończymy - tak-0/nie-1: "))
