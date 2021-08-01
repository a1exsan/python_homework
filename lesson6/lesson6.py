

class Animal:
    count_of_animal = 0

    def __init__(self, sound, color, count_of_legs):
        Animal.count_of_animal += 1
        self.sound = sound
        self._color = color
        self.__count_of_legs = count_of_legs

    def make_noise(self):
        print(self.sound)

    def _protected_func(self):
        print('It is protected')
        self.__privat_func()

    def __privat_func(self):
        print('In is privat')

class Bear(Animal):

    def hide(self):
        print('well done')

class Wolf(Animal):

    def sound_to_the_moon(self):
        print('Wooooow')


""""
bear = Bear('AAAA', 'white', 4)

bear.hide()

wolf = Wolf('BBB', 'gray', 4)
wolf.sound_to_the_moon()

animal = Animal('grrrr', 'black', 4)
print(animal.sound)
print(animal._color)
print(animal._Animal__count_of_legs)
print(animal._protected_func())
print(animal._protected_func())

animal = Animal('Blabla')
animal.make_noise()
print(animal.count_of_animal)

animal2 = Animal('Blabla')
print(animal.count_of_animal)

animal.color = 'green'

print(animal.color)
"""


class DrivingTransport:
    def drive(self):
        print('Drive')
    def test(self):
        print('D T')


class FlyingTransport:
    def fly(self):
        print('Fly')

    def test(self):
        print(' F T')


class CustomTransport(DrivingTransport, FlyingTransport):
    def test(self):
        print('C T')

    def on_param(self, frase, repeat=1):
        if repeat != 1:
            for i in range(repeat):
                print(frase)

        else:
            print(f'repeat 1     {frase}')

customT = CustomTransport()

customT.on_param('Hello', 4)




