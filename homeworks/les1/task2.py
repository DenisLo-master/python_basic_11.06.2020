time_seconds = ''
seconds = ''
minutes = ''
hours = ''

while True:
    time_in_seconds = input('Введите время в секундах:\n')
    if not time_in_seconds.isdigit():
        print('!!!введите только число!!!')
        continue
    time_in_seconds = int(time_in_seconds)
    break

hours = time_in_seconds // 3600
minutes = (time_in_seconds - hours * 3600) // 60
seconds = time_in_seconds - hours * 3600 - minutes * 60

if hours < 10:
    hours = f'0{hours}'
if minutes < 10:
    minutes = f'0{minutes}'
if seconds < 10:
    seconds = f'0{seconds}'

print(f'Время - {hours}:{minutes}:{seconds}')
