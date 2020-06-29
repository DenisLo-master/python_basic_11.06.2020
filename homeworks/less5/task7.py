"""7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название,
форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста."""

import json

firm = {}
average_profit = {}
statistics = []

with open('task7-file1.txt', 'r') as f1:
    template = []
    sum = 0
    count = 0
    for line in f1:
        template = line.split()
        profit = int(template[2]) - int(template[3])
        if profit > 0:
            firm[template[0]] = profit
            sum += profit
            count += 1
        else:
            firm[template[0]] = '-' + template[3]

average_profit['average_profit'] = sum / count
statistics.append(firm)
statistics.append(average_profit)
print(statistics)

with open('task7-file2.json', 'w', encoding='utf-8') as f2:
    json.dump(statistics, f2)
