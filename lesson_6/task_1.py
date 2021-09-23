"""1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный.
В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
(красный) - 7 секунд, (желтый) — 2 секунды, (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов,
и при его нарушении выводить соответствующее сообщение и завершать скрипт."""

import time
from datetime import datetime as dt


class TrafficLight:
    """
    TrafficLight class. Has 3 modes.
    Can change light indication based on each mode duration.
    """
    modes = (('red', 'yellow', 'green'), (7, 2, 14))
    __color = 'green'
    
    def running(self, DIAGNOSTICS_STATE=False):
        """
        TrafficLight running method, color depends on modes order.
        :var DIAGNOSTIC_STATE:  for diagnostics and malfunction cases
        if order is wrong - diagnostics state initialized
        """
        while not DIAGNOSTICS_STATE:
            for i in range(3):
                if self.__color == self.modes[0][i-1]:
                    self.__color = self.modes[0][i]
                    print(f'Switching to: {self.__color}')
                    log = f'State: {self.__color[:3]} || Diagnostics initialized: {DIAGNOSTICS_STATE} || ' \
                          f'time: {dt.now()}'
                    print(log)
                    time.sleep(self.modes[1][i])
                else:
                    DIAGNOSTICS_STATE = True
                    print(f'Malfunction occurred: {dt.now()} || at color: {self.__color} || '
                          f'expected: {self.modes[0][i-1]}')
                    break
                    # Save somewhere


n3223_e3554 = TrafficLight()
n3223_e3554.running()
