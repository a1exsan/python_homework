# written by: Alex fominsan@gmail.com

from sys import argv

def zarplata(work_hours, work_price, bonus):
    print(f'zarplata = {float(work_hours) * float(work_price) + float(bonus)}')

name, work_hours, work_price, bonus = argv

zarplata(work_hours, work_price, bonus)

