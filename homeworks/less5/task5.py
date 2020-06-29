"""5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран."""
import random

sum = 0
my_list = [str(random.randrange(10, 100)) for i in range(15)]
line = ' '.join(my_list)
for i in range(len(my_list)):
    sum += int(my_list[i])

with open('task5-file1.txt', 'w', encoding='Utf-8') as f:
    f.write(line)
    f.write(f'\nСумма чисел: {sum}')
