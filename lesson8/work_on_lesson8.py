class Calc:
    """ Some description """

    last_result = 0

    @staticmethod
    def num_sum(a, b):
        Calc.last_result = a + b
        return  Calc.last_result

    @classmethod
    def last_result_m(cls):
        return cls.last_result


print(Calc.num_sum(2, 4))

print(Calc.num_sum(4, 4))

print(Calc.last_result_m())

calc = Calc()

def test_def():

    """ Description """

    a = 10
    b = a * 2
    pass

print(Calc.__name__)
print(Calc.__dict__)
print(Calc.__doc__)

print(test_def.__doc__)

"""
class myException(Exception):
    def __init__(self, msg):
        self.msg = msg

try:
    a = input('Enter')
    if len(a) >= 10:
        raise myException('Error!!!!!')
except myException as message:
    print(message)
"""

import psutil as p

print(p.cpu_percent())
print(p.cpu_count())
print(p.disk_usage('/home'))

import requests as r

resp = r.get(url='https://google.com')
print(resp.status_code)



