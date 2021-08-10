
class Cell:
    def __init__(self, number):
        super().__init__()
        self.cell_number = number

    def __add__(self, other):
        return Cell(self.cell_number + other.cell_number)

    def __sub__(self, other):
        if self.cell_number >= other.cell_number:
            return Cell(self.cell_number - other.cell_number)
        else:
            Cell(0)

    def __mul__(self, other):
        return Cell(self.cell_number * other.cell_number)

    def __truediv__(self, other):
        if other.cell_number > 0:
            return Cell(self.cell_number // other.cell_number)
        else:
            print('Error: division by zero!')

    def make_order(self, num):
        if num > 0:
            s = ''
            index = 0
            for i in range(self.cell_number):
                s += '*'
                index += 1
                if index == num:
                    s += '\n'
                    index = 0
            return s
        else:
            print('Error: num must be larger then zero')

    def __str__(self):
        return self.make_order(5)


c1 = Cell(20)
c2 = Cell(25)
c3 = Cell(2)

print(c1.make_order(3))

c4 = c1 + c2

print(c4.make_order(6))

c5 = c2 / c3

print(c5.make_order(4))

c6 = c5 * c3

print(c6)

print(c1 + c2 * c3 / c4 - c1)

