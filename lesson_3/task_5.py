"""5. Программа запрашивает у пользователя строку чисел, разделённых пробелом.
При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделённых пробелом и снова нажать Enter.
Сумма вновь введённых чисел будет добавляться к уже подсчитанной сумме.

Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введён после нескольких чисел, то вначале нужно добавить сумму этих чисел
к полученной ранее сумме и после этого завершить программу.
"""


def summation(string=input('Enter the sequence of several numbers using " ": '), summary=0):
    if '$' in string:
        try:
            print('Some magic appears, the numbers jump off your IDE page and start dancing. Summation ends. ')
            return f"The final sum is: {summary + sum(map(int, (string[:string.index('$')].split())))}"
        except ValueError:
            print(f'The accumulated sum is: {summary}')
            return "You've broke everything! "

    try:
        summary += sum(map(int, string.split()))
        print(f'The sum is: {summary}')
    except ValueError:
        print(f'The accumulated sum is: {summary}')
        return "You've broke everything! "

    if input('Want to continue summation? ') in 'yesYES':
        return summation(input('Enter another sting of numbers: '), summary)
    return summary


print(summation())