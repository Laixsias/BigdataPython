year = {'Winter': (1, 2, 12),
           'Sping': (3, 4, 5),
           'Summer': (6, 7, 8),
           'Autumn': (9, 10, 11)}
try:
    month = int(input('Введите номер месяца '))
    for key in year.keys():
        if month in year[key]:
            print(key)
except ValueError:
    print('Вы ввели неверные данные')


year_list = ['Winter', 'Spring', 'Summer', 'Autumn']
try:
    month = int(input('Введите номер месяца '))
    if month ==1 or month == 12 or month == 2:
        print(year_list[0])
    elif month == 3 or month == 4 or month ==5:
        print(year_list[1])
    elif month == 6 or month == 7 or month == 8:
        print(year_list[2])
    elif month == 9 or month == 10 or month == 11:
        print(year_list[3])
except ValueError:
    print('Вы ввели неверные данные')
