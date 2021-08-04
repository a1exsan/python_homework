
class MyClass:

    def __init__(self, value, value2):
        self.value = value
        self.value2 = value2

    def __add__(self, other):
        return MyClass(self.value + other.value)

    def __str__(self):
        return f'value = {self.value}'

    def __setattr__(self, key, value):
        if key == 'modif':
            self.__dict__[key] = value * 2
        else:
            self.__dict__[key] = value

    def __getitem__(self, item):
        if item == 0:
            return self.value
        if item == 1:
            return self.value2

    def __gt__(self, other):
        return self.value > other.value


m1 = MyClass(10, 1)
m2 = MyClass(20,2)
m3 = MyClass(20,3)

m1.a = 1
m1.modif = 4

print(m1.modif)

#print(m1 + m2 + m3)

print(m2[1])

print(m2 > m1)

from abc import ABC, abstractmethod

class myInterAbs(ABC):

    @abstractmethod
    def show_info(self):
        pass

    def show_info2(self):
        pass

class myClass1(myInterAbs):
    def show_info(self):
        pass

obj1 = myClass1()

class myIter:
    def __init__(self, start=1):
        if start % 2 == 1:
            self.value = start
        else:
            self.value + 1

    def __next__(self):
        self.value += 2
        if self.value <= 20:
            return self.value
        else:
            raise StopIteration

    def __iter__(self):
        #self.value = 0
        return self

class myNum:
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        return myIter(self.value)

obj2 = myIter(15)

for i in obj2:
    print(i)

for i in obj2:
    print(i)

class Pen:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) > 2:
            self.__name =  name[0:1]
        else:
            self.__name =  name




p = Pen('n111')
print(p.name)

class Auto:
    def __init__(self, year):
        self.year = year
    @property
    def year(self):
        return self.__year
    @year.setter
    def year(self, year):
        if year < 2000:
            self.__year = 2000
        elif year > 2019:
            self.__year = 2019
        else:
            self.__year = year
    def get_auto_year(self):
        return f"Автомобиль выпущен в {str(self.year)} году"

a = Auto(2090)
print(a.get_auto_year())





