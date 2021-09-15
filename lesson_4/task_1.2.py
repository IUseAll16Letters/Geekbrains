"""1. Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника.
Используйте в нём формулу: (выработка в часах*ставка в час) + премия.
Во время выполнения расчёта для конкретных значений необходимо запускать скрипт с параметрами.
"""
# Solution with sys.argv
from sys import argv

name, work_hour, hour_rate, bonus = argv


def calculate_income():
    """

    Employee kpi: working hours >= 150

    """
    return f"Worker's salary: {int(work_hour) * int(hour_rate) + (int(bonus) if int(work_hour) >= 150 else 0)}. " \
           f"{'Including bonus: ' + str(bonus)  if int(work_hour) >= 150 else 'No bonus'}"


print(calculate_income())
