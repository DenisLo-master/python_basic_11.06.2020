"""3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict."""
while True:
    try:
        u_month = int(input('Введите номер месяца:\n'))
        break
    except ValueError:
        print('Ошибка: Введите целое число\n')
        continue

# seasons = {'зима': (1, 2, 12), 'весна': (3, 4, 5), 'лето': (6, 7, 8), 'осень': (9, 10, 11)}
# for s_key, s_value in seasons.items():
#     if u_month in s_value:
#         print(s_key)
#         break



seasons = {'зима': 0, 'весна': 1, 'лето': 2, 'осень': 3}
a = u_month // 3 % 4
for s_key, s_value in seasons.items():
    if a == s_value:
        print(f'Время года: {s_key}')
        break


