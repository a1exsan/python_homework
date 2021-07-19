# written by: Alex fominsan@gmail.com

a = [

(1, {'name': 'computer', 'price': '20000', 'amount': '5', 'units': 'pc.'}),
(2, {'name': 'printer', 'price': '6000', 'amount': '2', 'units': 'pc.'}),
(3, {'name': 'scaner', 'price': '10000', 'amount': '3', 'units': 'pc.'})

]

keys = list(a[0][1].keys())

ctrl = True
while ctrl:
    product = input('Enter product param as {name price amount units} or Q for quit: ')
    if product in ['q', 'Q']:
        ctrl = False
        break
    else:
        p_list = product.split(' ')
        if len(p_list) == 4:
            a.append((a[-1][0] + 1, {keys[i]: p_list[i] for i in range(len(p_list))}))
        else:
            print('Error entering format. Try again')

c = []
for i in range(len(a)):
    c.append(list(zip(*a[i][1].items()))[1])
    #print(c[-1])

c = list(zip(*c))

analitics = {keys[i]: list(c[i]) for i in range(len(c))}

for k in keys:
    print(f'{k}: {analitics[k]}')


#print(analitics)
