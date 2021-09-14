"""4. Программа принимает действительное положительное число x и целое отрицательное число y.
Выполните возведение числа x в степень y.
Задание реализуйте в виде функции my_func(x, y).
При решении задания нужно обойтись без встроенной функции возведения числа в степень.
"""


# Solution 1
def negative_pow(x, y):
    if x <= 0 or y >= 0:
        return 'Wrong input'

    rate = y
    # Option 1
    res_1 = 1
    while y:
        res_1 *= x
        y += 1

    #Option 2 (may have float problems)
    res_2 = 1
    while rate:
        res_2 *= 1 / x
        rate += 1

    return 1 / res_1, res_2


values = [5, -3]
print(negative_pow(*values))


# Solution 2
print((lambda number, power: number ** power)(*values))
