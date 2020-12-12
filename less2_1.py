my_list = [32, None, -77, 'True', True, 6.7]


def my_type(el):
    for el in range(len(my_list)):
        print(type(my_list[el]))
    return


my_type(my_list)
