goods = int(input("Введите количество товара "))
n = 1
my_dict = []
my_list = []
my_analysis = {}
while n <= goods:
    my_dict = dict({'название': input("введите название "), 'цена': input("Введите цену "),
                    'количество': input('Введите количество '), 'eд': input("Введите единицу измерения ")})
    my_list.append((n, my_dict))
    n += 1
    my_analysis = dict(
        {'название': my_dict.get('название'), 'цена': my_dict.get('цена'), 'количество': my_dict.get('количество'),
         'ед': my_dict.get('ед')})
print(my_analysis)
