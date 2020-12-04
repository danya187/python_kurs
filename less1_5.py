revenue = input("Введите сумму выручки\n>>>")

if revenue.isdigit():
    revenue = int(revenue)
else:
    print("Ошибка ввода числа,повторите попытку")
    exit()

cost = input("Введите сумму издержек\n>>>")

if cost.isdigit():
    cost = int(cost)
else:
    print("Ошибка ввода числа,повторите попытку")
    exit()

if revenue > cost:
    profit = revenue - cost
    print("Фирма работает в '+',сумма прибыли =", profit)
    number_staff = input("Введите число сотрудников\n>>>")
    profit_staff = profit // int(number_staff)
    print("Прибыль на 1 сотрудника -", profit_staff)
elif revenue == cost:
    print("Фирма работает в '0'")
else:
    print("Фирма работает в убыток")
