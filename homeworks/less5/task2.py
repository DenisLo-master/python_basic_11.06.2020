"""2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке."""

with open('task2-file1.txt', 'r') as f:
    lines = 0
    words= 0
    for line in f:
        lines += 1
        for word in line.split(' '):
            words +=1
        print(f'Строка {lines}, количество слов в строке: {words}')
print(f'Количество строк в файле: {lines}')

