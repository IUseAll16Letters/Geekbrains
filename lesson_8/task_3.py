"""3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
Класс-исключение должен контролировать типы данных элементов списка.

Длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу скрипта,
введя, например, команду “stop”. При этом скрипт завершается, сформированный список выводится на экран.
"""


class NotNumberError(Exception):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text


if __name__ == '__main__':
    my_list = []

    while True:
        user_input = input("Enter integer or stop to finish script: ")

        if user_input.lower() in "stop":
            break

        try:
            if not user_input.isdigit():
                raise NotNumberError(f"'{user_input}' is not digit")

            my_list.append(int(user_input))
        except NotNumberError as e:
            print(e)

    print(my_list)
