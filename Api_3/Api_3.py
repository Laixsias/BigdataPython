from Api_3_class_joblist import JoBList
from pprint import pprint

vacancy_db = JoBList('mongodb://172.0.0.1:27017/', 'vacancy', 'vacancy_db')
vacancy_db.print_salary(300_000)

vacancy_db.collection.update_one({'vacancy_link': 'https://hh.ru/vacancy/31828023'},
                                 {'$set': {'city':'Москва', 'company_name':'some compary'}})

objects = vacancy_db.collection.find().limit(1)
for obj in objects:
    pprint(obj)

vacancy = 'Big_data'

vacancy_db.search_job(vacancy)
objects = vacancy_db.collection.find().limit(1)
for obj in objects:
    pprint(obj)