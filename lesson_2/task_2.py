"""2. Для списка реализовать обмен значений соседних элементов.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д.
При нечётном количестве элементов последний сохранить на своём месте.
Для заполнения списка элементов нужно использовать функцию input().
"""


input_list = list(input('Enter elements of the list: '))

print(input_list)

for order, item in enumerate(input_list):
    if order % 2 == 1:
        input_list[order - 1], input_list[order] = input_list[order], input_list[order - 1]

print(input_list)