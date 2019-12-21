import requests
import re
url_1 = input()
url_2 = input()
res_1 = requests.get(url_1)
URLs_1 = re.findall(r'<a.*href=\"(.+)\"', res_1.text)
URLs_2 = []
for url in URLs_1:
    res_2 = requests.get(url)
    URLs_2.extend(re.findall(r'<a.*href=\"(.+)\"', res_2.text))
print("Yes" if url_2 in URLs_2 else "No")
'''
Рассмотрим два HTML-документа A и B.
Из A можно перейти в B за один переход, если в A есть ссылка на B,
 т. е. внутри A есть тег <a href="B">, возможно с дополнительными параметрами внутри тега.
Из A можно перейти в B за два перехода если существует такой документ C, 
что из A в C можно перейти за один переход и из C в B можно перейти за один переход.

Вашей программе на вход подаются две строки, содержащие url двух документов A и B.
Выведите Yes, если из A в B можно перейти за два перехода, иначе выведите No.

Обратите внимание на то, что не все ссылки внутри HTML документа могут вести на существующие HTML документы.

Sample Input 1:
https://stepic.org/media/attachments/lesson/24472/sample0.html
https://stepic.org/media/attachments/lesson/24472/sample2.html

Sample Output 1:
Yes

Sample Input 2:
https://stepic.org/media/attachments/lesson/24472/sample0.html
https://stepic.org/media/attachments/lesson/24472/sample1.html

Sample Output 2:
No

Sample Input 3:
https://stepic.org/media/attachments/lesson/24472/sample1.html
https://stepic.org/media/attachments/lesson/24472/sample2.html

Sample Output 3:
Yes
'''