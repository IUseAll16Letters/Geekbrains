"""7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта, создав экземпляры класса (комплексные числа) и
выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата."""


# Solution 1
class MyComplex:

    def __init__(self, real, imag=0):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        if isinstance(other, MyComplex):
            return MyComplex(self.real + other.real, self.imag + other.imag)
        else:
            raise TypeError(f'Wrong data type for other: {type(other)}, expected MyComplex')

    def __mul__(self, other):
        if isinstance(other, MyComplex):
            r = self.real * other.real - self.imag * other.imag
            i = self.real * other.imag + self.imag * other.real
            return MyComplex(r, i)
        else:
            raise TypeError(f'Wrong data type for other: {type(other)}')

    def __str__(self):
        return f"{self.real}{'+' if self.imag > 0 else '-'}{abs(self.imag)}j"

if __name__ == '__main__':
    c1 = MyComplex(2, 4*(-4))
    c2 = MyComplex(5)
    print(c1 + c2, complex(2, 4*(-4)) + complex(5))
    print(c1 * c2, complex(2, 4*(-4)) * complex(5))
    try:
        print(c1 + 'as')
    except TypeError as T:
        print(T)
