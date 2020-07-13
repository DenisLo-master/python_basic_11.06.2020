"""4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
 уникальные для каждого типа оргтехники.

5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу
в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
можно использовать любую подходящую структуру, например словарь.

6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например,
для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП."""


class Stock_Eq:
    __department_list = {1: 'Бухгалтерия', 2: 'Отдел продаж', 3: 'Маркетинговый отдел', 4: 'Клиентский отдел'}
    __stock_dict = {}

    @classmethod
    def department(cls):
        return cls.__department_list

    @classmethod
    def department_inn(cls, name):
        cls.__department_list[len(cls.__department_list) + 1] = name

    @classmethod
    def stock(cls):
        return cls.__stock_dict

    @classmethod
    def stock_inn(cls):
        stock_count = {}
        _index = None
        # если отдел уже есть
        if cls.department()[dep_choise] in cls.__stock_dict.keys():
            stock_count = cls.__stock_dict[cls.department()[dep_choise]]
            _key_equp = Office_equipment.equip[equip_choise]
            # если оборудование уже есть в отделе
            if _key_equp in stock_count.keys():
                stock_count[_key_equp] = stock_count[_key_equp] + count_choise
            # если оборудование нет в отделе
            else:
                stock_count[_key_equp] = count_choise
        # если отдела еще нет
        else:
            cls.__stock_dict[cls.department()[dep_choise]] = {Office_equipment.equip[equip_choise]: count_choise}


class DepartmentError(Exception):
    def __str__(self):
        return f'ОШИБКА: Выберите только код группы, если нужно создать новый отдел напишите "новый"'


class EquipmentError(Exception):
    def __str__(self):
        return f'ОШИБКА: Укажите только код оборудования из списка'


class CountError(Exception):
    def __str__(self):
        return f'ОШИБКА: Должно быть указано только целое, положительное число'


class MenuError(Exception):
    def __str__(self):
        return f'Выберете код меню 1 или 2'


class Office_equipment:
    equip = {}
    __idq = 0

    def __init__(self, name, color):
        self.name = name
        self.color = color
        Office_equipment.__idq += 1
        Office_equipment.equip[Office_equipment.__idq] = tuple(self.__str__().split(', '))

    @staticmethod
    def info():
        for _k, _i in Office_equipment.equip.items():
            print(_k, ":", _i)
        print('-' * 50)


class Printer(Office_equipment):
    def __init__(self, name, color, type):
        Printer.type = type
        super().__init__(name, color)

    @property
    def type(self):
        return self.type

    @type.setter
    def type(self, val):
        self.type = val

    def __str__(self):
        return f'{self.__class__.__name__}, {self.name}, цвет:{self.color}, тип:{self.type}'


class Scanner(Office_equipment):
    def __init__(self, name, color, format):
        Scanner.format = format
        super().__init__(name, color)

    @property
    def format(self):
        return self.format

    @format.setter
    def format(self, val):
        self.format = val

    def __str__(self):
        return f'{self.__class__.__name__}, {self.name}, цвет:{self.color}, формат:{self.format}'


class Copier(Office_equipment):
    def __init__(self, name, color, speed):
        Copier.speed = speed
        super().__init__(name, color)

    @property
    def speed(self):
        return self.speed

    @speed.setter
    def speed(self, val):
        self.speed = val

    def __str__(self):
        return f'{self.__class__.__name__}, {self.name}, цвет:{self.color}, скорость:{self.speed} л/мин'


# Примеры оборудования
p1 = Printer('Canon', 'black', 'b/w')
p2 = Printer('Samsung', 'white', 'color')
s1 = Scanner('MTR', 'red', 'A4')
s2 = Scanner('Xerox', 'black', 'A3')
c1 = Copier('Sams', 'blue', '15')
c2 = Copier('Can', 'gray', '60')

# Работа в меню
while True:
    try:
        _input = input(
            '\nМеню: 1 - показать склад, 2 - заказть оборудование, 3 - показать доступное оборудование:\n---->')
        if _input != '1' and _input != '2' and _input != '3':
            raise MenuError
        # Отобразить продукцию на складе
        elif _input == '1':
            if Stock_Eq.stock() == {}:
                print('\nНа складе ничего нет')
                continue
            for _k, _i in Stock_Eq.stock().items():
                print('\n', _k)
                for _ki, _ii in _i.items():
                    print(f'{_ki}: {_ii} шт')
            print('_' * 50)
            continue
        # заказ оборудования на склад для отдела...
        elif _input == '2':
            # Выбор отдела из списка или создание нового с выбором
            print('\n', Stock_Eq.department())
            while True:
                try:
                    _input = input('Выберете отдел(код или введите "новый"): ')
                    if not _input.isdigit() and _input != 'новый':
                        raise DepartmentError
                    elif _input == 'новый':
                        _input = input('\nВведите название нового отдела: ')
                        Stock_Eq.department_inn(_input)
                        dep_choise = [key for key, itm in Stock_Eq.department().items() if itm == _input][0]
                        break
                    elif not int(_input) in Stock_Eq.department().keys():
                        raise DepartmentError
                    else:
                        dep_choise = int(_input)
                        break
                except DepartmentError as e:
                    print('\n', e)

            # Выбор оборудования из списка
            print('_' * 50)
            for _k, _i in Office_equipment.equip.items():
                print(f'{_k}: {_i}')
            while True:
                try:
                    _input = input('Выберете тип офисного оборудования(код): ')
                    if not _input.isdigit():
                        raise EquipmentError
                    elif not int(_input) in Office_equipment.equip.keys():
                        raise EquipmentError
                    else:
                        equip_choise = int(_input)
                        break
                except EquipmentError as e:
                    print('\n', e)

            # Количество оборудования к закупке
            while True:
                try:
                    _input = input('\nУкажите количество оборудования к закупке: ')
                    if not _input.isdigit():
                        raise CountError
                    elif int(_input) <= 0:
                        raise CountError
                    else:
                        count_choise = int(_input)
                        break
                except CountError as e:
                    print('\n', e)

            Stock_Eq.stock_inn()
            print('_' * 50)
            continue
        elif _input == '3':
            Office_equipment.info()
    except MenuError as e:
        print('\n', e)
