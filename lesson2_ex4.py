# written by: Alex fominsan@gmail.com

input_str = input('Enter any sentence devided by space: ')

input_list = input_str.split(' ')

for i in range(len(input_list)):
    print(i + 1, f' {input_list[i][:10]}')
    #print(i + 1, f' {input_list[i][: (10, len(input_list[i]))[len(input_list[i]) <= 10]]}')
    #if len(input_list[i]) > 10:
    #    print(i + 1, f' {input_list[i][:10]}')
    #else:
    #    print(i + 1, f' {input_list[i]}')

