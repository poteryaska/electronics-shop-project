import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.00
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)
        super().__init__()

    def __str__(self):
        return f'{self.__name}'

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __add__(self, other):
        '''Складывает количество товаров двух экземпляров'''
        if isinstance(other, Item):
            return self.quantity + other.quantity
        else:
            raise TypeError('Класс не найден')

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if len(value) > 10:
            raise Exception('Длина наименования товара превышает 10 символов')
        self.__name = value

    @classmethod
    def instantiate_from_csv(cls, data='../src/items.csv'):
        '''инициализирует экземпляры класса Item из файла src/items.csv'''
        try:
            with open(data) as csvfile:
                reader = csv.DictReader(csvfile)
                cls.all = []
                for row in reader:
                    if row['name'] and row['price'] and row['quantity'] is not None:
                        cls(row['name'], row['price'], row['quantity'])
                    else:
                        raise InstantiateCSVError
        except InstantiateCSVError:
            a = InstantiateCSVError()
            print(a)
        except FileNotFoundError:
            print('Отсутствует файл items.csv')
        else:
            return cls.all

    @staticmethod
    def string_to_number(number: str):
        '''возвращает число из числа-строки'''
        try:
            new_number = int(number)
        except ValueError:
            # Try float.
            new_number = int(float(number))
        return new_number


class InstantiateCSVError(Exception):
    '''Класс-исключение, который проверяет не поврежден ли файл'''

    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else "Файл item.csv поврежден"

    def __str__(self):
        return self.message
