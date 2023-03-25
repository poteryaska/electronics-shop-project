from src.phone import Phone
from src.item import Item
import pytest


@pytest.fixture
def phone_test():
    return Phone("Nokia 3310", 1000, 2, 3)


@pytest.fixture
def item_test():
    return Item("Oppo reno 5", 18000, 2)


def test__repr__(phone_test):
    assert phone_test.__repr__() == "Phone('Nokia 3310', 1000, 2, 3)"


def test_number_of_sim(phone_test):
    assert phone_test.number_of_sim == 3


def test__add__():
    phone_1 = Phone("Nokia 3310", 1000, 2, 3)
    item_1 = Item("Oppo reno 5", 18000, 2)
    assert phone_1 + item_1 == 4
    assert item_1 + phone_1 == 4


def test_add():
    phone_1 = Phone("Nokia 3310", 1000, 2, 1)
    test_phone = TestPhone("Nokia 3310", 1000, 5)
    with pytest.raises(TypeError, match='Класс не найден'):
        assert phone_1 + test_phone == 'Класс не найден'


@pytest.fixture
def item_test_1():
    return Phone("Nokia 3310", 1000, 2, 0)


def test_number_of_sim_1(item_test_1):
    with pytest.raises(ValueError, match='Количество физических SIM-карт должно быть целым числом больше нуля.'):
        item_test_1.number_of_sim = 0


class TestPhone:
    def __init__(self, name: str, price: float, quantity: int) -> None:
        self.__name = name
        self.price = price
        self.quantity = quantity
