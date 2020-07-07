"""1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
 (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой
матрицы складываем с первым элементом первой строки второй матрицы и т.д."""


class Matrix:
    def __init__(self, list):
        self.list = list

    def __iter__(self):
        return Matrix(self.list)

    def __getitem__(self, item):
        return self.list[item]

    def __str__(self):
        return '\n'.join(map(str, self.list))

    def __call__(self, *args, **kwargs):
        print(self)

    def __add__(self, other):
        if len(self.list) == len(other.list):
            result = []
            for _i in range(len(self.list)):
                raw = []
                for _j in range(len(self.list[_i])):
                    raw.append(self.list[_i][_j] + other.list[_i][_j])
                result.append(raw)
            return Matrix(result)
        raise ValueError or IndexError('различаются матрицы')



if __name__ == '__main__':
    list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    list2 = [[11, 12, 13], [14, 15, 16], [17, 18, 19]]
    list3 = [[11, 12, 13], [14, 15, 16], [17, 18, 19], [20, 21, 22]]
    list4 = [[11, 12], [14, 15], [17, 18]]
    m1 = Matrix(list1)
    m2 = Matrix(list2)
    m3 = Matrix(list3)
    m4 = Matrix(list4)
print(1)
