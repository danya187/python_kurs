def division():

    try:
        divisible = int(input("Введите делимое число: "))
        divider = int(input("Введите делитель: "))
        answer = divisible / divider
        return answer
    except ValueError:
        return "Ошибка,введите ЧИСЛО"
    except ZeroDivisionError:
        return "Деление на ноль!Введите число, кроме нуля"


result = division()

print(result)
