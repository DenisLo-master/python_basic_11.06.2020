"""2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
 Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
  Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
  Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
   толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.
Например: 20м * 5000м * 25кг * 5см = 12500 т"""


class Road:
    _length = 20
    _width = 5000

    def square(self, thickness=1):
        self.sq = Road._length * Road._width
        self.mass = self.sq * (thickness / 100) * 25
        print(f'{self.mass / 1000} тонн')


a = Road()
a.square(15)
print(1)