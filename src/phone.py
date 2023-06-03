from src.item import Item

class Phone(Item):
    '''Cоздание экземпляра класса Phone
    # Переопределяем метод базового класса'''
    def __init__(self, name: str, price: float, quantity: int, _number_of_sim: int) -> None:
        '''# Вызываем метод базового класса'''
        super().__init__(name, price, quantity)
        '''# Дополнительный код'''
        self.number_of_sim = _number_of_sim

    @property
    def number_of_sim(self):
        """Возвращает атрибут, содержащий количество поддерживаемых сим-карт. К атрибуту можно обращаться без ()."""
        return self._number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, sim_number: int):
        if sim_number > 0 and isinstance(sim_number, int):
            self._number_of_sim = sim_number
        else:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")

    def __repr__(self):
        """
        Возвращает строку с описанием объекта Phone.
        """
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self._number_of_sim})"





