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

    @property
    def department(self):
        return Stock_Eq.__department_list

    @department.setter
    def department(self, name):
        Stock_Eq.__department_list[len(Stock_Eq.__department_list) + 1] = name

    @property
    def equip(self):
        return Office_equipment.equip

    @property
    def stock(self):
        return Stock_Eq.__stock_dict

    @stock.setter
    def stock(self, atr):
        stock_count = {}
        _index = None
        # если отдел уже есть
        if st.department[dep_choise] in st.__stock_dict.keys():
            stock_count = st.__stock_dict[st.department[dep_choise]]
            _key_equp = Office_equipment.equip[equip_choise]
            # если оборудование уже есть в отделе
            if _key_equp in stock_count.keys():
                stock_count[_key_equp] = stock_count[_key_equp] + count_choise
            # если оборудование нет в отделе
            else:
                stock_count[_key_equp] = count_choise
        # если отдела еще нет
        else:
            st.__stock_dict[st.department[dep_choise]] = {Office_equipment.equip[equip_choise]: count_choise}

    def __str__(self):
        return st.__stock_dict


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

    @


class Printer(Office_equipment):
    type = ''

    def __init__(self, name, color, type):
        Printer.type = type
        super().__init__(name, color)

    def __str__(self):
        return f'{self.__class__.__name__}, {self.name}, цвет:{self.color}, тип:{self.type}'


class Scanner(Office_equipment):
    format = ''

    def __init__(self, name, color, format):
        Scanner.format = format
        super().__init__(name, color)

    def __str__(self):
        return f'{self.__class__.__name__}, {self.name}, цвет:{self.color}, формат:{self.format}'


class Copier(Office_equipment):
    speed = ''

    def __init__(self, name, color, speed):
        Copier.speed = speed
        super().__init__(name, color)

    def __str__(self):
        return f'{self.__class__.__name__}, {self.name}, цвет:{self.color}, скорость:{self.speed}'


if __name__ == '__main__':
    st = Stock_Eq()

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
        _input = input('Меню: 1 - показать склад, 2 - заказть оборудование: ')
        if _input != '1' and _input != '2':
            raise MenuError
        # Отобразить продукцию на складе
        elif _input == '1':
            if st.stock == {}:
                print('\nНа складе ничего нет')
            for _k, _i in st.stock.items():
                print('\n', _k)
                for _ki, _ii in _i.items():
                    print(f'{_ki}: {_ii}шт')
            print('_' * 50)
            continue
        # заказ оборудования на склад для отдела...
        elif _input == '2':
            # Выбор отдела из списка или создание нового с выбором
            print('\n', st.department)
            while True:
                try:
                    _input = input('Выберете отдел(код или введите "новый"): ')
                    if not _input.isdigit() and _input != 'новый':
                        raise DepartmentError
                    elif _input == 'новый':
                        _input = input('\nВведите название нового отдела: ')
                        st.department = _input
                        dep_choise = [key for key, itm in st.department.items() if itm == _input][0]
                        break
                    elif not int(_input) in st.department.keys():
                        raise DepartmentError
                    else:
                        dep_choise = int(_input)
                        break
                except DepartmentError as e:
                    print('\n', e)

            # Выбор оборудования из списка
            print('\n')
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

            st.stock = 'new'
            print('_' * 50)
            continue
    except MenuError as e:
        print('\n', e)
