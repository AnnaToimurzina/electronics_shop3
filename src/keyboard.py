from src.item import Item

class LanguageMixin:
    __language = 'EN'

    def __init__(self, __language):
        self.__language = __language

    @property
    def language(self):
        return self.__language

    '''метод для изменения языка (раскладки клавиатуры)'''
    def change_lang(self):
        if self.__language == 'EN':
            self.__language = 'RU'
            return self
        else:
            self.__language = 'EN'
            return self


class Keyboard(Item, LanguageMixin):
    '''класс `Keyboard` для товара “клавиатура.
    Товар отличается от `Item` тем, что у него есть атрибут `language` и метод для изменения языка
    реализованный в классе LanguageMixin'''
    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)


    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Keyboard('{self.name}', {self.price}, {self.quantity})"