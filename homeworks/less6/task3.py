"""3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров)."""


class Worker:
    name = None
    surname = None
    position = None
    __income = {'wage': 10000, 'bonus': 6000}

class Position(Worker):
    full_name = None
    total_income = None

    def get_full_name(self):
        self.full_name = Position.name + ' ' + Position.surname
        return self.full_name

    def get_total_income(self):
        self.total_income = _Worker.__income['wage'] + _Position.__income['bonus']
        return self.total_income

Worker.name = 'Dima'
Worker.surname = 'Smirnov'
Worker.position = 'CEO'
# Worker.__income['wage']=120000
# Worker.__income['bonus']=200000

print(1)

