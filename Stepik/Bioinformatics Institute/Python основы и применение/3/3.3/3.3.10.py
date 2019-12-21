import sys
import re
for line in sys.stdin:
    line = line.strip()
    if ('1' not in line) and ('0' not in line) or (' ' in line):
        continue
    if re.fullmatch(r'(0|1(01*0)*1)*', line) != None:
        print(line)
    if line == '':
        break

'''
import sys
import re
for line in sys.stdin:
    line = line.strip()
    if ('1' not in line) and ('0' not in line) or (' ' in line):
        continue
    s1 = re.sub(r"(.)(.)", r"\1x", line)
    s2 = re.sub(r"(.)(.)", r"x\2", line)
    s2 = re.sub(r"((x.)+)(.)", r"\1x", s2)
    if s1.count('1') == s2.count('1') or line == '0' or line == '':
        print(line)
    if line == '':
        break
'''

'''Вам дана последовательность строк.
Выведите строки, содержащие двоичную запись числа, кратного 3.

Двоичной записью числа называется его запись в двоичной системе счисления.

Sample Input:
0
10010
00101
01001
Not a number
1 1
0 0

Sample Output:
0
10010
01001'''