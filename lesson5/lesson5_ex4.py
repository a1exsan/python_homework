# written by: Alex fominsan@gmail.com

translator = {1:'Один', 2:'Два', 3:'Три', 4:'Четыре', 5:'Пять'}

result = []

f1 = open('ex4.txt')

for line in f1:

    s = line[:-1].split('-')

    result.append(f"{translator[int(s[1])]} - {int(s[1])} \n")

f1.close()

f1 = open('ex4_result.txt', 'w')

f1.writelines(result)

f1.close()

