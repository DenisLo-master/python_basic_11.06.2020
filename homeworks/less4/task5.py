"""5. Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы). Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce()."""

import random

from functools import reduce

list = [random.randrange(100, 1001) for i in range(10)]
result = reduce(lambda x, y: x * y, list)
print(list)
print(result)
