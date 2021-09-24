"""1. Реализовать класс Matrix (матрица).
Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Реализовать перегрузку метода __str__() для вывода матрицы в привычном виде,
перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
"""


class Matrix:
    """ Class defining a matrix  """
    def __init__(self, matrix_data: list):
        """
        :param matrix_data: list of lists
        """
        self.__matrix = matrix_data
        matrix_rows = len(self.__matrix)
        self.__matrix_size = set([(matrix_rows, len(line)) for line in self.__matrix])

    def __add__(self, other: "Matrix") -> "Matrix":
        """
        Summation of matrices
        :return: Matrix type object with result list as attribute
        """
        if type(self) != type(other):
            raise ValueError('Summating wrong object type')
        if self.__matrix_size != other.__matrix_size:
            raise ValueError("Matrices have different size")
        
        res = []
        for m1, m2 in zip(self.__matrix, other.__matrix):
            res.append([v1 + v2 for v1, v2 in zip(m1, m2)])
        return Matrix(res)
        
    def __str__(self) -> str:
        return '\n'.join('\t'.join(map(str, row)) for row in self.__matrix)


d1 = [[1, 2, 5], [3, 4, 5]]
d2 = [[5, 6, 5], [7, 8, 7]]

ma = Matrix(d1)
mb = Matrix(d2)

print(ma + mb)