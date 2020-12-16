def my_func(*args):
    result = 0
    exit_flag = False
    for itm in args:
        try:
            result += float(itm) if itm else 0
        except ValueError as e:
            if itm == "q":
                exit_flag = not exit_flag
                break
    return result, exit_flag


user_sum = 0

while True:
    user_input = input("Введите число через пробел\n>>>").split(' ')
    result_sum, user_exit = my_func(*user_input)
    user_sum += result_sum
    print(f'сумма: {user_sum}')

    if user_exit:
        print("До свидания")
        break
