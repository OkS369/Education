import sys
import re
pattern = r'\b(a|A)+\b'
for line in sys.stdin:
    line = line.strip()
    print(re.sub(pattern, 'argh', line, 1,  flags=re.IGNORECASE))
    if line == '':
        break


'''Вам дана последовательность строк.
В каждой строке замените первое вхождение слова, состоящего только из латинских букв "a" (регистр не важен), на слово "argh".

Sample Input:
There’ll be no more "Aaaaaaaaaaaaaaa"
AaAaAaA AaAaAaA

Sample Output:
There’ll be no more "argh"
argh AaAaAaA'''