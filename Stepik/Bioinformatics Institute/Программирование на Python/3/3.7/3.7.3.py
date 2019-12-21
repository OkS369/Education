w = tuple(input().lower() for i in range(int(input())))
t, out = [], []
for i in range(int(input())):
    t = t + input().lower().split()
t = tuple(t)
for i in range(len(t)):
    if (t[i] not in w) and (t[i] not in out):
        print(t[i])
        out.append(t[i])
        
'''
d = int(input())
w = tuple(input().lower() for i in range(d))
l = int(input())
t, out = [], []
for i in range(l):
    temp = input().lower().split()
    t = t + temp
t = tuple(t)
for i in range(len(t)):
    if (t[i] not in w) and (t[i] not in out):
        print(t[i])
        out.append(t[i])
'''

'''
dic = {input().lower() for i in range(int(input()))}

wrd = set()
for w in range(int(input())):
    wrd |= {i.lower() for i in input().split()}

print(*wrd.difference(dic), sep="\n")
'''

'''
words = set(input().lower() for i in range(int(input())))
text = set(('\n'.join(input().lower() for i in range(int(input())))).split())
print('\n'.join(text - words))
'''

'''
Простейшая система проверки орфографии основана на использовании списка известных слов. Каждое слово в проверяемом тексте ищется в этом списке и, если такое слово не найдено, оно помечается, как ошибочное.
Напишем подобную систему.
Через стандартный ввод подаётся следующая структура: первой строкой — количество 
d
d
записей в списке известных слов, после передаётся  
d
d
 строк с одним словарным словом на строку, затем — количество 
l
l
строк текста, после чего — 
l
l
строк текста.
Напишите программу, которая выводит слова из текста, которые не встречаются в словаре. Регистр слов не учитывается. Порядок вывода слов произвольный. Слова, не встречающиеся в словаре, не должны повторяться в выводе программы.
﻿
Sample Input: 
3
a
bb
cCc
2
a bb aab aba ccc
c bb aaa
Sample Output: 
aab
aba
c
aaa
'''
