"""2. Создать текстовый файл (не программно), сохранить в нём несколько строк,
выполнить подсчёт строк и слов в каждой строке.
"""
FILE_NAME = 'task_2.txt'


# Lazily creating the file
# with open(FILE_NAME, 'a', encoding='utf-8') as fh:
#     for i in range(4):
#         fh.writelines(input('Leave a message: ') + '\n')


# Optional lines counter
print('lines in file: ', sum(1 for line in open(FILE_NAME)))


with open(FILE_NAME, 'r', encoding='utf-8') as f:
    lines_count = 0
    for i in f.readlines():
        lines_count += 1
        print("{:40} line number: {:>2}, words in line: {:>2}".format(i.replace('\n', ' '),
                                                                      lines_count, i.count(' ') + 1))
