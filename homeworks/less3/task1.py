"""1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль"""


def division(dividend: int, divider: int) -> int:
    """produces division

    param: dividend, divider - int
    :return: print result
    """
    try:
        result = dividend / divider
    except ZeroDivisionError:
        print('Ошибка деления на 0')
        exit()
    print(result)


while True:
    try:
        number1 = int(input('Введите делимое: '))
        break
    except ValueError:
        print('Введите целое число')
        continue
while True:
    try:
        number2 = int(input('Введите делитель: '))
        break
    except ValueError:
        print('Введите целое число')
        continue


division(number1, number2)
