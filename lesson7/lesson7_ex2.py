
from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def get_value(self):
        pass

    @property
    def tissue_consumption(self):
        return self.get_value()


class Сoat(Clothes):
    def __init__(self):
        super().__init__()

        self.volume = 30

    def get_value(self):
        return self.volume / 6.5 + 0.5



class Suit(Clothes):
    def __init__(self):
        super().__init__()

        self.height = 1.8

    def get_value(self):
        return self.height * 2 + 0.3


coat = Сoat()
coat.volume = 27
print(coat.tissue_consumption)

suit = Suit()
suit.height = 2
print(suit.tissue_consumption)
