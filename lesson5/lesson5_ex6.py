# written by: Alex fominsan@gmail.com

result_dict = {}

with open('ex6.txt') as f:

    for line in f:

        K = line[:-1].split(':')

        if K[0] != '':

            count = 0

            L = K[1].split('-')

            for i in L:

                count += int(i[:i.find('(')])

            result_dict[K[0]] = count

for k in result_dict.keys():

    print(f"{k}:  {result_dict[k]}")
