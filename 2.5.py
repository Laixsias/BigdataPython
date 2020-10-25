my_list = [7, 5, 3, 3, 2]
new_add = int(input('Введите рейтинг '))
c = my_list.count(new_add)
for element in my_list:
    if c > 0:
        i = my_list.index(new_add)
        my_list.insert(i+c, new_add)
        break
    else:
        if new_add > element:
            j = my_list.index(element)
            my_list.insert(j, new_add)
            break
        elif new_add < my_list[len(my_list) - 1]:
            my_list.append(new_add)
print(my_list)
