number = ''

while True:
    number = input('Введите число:\n')
    if not number.isdigit():
        print('!!!введите только число!!!')
        continue
    break
result = int(number) + int(number * 2) + int(number * 3)
print(f'выражение n + nn + nnn будет равно:{result}')