"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item
from src.phone import Phone


@pytest.fixture
def item_ifone():
    return Item("Айфон", 80000, 10)


def test_calculate_total_price(item_ifone):
    assert item_ifone.calculate_total_price() == 800000.00


def test_apply_discount(item_ifone):
    item_ifone.pay_rate = 0.5
    item_ifone.apply_discount()
    assert item_ifone.price == 40000.00


def test_name_1(item_ifone):
    item_ifone.name = "Айфон"


def test_string_to_number():
    assert Item.string_to_number('88.9') == 88
    assert Item.string_to_number('99') == 99


def test__repr__(item_ifone):
    assert item_ifone.__repr__() == "Item('Айфон', 80000, 10)"


def test__str__(item_ifone):
    assert item_ifone.__str__() == "Айфон"


def test__add__():
    phone_1 = Item("Nokia 3310", 1000, 2)
    item_1 = Phone("Oppo reno 5", 18000, 2, 1)
    assert phone_1 + item_1 == 4


def test_add():
    item_1 = Item("Nokia 3310", 1000, 2)
    test_phone = TestPhone("Nokia 3310", 1000, 5)
    with pytest.raises(TypeError, match='Класс не найден'):
        assert (item_1 + test_phone) == 'Класс не найден'

def test_instantiate_from_csv():
    assert Item.instantiate_from_csv(data='../tests/test_items.csv') == None

# def test_instantiate_from_csv_1():
#     with pytest.raises(FileNotFoundError) as error:
#         a = Item.instantiate_from_csv('../tests/test_item.csv')
#         assert a.error == "Отсутствует файл item.csv"

    # with pytest.raises(FileNotFoundError) as error:
    #     Item.instantiate_from_csv(data='../tests/test_item.csv')
    #     assert str(error) == "Отсутствует файл item.csv"


class TestPhone:
    def __init__(self, name: str, price: float, quantity: int) -> None:
        self.__name = name
        self.price = price
        self.quantity = quantity
