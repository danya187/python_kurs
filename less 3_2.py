name = input("Введите имя\n>>>")
surname = input("Введите фимилю\n>>>")
year = input("Введите возраст\n>>>")
city = input("Введите город\n>>>")
email = input("Введите email\n>>>")
tel = input("Введите телефон\n>>>")


def my_func(name, surname, year, city, email, tel):
    return ' '.join([name, surname, year, city, email, tel])


res = my_func(name, surname, year, city, email, tel)


print(res)
