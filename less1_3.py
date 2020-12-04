user_count = int(input("Введите число : "))
temp = str(user_count)
x_1 = temp + temp
x_2 = temp + temp + temp
result = user_count + int(x_1) + int(x_2)
print(f"Результат равен: {temp} + {x_1} + {x_2} = {result}")
