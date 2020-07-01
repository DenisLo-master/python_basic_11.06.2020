"""4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат."""


class Car:
    speed = 0
    color = None
    name = None
    police = bool
    count = 0
    direction = None

    def __init__(self):
        Car.count += 1
        print(Car.count)

    def go(self, speed):
        Car.speed = speed
        return 'поехали'

    def stop(self):
        Car.speed = 0
        return 'остановились'

    def turn(self, direction):
        Car.direction = direction
        return 'повернули'

    def show_speed(self):
        return Car.speed


class Town(Car):
    police = False
    def show_speed(self):
        if self.speed > 40:
            return 'Превышение скорости'
        return WorkCar.speed


class SportCar(Car):
    police = False

class WorkCar(Car):
    police = False
    def show_speed(self):
        if self.speed > 60:
            return f'Превышение скорости {WorkCar.speed}'
        return WorkCar.speed


class PoliceCar(Car):
    police = True


Car.color = 'Красный'
Car.name = 'Man'
Car.police = False
print('1')
