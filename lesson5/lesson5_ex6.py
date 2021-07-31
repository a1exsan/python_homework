# written by: Alex fominsan@gmail.com

result_dict = {}

with open('ex6.txt') as f:

    for line in f:

        K = line[:-1].split(':')

        if K[0] != '':

            result_dict[K[0]] = K[1].split('-')

for k in result_dict.keys():

    print(f"{k}:  {''.join(result_dict[k])}")
