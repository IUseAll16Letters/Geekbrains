"""6. Реализовать функцию int_func(), принимающую слова из маленьких латинских букв
и возвращающую их же, но с прописной первой буквой.
Например, print(int_func(‘text’)) -> Text.
   7. Продолжить работу над заданием. В программу должна попадать строка из слов, разделённых пробелом.
Каждое слово состоит из латинских букв в нижнем регистре. Нужно сделать вывод исходной строки,
но каждое слово должно начинаться с заглавной буквы.
Используйте написанную ранее функцию int_func().
"""


floyd = ['beyond the horizon of the place we lived when we were young',
         'in a world of magnets and miracles',
         'our thoughts strayed constantly and without boundary',
         'the ringing of the division bell had begun'
         ]


# Solution 1 - Original
def int_func(word):
    return word.capitalize()


def capitalize_line(line):
    line = line.split()
    return ' '.join(int_func(wrd) for wrd in line)


# Solution 2 - Lambda
lines = lambda seq: ' '.join(word.capitalize() for word in seq.split())


# The Solution 3 - Decorator fun
def the_capitalizer(fn):
    def wrapper(arg):
        return ' '.join(word.capitalize() for word in fn(arg))
    return wrapper


@the_capitalizer
def the_splitter(word_line):
    return word_line.split()


for string, func in enumerate([capitalize_line, lines, the_splitter, print]):
    print(func(floyd[string]))

print(the_splitter.__name__)
