"""3. Реализовать базовый класс Worker (работник).
определить атрибуты: name, surname, position (должность), income (доход);
последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus};
создать класс Position (должность) на базе класса Worker;
в классе Position реализовать методы получения полного имени сотрудника (get_full_name)
и дохода с учётом премии (get_total_income);
проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров.
"""


class Worker:
    """
    Worker init class
    :param name: employee name
    :param surname: employee surname
    :param position: employee position
    :param wage: employee raw income
    :param bonus: employee bonus (conditions are not provided)
    """
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    """
    Class that provides info about worker
    :get_full_name: - employee full name
    :get_total_income: - calculates employee total income
    """

    def get_full_name(self):
        return ' '.join([self.name, self.surname])

    def get_total_income(self):
        return f"{self.position}'s income is: {self._income['wage'] + self._income['bonus']}"


if __name__ == '__main__':
    employees = [{'name': 'Ivan', 'surname': 'Petrikov', 'position': 'Logistics dpt chief',
                  'wage': 125000, 'bonus': 38000}]
    iv = Position(**employees[0])
    print(iv.get_full_name(), iv.get_total_income(), sep='\n')