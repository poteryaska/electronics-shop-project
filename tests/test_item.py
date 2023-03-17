"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


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