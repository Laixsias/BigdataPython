costs = int(input('Введите сумму ваших издержек '))
revenue = int(input('Введите сумму вашего дохода '))
profit = revenue - costs
if profit >0 :
    print ('Ваша прибыл равна ', profit)
    staff = int(input('Введите численнсть сотрудников '))
    rent = profit/revenue
    print ('Ваша рентатебельность равна ', rent)
    pr_per_st = profit/staff
    print('Прибыль на одного сотрудника равна ',pr_per_st)
else :
    print ('Ваш убыток равен ', profit)