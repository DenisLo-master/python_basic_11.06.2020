"""
4. Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
"""


def my_func1(x: int, y: int) -> int:
    """
    Возведение числа в степень с использование **
    :param x: число
    :param y: степень
    :return: возведенное число x в степень y
    """
    result = x ** y
    return result


def my_func2(x: int, y: int) -> int:
    """
    Возведение числа в степень с использованием цикла
    :param x: число
    :param y: степень
    :return: возведенное число x в степень y
    """
    i = 2
    if y == 0:
        x = 1
    elif y == 1:
        x = x
    elif y > 0:
        i_result = x
        while i <= y:
            i_result = i_result * x
            i += 1
        x = i_result
    elif y == -1:
        x = 1 / x
    elif y < 0:
        i_result = x
        while i <= y * (-1):
            i_result = (i_result * x)
            i += 1
        x = 1 / i_result

    return x


while True:
    try:
        number1 = int(input('Введите целое положительное число: '))
        if number1 > 0:
            break
        else:
            raise ValueError
    except ValueError:
        print('Ошибка')
        continue
while True:
    try:
        number2 = int(input('Введите целое отрицательное число: '))
        if number2 < 0:
            break
        else:
             raise ValueError
    except ValueError:
        print('Ошибка')
        continue

print(my_func1(number1, number2))
print('-' * 30)
print(my_func2(number1, number2))
