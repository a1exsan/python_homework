# written by: Alex fominsan@gmail.com
import json

f_list = []

result = []

with open('ex7.txt') as f:

    s = 0.

    D = {}

    for line in f:

        L = line[:-1].split(' ')

        L.append(float(L[2]) - float(L[3]))

        if line != '':

            f_list.append(L)

            D[L[0]] = L[-1]

            if L[-1] > 0:

                s += L[-1]

                print(f" Прибыль {L[1]} {L[0]} составила {L[-1]}")

            else:

                print(f" Убытки {L[1]} {L[0]} составили {L[-1]}")

s /= len(f_list)

print(f" average_profit: {s}")

result.append(D)

result.append({'average_profit': s})

print(result)

with open('result_ex7.json', 'w') as f_json:

    json.dump(result, f_json)

with open('result_ex7.json') as f_json:

    obj = json.load(f_json)

    print(obj)