numbers = []
words = []
text = {}
t = 0
n = 0
with open('Гаррі Поттер і Філософський камінь.txt','r') as x:
    s = x.read().replace('\n', ' ').lower().split()
    s.sort()
    #print(s)
    for i in s:
        if i in text:
            text[i] += 1
        else:
            text[i] = 1
    #print(text)
    
    for i in text.keys():
        words.append(i)
        numbers.append(text[i])
    for i in range(len(numbers)):
        if t < numbers[i]:
            t = numbers[i]
            n = i
    #print(words, '\n', numbers, sep = '')
    print(words[n], numbers[n], sep = ' ')

'''
Недавно мы считали для каждого слова количество его вхождений в строку. Но на все слова может быть не так интересно смотреть, как, например, на наиболее часто используемые.
Напишите программу, которая считывает текст из файла (в файле может быть больше одной строки) и выводит самое частое слово в этом тексте и через пробел то, сколько раз оно встретилось. Если таких слов несколько, вывести лексикографически первое (можно использовать оператор < для строк).
Слова, написанные в разных регистрах, считаются одинаковыми.

﻿
Sample Input: 
abc a bCd bC AbC BC BCD bcd ABC
Sample Output: 
abc 3
'''
