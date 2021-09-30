"""1. Реализовать класс «Дата»,
функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год». -
В рамках класса реализовать два метода. Первый, с декоратором @classmethod.
Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число». -
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""


class Number(int):
    def __str__(self):
        return f'{self:02}'


class Date:
    time = ('y', 'm', 'd')

    def __init__(self, data: str):
        time_per = data.split('-')

        if not self.validate(time_per):
            raise ValueError(f'{data} - date is invalid')

        self.y, self.m, self.d = self.transfer(time_per)

    def __iter__(self):
        for att in self.time:
            yield self.__getattribute__(att)

    @classmethod
    def transfer(cls, dt):
        return [Number(_) for _ in dt]

    @staticmethod
    def validate(data):
        try:
            d, m, y = [int(i) for i in data]
        except TypeError:
            print('7')
            return False
        days = 30 if m in (4, 6, 9, 11) else 28 + (y % 4 == 0) if m == 2 else 31
        return all([y >= 1970, 1 <= m <= 12, 1 <= d <= days])

    def __str__(self):
        return f"The date is: {'-'.join([str(item) for item in self])}"


dates = ['35-08-1987', '20-02-2002', '29-02-2004', 'as-08-2002']

for i in dates:
    try:
        print(Date(i))
    except ValueError as E:
        print(E)
