import pytest
from src.item import Item

@pytest.fixture
def item():
    return Item("Смартфон", 10000, 20)

def test_item_str(item):
    assert str(item) == "Item ({'_Item__name': 'Смартфон', 'price': 10000, 'quantity': 20})"

def test_item_name(item):
    assert item.name == "Смартфон"

def test_item_price(item):
    assert item.price == 10000

def test_item_quantity(item):
    assert item.quantity == 20

def test_instantiate_from_csv(item):
    assert item.name == "Смартфон"
    assert item.price == 10000
    assert item.quantity == 20

def test_instantiate_no_file():
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv()


def test_item_list():
    assert len(Item.all) == 0
    item1 = Item("Смартфон", 10000, 20)
    assert len(Item.all) == 1
    item2 = Item("Ноутбук", 20000, 5)
    assert len(Item.all) == 2
def test_item_list2():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)
    item.all = []
    assert isinstance(item.all, list)

def test_item_creation(item):
    assert item.name == "Смартфон"
    assert item.price == 10000
    assert item.quantity == 20


def test_calculate_total_price(item):
    assert item.calculate_total_price() == 200000

def test_apply_discount(item):
    item.pay_rate = 0.8
    item.apply_discount()
    assert item.price == 8000

def test_name_too_long_len(item):
    """Название товара слишком длинное"""
    with pytest.raises(Exception):
        item.name = 'ТелефонТелефонТелефон'








