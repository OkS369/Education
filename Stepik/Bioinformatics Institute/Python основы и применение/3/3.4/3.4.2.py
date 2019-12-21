import requests
import re
url = input().strip()
response = requests.get(url).text
pattern = r'''(?:<a.*href=(?:\'|\"))(?:.{0,6}://)*(w*\.?(?:[\w\d-]+\.)+\w+)(?:/?)'''
URLs = re.findall(pattern, response)
ans = sorted(list(set(URLs)))
for i in ans:
    print(i)

'''
Вашей программе на вход подается ссылка на HTML файл.
Вам необходимо скачать этот файл, затем найти в нем все ссылки вида <a ... href="..." ... > и вывести список сайтов,
 на которые есть ссылка.

Сайтом в данной задаче будем называть имя домена вместе с именами поддоменов. 
То есть, это последовательность символов, которая следует сразу после символов протокола, если он есть,
 до символов порта или пути, если они есть, за исключением случаев с относительными ссылками вида
<a href="../some_path/index.html">.

Сайты следует выводить в алфавитном порядке.

# url = 'http://pastebin.com/raw/2mie4QYa'
# url = 'http://pastebin.com/raw/hfMThaGb'
# url = 'http://pastebin.com/raw/7543p0ns'
'''