"""5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить её на экран.
"""
# Optional
# FILE_NAME = input('Enter file name: ')

FILE_NAME = 'task_5.txt'


with open(FILE_NAME, 'w+', encoding='utf-8') as F:
    F.write(input('Enter numbers in one line: '))
    F.seek(0)
    print(sum(map(int, F.read().split())))
