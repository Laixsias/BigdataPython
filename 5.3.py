with open('test_5.3.txt', 'r') as salary:
    sal = []
    poor = []
    list = salary.read().split('\n')
    for i in list:
        i = i.split()
        if int(i[1]) < 20000:
           poor.append(i[0])
        sal.append(i[1])
print(f'Оклад меньше 20.000 {poor}, средний оклад {sum(map(int, sal)) / len(sal)}')