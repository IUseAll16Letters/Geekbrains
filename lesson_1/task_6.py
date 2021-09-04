"""6. Спортсмен занимается ежедневными пробежками.
В первый день его результат составил a километров.
Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
Например: a = 2, b = 3. Результат: 1-й день: 2; 2-й день: 2,2; 3-й день: 2,42; 4-й день: 2,66;
5-й день: 2,93; 6-й день: 3,22.
Ответ: на 6-й день спортсмен достиг результата — не менее 3 км."""

# Solution 1
run_distance, goal = int(input('Starting distance of athlete: ')), int(input('Athlete goal: '))
athlete_progress = 0.1

days = 1
while run_distance < goal:
    run_distance += athlete_progress * run_distance
    days += 1

print(f'Athlete has reached the goal to run {goal} km on day number {days}')


# Solution 2
def run_progress(start_distance, target, progress, day=1):
    if start_distance < target:
        return run_progress(start_distance + start_distance * progress, target, progress, day + 1)
    return f'Athlete has reached the goal to run {target} km on day number {day}'


print(run_progress(2, 3, 0.1))


# Solution 3
from math import ceil, log


def calculate_days(start, trgt, progr):
    if start >= trgt:
        return 0
    return 1 + ceil(log(trgt / start, 1 + progr))


print(f'Athlete has reached the goal to run {3} km on day number {calculate_days(2, 3, 0.1)}')