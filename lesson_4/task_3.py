"""3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Решите задание в одну строку.
Подсказка: используйте функцию range() и генератор.
"""


# Solution 1. Oneliner
division_generator = lambda: (i for i in range(20, 241) if i % 21 == 0 or i % 20 == 0)


# Solution 2. iq55
def division():
    for i in range(21, 241, 21):
        yield i
    for i in range(20, 241, 20):
        yield i

if __name__ == '__main__':
    print(*division_generator())
    print(*sorted(division()))
