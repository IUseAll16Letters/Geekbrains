"""3. Необходимо создать класс Клетка. В его конструкторе инициализировать параметр,
соответствующий количеству ячеек клетки.
Должны быть реализованы методы перегрузки арифметических операторов: (__add__()), (__sub__()), (__mul__()),
(__truediv__()). Данные методы должны применяться только к клеткам.
В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
Данный метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
"""


class Cell:
    """ Class of simple cell """
    def __init__(self, size):
        """
        :param size: Size of the cell. Check setattr for limit values
        """
        self.size = size
    
    def __add__(self, other):
        """ Summation of cells """
        if isinstance(other, Cell):
            return Cell(self.size + other.size)
        raise ValueError('Wrong class')
        
    def __sub__(self, other):
        """ Subtraction of cells """
        if isinstance(other, Cell):
            if self.size > other.size:
                return Cell(self.size - other.size)
            return "2nd Cell is bigger than initial, cell will be destroyed"
        raise ValueError('Wrong class')
        
    def __mul__(self, other):
        """ Multiplication of cells """
        if isinstance(other, Cell):
            return Cell(self.size * other.size)
        raise ValueError('Wrong class')
    
    def __truediv__(self, other):
        """ True Division of cells. For Cell - floor div"""
        if isinstance(other, Cell):
            return Cell(self.size // other.size)
        raise ValueError('Wrong class')

    def __setattr__(self, key, value):
        """ Sets the limitation for size attribute """
        if key == 'size' and value <= 0:
            print('Size value too low, set to minimal possible value: 1')
            self.__dict__[key] = 1
        else:
            self.__dict__[key] = value

    def __str__(self):
        return f'Cell size is {self.size}'
    
    def make_order(self, row):
        """
        Displaying method
        :param row: how many cells in one line as oneliner
        """
        return '\n'.join('*' * row for _ in range(self.size // row)) + f"\n{'*' * (self.size % row)}"


if __name__ == '__main__':
    v = Cell(0)
    h = Cell(14)
    m = Cell(25)
    print(h)
    print(m)
    print((h + m).make_order(min(h.size, m.size)))
    print(h + m)
    print(h - m)
    print(m - h)
    print(h * m)
    print(h / m)
    print(m / h)
    g = m / h
    print(g.make_order(4))
