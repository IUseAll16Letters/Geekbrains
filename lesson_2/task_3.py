"""3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить, к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и dict.
"""
from calendar import month_name


# Dictionary containing seasons
SEASONS = {'Winter': [12, 1, 2], 'Spring': [3, 4, 5], 'Summer': [6, 7, 8], 'Autumn': [9, 10, 11]}

# Lists of seasons
Winter = ('Winter', [12, 1, 2])
Spring = ('Spring', [3, 4, 5])
Summer = ('Summer', [6, 7, 8])
Autumn = ('Autumn', [9, 10, 11])

while True:
    try:
        month_input = int(input('Enter the month to get the season this month belongs to: '))
    except ValueError:
        print('Input error. Enter a number from 1 to 12.')
        continue
    if 0 < month_input <= 12:
        break
    else:
        print('Number should be from 1 to 12.')

for season, months in SEASONS.items():
    if month_input in months:
        print(f'{month_name[month_input].capitalize()} is in {season}. Solution using dictionary')

for season, months in [Winter, Spring, Summer, Autumn]:
    if month_input in months:
        print(f'{month_name[month_input].capitalize()} is in {season}. Solution using lists')