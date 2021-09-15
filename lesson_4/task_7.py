"""7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
При вызове функции должен создаваться объект-генератор. Функция вызывается следующим образом: for el in fact(n).
Она отвечает за получение факториала числа. В цикле нужно выводить только первые n чисел, начиная с 1! и до n!.
Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
"""
import functools


# Solution 0: from math import factorial
# Solution 1
def conseq_multiplication(el_p, el):
    return el_p * el


fact = lambda num: functools.reduce(conseq_multiplication, (i for i in range(1, num + 1)))


def fact_in_face(n):
    for el in range(n + 1):
        if el == 0:
            yield 1
        else:
            yield fact(el)


# Solution 2
def fact(n):
    return 1 if n == 0 else n * fact(n - 1)


def face_the_fact(n):
    for el in range(n + 1):
        yield fact(el)


if __name__ == '__main__':
    print(*fact_in_face(6))
if __name__ == '__main__':
    print(*face_the_fact(6))
