"""7. Создать вручную и заполнить несколькими строками текстовый файл,
в котором каждая строка будет содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1   ООО   10000   5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчёт средней прибыли её не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
а также словарь со средней прибылью. Если фирма получила убытки, также добавить её в словарь (со значением убытков).
"""
import json
FILE_NAME = 'task_7.txt'


# Generating data
# import random
# OWNERSHIP = ('LLC', 'Corp')
# with open(FILE_NAME, 'a', encoding='utf-8') as F:
#     for i in range(6):
#         F.write(f"{input('Comp.name: ')} {random.choice(OWNERSHIP)} {random.randrange(10000, 25000, 1000)} "
#                 f"{random.randrange(10000, 20000, 1000)}\n")

with open(FILE_NAME, 'r', encoding='UTF-8') as F:
    result = [{}, {'average_profit': 0}]
    for line in F.readlines():
        line = line.split()
        profit = int(line[2]) - int(line[3])
        print("{:>20} results are following: {:>5} units. ".format(line[0] + ' ' + line[1], profit))
        if profit > 0:
            result[0][line[0]] = profit
            result[1]['average_profit'] += profit
    result[1]['average_profit'] /= len(result[0].keys())

with open('task_7.json', 'w') as J:
    json.dump(result, J)
