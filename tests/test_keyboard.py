import pytest
from src.keyboard import LanguageMixin, Keyboard

def test_init():
    obj = LanguageMixin('RU')
    assert obj.language == 'RU'

def test_change_lang():
    obj = LanguageMixin('EN')
    obj.change_lang()
    assert obj.language == 'RU'
    obj.change_lang()

def test_keyboard_creation():
    keyboard = Keyboard("Logitech K380", 2999.0, 10)
    assert keyboard.name == "Logitech K380"
    assert keyboard.price == 2999.0
    assert keyboard.quantity == 10

def test_keyboard_str():
    keyboard = Keyboard("Logitech K380", 2999.0, 10)
    assert str(keyboard) == "Logitech K380"

def test_keyboard_repr():
    keyboard = Keyboard("Logitech K380", 2999.0, 10)
    assert repr(keyboard) == "Keyboard('Logitech K380', 2999.0, 10)"

