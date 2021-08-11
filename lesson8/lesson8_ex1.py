
class Date():
    DATE_STR = ''

    def __init__(self, date_str):
        Date.DATE_STR = date_str

    @classmethod
    def date(cls):

        date_list = cls.DATE_STR.split('-')
        date_list = [int(s) for s in date_list]

        return date_list

    @staticmethod
    def get_date(date):
        dl = date.split('-')
        dl = [int(s) for s in dl]

        if dl[0] in range(1, 32) and dl[1] in range(1,13):
            if dl[1] == 2 and dl[0] > 29:
                print(f'Error: days in february is too match!!!')
            else:
                return dl
        else:
            print('Date format incorrect!!!')



date = Date('21-08-2021')
print(date.date())

print(Date.get_date('21-2-1985'))

print(Date.get_date('28-2-1985'))

print(Date.get_date('30-2-1985'))