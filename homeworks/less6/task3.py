"""3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров)."""


class Worker:
    def __init__(self, name, surname, wage, bonus):
        self.name = name
        self.surname = surname
        self.__income = {'wage': wage, 'bonus': bonus}

    def get_full_name(self):
        self.full_name = self.name + ' ' + self.surname
        return self.full_name

    def get_total_income(self):
        self.total_income = self.__income['wage'] + self.__income['bonus']
        return self.total_income


class Position(Worker):
    def __init__(self, position, name, surname, wage, bonus):
        self.position = position
        super().__init__(name, surname, wage, bonus)


if __name__ == '__main__':
    tmp = Position('Менеджер', 'Dims', 'Pitpit', 120000, 19000)

print(1)
