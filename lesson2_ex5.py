# written by: Alex fominsan@gmail.com

rating = [8,7,7,5]

num = int(input('Enter number 0 - 9: '))

#rating.append(num)
#rating.sort(reverse=True)

for i in range(len(rating)):
    if num > rating[i]:
        rating.insert(i, num)
        break
    elif i == len(rating) - 1:
        rating.append(num)

print(f'rating is: ', end = '')

for i in range(len(rating) - 1):
    print(f'{rating[i]}, ', end = '')

print(f'{rating[-1]}', end = '')

