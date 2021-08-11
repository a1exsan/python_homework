
class ComplexNumber:
    def __init__(self, real, im):
        self.real = real
        self.im = im

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.im + other.im)

    def __mul__(self, other):
        return ComplexNumber(self.real * other.real - self.im * other.im,
                             self.real * other.im + self.im * other.real)

    def __str__(self):
        if self.im >= 0:
            return f'({self.real} + {self.im} i)'
        if self.im < 0:
            return f'({self.real} - {abs(self.im)} i)'

print((ComplexNumber(10, -1) + ComplexNumber(2, 2)) * ComplexNumber(0.1, 1))

print(ComplexNumber(10, -1) + ComplexNumber(2, 2))

print(ComplexNumber(5, 5) * ComplexNumber(2, 2))

print(ComplexNumber(5, 5) * ComplexNumber(2, -2))