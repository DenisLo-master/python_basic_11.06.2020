"""2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой."""


class MyZeroDivisionError(Exception):
    def __str__(self):
        return f'ОШИБКА: Деление на 0 не допустимо'



dividend = int(input('Введите делимое: '))
while True:
    try:
        divider = int(input('Введите делитель: '))
        if divider == 0:
            raise MyZeroDivisionError
    except MyZeroDivisionError as e:
        print(e)
    else:
        print(dividend / divider)
        break
