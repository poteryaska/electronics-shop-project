from src.item import Item


class Phone(Item):
    """
    Класс для представления телефонов в магазине.
    """

    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int) -> None:
        """
        Создание экземпляра класса Phone.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        :param number_of_sim: Количество сим-карт в телефоне.
        """
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    def __repr__(self):
        '''Вывод информации о телефоне'''
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    @property
    def number_of_sim(self):
        '''Возвращает количество сим-карт в телефоне'''
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, number_of_sim):
        '''Проверяет и устанавливает количество сим карт в телефоне'''
        if number_of_sim > 0 and type(number_of_sim) is int:
            self.__number_of_sim = number_of_sim
        else:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")
