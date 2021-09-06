"""4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки. Строки нужно пронумеровать.
Если слово длинное, выводить только первые 10 букв в слове.
"""


input_string = input('Enter several random words: ').split()

for order, word in enumerate(input_string, 1):
    print(f'{order}. {word[:10]}')