# written by: Alex fominsan@gmail.com

from itertools import count

from itertools import cycle

for num in count(4):
    if num > 100:
        break
    else:
        print(num)

c = 0
for i in cycle(['list', 'dict', 'set']):
    if c > 20:
        break
    else:
        print(i)
    c += 1
