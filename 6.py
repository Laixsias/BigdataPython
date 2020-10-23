first_day_km= int(input('Введите результат первого дня '))
res_km =int(input('Введете желаемый резульат '))
day=1
while first_day_km < res_km:
    first_day_km *=1.1
    day +=1
print ('На', day,'-й день спортсмен достигнет результата не менее', res_km,'км' )