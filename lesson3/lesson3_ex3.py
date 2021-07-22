# written by: Alex fominsan@gmail.com

def my_func(*args):
    a = list(args)
    a.sort(reverse=True)
    return sum(a[:2])

print(my_func(6, 3, 4))