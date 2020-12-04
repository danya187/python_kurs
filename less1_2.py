number_of_user = input("Введите время в секундах\n>>>")

if number_of_user.isdigit():
    number_of_user = int(number_of_user)
else:
    print("Ошибка ввода числа,повторите попытку")
    exit()

hours = number_of_user // 3600
minutes = (number_of_user - hours * 3600) // 60
seconds = number_of_user - (hours * 3600 + minutes * 60)
print(f"Время в формате чч:мм:сс {hours} : {minutes} : {seconds}")
