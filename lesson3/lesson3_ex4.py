# written by: Alex fominsan@gmail.com

def my_func1(x, y):
    return x ** y

def my_func2(x, y):
    ret = 1.
    for i in range(abs(y)):
        ret *= 1 / x
    return ret

x = float(input('Enter float number: '))

y = int(input('Enter integer negative number: '))

print(my_func1(x, y))

print(my_func2(x, y))