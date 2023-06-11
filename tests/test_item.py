import pytest
from src.item import Item
from src.phone import Phone
from src.item import InstantiateCSVError
import os
import csv




@pytest.fixture
def item():
    return Item("Смартфон", 10000, 20)

def test_item_name(item):
    assert item.name == "Смартфон"


def test_instantiate_from_csv(item):
    assert item.name == "Смартфон"
    assert item.price == 10000
    assert item.quantity == 20

def test_instantiate_no_file():
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv()
        with pytest.raises(FileNotFoundError):
            os.rename('temp_missing.csv', '..\src\items.csv')
            Item.instantiate_from_csv()

def test_instantiate_2():
    data_csv = os.path.join('..\src\temp_invalid.csv')
    with open(data_csv, newline='', encoding='windows-1251') as file:
        csvreader = csv.DictReader(file)
        for row in csvreader:
            Item(row['name'], row['price'], row['quantity'])
def test_instantiate_from_csv_missing_fields():
    with pytest.raises(InstantiateCSVError):
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

def test_addition_with_item():
    phone1 = Phone("iPhone 14", 120000, 5, 2)
    item1 = Item("Смартфон", 10000, 20)
    result = phone1.quantity + item1.quantity
    assert result == 25










