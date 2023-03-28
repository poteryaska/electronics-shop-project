from src.item import Item

class KeyBoardMixin:

    pass
class KeyBoard(Item, KeyBoardMixin):
    def __init__(self, name: str, price: float, quantity: int, language: str) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        :param language: Язык
        """
        self.language = language

    def change_language(self):


