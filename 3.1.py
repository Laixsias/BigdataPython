def num(*args):
    try:
        arg1=int(input('Введите первое число: ' ))
        arg2=int(input('Введите второе число: '))
        b = arg1 / arg2
    except ZeroDivisionError:
        return 'Деление на 0!'
    except ValueError:
        return 'Введены неверные данные'

    return b
print(f'Результат деления : {num()}')
