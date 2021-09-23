"""5. Реализовать класс Stationery (канцелярская принадлежность).
определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationery:
    """ Overall stationery class"""
    title = 'Stationery'

    def draw(self, image):
        """
        Overall Stationery draws
        :param image: - any image you want, kid
        """
        print('Something somewhere')


class Pen(Stationery):
    """ Class for pen, the pen can only write sth down """
    title = 'Pen'

    def draw(self, image):
        """
        Drawing with Pen
        :param image: - any image you want, kid
        """
        print(f'The {self.title} is writing a(an) {image}')


class Pencil(Stationery):
    """ Class for pencil, the pencil draw anything you like """
    title = 'Pencil'

    def draw(self, image):
        """
        Drawing with Pencil
        :param image: - any image you want, kid
        """
        print(f'The {self.title} is drawing a(an) {image}')


class Handle(Stationery):
    """ Class for handle, the handle's purpose is to mark or highlight drawn with pen """
    title = 'Handle'

    def draw(self, image):
        """
        Highlighting with handle
        :param image: - anything you want to mark
        """
        print(f'The {self.title} is highlighting a(an) {image}')


first_pen = Pen()
first_pen.draw('Super important document')

first_pencil = Pencil()
first_pencil.draw('Village people')

first_handle = Handle()
first_handle.draw(f'Super important documents written by {first_pen.title}')
