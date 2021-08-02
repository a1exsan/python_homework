
from itertools import count

import time

class TrafficLight():
    def __init__(self, init_color='red'):
        self.__color__ = init_color

    def running(self):

        print(f'{self.__color__} --> ', end='')

        if self.__color__ == 'red':
            time.sleep(7)
            self.__color__ = 'yellow'

        elif self.__color__ == 'yellow':
            time.sleep(2)
            self.__color__ = 'green'

        elif self.__color__ == 'green':
            time.sleep(8)
            self.__color__ = 'red'


tl1 = TrafficLight(init_color='green')

for el in count(1):
    tl1.running()

    if el > 5:
        break
