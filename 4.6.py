from itertools import count, cycle
# for i in count(int(input('Введите стартовое число: '))):
#     print(i)
list = [5, 10, 50, 112, 15, 16, 48]
for i in cycle(list):
    print(i)

