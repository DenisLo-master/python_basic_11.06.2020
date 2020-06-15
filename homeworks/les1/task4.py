#4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

number = ''
numbers = []

while True:
    number = input('Введите число:\n')
    if not number.isdigit():
        print('!!!введите только целое положительное число!!!')
        continue
    if int(number) < 10:
        print('!!!введите число больше 10!!!')
        continue
    break
i = len(number)
print(i)
while not i == 0:
    n = len(number)
    while not n == 0:
        if number[i] - number[n] > 0
    i -= 1
    i = len(numbers)