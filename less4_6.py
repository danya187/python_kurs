from itertools import count

for el in count(int(input('Введите стартовое число '))):
    if el > 3456: # рандомное стоп число, инчае список будет бесконечным
        break
    else:
        print(el)


from itertools import cycle

с = 0
my_list = ["ABC", True, 123, None]
for el in cycle(my_list):
    if с > 26: # рандомное стоп число, инчае список будет бесконечным
        break
    print(el)
    с += 1
