"""3. Реализовать функцию my_func(), которая принимает три позиционных аргумента
и возвращает сумму наибольших двух аргументов.
"""
import random


# For 3 arguments
def sum_args(a, b, c):
    return sum(sorted([a, b, c])[:-3:-1])


# Test purpose
for _ in range(11):
    numbers = [random.randint(1, 10) for i in range(3)]
    print(numbers, sum_args(*numbers), sep='; ')
