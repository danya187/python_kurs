
seasons_list = ['зима', 'весна', 'лето', 'осень']
seasons_dict = {1: 'январь', 2: 'февраль', 3: 'март', 4: 'апрель', 5: 'май', 6: 'июнь', 7: 'июль', 8: 'август', 9: 'сентябрь', 10: 'октябрь', 11: 'ноябрь', 12: 'декабрь'}
month = int(input("Введите месяц по номеру "))
# вижу, что строка длинная, можно сделать 2 seasons_dict
if month == 1 or month == 12 or month == 2:
    print(seasons_dict.get(month))
    print(seasons_list[0])
elif month >= 3 or month <= 5:
    print(seasons_dict.get(month))
    print(seasons_list[1])
elif month >= 6 or month <= 8:
    print(seasons_dict.get(month))
    print(seasons_list[2])

elif month >= 9 or month <= 11:
    print(seasons_dict.get(month))
    print(seasons_list[3])
else:
    print("Такого месяца не существует")
