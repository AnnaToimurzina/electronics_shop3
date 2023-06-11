import os.path
import src.item
import csv


class InstantiateCSVError(Exception):
    pass


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __str__(self):
        """
        Возвращает строку со значением объекта Item.
        """
        return f'{self.__name}'

    def __repr__(self):
        """
        Возвращает строку с описанием объекта Item.
        """
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)


    # Геттер для name
    @property
    def name(self):
        """Возвращает имя товара. К атрибуту можно обращаться без ()."""
        return self.__name

    # Чтобы иметь возможность присваивать атрибуту name значения,
    # надо определить его сеттер. Это работает только для атрибутов с @property
    '''В этом сеттере `name` проверяем, что длина наименования товара не больше 10 символов'''

    @name.setter
    def name(self, name_2: str):
        if len(name_2) <= 10:
            self.__name = name_2
        else:
            raise Exception('Длина товара более 10 символов')

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.
        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self):
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate



    '''класс-метод, инициализирующий экземпляры класса `Item` данными из файла'''
    @classmethod
    def instantiate_from_csv(cls):
        cls.all.clear()
        data_csv = os.path.join('..\src\items.csv')
        try:
            with open(data_csv, newline='', encoding='windows-1251') as file:
                csvreader = csv.DictReader(file)
                for row in csvreader:
                    if 'name' not in row or 'price' not in row or 'quantity' not in row:
                        raise InstantiateCSVError('Файл item.csv поврежден')
        except FileNotFoundError:
            raise FileNotFoundError('Отсутствует файл item.csv')


    '''статический метод, возвращающий число из числа-строки'''
    @staticmethod
    def string_to_number(string_number):
        return float(string_number.replace(',', '.'))

    def __add__(self, other) -> int:
        """
        Реализация операции сложения для экземпляров класса Phone и Item(сложение по количеству товара в магазине).
        :param other: Другой объект, с которым нужно выполнить операцию."""

        if not isinstance(other, Item):
            raise ValueError('только экземпляры Item класса и Phone')
        else:
            return self.quantity + other.quantity



