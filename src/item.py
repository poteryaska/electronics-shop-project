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
    def instantiate_from_csv(cls):
        '''инициализирует экземпляры класса Item из файла src/items.csv'''
        csv_data = []
        with open('../src/items.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                Item.__init__(row['name'], row['price'], row['quantity'])
        #         csv_data.append(row['name'])
        #         csv_data.append(row['price'])
        # print(csv_data)
        #         print(row)
            #     csv_data.append(row['name'], row['price'], row['quantity'])


    @staticmethod
    def string_to_number(number: str):
        return int(number)