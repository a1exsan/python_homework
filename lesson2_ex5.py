# written by: Alex fominsan@gmail.com

rating = [8,7,7,5]

num = int(input('Enter number 0 - 9: '))

rating.append(num)
rating.sort(reverse=True)

print(f'rating is: ', end = '')

for i in range(len(rating) - 1):
    print(f'{rating[i]}, ', end = '')

print(f'{rating[-1]}', end = '')

