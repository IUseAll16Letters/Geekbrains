"""1. Поработайте с переменными, создайте несколько, выведите на экран,
запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран."""

variable_1 = {'a': 250, 'b': 150}
variable_2 = 1900

print(f'variable_1: {variable_1}, variable_2: {variable_2}')

input_str = input('Enter any sting: ')
while True:
    try:
        input_int = int(input('Enter any integer: '))
        break
    except ValueError:
        print('Wrong value, int expected')

print(input_str, input_int)
