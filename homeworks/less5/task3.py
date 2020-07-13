"""3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. Определить,
кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников."""


user_list = []
with open('task3-file1.txt', 'r') as f:
    for line in f:
        template = []
        for word in line.split():
            template.append(word)
        user_list.append(template)
print(user_list)

low_salary = 20000
i = 0
sum_salary = 0
avr = 0
print('-' * 34)
print(f'Сотрудники c окладом менее 20 000:')
for i in range(len(user_list)):
    if int(user_list[i][1]) < low_salary:
        print(user_list[i][0])
        sum_salary += int(user_list[i][1])
        avr += 1
print('-' * 34)
print(f'Средний доход сотрудников: {int(sum_salary / avr)}')
