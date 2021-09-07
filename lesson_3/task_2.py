"""2. Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Осуществить вывод данных о пользователе одной строкой.
"""
from random import randint as r, choice
from string import ascii_letters as asc


def user_info(name, surname, born, city, email='a', phone='a'):
    return f"User: {name} {surname}. Was born in {born}. Lives in {city}. Contacts: email - {email}; phone - {phone}"


# Generating a perfect user
random_word = lambda x, y: ''.join(choice(asc) for _ in range(r(x, y))).capitalize()
n = random_word(3, 10)
s = random_word(3, 15)
y = int(r(1901, 2002))
c = '-'.join((random_word(3, 10) for _ in range(choice([1, 1, 1, 2]))))
e = f'{random_word(3, 15)}@{random_word(2, 4)}.{random_word(2, 3)}'
p = f"+{r(1,9)}({''.join(str(r(0, 9)) for i in range(3))}){''.join(str(r(0, 9)) for i in range(7))}"


print(user_info(n, s, y, c, e, p))
