"""2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123]."""

import random

count = random.randrange(10, 20)
list = []
for i in range(count):
    list.append(random.randrange(1, 1000))
print(list)

result = []
for n in range(len(list)):
    print(n)
    if list[n] > list[n - 1]:
        result.append(list[n])
print(result)
