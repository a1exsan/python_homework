# written by: Alex fominsan@gmail.com

from random import randint as ri

with open('ex5.txt', 'w') as f:

    f.writelines([f"{ri(1, 20)} " for i in range(20)])

with open('ex5.txt') as f:

    print(sum([int(i) for i in f.read().split(' ') if i != '']))
