file = open('test.txt', 'w')
line = input('Введите текст \n')
while line:
    file.writelines(line)
    line = input('Введите текст \n')
    if not line:
        break
file.close()
my_f = open('test.txt', 'r')
log = file.readlines()
print(log)
my_f.close()