"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.
"""


def my_func(num1: int, num2: int, num3: int) -> int:
    """
    search for two of the smallest arguments out of three

    :param num1: any number
    :param num2: any number
    :param num3: any number
    :return: print (sum of two max value)
    """
    m1_num = 0
    m2_num = 0
    i = 0
    numbers = [num1, num2, num3]
    while i < len(numbers):
        m1_num = numbers[i] if numbers[i] > m1_num else m1_num
        i += 1
    i = 0
    while i < len(numbers):
        m2_num = numbers[i] if m1_num > numbers[i] > m2_num else m2_num
        i += 1
    print(m1_num + m2_num)


my_func(14, 15, 7)
