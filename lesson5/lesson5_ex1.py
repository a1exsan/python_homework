# written by: Alex fominsan@gmail.com

with open("test.txt", "w") as f_obj:

    run = True

    while run:

        text = input('Enter some text: ')

        if text == '':

            run = False

        print(text, file=f_obj)