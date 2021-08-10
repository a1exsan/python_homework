
class ItIsNum(Exception):
    text = 'Error: you entered text but not number !!!'

list_number = []

while True:
    inp = input('Enter number in 0..99999999 (for exit enter Q or q) ')

    if inp in ['Q', 'q']:
        print(list_number)
        break

    try:
        if not inp.isdigit():
            raise ItIsNum()

    except ItIsNum as err:
        print(err.text)

    else:
        list_number.append(int(inp))