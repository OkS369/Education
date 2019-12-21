import sys
import re
for line in sys.stdin:
    line = line.strip()
    print(re.sub(r'(\w)(\w+)',  r"\2\1", line))
    if line == '':
        break


'''Вам дана последовательность строк.
В каждой строке замените все вхождения нескольких одинаковых букв на одну букву.
Буквой считается символ из группы \w.

Sample Input:
attraction
buzzzz

Sample Output:
atraction
buz'''