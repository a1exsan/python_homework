# written by: Alex fominsan@gmail.com

def str_to_number(input_str):
    sign = 1
    if input_str.find('-') > -1:
        sign = -1
        input_str = input_str.replace('-', '')

    if input_str.isdigit():
        return sign * int(input_str)
    elif input_str.find('.') > -1 or input_str.find(',') > -1:
        return sign * float(input_str.replace(',', '.'))
    else:
        return 0

def main():
    run = True
    numbers = []
    while run:
        user_input = input('Enter sequence of number or (q, Q, exit) for quit: ').split(' ')

        for ui in user_input:
            if ui in ['q', 'Q', 'exit']:                # quit conditions
                run = False
            else:
                numbers.append(str_to_number(ui))

        print(sum(numbers))


main()
