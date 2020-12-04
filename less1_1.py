print("Hello everybody!")

user_name = input("Введите ваше имя\n>>>")

if user_name.isalpha():
    user_name = str(user_name)
else:
    print("Ошибка ввода имени")
    exit()

print("Доброго времени суток," + user_name)
