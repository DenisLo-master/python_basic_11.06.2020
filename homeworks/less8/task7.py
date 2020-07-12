"""7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата."""


class Complex_number:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        self.c_number = complex(self.num1, self.num2)

    def __repr__(self):
        return f'({self.num1}+{self.num2}j)'

    def __add__(self, other):
        # return self.c_number + other.c_number
        print(f'({self.num1 + other.num1}+{self.num2 + other.num2}j)')

    def __mul__(self, other):
        # return self.c_number * other.c_number
        print(f'({self.num1 * other.num1 - self.num2 * other.num2}+{self.num1 * other.num2 + other.num1 * self.num2}j)')


if __name__ == '__main__':
    x = Complex_number(1, 2)
    y = Complex_number(3, 4)
print(1)
