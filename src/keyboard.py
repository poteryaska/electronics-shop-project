from src.item import Item

class KeyBoardMixin:
    '''Класс Миксин для хранения и изменения раскладки клавиатуры'''
    def __init__(self, language="EN"):
        self.__language = language
    @property
    def language(self):
        """Возвращает раскладку клавиатуры"""
        return self.__language

    # @language.setter
    # def language(self, new_language):
    #     """Устанавливает раскладку клавиатуры"""
    #     if new_language == 'RU' or new_language == 'EN':
    #         self.__language = new_language
    #     else:
    #         raise AttributeError("Unknown language")

    def change_lang(self):
        """Изменяет раскладку клавиатуры """
        if self.__language == "EN":
            self.__language = "RU"
        elif self.__language == "RU":
            self.__language = "EN"
        else:
            raise AttributeError('Доступны только EN/RU')
        return self

class KeyBoard(Item, KeyBoardMixin):
    """
    Класс для представления клавиатур в магазине.
    """
    pass




