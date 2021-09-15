"""6. Реализовать два небольших скрипта.
1) итератор, генерирующий целые числа, начиная с указанного;
2) итератор, повторяющий элементы некоторого списка, определённого заранее.
Подсказка: используйте функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным. Предусмотрите условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3.
При достижении числа 10 — завершаем цикл. Вторым пунктом необходимо предусмотреть условие, при котором повторение элементов списка прекратится.
"""
from itertools import count, cycle


Jacksons_five = ['ABC. Easy as: One, two, Three.',
                 'Or simple as: Do Re Mi',
                 'ABC, one, two, three, baby, you and me girl!']

# 1)
for elm in count(int(input('Starting number for endless fun: '))):
    print(elm)
    if elm >= 44:
        print('End condition reached. No more fun for you! \n')
        break

# 2)
for elm in cycle(Jacksons_five):
    print(elm)
    if 'girl' in elm:
        break
