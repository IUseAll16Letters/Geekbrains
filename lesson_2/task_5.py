"""Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел, который не возрастает.
У пользователя нужно запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться после них.
"""
from random import randint


my_list = sorted((randint(1, 10) for i in range(10)), reverse=True)
input_num = int(input('Enter number in range 1 to 10: '))

insert_pos = None
for j, i in enumerate(my_list):
    if input_num <= i:
        continue
    else:
        insert_pos = j
        break

my_list_two = my_list.copy()
my_list_two.append(input_num)
my_list_one = my_list.copy()

# Solution 1
if not insert_pos:
    my_list_one.append(input_num)
else:
    my_list_one = my_list[:insert_pos] + [input_num] + my_list[insert_pos:]  # Solution 1


# Solution 2
if not insert_pos:
    my_list_two.append(input_num)
else:
    rd = len(my_list_two) - 1
    while rd > insert_pos:
        my_list_two[rd], my_list_two[rd - 1] = my_list_two[rd - 1], my_list_two[rd]
        rd -= 1

print(f'{my_list_two} - list b')
print(f'{my_list_one} - list a')