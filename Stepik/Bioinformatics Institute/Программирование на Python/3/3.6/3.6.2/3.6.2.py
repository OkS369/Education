import requests
link = 'https://stepic.org/media/attachments/course67/3.6.3/'
counter = 0
with open('dataset_3378_3.txt','r') as x:
    link = 'https://stepic.org/media/attachments/course67/3.6.3/'
    url = x.readline().strip()
    name = requests.get(url).text
while (True):
    text = name.strip().split()
    if text[0] == 'We':
        break
        print(url, name, counter, text, sep = '\n')
    url = link + name.strip()
    name = requests.get(url).text
    #print(url, name, counter, text, sep = '\n')
    counter += 1
    if counter > 251:
        break

'''
Имеется набор файлов, каждый из которых, кроме последнего, содержит имя следующего файла.
Первое слово в тексте последнего файла: "We".
Скачайте предложенный файл. В нём содержится ссылка на первый файл из этого набора. 
Все файлы располагаются в каталоге по адресу:
https://stepic.org/media/attachments/course67/3.6.3/
Загрузите содержимое ﻿последнего файла из набора, как ответ на это задание.
'''
