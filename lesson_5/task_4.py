"""4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Напишите программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""
FILE_NAME = 'task_4.txt'


var = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
# with open(FILE_NAME, 'w', encoding='utf-8') as f:
#     for i in range(4):
#         words = tuple(var)
#         f.write(f'{words[i]} - {i+1}\n')


with open(FILE_NAME) as F:
    new_file = open('task_4_1.txt', 'w', encoding='utf-8')
    for i in F.readlines():
        word, separator, num = i.split()
        translated_line = f"{var[word]} {separator} {num}"
        print(translated_line)
        new_file.write(translated_line+'\n')
    new_file.close()