"""1. Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя, а указать явно, в программе."""

my_list = ['text', 1, [12, 13, 14], {1: 100, 2: 200, 3: 300}, ('a', 'b', 'c'), {1, 3, 4, 5}]
i = 0
while i < len(my_list):
    print(type(my_list[i]))
    i += 1
