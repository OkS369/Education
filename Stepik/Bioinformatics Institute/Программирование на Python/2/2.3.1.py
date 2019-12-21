a,b,c,d = int(input()),int(input()),int(input()),int(input())
for i in range(c,d+1):    print('\t', i, sep = '', end = '')
print()
for i in range(a,b+1):
    print(i,'\t', sep = '', end = '')
    for j in range(c,d+1):
        print(i*j,'\t', sep = '', end = '')
    print()

'''
a a*c a*c+1 ... a*d
a+1...a+1*d
...
b b*c...b*d
'''

'''
Когда Павел учился в школе, он запоминал таблицу умножения прямоугольными блоками. Для тренировок ему бы очень пригодилась программа, которая показывала бы блок таблицы умножения.
Напишите программу, на вход которой даются четыре числа a, b, c и d, каждое в своей строке. Программа должна вывести фрагмент таблицы умножения для всех чисел отрезка [a;b] на все числа отрезка [c;d].
Числа a, b, c и d являются натуральными и не превосходят 10, a≤b, c≤d.
Следуйте формату вывода из примера, для разделения элементов внутри строки используйте '\t' — символ табуляции. Заметьте, что левым столбцом и верхней строкой выводятся сами числа из заданных отрезков — заголовочные столбец и строка таблицы.﻿
Sample Input 1: 
7
10
5
6
Sample Output 1: 
	5	6
7	35	42
8	40	48
9	45	54
10	50	60
Sample Input 2: 
5
5
6
6
Sample Output 2: 
	6
5	30
Sample Input 3: 
1
3
2
4
Sample Output 3: 
	2	3	4
1	2	3	4
2	4	6	8
3	6	9	12
'''
