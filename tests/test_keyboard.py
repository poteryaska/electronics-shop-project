from src.keyboard import KeyBoard
import pytest

@pytest.fixture()
def test_keyboard():
    return KeyBoard('Aser', 5000, 4)

def test_keyboard_name(test_keyboard):
    assert test_keyboard.name == 'Aser'

def test_change_lang(test_keyboard):
    assert test_keyboard.language == 'EN'
    test_keyboard.change_lang()
    assert test_keyboard.language == 'RU'

def test_language(test_keyboard):
    with pytest.raises(AttributeError, match='Unknown language'):
        test_keyboard.language = 'KR'
