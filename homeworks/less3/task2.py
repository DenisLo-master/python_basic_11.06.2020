"""2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой."""

def profile(name: str, surname: str, date_of_b: str, city: str, email: str, phone: int) -> str:
    """
    displays user profile in line

    :return: result all params in line
    """
    result = f'Анкета поьзователя: {name}, {surname}, {date_of_b}, {city}, {email}, {phone}'
    return result

print(profile(name='Den', surname='L', date_of_b='25.01.85', city='Saint-Peterburg', email='denis.lkg@gmail.com', phone='9261577467'))
