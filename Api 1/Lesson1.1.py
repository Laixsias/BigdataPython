import requests
import json

url = 'https://api.github.com'
user ='Laixsias'
a = requests.get(f'{url}/users/{user}/repos')
with open('data.json', 'w') as f:
    json.dump(a.json(), f)
for i in a.json():
    print(i['name'])






