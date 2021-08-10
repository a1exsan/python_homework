
class DevByZero(Exception):
    def __init__(self):
        self.text = '!!! Division by zero !!!'

try:
    l = input('Enter tow number (a, b) splitted by comma: ').split(',')

    a, b = float(l[0]), float(l[1])

    if b == 0:
        raise DevByZero()

except DevByZero as error:

    print(error.text)

else:
    print(f'relation a to b is: {a / b}')

