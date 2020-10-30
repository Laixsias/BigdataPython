def num_3(a,b,c):
    if a >= c and b >= c:
        return a + b
    elif a > b and a < c:
        return a + c
    else:
        return b + c
print(f'Сумма больших введенных чисел - {num_3(int(input("Введите первое число ")), int(input("Введите второе число ")), int(input("Введите третье чилсло ")))}')