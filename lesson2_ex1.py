# written by: Alex fominsan@gmail.com

any_types = [1, 3.14, 'string', [1, 2, 3, 4], (True, False), {'a': 10, 'b': 20}, b'text']

print(any_types)

print([type(i) for i in any_types]) # выводим типы списком

for t in any_types:                 # выводим типы циклом
    print(t, ' type is: ', type(t))



