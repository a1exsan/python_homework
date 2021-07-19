# written by: Alex fominsan@gmail.com

input_str = input('Enter any sentence larger then two words: ')

input_list = input_str.split(' ')

print(f'Splitted init sentence: {input_list}')

for i in range(len(input_list) // 2):
    k1, k2 = 2 * i, 2 * i + 1
    tmp = input_list[k1]
    input_list[k1] = input_list[k2]
    input_list[k2] = tmp

print(f'Modified sentence: {input_list}')