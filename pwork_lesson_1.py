
# written by: Alex fominsan@gmail.com

import time


def exercise_1():

    ii = 10
    print(ii)

    pi = 3.14
    print(f'pi number is: {pi}')

    ss = 'python is good language'
    print(ss)

    count_days = input('Please enter, How many days in a year? ')
    print('you entered: ', count_days)

    name = input('Please enter, What is your name? ')
    print('you entered: %s' % name)

    age = input('Please enter, How old are you? ')
    print('you entered: {}, {}, {}'.format(age, age, age))


def exercise_2():

    seconds = int(input('Please enter time in seconds? '))
    if seconds > 100:
        print('you entered: ', time.strftime('%H:%M:%S', time.gmtime(seconds)))
    else:
        hours = seconds // (60*60)
        seconds %= (60*60)
        minutes = seconds // 60
        seconds %= 60
        print("%01i:%02i:%02i" % (hours, minutes, seconds))


def exercise_3():
    num = int(input('Please enter natural number 0 - 999999999? '))
    print(num * (1 + 11 + 111))


def exercise_4():
    num = list(input('Please enter natural number 0 - 999999999? '))
    pos, max_n = 0, 0
    while pos < len(num):
        if max_n < int(num[pos]):
            max_n = int(num[pos])
        pos += 1
    print(f'maximum number is: {max_n}')


def exercise_5():
    pp = float(input('enter proceeds of company: '))
    zz = float(input('enter cost of company: '))
    sign = pp - zz
    status = ''
    if sign > 0:
        status = 'profit'
        rent = sign * 100 // pp
        num_of_members = int(input('enter number of members of company: '))
        pp_m = pp / num_of_members
        print(f'profit per members: {pp_m}, profitability of proceeds is {rent}')
    else:
        status = 'loss'
    print(f'company is {status}')


def exercise_6():

    a = float(input('number km on the first day: '))
    b = float(input('number km on thr last day: '))

    day = 1
    while a < b:
        a += 0.1 * a
        day += 1

    print(f'The distance {b} km will be achieved after {day} days')


def main():
    ctrl = True
    while ctrl:

        input_s = input("Enter exercise number or type q on exit: ")

        if input_s == '1':
            print('Exercise: ', input_s)
            exercise_1()
        elif input_s == '2':
            print('Exercise: ', input_s)
            exercise_2()
        elif input_s == '3':
            print('Exercise: ', input_s)
            exercise_3()
        elif input_s == '4':
            print('Exercise: ', input_s)
            exercise_4()
        elif input_s == '5':
            print('Exercise: ', input_s)
            exercise_5()
        elif input_s == '6':
            print('Exercise: ', input_s)
            exercise_6()
        elif input_s in ['q', 'Q', 'quit', 'exit', 'Quit', 'Exit', 'qqq', 'qq']:
            print('Good by!')
            ctrl = False
        else:
            print('Enter exercise number from 1 to 6')


if __name__ == '__main__':
    main()
