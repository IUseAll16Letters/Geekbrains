"""Создать текстовый файл (не программно).
Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
Выполнить подсчёт средней величины дохода сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32
"""
from random import randrange
FILE_NAME = 'task_3.txt'


# with open(FILE_NAME, 'w', encoding='utf-8') as f:
#     for i in range(10):
#         f.writelines(f"{input('Enter employee name: ')} {randrange(19000, 35000, 500)}")


with open(FILE_NAME, 'r') as f:
    salary_sum = 0
    items = 0
    for line in f.readlines():
        name, sal = ''.join(item for item in line if not item.isdigit()),\
                    int(''.join(item for item in line if item.isdigit()))
        if int(sal) < 20000:
            print(name, end='')
        items += 1
        salary_sum += int(sal)
    print(f'Average salary is: {salary_sum / items}')