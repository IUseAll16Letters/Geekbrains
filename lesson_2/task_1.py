"""1. Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента.
Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
"""


test_list = [1, 0, 1, 11, 12, 2, 4]


class Test:
    default_attr = 'def'


values = [str(test_list[0]), test_list[0], float(test_list[0]),
          complex(test_list[0]), test_list, set(test_list), frozenset(test_list),
          tuple(test_list), bool(test_list[1]), {test_list[0]: test_list[1]},
          range(len(test_list)), bytes(test_list), bytearray(test_list),
          memoryview(bytes(test_list)), Test, print(type(type(test_list[1])))]


for i in values:
    print(type(i))