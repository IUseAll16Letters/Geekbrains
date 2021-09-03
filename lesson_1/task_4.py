"""4. Пользователь вводит целое положительное число.
      Найдите самую большую цифру в числе.
      Для решения используйте цикл while и арифметические операции."""

user_input = input('Enter any positive integer')


max_digit = 0
while user_input:
    if user_input[0] == '9':
        max_digit = 9
        break
    if int(user_input[0]) > max_digit:
        max_digit = int(user_input[0])
    user_input = user_input[1:]

print(max_digit)
