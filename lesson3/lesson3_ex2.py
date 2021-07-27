# written by: Alex fominsan@gmail.com

def get_user_data(**kwargs):
    return kwargs

user_data = input('Entar data as template splitted by comma (name, last name, birthday, city, e-mail, phone)').split(', ')

print(get_user_data(name=user_data[0],
                    l_name=user_data[1],
                    birthday=user_data[2],
                    city=user_data[3],
                    Email=user_data[4],
                    phone=user_data[5]
                    ))
