# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.

user_words = input('Введите слова через проблел:\n')
user_list = user_words.split()
id_word = 0
for item in user_list:
    id_word += 1
    print(f'{id_word}. {item[:10]}')