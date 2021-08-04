# written by: Alex fominsan@gmail.com

from random import random as rd

init_list = [int(10 * rd()) for i in range(15)]

print(init_list)

extracted_list = [a for i, a in enumerate(init_list[1:]) if a > init_list[i]]

print(extracted_list)
