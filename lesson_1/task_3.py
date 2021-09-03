"""3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
      Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369."""


# Solution 1
user_input = input('Enter any positive integer:')

result = 0
for i in range(1, 4):
    result += int(user_input * i)
print(result)

# Solution 2
result = int(user_input) + int(user_input + user_input) + int(user_input + user_input + user_input)
print(result)

# Solution 3
result = sum(int(user_input * i) for i in range(1, 4))
print(result)