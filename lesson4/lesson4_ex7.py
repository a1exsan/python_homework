v

from math import factorial as f

def fact(n):
    for i in range(1, n + 1):
        yield f(i)

for el in fact(10):
    print(el)