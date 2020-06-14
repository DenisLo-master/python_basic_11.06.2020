"Home Work"

greeting = 'Привет, незнакомец!!!'
name = ''
numbers = []
count = 5
i = count - 1

print(greeting)
name = input('Как тебя зовут?\n')
print(f'Спасибо, {name}, а теперь введите пожалуйста {count} чисел')

while i > -1:
    number = input(f'Число №{count-i}:\n')
    if number.isdigit():
        numbers.append(number)
        i -= 1
        continue
    print('!!!введите только число!!!')
print(f'{name}, Вы ввели {numbers}')

