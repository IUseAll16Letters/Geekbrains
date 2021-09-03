"""2. Пользователь вводит время в секундах
      Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс
      Используйте форматирование строк"""

# Input validation
while True:
    try:
        time_input = abs(int(input('Enter time in seconds: ')))
        break
    except ValueError:
        print('Invalid input. Enter positive integer')
time_sec = time_input


# Solution 1
# Calculating hours, minutes, seconds
hours = time_sec // 3600
time_sec %= 3600
minutes = time_sec // 60
time_sec %= 60

print(f'Current time is: {hours:02d}:{minutes:02d}:{time_sec:02d}')


# Solution 2
TIME_VALUES = [("years", 31536000),
               ("days", 86400),
               ("hours", 3600),
               ("minutes", 60),
               ("seconds", 1)]


def format_duration(seconds):
    if seconds == 0:
        return "The time is now!"

    result = []
    for unit, duration in TIME_VALUES:
        n = seconds // duration
        if n:
            result.append(f'{str(n)} {unit}')
            seconds -= n * duration
            if n == 1:
                result[-1] = result[-1][:-1]

    return ", ".join(result)


print(format_duration(time_input))