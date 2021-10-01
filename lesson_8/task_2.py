"""2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию
и не завершиться с ошибкой."""


class MyZeroDivision(Exception):

    def __str__(self):
        return "Impossible to divide by 0 pieces"


class Number(float):

    def __truediv__(self, other):
        try:
            if other == 0:
                raise MyZeroDivision
            else:
                return Number(float(self) / float(other))
        except MyZeroDivision as E:
            return E

if __name__ == '__main__':
    h = Number(15)
    m = Number(0)

    print(h / m)
    print(h / 4)
    print(0 / 15)
    print(15 / -15)