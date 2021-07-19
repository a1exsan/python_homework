# written by: Alex fominsan@gmail.com

rating = [8,7,7,5]

num = int(input('Enter number 0 - 9: '))

rating.reverse()

if len(rating) == 0:
    rating.append(num)
else:
    if num in rating:
        index = rating.index(num)
        rating.insert(index, num)
    else:
        if num >= max(rating):
            rating.append(num)
        else:
            rating.insert(0, num)

rating.reverse()

print(f'rating is: ', end = '')

for i in range(len(rating) - 1):
    print(f'{rating[i]}, ', end = '')

print(f'{rating[-1]}', end = '')

