"""1. Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника.
Используйте в нём формулу: (выработка в часах*ставка в час) + премия.
Во время выполнения расчёта для конкретных значений необходимо запускать скрипт с параметрами.
"""
# Solution with argprase
import argparse


parser = argparse.ArgumentParser(description='Calculating employee salary.')
parser.add_argument('-w', '--hours_worked', type=int, required=True, default=0,
                    help='Enter amount of employee working hours for scored period. (1 Month)')
parser.add_argument('-r', '--rate', type=int, required=True, default=5,
                    help='Enter the employee 1/h pay rate.')
parser.add_argument('-b', '--bonus', type=int, required=True, default=0,
                    help='Enter the employee bonus rate. Conditions for obt. bonus = more than 150 hours worked.')
args = parser.parse_args()


def salary():
    """

    Employee kpi: working hours >= 150

    """
    bonus = args.bonus if args.hours_worked >= 150 else 0
    bonus_notification = f'Including bonus: {bonus}' if bonus else ''
    return f"Employee's salary is: {args.hours_worked * args.rate + bonus}. " + bonus_notification


print(salary())
