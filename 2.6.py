dictionary = ["имя", "цена", "количество", "ед"]

goods = []

while input("Хотите добавить новый продукт ? Введите да/нет: ") == 'да':
    new_goods = {}
    for key in dictionary:
        new_goods[key] = input("Введите параметр \"" + key + "\" для нового товара: ")
    goods.append(new_goods)

print(goods)

analitics = {}
for good in goods:
    for key, value in good.items():
        if key in analitics:
            if value not in analitics[key]:
                analitics[key].append(value)
        else:
            analitics[key] = [value]

print(analitics)