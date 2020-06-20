#3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

number = ''

while True:
    number = input('Введите число:\n')
    if not number.isdigit():
        print('!!!введите только целое положительное число!!!')
        continue
    break
result = int(number) + int(number * 2) + int(number * 3)
print(f'выражение n + nn + nnn будет равно:{result}')