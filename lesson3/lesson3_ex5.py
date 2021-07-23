# written by: Alex fominsan@gmail.com

def main():
    run = True
    numbers = []
    while run:
        user_input = input('Enter sequence of number or (q, Q, exit) for quit: ').split(' ')

        for ui in user_input:
            if ui in ['q', 'Q', 'exit']:                # quit conditions
                run = False
            elif ui.isdigit():
                numbers.append(int(ui))                    # adding integer numbers
            elif ui.find('.') > -1 or ui.find(',') > -1:
                numbers.append(float(ui.replace(',', '.'))) # adding floating point numbers

        print(sum(numbers))


main()
