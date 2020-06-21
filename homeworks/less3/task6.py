"""6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func()."""


def int_func(word: str) -> str:
    """
    function to replace the first lowercase letter with an uppercase

    :param word: lowercase word
    :return: The first letter in the word is uppercase
    """
    capital_letter = word[0].upper()
    result_word = capital_letter + word[1:]
    return result_word


i = 0
result_text = ''
text = input('Введите слова через пробел:\n')
list_word = text.split()
while i < len(list_word):
    list_word[i] = int_func(list_word[i])
    result_text = result_text + list_word[i] + ' '
    i += 1
print(result_text)
