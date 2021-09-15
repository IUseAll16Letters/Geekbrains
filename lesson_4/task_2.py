"""2. Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для его формирования используйте генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
"""
from random import randint
source_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
random_list = [randint(1, 350) for i in range(randint(10, 100))]


# Solution 1
def conseq_comparison(data):
    current = data[0]
    for i in data:
        if i > current:
            yield i
        current = i


# Solution 2, oneliner
conseq_oneline = lambda data: (i for j, i in enumerate(data) if data[j-1 if j != 0 else 0] < data[j])


if __name__ == '__main__':
    print(*conseq_comparison(source_list))
    print(*conseq_oneline(source_list))
    print(*conseq_comparison(random_list))
    print(*conseq_oneline(random_list))
