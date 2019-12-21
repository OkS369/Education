import sys, re
pattern = r'cat'
for line in sys.stdin:
    line = line.rstrip()
    if len(re.findall(pattern, line)) >= 2:
        print(line)
    if line == '':
        break


'''
Вам дана последовательность строк.
Выведите строки, содержащие "cat" в качестве подстроки хотя бы два раза.

Sample Input:
catcat
cat and cat
catac
cat
ccaatt

Sample Output:
catcat
cat and cat
'''