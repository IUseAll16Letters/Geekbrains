"""3. Реализовать функцию my_func(), которая принимает три позиционных аргумента
и возвращает сумму наибольших двух аргументов.
"""
import random


# For 3 arguments. V1
def sum_args_a(a, b, c):
    return sum(sorted([a, b, c])[:-3:-1])
# V2
def sum_args_b(a, b, c):
    return sum(sorted([a, b, c], reverse=True)[:2])


# V3
sum_args_c = lambda a, b, c: sum(sorted([a, b, c], reverse=True)[:2])


# Test purpose
for _ in range(11):
    num = [random.randint(1, 10) for i in range(3)]
    print(num, (*(i(*num) for i in [sum_args_a, sum_args_b, sum_args_c]), ), sep='; ')
