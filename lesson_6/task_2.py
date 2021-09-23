"""2. Реализовать класс Road (дорога). определить атрибуты: length (длина), width (ширина);
значения атрибутов должны передаваться при создании экземпляра класса;
атрибуты сделать защищёнными;
определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
использовать формулу: длина * ширина * масса асфальта для покрытия одного кв. метра дороги асфальтом,
толщиной в 1 см*число см толщины полотна.

Например: 20 м*5000 м*25 кг*5 см = 12500 т.
"""


class Road:
    """
    Road surface class
    """
    def __init__(self, length, width):
        """
        :param length:  - road length
        :param width:  - road width
        """
        self._length = length
        self._width = width

    def ground_mass(self, thickness, mass=25):
        """
        Calculate the mass of raw asphalt
        :param thickness: thickness of road surface
        :param mass: mass of 1kilo of raw asphalt
        :return: mass of the required raw asphalt in tons
        """
        mass = 25
        print(f"To cover the road of {self._width} x {self._length} meters square, "
              f"with surface of {thickness} cm thickness:")
        return f'required {(self._width * self._length * mass * thickness) // 1000} tons of asphalt. '


if __name__ == '__main__':
    with open('task_2.txt', 'r+') as S:
        for i in S.readlines():
            l, w, th = list(map(int, i.split()))
            hw = Road(l, w)
            print(hw.ground_mass(th))
