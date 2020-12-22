with open('file_2.txt', 'r') as my_file:

    content = my_file.read()
    print(f'Содержимое файла: \n {content}')

with open('file_2.txt', 'r') as my_file:
    content = my_file.readlines()
    print(f'Количество строк в файле - {len(content)}')

with open('file_2.txt', 'r') as my_file:

    content = my_file.readlines()

    for i in range(len(content)):
        print(f'Окличество символов {i + 1} - ой строки {len(content[i])}')
        with open('file_2.txt', 'r') as my_file:
            content = my_file.read()
            content = content.split()

    print(f'Общее количество слов - {len(content)}')
