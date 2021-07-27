# written by: Alex fominsan@gmail.com

def int_func(input_str):
    sl = list(input_str)
    sl[0] = sl[0].upper()
    return ''.join(sl)

def main():
    user_input = input('Enter sentence splitted by space: ').split(' ')

    print(user_input)

    for ui in user_input:
        print(f'{int_func(ui)} ', end = '')

main()
