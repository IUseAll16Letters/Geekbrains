"""5. Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти чётные числа от 100 до 1000 (включая границы).
Нужно получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
"""
from functools import reduce


# Solution 0
con_mult = lambda a, b: a * b


# Solution 1
def conseq_multiplication(el_p, el):
    return el_p * el


if __name__ == '__main__':
    print(f'multiplication result: {reduce(conseq_multiplication, (elm for elm in range(100, 1001) if elm % 2 == 0))}')
    print(f'multiplication result: {reduce(con_mult, (elm for elm in range(100, 1001) if elm % 2 == 0))}')