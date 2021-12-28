every_week = 10
old_every_week = 17
percent = 0.05
sum1 = 0
sum2 = 0
more_profit = 0
weeks = int(input('Podaj liczbę tygodni: '))

#              sum2 = weeks * old_every_week

for i in range(1, weeks+1):
    sum1 += round(every_week + (sum1 * percent), 2)
    sum2 = old_every_week * i
    if sum1 > sum2 and more_profit == 0:
        more_profit = i

print(f"Kieszonkowe w nowym wariancie: {round(sum1, 2)} zł")
print(f"Kieszonkowe starym wariancie: {sum2} zł")
if more_profit > 0:
    print(f"Już po {more_profit} tygodniach oszczędzania, zarabiasz więcej w nowym wariancie")

