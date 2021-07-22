# written by: Alex fominsan@gmail.com

def a_dev_b(a, b):
    # division a by b
    if b != 0:
        return print(f'a / b = {a / b}')
    else:
        return print("error: division by zero")

a_dev_b(
        float(input('Enter float number a: ')),
        float(input('Enter float number b: '))
        )