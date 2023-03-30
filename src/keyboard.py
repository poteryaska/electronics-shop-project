from src.item import Item


class KeyBoardMixin:
    '''Класс Миксин для хранения и изменения раскладки клавиатуры'''

    def __init__(self, language="EN"):
        self.__language = language

    @property
    def language(self):
        """Возвращает раскладку клавиатуры"""
        return self.__language

    def change_lang(self):
        """Изменяет раскладку клавиатуры """
        if self.__language == "EN":
            self.__language = "RU"
        elif self.__language == "RU":
            self.__language = "EN"
        else:
            raise AttributeError
        return self


class KeyBoard(Item, KeyBoardMixin):
    """
    Класс для представления клавиатур в магазине.
    """
    pass
