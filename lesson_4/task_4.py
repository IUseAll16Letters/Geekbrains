"""4. Представлен список чисел. Определите элементы списка, не имеющие повторений.
Сформируйте итоговый массив чисел, соответствующих требованию.
Элементы выведите в порядке их следования в исходном списке.
Для выполнения задания обязательно используйте генератор.
"""
source_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]


# Solution 1 O(m + n)
def get_uniques(data):
    res = {}
    for i in data:
        if i in res.keys():
            res[i] += 1
        else:
            res[i] = 1

    for j, i in res.items():
        if i == 1:
            yield j


# Solution 2. Nested loop
def uniques(data):
    return (i for i in set(data) if data.count(i) == 1)

if __name__ == '__main__':
    print(*get_uniques(source_list))
    print(*uniques(source_list))
