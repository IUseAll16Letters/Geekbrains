"""1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль."""


def division(x, y):
    try:
        if y == '0':
            print("Wrong input, divisor can't be 0. ")
            if input('Want re-enter the numbers? ').lower() in 'yes':
                return division(input('Enter dividend: '), input('Enter divisor: '))
            else:
                return 'Quit. '
        else:
            x, y = float(x), float(y)
            return round(x / y, 5)
    except ValueError:
        print('Wrong input. Expected number. ')
        if input('Want re-enter the numbers? ').lower() in 'yes':
            return division(input('Enter dividend: '), input('Enter divisor: '))
        else:
            return 'Quit. '


print(division(input('Enter dividend: '), input('Enter divisor: ')))
