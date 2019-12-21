import requests
import json

client_id = 'fa2a294d37367f76dd2f'
client_secret = '77be927b49eda2158f6720d80034fcb8'
r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })
j = json.loads(r.text)
token = j["token"]
headers = {"X-Xapp-Token": token}
URL = 'https://api.artsy.net/api/artists/'
artists = {}
with open("dataset_24476_5.txt", encoding="UTF-8") as f:
    lines = f.readlines()
    for l in lines:
        ID = l.strip()
        r = requests.get(URL + ID, headers=headers)
        j = json.loads(r.text)
        #print(j)
        artists[j["sortable_name"]] = j["birthday"]
res = sorted(artists, key=artists.__getitem__)
for i in res:
    print(i)
'''
В этой задаче вам необходимо воспользоваться API сайта artsy.net

API проекта Artsy предоставляет информацию о некоторых деятелях искусства, их работах, выставках.

В рамках данной задачи вам понадобятся сведения о деятелях искусства (назовем их, условно, художники).

Вам даны идентификаторы художников в базе Artsy.
Для каждого идентификатора получите информацию о имени художника и годе рождения.
Выведите имена художников в порядке неубывания года рождения. 
В случае если у художников одинаковый год рождения, выведите их имена в лексикографическом порядке.
'''