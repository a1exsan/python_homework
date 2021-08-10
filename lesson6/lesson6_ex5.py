
class Stationary():
    def __init__(self):
        self.title = 'stationary'

    def draw(self):
        print('start drawing!')

class Pen(Stationary):
    def __init__(self):
        super().__init__()
        self.title = 'Pen'

    def draw(self):
        print(f'start drawing {self.title}!')

class Pencil(Stationary):
    def __init__(self):
        super().__init__()
        self.title = 'Pencil'

    def draw(self):
        print(f'start drawing {self.title}!')

class Handle(Stationary):
    def __init__(self):
        super().__init__()
        self.title = 'Handle'

    def draw(self):
        print(f'start drawing {self.title}!')


stationary = Stationary()
stationary.draw()

pen = Pen()
pen.draw()

pencil = Pencil()
pencil.draw()

handle = Handle()
handle.draw()
