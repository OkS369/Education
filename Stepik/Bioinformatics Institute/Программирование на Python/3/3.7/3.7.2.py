def changing(d,text):
    for i in range(len(text)):
        for j in d.keys():
            if text[i] == j:
                print(d[j], sep = '', end = '')
    print()
alpha1, alpha2, text1, text2 = input(), input(), input(), input()
d1, d2 = dict(zip(alpha1,alpha2)), dict(zip(alpha2,alpha1))
changing(d1,text1)
#print()
changing(d2,text2)

'''
source, dest = input(), input()
decoded = input()
encoded = input()

print(decoded.translate(str.maketrans(source, dest)))
print(encoded.translate(str.maketrans(dest, source)))
'''

'''
a,b,c,d=input(),input(),input(),input()
print(''.join(b[a.index(i)] for i in c))
print(''.join(a[b.index(i)] for i in d))
'''

'''
# Считываем 4 строки в цикле
original, coding, first_string, second_string = (input() for i in range(4))

# По индексу символа из оригинала берём символ на замену из кодировки,
# для каждого символа из строки, которую нужно закодировать
print(*[coding[original.find(symbol)] for symbol in first_string], sep='')
# Аналогично, только наоборот :D
print(*[original[coding.find(symbol)] for symbol in second_string], sep='')
'''

'''
В какой-то момент в Институте биоинформатики биологи перестали понимать, что говорят информатики: они говорили каким-то странным набором звуков. 
В какой-то момент один из биологов раскрыл секрет информатиков: они использовали при общении подстановочный шифр, т.е. заменяли каждый символ исходного сообщения на соответствующий ему другой символ. Биологи раздобыли ключ к шифру и теперь нуждаются в помощи: 
Напишите программу, которая умеет шифровать и расшифровывать шифр подстановки. Программа принимает на вход две строки одинаковой длины, на первой строке записаны символы исходного алфавита, на второй строке — символы конечного алфавита, после чего идёт строка, которую нужно зашифровать переданным ключом, и ещё одна строка, которую нужно расшифровать.
Пусть, например, на вход программе передано:
abcd
*d%#
abacabadaba
#*%*d*%
Это значит, что символ a исходного сообщения заменяется на символ * в шифре, b заменяется на d, c — на % и d — на #.
Нужно зашифровать строку abacabadaba и расшифровать строку #*%*d*% с помощью этого шифра. Получаем следующие строки, которые и передаём на вывод программы:
*d*%*d*#*d*
dacabac
﻿
Sample Input 1: 
abcd
*d%#
abacabadaba
#*%*d*%
Sample Output 1: 
*d*%*d*#*d*
dacabac
Sample Input 2: 
dcba
badc
dcba
badc
Sample Output 2: 
badc
dcba
'''
