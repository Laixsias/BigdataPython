rus = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
new_file = []
with open('test_5.4.txt', 'r') as num:
    for i in num:
        i = i.split(' ', 1)
        new_file.append(rus[i[0]] + '  ' + i[1])
    print(new_file)
with open('test_5.4.txt', 'r') as file_obj_2:
    file_obj_2.writelines(new_file)
