"""5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел. "
У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2]."""

while True:
    try:
        u_number = int(input('Введите число:\n'))
        break
    except ValueError:
        print('Ошибка: Введите целое число\n')
        continue

my_list = [7, 5, 3, 3, 2]
i = 0
while i < len(my_list):
    if u_number > my_list[0]:
        my_list.insert(0, u_number)
        break
    elif u_number < my_list[-1]:
        my_list.append(u_number)
        break
    elif u_number == my_list[i]:
        count = my_list.count(u_number)
        my_list.insert(i + count, u_number)
        break
    i += 1
print(my_list)

