count = int(input("введите целое положиетлдьное число\n>>>"))
largest_number = count % 10
count = count // 0
while count > 0:
    if count % 10 > largest_number:
        largest_number = count % 10
        count = count // 10
print("Наибольшая цифра в числе", largest_number)
