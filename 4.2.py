list = [5, 12, 90, 55, 100, 3, 80, 26, 32,0.98]
list_2 = [num for i, num in enumerate(list) if list[i] > list[i - 1] and i != 0]
print(list_2)