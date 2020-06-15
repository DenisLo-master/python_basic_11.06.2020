#4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

number = ''
numbers = []
current_max = 0

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
while not i == 0:
    if int(number[i-1]) > int(current_max):
        current_max = number[i-1]
    i -= 1
print(f'Максимальное число - {current_max}')