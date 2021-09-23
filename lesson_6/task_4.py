"""4. Реализуйте базовый класс Car.
у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
"""


class Car:
    """ Car base class """
    def __init__(self, color, name, is_police: bool = False):
        """
        :param color: - car color
        :param name: - car brand + car model name
        :param is_police: - checks if the car is police or not
        """
        self._speed = 0
        self.color = color
        self.name = name
        self.is_police = is_police
        self._direction = None

    def show_speed(self):
        """ Default speed display """
        print(f'{self.name} speed is: {self._speed}')

    def go(self, speed: int):
        """ Car is moving
        :param speed: = set car movement speed to speed
        """
        try:
            self._speed = int(speed)
            print(f"{self.color} {self.name} reached speed: {speed}")
        except ValueError:
            print('Wrong speed value')

    def stop(self, spd=0):
        """
        Slows down the car until it's full stop or slows down if speed limit is exceeded
        :param spd: 0 if you need to stop car, spd if you need to reduce speed in case of overreaching speed limit
        """
        from time import sleep
        for speed_value in range(self._speed, spd - 1, -int(self._speed / 5)):
            self._speed = speed_value
            print(f'\r{self.name} is slowing. Speed is {self._speed}', end='')
            sleep(0.5)
        self._speed = spd
        print('\nCar stopped.' if spd == 0 else f'\nCurrent speed is set to: {self._speed}')

    def turn(self, way):
        """
        Provides car movement direction
        :param way: movement direction  ('right', 'left', 'reversal')
        """
        if not self._speed:
            print("Can't make a turn, speed is 0")
            return
        if way.lower() not in ('left', 'right', 'reversal'):
            print(f'{way.title()} is wrong direction')
        else:
            print(f'{self.name} is moving {way}')
            self._direction = way

    @property
    def direction(self):
        """ Movement direction getter """
        return self._direction


class TownCar(Car):
    """ Town car class
    :param speed: has max speed limit = 60
    """
    # Optional solution _max_speed = 60, then check via hasattr(self, _max_speed)
    def show_speed(self):
        if self._speed >= 60:
            print(f'You are exceeding the speed limit for {self.__class__.__name__}')
            self.stop(60)
        else:
            print(f'{self.name} speed is {self._speed}')


class SportCar(Car):
    pass


class WorkCar(Car):
    """ Cargo carrier car class
    :param speed: has max speed limit = 40
    """
    def show_speed(self):
        if self._speed >= 40:
            print(f'You are exceeding the speed limit for {self.__class__.__name__}')
            self.stop(40)


class PoliceCar(Car):
    """ Class that marks car as police"""
    def __init__(self, name, color):
        super().__init__(name, color, is_police=True)


freds_garage = {TownCar:   ['Brown Metallic', 'Porsche Cayenne'],
                SportCar:  ['Red', 'Porsche 959'],
                WorkCar:   ['Green', 'VW Caravelle'],
                PoliceCar: ['White and Blue', 'Skoda Octavia']
                }

if __name__ == '__main__':
    for key, value in freds_garage.items():
        car = key(*value)
        # Display car data
        print('Car data'.center(28, '*'))
        print(f'Car class is: {car.__class__.__name__}')
        print(f'Car name is: {car.name}')
        print(f'Car color is: {car.color}')
        print(f'The car is undercover: {car.is_police}')
        print()

        # Display car moving features
        print('Car is moving'.center(28, '*'))
        car.show_speed()
        car.go(166)
        car.show_speed()
        car.stop()
        car.go(77)
        car.turn('right')
        print()