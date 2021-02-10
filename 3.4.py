def grade(x,y):
    return 1 / x ** abs(y)
    #return x ** y
print(f'Результат возведения {grade(int(input("Веведите первое число ")), int(input("Введите второе число ")))}')
