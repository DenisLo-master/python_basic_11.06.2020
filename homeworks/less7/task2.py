"""
2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта —
 одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
 У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
 Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""

from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, name):
        self.name = name

    def type(self):
        print(self.__class__.__name__)

    @abstractmethod
    def size(self):
        pass

    @abstractmethod
    def consumption(self):
        pass


class Suit(Clothes):
    @property
    def size(self):
        return self.__H

    @size.setter
    def size(self, param):
        self.__H = param

    def consumption(self):
        self.__result = 2 * self.__H + 0.3
        return f'расход материала на {self.__class__.__name__} "{self.name}" составит {self.__result} п.м'

class Coat(Clothes):
    @property
    def size(self):
        return self.__V

    @size.setter
    def size(self, param):
        self.__V = param

    def consumption(self):
        self.__result = self.__V/6.5 + 0.5
        return f'расход материала на {self.__class__.__name__} "{self.name}" составит {self.__result} п.м'


if __name__ == '__main__':
    a1= Suit('Чилинтано')
    a2= Suit('Bond')
    a2.size=1.5
    b1=Coat('Colombo')

print(1)