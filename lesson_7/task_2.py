"""Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм.
размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани.
Реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""


from abc import ABC, abstractmethod


class AbstractClothes(ABC):
    """ Clothes interface """
    @property
    @abstractmethod
    def size(self):
        """ Default clothes size as property """
        pass
    
    @abstractmethod
    def _calc_required(self):
        """ Calculation of patterns required """
        pass


class Clothes(AbstractClothes):
    _clothes_created = []

    def __init__(self, name, size):
        """
        :param name: - Item name
        :param size: - Item size (height or size possible)
        :param rq_pattern: - Meters of pattern cloth required to make Item
        """
        self._name = name
        self._size = size
        self._rq_pattern = self._calc_required()

        self._clothes_created.append(self)

    @property
    def size(self):
        """ Getting the size """
        return self._size

    @size.setter
    def size(self, value):
        """ Setting the size """
        self._size = value
        self._calc_required()

    def _calc_required(self):
        return None

    @property
    def summary(self):
        return sum(i._rq_pattern for i in self._clothes_created)

    def __str__(self):
        definition = 'height' if self.__class__.__name__ == 'Suit' else 'volume'
        return f'To make {self._name} {self.__class__.__name__.lower()} ' \
               f"of {definition} {self.size} need {self._rq_pattern} m^2 of pattern"


class Suit(Clothes):

    # Prishlos obhoditsya vot takoy urodlivoy zaplatkoy... i translitom ://
    def _calc_required(self):
        self._rq_pattern = round((self.height / 100) * 2 + 0.3, 2)
        return self._rq_pattern

    @property
    def height(self):
        """ Size from Clothes class """
        return self.size

    @height.setter
    def height(self, value):
        self.size = value


class Coat(Clothes):
    # I snova vot takaya urodlivaya zaplatka... i translit ://
    def _calc_required(self):
        self._rq_pattern = round(self.volume / 6.5 + 0.5, 2)
        return self._rq_pattern

    @property
    def volume(self):
        return self.size

    @volume.setter
    def volume(self, value):
        self.size = value


if __name__ == '__main__':
    cach = Suit('Cacharel', 182)
    print(cach)
    cach.height = 195
    print(cach)
    print(cach.summary)

    guc = Coat('You Gucci', 25)
    print(guc)
    guc.volume = 48
    print(guc)
    print(guc.summary, cach.summary)
