# 5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек,
# или убыток — издержки больше выручки). Выведите соответствующее сообщение. Если фирма отработала с прибылью,
# вычислите рентабельность выручки (соотношение прибыли к выручке). Далее запросите численность сотрудников фирмы и
# определите прибыль фирмы в расчете на одного сотрудника.

revenue = ''
costs = ''
count_employee = ''

while True:
    revenue = input('Введите выручку Вашей компании:\n')
    if not revenue.isdigit():
        print('!!!введите только целое положительное число!!!')
        continue
    break

while True:
    costs = input('Введите издержки Вашей компании:\n')
    if not revenue.isdigit():
        print('!!!введите только целое положительное число!!!')
        continue
    break

if revenue > costs:
    print('Ваша компания отработала с прибылью')
    profit = int(revenue)-int(costs)
    profitability = profit/int(revenue)
    while True:
        count_employee = input('Введите количество сотрудников в Вашей компании:\n')
        if not count_employee.isdigit():
            print('!!!введите только число!!!')
            continue
        break
    profit_per_employee = profit / int(count_employee)
    print(f'Прибыль Вашей компании: {profit}', f'Прибыль в расчете на одного сотрудника: {profit_per_employee}', sep = '\n')


else:
    print('К сожалению, Ваша компания отработала в убыток')