import datetime

now = datetime.datetime.now().year

name = input('Podaj imię i nazwisko: ')
birthday_year =input('Podaj rok urodzenia: ')

hundred_year = int(birthday_year) + 100
for i in range(20):
    print('Sto lat ukończysz w roku', hundred_year, 'czyli za', hundred_year-now)