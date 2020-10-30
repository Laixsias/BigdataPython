s = 0
try:
    while True:
        for n in map(int, input('Введите чиcла через пробел или любой другой символ для завершения ').split()):
            s += n
        print(s)
except ValueError:
    print(s)