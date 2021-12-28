def cmNaM(cm):
    if cm >=0:
        m = cm//100
        reszta_cm = cm%100
        string = 'Długość w metrach wynosi '+str(m)+' m i '+str(reszta_cm)+' cm'
        return string

cm = 0
m = 0
reszta_cm = 0
while cm > -1:
    cm = int(input('Podaj długość w centymetrach: '))
    print(cmNaM(cm))

print('Do widzenia')