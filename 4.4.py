list = [12, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
list_2 = [x for x in list if list.count(x) == 1]
print(list_2)