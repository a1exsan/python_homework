

class Worker():
    def __init__(self):

        self.name = ''
        self.surname = ''
        self.position = ''
        self._income = {}

class Position(Worker):
    def __init__(self, name, surname, position, income={'wage':100000., 'bonus':50000.}):

        self.name = name
        self.surname = surname
        self.position = position
        self._income = income

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


p1 = Position('Ivan', 'Ivanov', 'manager')

print(p1.get_full_name(), ' ', p1.get_total_income())

p2 = Position('Dmitry', 'Petrov', 'researcher', {'wage':90000., 'bonus':70000.})

print(p2.get_full_name(), ' ', p2.get_total_income())

