# written by: Alex fominsan@gmail.com

n_month = input('Enter number of month 1 - 12: ')

a, b, c, d = 'winter', 'spring', 'summer', 'autumn'

season_dict = {'12': a, '1': a, '2': a, '3': b, '4': b, '5': b, '6': c, '7': c, '8': c, '9': d, '10': d, '11':d}

print(f' Your month is the {season_dict[n_month]} month. (realised using dictionary type)')

season_list = [a, a, b, b, b, c, c, c, d, d, d, a]

print(f' Your month is the {season_list[int(n_month) - 1]} month. (realised using list type)')
