# written by: Alex fominsan@gmail.com

with open("test.txt", "w") as f_obj:

    while True:

        text = input('Enter some text: ')

        if text == '':

            break

        print(text, file=f_obj)