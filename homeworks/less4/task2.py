"""2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123]."""

import random

list = [random.randrange(1, 1000) for i in range(10, 20)]
print(list)

# result = []
# for n in range(len(list)):
#     if list[n] > list[n - 1]:
#         result.append(list[n])
# print(result)


result = [item for idx, item in enumerate(list) if idx and item > list[idx - 1]]
print(result)
