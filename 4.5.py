from functools import reduce
def list(a, b):
    return a * b
list_2 = [x for x in range(100, 1001) if x % 2 == 0]
print(reduce(list, list_2))