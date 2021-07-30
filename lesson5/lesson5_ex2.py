# written by: Alex fominsan@gmail.com

with open('test_ex2.txt') as f_obj:

    lines = f_obj.readlines()

    print(f'Count file strings: {len(lines)}')

    for i, l in enumerate(lines):

        print(f"Number of words in the {i} string: {len(l.split(' '))}")
