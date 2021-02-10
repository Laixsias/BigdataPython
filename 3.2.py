def bio(**kwargs):
    return list(kwargs.values())
def bio_list():
    print(bio(name=input('Введите имя: '),
               s_name=input('Введите фамилию: '),
               b_year=input('Введите год рождения: '),
               l_state=input('Введите город проживания: '),
               e_mail=input('Введите e-mail: '),
               phone =input('Введите номер телефона: ')))
print(bio_list())