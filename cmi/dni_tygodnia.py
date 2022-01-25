def dzien_tygodnia(d,m,r):
    rm = (-1,0,3,3,6,1,4,6,2,5,0,3,5)

    dt = d + rm[m] + (r-1900) + (r-1900)//4
    if r%4==0 and m<3:
        dt=dt-1
    return dt%7
#end_fill

dni = ('niedziela', 'poniedziałek', 'wtorek', 'środa', 'czwartek', 'piatek', 'sobota')

d=int(input("dzień 1-31: "))
m=int(input("miesiąc 1-12: "))
r=int(input("rok 1900-2099: "))

print(dni[dzien_tygodnia(d,m,r)])