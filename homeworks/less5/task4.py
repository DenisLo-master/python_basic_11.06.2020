"""4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл."""

i = 0
dictionary = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
with open('task4-file1.txt', 'r') as f1:
    for line in f1:
        new_line = ''
        for word in line.split():
            if word in dictionary.keys():
                word_ru = dictionary[word]
                new_line += word_ru
            else:
                new_line += ' ' + word
        new_line += '\n'
        with open('task4-file2.txt', 'a') as f2:
            f2.write(new_line)
