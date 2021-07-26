# written by: Alex fominsan@gmail.com

init_list = [2, 22, 3, 4, 1, 11, 45, 45, 23, 22, 2, 11, 6]

out_list = [i for i in init_list if init_list.count(i) == 1]

print(out_list)