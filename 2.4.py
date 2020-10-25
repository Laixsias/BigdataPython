data = input("Введите данные через пробел ")
a = data.split(' ')
for i, b in enumerate(a, 1):
    if len(b) > 10:
        b = b[0:10]
    print(i, ':', b)
