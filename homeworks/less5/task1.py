"""1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка."""

while True:
    user_text = input('Введите текст для записи в файл:\n')
    if user_text == '':
        break
    with open('sample.txt', 'a', encoding='utf-8') as f:
        f.write(user_text)
