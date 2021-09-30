"""7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта, создав экземпляры класса (комплексные числа) и
выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата."""


# Solution 2
class MyComplex:

    def __init__(self, real, imag=0):
        self.__complex = complex(real, imag)

    def __add__(self, other):
        if isinstance(other, MyComplex):
            comp = self.__complex + other.__complex
            return MyComplex(comp.real, int(comp.imag))
        else:
            raise TypeError(f'Wrong data type for other: {type(other)}')

    def __mul__(self, other):
        if isinstance(other, MyComplex):
            value = self.__complex * other.__complex
            return MyComplex(value)
        else:
            raise TypeError(f'Wrong data type for other: {type(other)}')

    def __str__(self):
        return self.__complex.__str__()


if __name__ == '__main__':
    c1 = MyComplex(2, 4*(-4))
    c2 = MyComplex(5)
    print(c1 + c2, complex(2, 4*(-4)) + complex(5))
    print(c1 * c2, complex(2, 4*(-4)) * complex(5))
    try:
        print(c1 + 'as')
    except TypeError as T:
        print(T)
