# written by: Alex fominsan@gmail.com

names, salary = [], []

with open('ex3.txt') as f:

    for line in f:

        l = line[:-1].split(' ')

        names.append(l[0])

        salary.append(float(l[1]))

    print(names, salary)

print(f"mean salary is {sum(salary) / len(salary)}")

for i, n in enumerate(names):

    if salary[i] < 20000:

        print(f"salary of {n} less then 20000")