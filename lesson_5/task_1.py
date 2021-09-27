"""1. Создать программный файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных будет свидетельствовать пустая строка.
"""

FILE_NAME = 'task_1.txt'
print('File name:', FILE_NAME)


with open(FILE_NAME, 'a', encoding='utf-8') as F:
    while True:
        user_message = input('Leave the message for ancestors: ')
        if user_message:
            F.writelines(user_message + '\n')
        else:
            break

