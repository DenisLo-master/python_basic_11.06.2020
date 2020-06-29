"""6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество. Важно,
чтобы для каждого предмета не обязательно были все типы занятий. Сформировать словарь,
 содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}"""


dict = {}
# Вариант1:
# with open('task6-file1.txt', 'r') as f:
#     for line in f:
#         sum = 0
#         for item in line.split():
#             if ':' in item:
#                 lesson = item
#             else:
#                 number = ''
#                 for n in item:
#                     if n.isdigit():
#                         number += n
#                 if number != '':
#                     sum += int(number)
#         dict[lesson] = sum
#     print(dict)

# Вариант2:
template = []
item_list = []
with open('task6-file1.txt', 'r') as f:
    for line in f:
        item_list.clear()
        for item in line.split():
            item_list.append(item)
        template.append(item_list.copy())

for line in template:
    sum = 0
    for item in line:
        if ':' in item:
            lesson = item
        else:
            number = ''
            for n in item:
                if n.isdigit():
                    number += n
            if number != '':
                sum += int(number)
        dict[lesson] = sum
print(dict)
