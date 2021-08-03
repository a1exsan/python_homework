
class Car():
    def __init__(self):
        self.speed = 0
        self.color = 'white'
        self.name = 'Car'
        self.is_police = False

    def go(self):
        print(f'{self.name} is driving!')

    def stop(self):
        print(f'{self.name} is stand!')
        self.speed = 0

    def turn(self, direction):
        print(f'{self.name} is turn on the {direction}!')

    def show_speed(self):
        print(f'{self.name} speed is {self.speed} km/h')
        return self.speed

class TownCar(Car):
    def __init__(self):
        super().__init__()
        self.name = 'TownCar'

    def show_speed(self):
        print(f'{self.name} speed is {self.speed} km/h')
        if self.speed > 60:
            print(f'{self.name} speed limit exceeded!!!')
        return self.speed

class SportCar(Car):
    def __init__(self):
        super().__init__()
        self.name = 'SportCar'

class WorkCar(Car):
    def __init__(self):
        super().__init__()
        self.name = 'WorkCar'

    def show_speed(self):
        print(f'{self.name} speed is {self.speed} km/h')
        if self.speed > 40:
            print(f'{self.name} speed limit exceeded!!!')
        return self.speed

class PoliceCar(Car):
    def __init__(self):
        super().__init__()
        self.is_police = True

        self.name = 'PoliceCar'


car = Car()
car.speed = 100
car.go()
car.show_speed()
car.turn('left')
car.stop()
car.show_speed()

townCar = TownCar()
townCar.speed = 100
townCar.go()
townCar.show_speed()
townCar.turn('right')

policeCar = PoliceCar()
policeCar.speed = 150
policeCar.go()
policeCar.show_speed()
print(policeCar.is_police)

workCar = WorkCar()
workCar.speed = 50
workCar.go()
print(workCar.color)
workCar.show_speed()
workCar.turn('right')
workCar.stop()

sportCar = SportCar()
sportCar.speed = 200
sportCar.show_speed()
sportCar.go()
print(sportCar.is_police)
sportCar.speed = 100
sportCar.show_speed()
sportCar.turn('left')
sportCar.stop()
sportCar.show_speed()