from math import factorial
from itertools import count
n = int(input('Ввведите число '))
def fibo_gen():
    for el in count(n):
        yield factorial(el)
x = 1
for i in fibo_gen():
    print('Факториал {} - {}'.format(x, i))
    if x == n:
        break
    x += 1