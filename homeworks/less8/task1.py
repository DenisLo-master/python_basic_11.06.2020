"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц,
год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
 месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""
import datetime as dt


class Date:
    today = None
    day = int
    month = int
    year = int

    def __init__(self):
        Date.today = dt.date.today()
        self.log_date = dt.date.strftime(Date.today, '%d-%m-%Y')

    def __repr__(self):
        return str(self.log_date)

    @classmethod
    def convert(cls):
        cls.day = cls.today.day + 30
        cls.month = cls.today.month
        cls.year = cls.today.year

    @staticmethod
    def validation():
        if Date.day < 1 or Date.day > 31:
            print(Date.day, 'День указан не верно')
        if Date.month < 1 or Date.month > 12:
            print(Date.month, 'Месяц указан не верно')
        if Date.year < 0 or Date.year > 2020:
            print(Date.year, 'Месяц указан не верно')


if __name__ == '__main__':
    a = Date()
    a.convert()
    b = Date()
    a.validation()
    print(1)
